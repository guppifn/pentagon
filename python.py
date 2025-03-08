import os
import time
import random
from faker import Faker
from pyfiglet import Figlet
from termcolor import colored
import tkinter as tk
from tkinter import filedialog

# Set up folder paths in Documents/Python
base_folder = os.path.join(os.path.expanduser("~"), "Documents", "Python")
credentials_folder = os.path.join(base_folder, "credentials")
classified_folder = os.path.join(base_folder, "classified")
os.makedirs(credentials_folder, exist_ok=True)
os.makedirs(classified_folder, exist_ok=True)

# Global flag to ensure "Access Database" is run before any other option
database_accessed = False

# ASCII skull animation frames (using raw string literals)
skull_frame1 = r"""
                        │
                        pN▒g▒p▒g▒▒g▒ge
                       ▒▒▒▒▒▒▒░░▒░▒░▒
                     _0▒░▒░▒░░▒▒▒▒▒▒▒!
                     4▒▒▒▒▒░░░▒░░▒▒▒▒▒Y
                     │` ~~#00░░0 MMM"M│
                          `gM░M7
                    │       00q0       │
      J0IN          #▒____g▒0░░P______0
                    #▒0g_p#░░04▒▒&,__M#
       U5           0▒▒▒▒▒00   ]0▒▒▒▒00
                     │\j▒▒0'  `0▒▒▒4M'
                      │\#▒▒&▒▒gg▒▒0& │
                     " ▒▒00▒▒▒▒00▒▒'d
                     %  ¼▒  ~P▒¼▒▒│¼¼│
                     M▒9  ▒▒      ▒j,g
                     l▒g▒   @▒9     ▒
                      ~▒0▒▒▒p ▒g▒  %
                        @░▒▒▒▒▒  ▒▒░
                         M0░░  ░░^
                           `
"""

skull_frame2 = r"""
                        │
                        pN▒g▒p▒g▒▒g▒ge
                       ▒▒▒▒▒▒▒░░▒░▒░▒
                     _0▒░▒░▒░░▒▒▒▒▒▒▒!
                     4▒▒▒▒▒░░░▒░░▒▒▒▒▒Y
                     │` ~~#00░░0 MMM"M│
                          `gM░M7
                    │       00q0       │
                    │       \   /       │
      J0IN          #▒____g▒0░░P______0
                    #▒0g_p#░░04▒▒&,__M#
       U5           0▒▒▒▒▒00   ]0▒▒▒▒00
                     │\j▒▒0'  `0▒▒▒4M'
                      │\#▒▒&▒▒gg▒▒0& │
                     " ▒▒00▒▒▒▒00▒▒'d
                     %  ¼▒  ~P▒¼▒▒│¼¼│
                     M▒9  ▒▒      ▒j,g
                     l▒g▒   @▒9     ▒
                      ~▒0▒▒▒p ▒g▒  %
                        @░▒▒▒▒▒  ▒▒░
                         M0░░  ░░^
                           `
"""

def animate_skull(duration=5):
    """Animates a skull (opening and closing its mouth) for a given duration."""
    start = time.time()
    frames = [skull_frame1, skull_frame2]
    i = 0
    while time.time() - start < duration:
        clear_screen()
        print(colored(frames[i % 2], "green"))
        time.sleep(0.5)
        i += 1
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_loading(task):
    print(colored(f"[+] {task}...", "green"))
    for _ in range(random.randint(3, 7)):
        print(colored(
            f"[~] {random.choice(['Decrypting...', 'Bypassing Firewall...', 'Establishing Secure Connection...', 'Fetching Data...', 'Uploading Payload...', 'Injecting Exploit...', 'Brute-forcing Encryption...'])}",
            "yellow"))
        time.sleep(random.uniform(0.5, 1.5))
    print(colored(f"[✓] {task} Completed!", "cyan"))
    print()

