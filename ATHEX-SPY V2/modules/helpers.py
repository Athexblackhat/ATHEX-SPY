import os
import platform
import subprocess
import datetime
import socket
from modules.color import Color as C

DOWNLOAD_DIR = "Downloaded-Files"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def run_command(command, shell=True, capture_output=False, check=False):
    """Run a shell command and optionally return output."""
    try:
        if capture_output:
            result = subprocess.run(command, shell=shell, capture_output=True, text=True)
            return result.stdout + result.stderr
        else:
            subprocess.run(command, shell=shell, check=check)
            return ""
    except subprocess.CalledProcessError as e:
        print(f"{C.RED}[!] Command failed: {e}{C.RESET}")
        return ""
    except Exception as e:
        print(f"{C.RED}[!] Error executing command: {e}{C.RESET}")
        return ""

def get_timestamp():
    """Return a timestamp string for file naming."""
    now = datetime.datetime.now()
    return f"{now.year}-{now.month:02d}-{now.day:02d}-{now.hour:02d}-{now.minute:02d}-{now.second:02d}"

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def open_file(filepath):
    """Open a file with the default system application."""
    system = platform.system()
    if system == 'Windows':
        os.system(f'start "" "{filepath}"')
    elif system == 'Darwin':
        os.system(f'open "{filepath}"')
    else:
        os.system(f'xdg-open "{filepath}"')

def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def input_with_default(prompt, default=""):
    """Get user input with a default value if empty."""
    value = input(prompt).strip()
    return value if value else default

def confirm_action(message):
    """Ask user for Y/N confirmation."""
    choice = input(f"{C.WHITE}{message} (y/n): {C.RESET}").lower()
    return choice == 'y' or choice == ''