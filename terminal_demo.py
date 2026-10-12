import time
import random
import sys

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

def show_banner():
    banner = f"""
{RED}██████╗ ██╗    ██╗███╗   ███╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗{RESET}
{RED}██   ██╗██║    ██║████╗ ████║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝{RESET}
{RED}██   █╔╝██║ █╗ ██║██╔████╔██║    ███████║███████║██║     █████╔╝    ██║   {RESET}
{RED}██   ██ ██║███╗██║██║╚██╔╝██║    ██╔══██║██╔══██║██║     ██╔═██╗    ██║   {RESET}
{RED}██    █ ╚███╔███╔╝██║ ╚═╝ ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   {RESET}
{RED}███████  ╚══╝╚══╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   {RESET}
{MAGENTA}          DWM HackIT v3.0 - Elite Edition{RESET}
"""
    print(banner)

def cinematic_loading(task_name, duration=12, special_message=None):
    print(f"\n{CYAN}{task_name}{RESET}")
    for i in range(101):
        time.sleep(duration / 100)
        sys.stdout.write(f"\r{MAGENTA}[{'=' * (i // 2)}{' ' * (50 - i // 2)}] {i}%{RESET}")
        sys.stdout.flush()
        if special_message and i == 50:
            print(f"\n{RED}{special_message}{RESET}")
    print("\n")

def network_infiltration():
    print(f"{CYAN}[+] Initializing Network Infiltration Protocols...{RESET}")
    
    cinematic_loading("[*] Scanning for active devices in the network...", 10)
    for _ in range(6):
        ip = f"203.0.113.{random.randint(1, 254)}"  # documentation-only addresses
        os = random.choice(["Linux", "Windows Server", "IoT Device", "MacOS"])
        print(f"{GREEN}[DEVICE DETECTED] IP: {ip} - OS: {os}{RESET}")
        time.sleep(1.2)

    cinematic_loading("[*] Identifying vulnerabilities in detected devices...", 8)
    for _ in range(4):
        vuln = f"Vulnerability-{random.randint(100, 999)}"
        severity = random.choice(["Low", "Medium", "High", "Critical"])
        print(f"{RED}[VULNERABILITY] {vuln} - Severity: {severity}{RESET}")
        time.sleep(1.5)
    
    cinematic_loading("[*] Gaining access to the network...", 7)
    print(f"{GREEN}[+] Access to network established.{RESET}")
    time.sleep(1)

def data_extraction():
    print(f"{CYAN}[+] Initializing Data Extraction Protocols...{RESET}")
    
    cinematic_loading("[*] Scanning for sensitive data...", 12)
    for _ in range(5):
        file_name = f"file_{random.randint(1000, 9999)}.pdf"
        data_size = random.randint(50, 500)
        print(f"{GREEN}[FILE DETECTED] {file_name} - Size: {data_size}MB{RESET}")
        time.sleep(1.5)

    cinematic_loading("[*] Extracting data...", 10)
    print(f"{GREEN}[+] Data extraction completed successfully!{RESET}")
    time.sleep(1)

def secure_connection_setup():
    print(f"{CYAN}[+] Initializing Secure Connection Setup...{RESET}")
    
    cinematic_loading("[*] Establishing encrypted channel...", 10)
    print(f"{GREEN}[+] Secure connection established!{RESET}")
    time.sleep(1)

def show_tools_menu():
    print(f"\n{MAGENTA}Select an operation to perform:{RESET}")
    print(f"{CYAN}1. Network Infiltration{RESET}")
    print(f"{CYAN}2. Data Extraction{RESET}")
    print(f"{CYAN}3. Secure Connection Setup{RESET}")
    print(f"{CYAN}4. Exit{RESET}")

def main():
    print("SIMULATION ONLY - no network scanning, access, or data extraction occurs.\n")
    show_banner()
    
    while True:
        show_tools_menu()
        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == "1":
            network_infiltration()
        elif choice == "2":
            data_extraction()
        elif choice == "3":
            secure_connection_setup()
        elif choice == "4":
            print(f"{GREEN}[+] Exiting DWM HackIT...{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid choice. Please select a valid option.{RESET}")

if __name__ == "__main__":
    main()
