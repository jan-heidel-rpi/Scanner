import os
import platform

import requests
from bs4 import BeautifulSoup

MAC_URL = "http://standards-oui.ieee.org/oui.txt"

class Vendor_Download(object):
    def __init__(self):
        if platform.system() == "Windows":
            self.MAC_ADDRESS_PATH = os.path.dirname(os.path.realpath(__file__)) + "\mac_vendor.txt"
        else:
            self.MAC_ADDRESS_PATH = os.path.dirname(os.path.realpath(__file__)) + "/Hack_module.txt"
        self.download()
    def download(self):
        if os.path.exists(self.MAC_ADDRESS_PATH):
            os.remove(self.MAC_ADDRESS_PATH)
        addresses = requests.get(url=MAC_URL)
        soup = BeautifulSoup(addresses.text, "lxml").text
        with open(self.MAC_ADDRESS_PATH, "a", encoding="utf8") as MAC_ADDRESS:
            for line in soup.split("\n"):
                if "(base 16)" in line:
                    MAC_ADDRESS.write(line.replace("(base 16)", ""))