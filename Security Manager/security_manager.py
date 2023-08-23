import subprocess
import ctypes

# Running Commands with administrative privileges

def run_as_admin(command):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", command, None, None, 1)
    except Exception as e:
        print("Error:", e)

# Disabling USB ports using Windows Registry
def disable_usb_ports():
    try:
        subprocess.run(['reg', 'add', r'HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR', '/v', 'Start', '/t', 'REG_DWORD', '/d', '4', '/f'], check=True)
        print("USB ports have been disabled.")
    except subprocess.CalledProcessError:
        print("Failed to disable USB ports.")

# Disabling Bluetooth using Windows Registry
def disable_bluetooth():
    try:
        subprocess.run(['reg', 'add', r'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\bluetooth', '/v', 'Value', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
        print("Bluetooth has been disabled.")
    except subprocess.CalledProcessError:
        print("Failed to disable Bluetooth.")

# Restricting Command Prompt access using Group Policy (gpedit.msc)
def restrict_command_prompt():
    command = "gpedit.msc"
    run_as_admin(command)

# Blocking access to a specific website using the hosts file
def block_website(website):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    try:
        with open(hosts_path, "a") as hosts_file:
            hosts_file.write("127.0.0.1 {}\n".format(website))
        print("Access to {} has been blocked.".format(website))
    except Exception as e:
        print("Error:", e)

def main():
    # Applying security measures
    disable_usb_ports()
    disable_bluetooth()  # Fixed function call here
    restrict_command_prompt()
    block_website("facebook.com")

if __name__ == "__main__":
    main()