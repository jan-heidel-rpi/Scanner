import platform
import platform
import re
import os

MAC_URL = "http://standards-oui.ieee.org/oui.txt"


class Lookup(object):
    def search(mac):
        if platform.system() == "Windows":
            MAC_ADDRESS_PATH = os.path.dirname(os.path.realpath(__file__)) + "\mac_vendor.txt"
        else:
            MAC_ADDRESS_PATH = os.path.dirname(os.path.realpath(__file__)) + "/Hack_module.txt"

        # Check if we have the MAC address list, if not, ask if user wants to download it

        # Check if enough arguments are provided, else, verify input
        # Make format equal to our datas format so that we can process it properly
        mac_address = mac.replace(":", "").replace("-", "").upper()
        print(mac_address)
        # Verify MAC address
        if not re.match("^([0-9A-Fa-f]{12})$", mac_address):
            print("[!] Invalid MAC address\n")

        with open(MAC_ADDRESS_PATH, "r", encoding="utf8") as m:
            # Compare entered MAC address with addresses in text file
            MAC_ADDRESS = m.read()
            for address in MAC_ADDRESS.split("\n"):
                if address[0:6] == mac_address[0:6]:
                    return address[7:].strip()
                    break
            else:
                return "[!] MAC address not found"
