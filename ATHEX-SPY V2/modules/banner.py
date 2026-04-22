from modules.color import Color as C

version = "v3.0 Advanced"

banner_main = f"""
{C.RED}
{C.RED}   █████╗ ████████╗██╗  ██╗███████╗██╗  ██╗  ███████╗██████╗ ██╗   ██╗   
{C.RED}  ██╔══██╗╚══██╔══╝██║  ██║██╔════╝╚██╗██╔╝  ██╔════╝██╔══██╗╚██╗ ██╔╝   
{C.RED}  ███████║   ██║   ███████║█████╗   ╚███╔╝   ███████╗██████╔╝ ╚████╔╝    
{C.RED}  ██╔══██║   ██║   ██╔══██║██╔══╝   ██╔██╗   ╚════██║██╔═══╝   ╚██╔╝     
{C.RED}  ██║  ██║   ██║   ██║  ██║███████╗██╔╝ ██╗  ███████║██║        ██║      
{C.RED}  ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚══════╝╚═╝        ╚═╝      
{C.RED}                         ADB TOOLKIT VERSION 2.0                               {C.RESET}
        {C.YELLOW}{version}{C.RESET}        {C.WHITE}Created by ATHEX | +92 3490916663{C.RESET}
"""

# You can add more banners for different pages as before.
banner_page1 = banner_main
banner_page2 = f"""{C.CYAN}... (some ASCII art) ...{C.RESET}"""
# For simplicity, I'll reuse banner_main with a color change for different pages.
banner_list = [banner_main, banner_main, banner_main, banner_main, banner_main]

# Menus for 5 pages
menu1 = f"""
{C.WHITE} 1. {C.GREEN}Connect a Device              {C.WHITE}11. {C.GREEN}Install an APK
{C.WHITE} 2. {C.GREEN}List Connected Devices        {C.WHITE}12. {C.GREEN}Uninstall an App
{C.WHITE} 3. {C.GREEN}Disconnect All Devices        {C.WHITE}13. {C.GREEN}List Installed Apps
{C.WHITE} 4. {C.GREEN}Scan Network for Devices      {C.WHITE}14. {C.GREEN}Access Device Shell
{C.WHITE} 5. {C.GREEN}Mirror & Control Device       {C.WHITE}15. {C.GREEN}Hack Device (Metasploit)
{C.WHITE} 6. {C.GREEN}Take Screenshot               {C.WHITE}16. {C.GREEN}List Files/Folders
{C.WHITE} 7. {C.GREEN}Screen Record                 {C.WHITE}17. {C.GREEN}Send SMS
{C.WHITE} 8. {C.GREEN}Download File/Folder          {C.WHITE}18. {C.GREEN}Copy WhatsApp Data
{C.WHITE} 9. {C.GREEN}Send File/Folder to Device    {C.WHITE}19. {C.GREEN}Copy All Screenshots
{C.WHITE}10. {C.GREEN}Run an App                    {C.WHITE}20. {C.GREEN}Copy All Camera Photos
{C.YELLOW}  N : Next Page  |  P : Previous Page  |  99 : Clear  |  0 : Exit  (Page 1/5){C.RESET}
"""

menu2 = f"""
{C.WHITE}21. {C.GREEN}Anonymous Screenshot          {C.WHITE}31. {C.GREEN}Unlock Device
{C.WHITE}22. {C.GREEN}Anonymous Screen Record       {C.WHITE}32. {C.GREEN}Lock Device
{C.WHITE}23. {C.GREEN}Open a Link on Device         {C.WHITE}33. {C.GREEN}Dump All SMS
{C.WHITE}24. {C.GREEN}Display a Photo on Device     {C.WHITE}34. {C.GREEN}Dump All Contacts
{C.WHITE}25. {C.GREEN}Play an Audio on Device       {C.WHITE}35. {C.GREEN}Dump Call Logs
{C.WHITE}26. {C.GREEN}Play a Video on Device        {C.WHITE}36. {C.GREEN}Extract APK from App
{C.WHITE}27. {C.GREEN}Get Device Information        {C.WHITE}37. {C.GREEN}Stop ADB Server
{C.WHITE}28. {C.GREEN}Get Battery Information       {C.WHITE}38. {C.GREEN}Power Off Device
{C.WHITE}29. {C.GREEN}Restart Device                {C.WHITE}39. {C.GREEN}Use Keycodes (Control)
{C.WHITE}30. {C.GREEN}Advanced Reboot Options       {C.WHITE}40. {C.GREEN}Update ATHEX-SPY
{C.YELLOW}  N : Next Page  |  P : Previous Page  |  99 : Clear  |  0 : Exit  (Page 2/5){C.RESET}
"""

menu3 = f"""
{C.WHITE}41. {C.GREEN}Record Mic Audio               {C.WHITE}46. {C.GREEN}Live Keylogger (getevent)
{C.WHITE}42. {C.GREEN}Stream Mic Audio               {C.WHITE}47. {C.GREEN}GPS Location Tracker
{C.WHITE}43. {C.GREEN}Record Device Audio            {C.WHITE}48. {C.GREEN}Camera Snap (Front/Back)
{C.WHITE}44. {C.GREEN}Stream Device Audio            {C.WHITE}49. {C.GREEN}View Browsing History
{C.WHITE}45. {C.GREEN}Mirror with Audio              {C.WHITE}50. {C.GREEN}Extract WiFi Passwords
{C.YELLOW}  N : Next Page  |  P : Previous Page  |  99 : Clear  |  0 : Exit  (Page 3/5){C.RESET}
"""

menu4 = f"""
{C.WHITE}51. {C.GREEN}Full Device Backup (adb backup) {C.WHITE}56. {C.GREEN}Live Logcat Stream
{C.WHITE}52. {C.GREEN}Network Traffic Capture (tcpdump) {C.WHITE}57. {C.GREEN}Vulnerability Scan (Exported)
{C.WHITE}53. {C.GREEN}Bypass Lock Screen (Attempt)    {C.WHITE}58. {C.GREEN}Dump System Info
{C.WHITE}54. {C.GREEN}Install Burp Certificate        {C.WHITE}59. {C.GREEN}Open Reverse Shell
{C.WHITE}55. {C.GREEN}Screen Stream via Web           {C.WHITE}60. {C.GREEN}Check Root Status
{C.YELLOW}  N : Next Page  |  P : Previous Page  |  99 : Clear  |  0 : Exit  (Page 4/5){C.RESET}
"""

menu5 = f"""
{C.WHITE}61. {C.GREEN}Brute Force PIN (4-digit)      {C.WHITE}66. {C.GREEN}Uninstall System App
{C.WHITE}62. {C.GREEN}Frida Server Setup             {C.WHITE}67. {C.GREEN}List Running Processes
{C.WHITE}63. {C.GREEN}Inject Frida Script            {C.WHITE}68. {C.GREEN}Kill Process
{C.WHITE}64. {C.GREEN}Dump App Memory                {C.WHITE}69. {C.GREEN}Port Forwarding
{C.WHITE}65. {C.GREEN}Disable Play Protect           {C.WHITE}70. {C.GREEN}Reboot to EDL Mode
{C.YELLOW}  P : Previous Page  |  99 : Clear  |  0 : Exit  (Page 5/5){C.RESET}
"""

menu = [menu1, menu2, menu3, menu4, menu5]