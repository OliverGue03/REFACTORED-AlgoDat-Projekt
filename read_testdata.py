import os
import glob

def find_networks():
    return sorted(glob.glob("*.json"))

def select_network():

    networks = find_networks()

    if not networks:
        print("No networks have been found.")
        return ""
    
    print("\nAvailable networks")
    print("="*50)

    for i, filename in enumerate(networks, 1):
        size = os.path.getsize(filename)
        size_str = f"{size} B" if size < 1024 else f"{size/1024:.1f} KB"
        print(f" [{i}] {filename:<30} ({size_str})")

    print(f" [0] Cancel")
    print("="*50)

    while True:
        try:
            choice = int(input("\nChoose network: ").strip())

            if choice == 0:
                return ""
            
            if 1 < choice < len(networks):
                return networks[choice - 1]
            else:
                print(f"Please choose a number between 0 and {len(networks)}.")
        
        except ValueError:
            print("Please choose a correct number.")