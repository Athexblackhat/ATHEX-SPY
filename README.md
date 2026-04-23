<a href="https://github.com/Athexhacker/ATHEX-SPY"><img src="logo.png" alt="0" border="0" /></a> 

![Geo-Phone](https://img.shields.io/badge/version-v[2.0]-blue.svg)

<div align="center">
  
# 💀⚡ **ATHEX-SPY** ⚡💀
  
### 🕵️ **The Ultimate Android Exploitation Framework** 🕵️

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=25&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=435&lines=SYSTEM+BREACH+INITIATED;HACK+ANDROID+DEVICES;METERPRETER+IN+ONE+CLICK;YOUR+PHONE+IS+NOW+MINE)](https://git.io/typing-svg)


![Python](https://img.shields.io/badge/PYTHON-v3.10%2B-brightgreen?style=for-the-badge&logo=python)
![GitHub last commit](https://img.shields.io/github/last-commit/Athexhacker/ATHEX-SPY?color=yellow&label=UPDATED&style=for-the-badge&logo=github)
![GitHub Repo stars](https://img.shields.io/github/stars/Athexhacker/ATHEX-SPY?color=green&style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/Athexhacker/ATHEX-SPY?color=blue&style=for-the-badge&logo=github)

</div>

#### Complete Automation to get a Meterpreter session in One Click

This tool can automatically __Create__, __Install__, and __Run__ payload on the target device using __Metasploit-Framework__ and __ADB__ to completely hack the Android Device in one click if the device has open ADB port `TCP 5555`.

The goal of this project is to make penetration testing and vulnerability assessment on Android devices easy. Now you don't have to learn commands and arguments, ATHEX SPY does it for you. Using this tool, you can test the security of your Android devices easily.

> [!TIP]
> __ATHEX-SPY__ can also be used as a complete ADB Toolkit to perform various operations on Android devices over Wi-Fi as well as USB. 




## 📌 Overview

**ATHEX-SPY v2.0 Advanced** is a comprehensive Android exploitation, penetration testing, and forensic toolkit with **70+ powerful features**. This tool automates everything from basic ADB operations to advanced post-exploitation techniques including:

- 🔓 One-click Meterpreter session generation
- 🎯 Live keylogging via `getevent`
- 📍 GPS location tracking
- 📷 Remote camera capture
- 🎤 Microphone & device audio recording/streaming
- 🔐 WiFi password extraction
- 🌐 Network traffic capture with tcpdump
- 💉 Frida dynamic instrumentation
- 📱 Full device backup and system dump
- 🛡️ Lock screen bypass attempts
- 🔍 Vulnerability scanning for exported components

The goal is to provide security researchers and penetration testers with a complete toolkit for Android device assessment.

---

## 🚀 Features (70+ Total)

### 📄 PAGE 1 - Core ADB Operations (1-20)

| # | Feature | Description |
|---|---------|-------------|
| 1 | Connect a Device | Connect to device via ADB over TCP/IP |
| 2 | List Connected Devices | Display all connected ADB devices |
| 3 | Disconnect All Devices | Disconnect all ADB connections |
| 4 | Scan Network for Devices | Discover devices on local network using nmap |
| 5 | Mirror & Control Device | Full screen mirroring with scrcpy |
| 6 | Take Screenshot | Capture and pull screenshot |
| 7 | Screen Record | Record screen with custom duration |
| 8 | Download File/Folder | Pull files from device |
| 9 | Send File/Folder to Device | Push files to device |
| 10 | Run an App | Launch app by package name |
| 11 | Install an APK | Install APK from computer |
| 12 | Uninstall an App | Remove app by package name |
| 13 | List Installed Apps | Show all third-party packages |
| 14 | Access Device Shell | Interactive ADB shell |
| 15 | Hack Device (Metasploit) | One-click Meterpreter payload generation |
| 16 | List Files/Folders | Browse /sdcard contents |
| 17 | Send SMS | Send SMS via service call (experimental) |
| 18 | Copy WhatsApp Data | Extract WhatsApp media and databases |
| 19 | Copy All Screenshots | Bulk screenshot extraction |
| 20 | Copy All Camera Photos | Bulk photo extraction |

### 📄 PAGE 2 - Stealth & Information Gathering (21-40)

| # | Feature | Description |
|---|---------|-------------|
| 21 | Anonymous Screenshot | Screenshot + auto-delete from device |
| 22 | Anonymous Screen Record | Recording + auto-delete from device |
| 23 | Open a Link on Device | Launch URL in browser |
| 24 | Display a Photo on Device | Push and display image |
| 25 | Play an Audio on Device | Push and play audio file |
| 26 | Play a Video on Device | Push and play video file |
| 27 | Get Device Information | Model, OS, chipset, build details |
| 28 | Get Battery Information | Battery level, temp, health status |
| 29 | Restart Device | Normal system reboot |
| 30 | Advanced Reboot Options | Recovery, Bootloader, Fastboot |
| 31 | Unlock Device | Swipe + PIN/password input |
| 32 | Lock Device | Turn off screen |
| 33 | Dump All SMS | Extract SMS database |
| 34 | Dump All Contacts | Extract contacts database |
| 35 | Dump Call Logs | Extract call history |
| 36 | Extract APK from App | Pull APK from installed package |
| 37 | Stop ADB Server | Kill ADB daemon |
| 38 | Power Off Device | Shutdown device |
| 39 | Use Keycodes | Interactive remote control menu |
| 40 | Update ATHEX-SPY | Git pull latest version |

### 📄 PAGE 3 - Audio, Surveillance & Tracking (41-50)

| # | Feature | Description |
|---|---------|-------------|
| 41 | Record Mic Audio | Save microphone audio to file |
| 42 | Stream Mic Audio | Live microphone streaming |
| 43 | Record Device Audio | Capture internal device audio |
| 44 | Stream Device Audio | Live internal audio streaming |
| 45 | Mirror with Audio | scrcpy with audio support |
| 46 | Live Keylogger | Raw input event monitoring (getevent) |
| 47 | GPS Location Tracker | Extract location from dumpsys |
| 48 | Camera Snap | Trigger front/back camera |
| 49 | View Browsing History | Extract Chrome history database |
| 50 | Extract WiFi Passwords | Pull WifiConfigStore.xml or wpa_supplicant.conf |

### 📄 PAGE 4 - Forensics & Network Analysis (51-60)

| # | Feature | Description |
|---|---------|-------------|
| 51 | Full Device Backup | ADB backup (-apk -shared -all -system) |
| 52 | Network Traffic Capture | tcpdump packet capture |
| 53 | Bypass Lock Screen | Clear locksettings (requires root) |
| 54 | Install Burp Certificate | Push cert to system trust store |
| 55 | Screen Stream via Web | scrcpy V4L2/webcam stream |
| 56 | Live Logcat Stream | Real-time log monitoring |
| 57 | Vulnerability Scan | Detect exported activities/services |
| 58 | Dump System Info | Full dumpsys output |
| 59 | Open Reverse Shell | Netcat reverse connection |
| 60 | Check Root Status | Verify su binary access |

### 📄 PAGE 5 - Advanced Exploitation & Post-Exploitation (61-70)

| # | Feature | Description |
|---|---------|-------------|
| 61 | Brute Force PIN | 4-digit PIN simulation |
| 62 | Frida Server Setup | Push and start frida-server |
| 63 | Inject Frida Script | Load and run Frida JavaScript |
| 64 | Dump App Memory | Frida-based memory enumeration |
| 65 | Disable Play Protect | Turn off Google Play verification |
| 66 | Uninstall System App | Remove system packages (root) |
| 67 | List Running Processes | ps command output |
| 68 | Kill Process | Terminate by PID |
| 69 | Port Forwarding | Local to remote port mapping |
| 70 | Reboot to EDL Mode | Emergency Download Mode (Qualcomm) |

---

## 📋 Requirements

| Software | Purpose | Installation |
|----------|---------|--------------|
| **Python 3.10+** | Runtime environment | [python.org](https://www.python.org/) |
| **ADB** | Android Debug Bridge | [Platform Tools](https://developer.android.com/studio/releases/platform-tools) |
| **Metasploit Framework** | Payload generation & handler | [Metasploit](https://www.metasploit.com/) |
| **scrcpy** | Screen mirroring & audio | [scrcpy](https://github.com/Genymobile/scrcpy) |
| **nmap** | Network scanning | [nmap.org](https://nmap.org/) |
| **Frida** (Optional) | Dynamic instrumentation | [frida.re](https://frida.re/) |
| **tcpdump** (Optional) | Network capture | [tcpdump-android](https://github.com/extremecoders-re/tcpdump-android-builds) |





# Features 
## v1.0

* Connect device using ADB remotely.
* List connected devices.
* Disconnect all devices.
* Access connected device shell.
* Stop ADB Server.
* Take screenshot and pull it to computer automatically.
* Screen Record target device screen for a specified time and automatically pull it to computer.
* Download file/folder from target device.
* Send file/folder from computer to target device.
* Run an app.
* Install an APK file from computer to target device.
* Uninstall an app.
* List all installed apps in target device.
* Restart/Reboot the target device to `System`, `Recovery`, `Bootloader`, `Fastboot`.
* __Hack Device Completely__ : 
  - Automatically fetch your `IP Address` to set `LHOST`.
  - Automatically create a payload using `msfvenom`, install it, and run it on target device.
  - Then automatically launch and setup __Metasploit-Framework__ to get a `meterpreter` session.
  - Getting a `meterpreter` session means the device is completely hacked using Metasploit-Framework, and you can do anything with it.


## v1.1

* List all files and folders of the target devices.
* Copy all WhatsApp Data to computer.
* Copy all Screenshots to computer.
* Copy all Camera Photos to computer.
* Take screenshots and screen-record anonymously (Automatically delete file from target device).
* Open a link on target device.
* Display an image/photo on target device.
* Play an audio on target device.
* Play a video on target device.
* Get device information.
* Get battery information.
* Use Keycodes to control device remotely.


## v1.2

* Send SMS through target device.
* Unlock device (Automatic screen on, swipe up and password input).
* Lock device.
* Dump all SMS from device to computer.
* Dump all Contacts from device to computer.
* Dump all Call Logs from device to computer.
* Extract APK from an installed app.

## v1.3

* Mirror and Control the target device. 

## v1.4

* Power off the target device. 

## v1.5

* Scan local network for connected devices to get Target IP Address. 

## v1.6

* Record Microphone Audio
* Stream Microphone Audio
* Record Device Audio
* Stream Device Audio

## V2.0 (Current)
v2 Advanced (Current)
*✅ 70 total features across 5 interactive pages*

*✅ Live keylogger (getevent monitoring)*

*✅ GPS location tracking*

*✅ WiFi password extraction*

*✅ Camera snap (front/back)*

*✅ Chrome browsing history extraction*

*✅ Full device backup (ADB backup)*

*✅ Network capture with tcpdump*

*✅ Live logcat streaming*

*✅ Vulnerability scanning*

*✅ Frida integration (setup, script injection, memory dump)*

*✅ Reverse shell capability*

*✅ Port forwarding*

*✅ EDL reboot mode*

*✅ PIN brute force simulation*

*✅ Play Protect disable*

*✅ System app uninstallation*

*✅ Process management*

*✅ Burp Suite certificate installation*

*✅ Screen streaming via web*

v1.6 (Previous)
Initial release with core ADB features

Metasploit integration

Audio recording and streaming

# Requirements  
* [`python3`](https://www.python.org/) : Python 3.10 or Newer
* [`pip`](https://pip.pypa.io/en/stable/installation/) : Package installer for Python
* [`adb`](https://developer.android.com/studio/command-line/adb) : Android Debug Bridge (ADB) from `Android SDK Platform Tools`
* [`metasploit-framework`](https://www.metasploit.com/) : Metasploit-Framework (`msfvenom` and `msfconsole`)
* [`scrcpy`](https://github.com/Genymobile/scrcpy) : Scrcpy
* [`nmap`](https://nmap.org/) : Nmap


# Run ATHEX-SPY

__ATHEX-SPY__ does not need any installation and runs directly using `python3`

> [!IMPORTANT]
> **ATHEX-SPY** requires Python version __3.10 or higher__. Please update Python before running the program.

#### On Linux / macOS :

Make sure all the [required](https://github.com/Athexhacker/ATHEX-SPY#requirements) software are installed.

Open terminal and paste the following commands : 
```
git clone https://github.com/Athexhacker/ATHEX-SPY.git
```
```
cd ATHEX-SPY/
```
```
pip install -r requirements.txt
```
```
python3 ATHEX-SPY.py
```
#### On Windows :

Make sure all the [required](https://github.com/Athexhacker/ATHEX-SPY#requirements) software are installed.


Open terminal and paste the following commands : 
```
git clone https://github.com/Athexhacker/ATHEX-SPY.git
```
```
cd ATHEX-SPY/
```
```
pip install -r requirements.txt
```
1. Download and extract latest `platform-tools` from [here](https://developer.android.com/studio/releases/platform-tools.html#downloads).

2. Copy all files from the extracted `platform-tools` or `adb` directory to __ATHEX-SPY__ directory and then run :

```
python ATHEX-SPY.py
```

# Tutorial


## Setting up Android Phone for the first time

* __Enabling the Developer Options__

1. Open `Settings`.
2. Go to `About Phone`.
3. Find `Build Number`.
4. Tap on `Build Number` 7 times.
5. Enter your pattern, PIN or password to enable the `Developer options` menu.
6. The `Developer options` menu will now appear in your Settings menu.

* __Enabling USB Debugging__

1. Open `Settings`.
2. Go to `System` > `Developer options`.
3. Scroll down and Enable `USB debugging`.

* __Connecting with Computer__

1. Connect your Android device and `adb` host computer to a common Wi-Fi network.
2. Connect the device to the host computer with a USB cable.
3. Open a terminal in the computer and enter the following command :
```
adb devices
```
4. A pop-up will appear in the Android phone when you connect your phone to a new PC for the first time : `Allow USB debugging?`.
5. Click on `Always allow from this computer` check-box and then click `Allow`.
6. Then in the terminal enter the following command :
```
adb tcpip 5555
```
7. Now you can connect the Android Phone with the computer over Wi-Fi using `adb`.
8. Disconnect the USB cable.
9. Go to `Settings` >  `About Phone` > `Status` > `IP address` and note the phone's `IP Address`.
10. Run __ATHEX-SPY__ and select `Connect a device` and enter the target's `IP Address` to connect over Wi-Fi.



## Connecting the Android phone for the next time

1. Connect your Android device and host computer to a common Wi-Fi network.
2. Run __ATHEX-SPY__ and select `Connect a device` and enter the target's `IP Address` to connect over Wi-Fi.


## 🎯 Tested Platforms

*✅ Kali Linux -	Fully Supported*
*✅ Ubuntu 22.04+ -	Fully Supported*
*✅ Linux Mint -	Fully Supported*
*✅ Fedora -	Fully Supported*
*✅ Arch Linux -	Fully Supported*
*✅ Parrot OS	- Fully Supported*
*✅ Windows 11	- Supported*
*✅ Windows 10	- Supported*
*✅ macOS	- Supported*
[!NOTE]
Linux is recommended for full feature compatibility. Some advanced features (audio streaming, Frida, tcpdump) work best on Linux.

🛠️ Advanced Feature Setup
Frida Dynamic Instrumentation
bash
# Install Frida on host
pip install frida-tools

## Download frida-server for your device architecture
from:

```
https://github.com/frida/frida/releases

Rename to 'frida-server' and place in ATHEX-SPY directory
```
tcpdump Network Capture


## Download tcpdump binary for Android
from: 
```
https://github.com/extremecoders-re/tcpdump-android-builds/releases

Rename to 'tcpdump' and place in ATHEX-SPY directory
```

> [!NOTE]
> All the new features are primarily tested on **Linux**, thus **Linux** is recommended for running ATHEX-SPY.
Some features might not work properly on Windows.

# Installing ADB 

#### ADB on Linux :

Open terminal and paste the following commands :

* __Debian / Ubuntu__
```
sudo apt update
```
```
sudo apt install adb
```

* __Fedora__
```
sudo dnf install adb
```

* __Arch Linux / Manjaro__
```
sudo pacman -Sy android-tools
```

For other Linux Distributions : [Visit this Link](https://developer.android.com/studio/releases/platform-tools#downloads)

#### ADB on macOS :

Open terminal and paste the following command :

```
brew install android-platform-tools
```

or Visit this link : [Click Here](https://developer.android.com/studio/releases/platform-tools.html#downloads)

#### ADB on Windows :

Visit this link : [Click Here](https://developer.android.com/studio/releases/platform-tools.html#downloads)

#### ADB on Termux :
```
pkg update
```
```
pkg install android-tools
```


# Installing Metasploit-Framework 

#### On Linux / macOS :
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
 ```
 
or Follow this link : [Click Here](https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html#installing-metasploit-on-linux--macos)

or Visit this link : [Click Here](https://www.metasploit.com/download)

#### On Windows :

Visit this link : [Click Here](https://www.metasploit.com/download)

or Follow this link : [Click Here](https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html#windows-anti-virus-software-flags-the-contents-of-these-packages)

# Installing scrcpy

Visit the `scrcpy` GitHub page for latest installation instructions : [Click Here](https://github.com/Genymobile/scrcpy#get-the-app)

**On Windows** : Copy all the files from the extracted **scrcpy** folder to **PhoneSploit** folder.

> [!IMPORTANT]  
> If `scrcpy` is not available for your Linux distro like **Kali Linux**, then you can either manually install it : [Manual Guide](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md),
or build it with a few simple steps : [Build Guide](https://github.com/Genymobile/scrcpy/blob/master/doc/build.md#build-scrcpy)

# Installing Nmap

#### Nmap on Linux :

Open terminal and paste the following commands :

* __Debian / Ubuntu__
```
sudo apt update
```
```
sudo apt install nmap
```

* __Fedora__
```
sudo dnf install nmap
```

* __Arch Linux / Manjaro__
```
sudo pacman -Sy nmap
```

For other Linux Distributions : [Visit this Link](https://nmap.org/download.html)

#### Nmap on macOS :

Open terminal and paste the following command :

```
brew install nmap
```

or Visit this link : [Visit this Link](https://nmap.org/download.html)

#### Nmap on Windows :

Download and install the latest stable release : [Click Here](https://nmap.org/download.html#windows)

#### Nmap on Termux :
```
pkg update
```
```
pkg install nmap
```



# Disclaimer

* Neither the project nor its developer promote any kind of illegal activity and are not responsible for any misuse or damage caused by this project.
* This project is for educational purpose only.
* Please do not use this tool on other people's devices without their permission.
* Do not use this tool to harm others.
* Use this project responsibly on your own devices only.
* It is the end user's responsibility to obey all applicable local, state, federal, and international laws.
* contact for any kind of help about ethical hacking +92 3490916663




<div align="center">
Made with 💀 by ATHEX BLACK HAT

Copyright © 2025 Athexblackhat

</div> ```