def generate_data():
    fake = Faker()
    file_path = os.path.join(credentials_folder, "credentials.txt")
    with open(file_path, "w") as f:
        for _ in range(20):
            # Generate email with @defense.gov domain
            email = fake.email().split('@')[0] + "@defense.gov"
            password = fake.password()
            ssn = fake.ssn()
            bank = fake.bank_country()
            f.write(f"Email: {email} | Password: {password} | SSN: {ssn} | Bank: {bank}\n")
    print(colored(f"[+] Credentials saved to {file_path}", "green"))

def generate_pentagon_docs():
    html_path = os.path.join(classified_folder, "classified_links.html")
    links = [
        "https://nara-media-001.s3.amazonaws.com/arcmedia/research/pentagon-papers/Pentagon-Papers-Index.pdf",
        "https://catalog.archives.gov/id/5890484",
        "https://nara-media-001.s3.amazonaws.com/arcmedia/research/pentagon-papers/Pentagon-Papers-Part-I.pdf",
        "https://catalog.archives.gov/id/5890485",
        "https://nara-media-001.s3.amazonaws.com/arcmedia/research/pentagon-papers/Pentagon-Papers-Part-II.pdf"
    ]
    with open(html_path, "w") as f:
        f.write("""<html>
<head>
    <title>Classified Pentagon Documents</title>
    <style>
        body {color: green; font-family: 'Bloody'; background-color: black; text-align: center;}
        h1 {text-decoration: underline;}
        ol {padding: 0; text-align: left; display: inline-block;}
        li {margin: 10px; font-size: 18px;}
        a {color: lime; text-decoration: none;}
        a:hover {text-decoration: underline;}
    </style>
</head>
<body>
    <h1>Leaked Pentagon Papers</h1>
    <ol>""")
        for i, link in enumerate(links, 1):
            f.write(f"<li><a href='{link}' target='_blank'>{link}</a></li>")
        f.write("</ol></body></html>")
    print(colored(f"[+] Classified document links saved: {html_path}", "green"))

def hide_ip():
    print(colored("[+] Activating IP Masking...", "green"))
    time.sleep(2)
    print(colored("[✓] IP hidden successfully!", "cyan"))

def upload_to_onionshare():
    # Open a file picker to select a folder under the base folder
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder = filedialog.askdirectory(initialdir=base_folder, title="Select a folder to upload to OnionShare")
    if folder:
        fake_loading("Uploading to OnionShare")
        print(colored(f"[+] Folder '{folder}' uploaded to OnionShare (simulated).", "cyan"))
    else:
        print(colored("[!] No folder selected.", "red"))
    input("Press Enter to continue...")

def main_menu():
    global database_accessed
    # Show skull animation on startup
    animate_skull(duration=5)
    
    while True:
        clear_screen()
        elite_font = Figlet(font='bloody')
        # Changed title from "PYTHON HACK" to "PYTHON"
        print(colored(elite_font.renderText("PYTHON"), "green"))
        print(colored("\n[1] DDoS Attack", "green"))
        print(colored("[2] Leak Admin Credentials", "green"))
        print(colored("[3] Retrieve Classified Pentagon Docs", "green"))
        print(colored("[4] Upload to OnionShare", "green"))
        print(colored("[5] Exit", "green"))
        
        choice = input(colored("\nSelect an option: ", "green")).strip()
        
        # Enforce that "Access Database" runs first before any option (except Exit)
        if choice != "5" and not database_accessed:
            fake_loading("Accessing Database")
            database_accessed = True

        if choice == "1":
            fake_loading("Launching DDoS Attack")
        elif choice == "2":
            fake_loading("Leaking Admin Credentials")
            generate_data()
        elif choice == "3":
            fake_loading("Hacking Pentagon Database")
            generate_pentagon_docs()
        elif choice == "4":
            upload_to_onionshare()
        elif choice == "5":
            print(colored("Exiting...", "red"))
            break
        else:
            print(colored("Invalid choice. Try again.", "red"))
            input("Press Enter to continue...")
            continue
        
        # After processing a valid option (except exit), automatically hide IP.
        hide_ip()
        input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
