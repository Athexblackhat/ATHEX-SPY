#!/usr/bin/env python3
import os
import sys
import platform
from modules.color import Color as C
from modules.banner import menu, banner_list, version
from modules.helpers import clear_screen, ensure_dir
from modules import adb_core as adb
from modules import advanced as adv

DOWNLOAD_DIR = "Downloaded-Files"
ensure_dir(DOWNLOAD_DIR)

# Global state
current_page = 0
total_pages = len(menu)
run_tool = True

# Banner color mapping per page
banner_colors = [C.RED, C.CYAN, C.YELLOW, C.GREEN, C.MAGENTA]

def display_page():
    clear_screen()
    print(banner_colors[current_page] + banner_list[current_page] + C.RESET)
    print(menu[current_page])

def change_page(direction):
    global current_page
    if direction == 'n' and current_page < total_pages - 1:
        current_page += 1
    elif direction == 'p' and current_page > 0:
        current_page -= 1
    display_page()

def main_menu():
    global run_tool          # <-- Move global declaration to top of function
    display_page()
    while run_tool:
        try:
            print(f"\n{C.CYAN} 99 : Clear Screen                0 : Exit{C.RESET}")
            option = input(f"{C.RED}[Main Menu] {C.WHITE}Enter selection > {C.RESET}").strip().lower()
            if option in ['p', 'n']:
                change_page(option)
            elif option == '0':
                run_tool = False
                print(f"{C.GREEN}Exiting...{C.RESET}")
            elif option == '99':
                display_page()
            else:
                handle_option(option)
        except KeyboardInterrupt:
            run_tool = False
            print(f"\n{C.GREEN}Exiting...{C.RESET}")
        except Exception as e:
            print(f"{C.RED}[!] Error: {e}{C.RESET}")

def handle_option(opt):
    # Page 1 (options 1-20)
    if current_page == 0:
        options_page1 = {
            '1': lambda: adb.connect_device(),
            '2': adb.list_devices,
            '3': adb.disconnect_all,
            '4': adb.scan_network,
            '5': lambda: adb.mirror_device(),
            '6': adb.take_screenshot,
            '7': adb.screen_record,
            '8': adb.pull_file,
            '9': adb.push_file,
            '10': adb.run_app,
            '11': adb.install_apk,
            '12': adb.uninstall_app,
            '13': adb.list_apps,
            '14': adb.get_shell,
            '15': adb.hack_device,
            '16': adb.list_files,
            '17': adb.send_sms,
            '18': adb.copy_whatsapp,
            '19': adb.copy_screenshots,
            '20': adb.copy_camera,
        }
        if opt in options_page1:
            options_page1[opt]()
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")
    # Page 2 (options 21-40)
    elif current_page == 1:
        options_page2 = {
            '21': lambda: adb.take_screenshot(anonymous=True),
            '22': lambda: adb.screen_record(anonymous=True),
            '23': adb.open_link,
            '24': adb.display_photo,
            '25': adb.play_audio,
            '26': adb.play_video,
            '27': adb.get_device_info,
            '28': adb.get_battery_info,
            '29': lambda: adb.reboot_device('system'),
            '30': lambda: advanced_reboot_menu(),
            '31': adb.unlock_device,
            '32': adb.lock_device,
            '33': adb.dump_sms,
            '34': adb.dump_contacts,
            '35': adb.dump_call_logs,
            '36': adb.extract_apk,
            '37': adb.stop_adb,
            '38': adb.power_off,
            '39': adb.use_keycodes,
            '40': adb.update_tool,
        }
        if opt in options_page2:
            options_page2[opt]()
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")
    # Page 3 (options 41-50)
    elif current_page == 2:
        options_page3 = {
            '41': lambda: adb.record_audio('mic', stream=False),
            '42': lambda: adb.record_audio('mic', stream=True),
            '43': lambda: adb.record_audio('device', stream=False),
            '44': lambda: adb.record_audio('device', stream=True),
            '45': lambda: adb.mirror_device(),  # Mirror with audio is default in scrcpy
            '46': adv.live_keylogger,
            '47': adv.gps_location,
            '48': lambda: adv.camera_snap(camera='back'),
            '49': adv.view_browsing_history,
            '50': adv.extract_wifi_passwords,
        }
        if opt in options_page3:
            options_page3[opt]()
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")
    # Page 4 (options 51-60)
    elif current_page == 3:
        options_page4 = {
            '51': adv.full_backup,
            '52': adv.network_capture,
            '53': adv.bypass_lock_screen,
            '54': adv.install_burp_cert,
            '55': adv.screen_stream_web,
            '56': adv.live_logcat,
            '57': adv.vulnerability_scan,
            '58': adv.dump_system_info,
            '59': adv.open_reverse_shell,
            '60': adv.check_root,
        }
        if opt in options_page4:
            options_page4[opt]()
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")
    # Page 5 (options 61-70)
    elif current_page == 4:
        options_page5 = {
            '61': adv.brute_force_pin,
            '62': adv.frida_setup,
            '63': adv.inject_frida_script,
            '64': adv.dump_app_memory,
            '65': adv.disable_play_protect,
            '66': adv.uninstall_system_app,
            '67': adv.list_processes,
            '68': adv.kill_process,
            '69': adv.port_forward,
            '70': adv.reboot_edl,
        }
        if opt in options_page5:
            options_page5[opt]()
        else:
            print(f"{C.RED}Invalid option.{C.RESET}")

def advanced_reboot_menu():
    print(f"\n{C.WHITE}1. Reboot to Recovery\n2. Reboot to Bootloader\n3. Reboot to Fastboot{C.RESET}")
    choice = input("Select > ").strip()
    if choice == '1': adb.reboot_device('recovery')
    elif choice == '2': adb.reboot_device('bootloader')
    elif choice == '3': adb.reboot_device('fastboot')
    else: print(f"{C.RED}Invalid selection.{C.RESET}")

if __name__ == "__main__":
    # Check dependencies
    if not adb.check_adb_installed():
        print(f"{C.RED}[!] ADB is not installed. Please install Android SDK Platform Tools.{C.RESET}")
        sys.exit(1)
    main_menu()