import scapy
from ping3 import ping
from scapy.layers.inet import TCP, IP, ICMP
from scapy.sendrecv import sr, sr1
from .lookup import Lookup
import csv

class Fast_scans(object):

    def Basic(i, Ip, op_verbose):
        host_ip = Ip + str(i)
        print(host_ip)
        response = ping(host_ip, timeout=0.5)
        if response == None:
            pass

        else:
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            # hostname = socket.sethostname(host_ip)
            try:
                hersteller = Lookup.search(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
            except:
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
    def Normal(i, Ip, op_verbose):
        host_ip = Ip + str(i)
        print(host_ip)
        response = ping(host_ip, timeout=0.5)
        if response == None:
            pass

        else:
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            # hostname = socket.sethostname(host_ip)
            try:
                hersteller = Lookup.search(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
            except:
                port_list = []
                for n in range(1, 1001):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])

    def Hard(i, Ip, op_verbose):
        host_ip = Ip + str(i)
        print(host_ip)
        response = ping(host_ip, timeout=0.5)
        if response == None:
            pass

        else:
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            # hostname = socket.sethostname(host_ip)
            try:
                hersteller = Lookup.search(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
            except:
                port_list = []
                for n in range(1, 65536):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
    def Ping(i, Ip):
        host_ip = Ip + str(i)
        print(host_ip)
        response = ping(host_ip, timeout=0.5)
        if response == None:
            pass

        else:
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            # hostname = socket.sethostname(host_ip)
            try:
                hersteller = Lookup.search(mac)
                port_list = []
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller," "])
            except:
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, " "])
class Range_Scans(object):
        def Basic(i, Ip, op_verbose):
            host_ip = Ip + str(i)
            print(host_ip)
            response = ping(host_ip, timeout=0.5)
            if response == None:
                pass

            else:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                print(mac)
                # hostname = socket.sethostname(host_ip)
                try:
                    hersteller = Lookup.search(mac)
                    print(hersteller)
                    port_list = []
                    for n in range(1, 100):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open(tcp)")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
                except:
                    port_list = []
                    for n in range(1, 100):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open(tcp)")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", 'hersteller', ports])

        def Normal(i, Ip, op_verbose):
            host_ip = Ip + str(i)
            print(host_ip)
            response = ping(host_ip, timeout=0.5)
            if response == None:
                pass

            else:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                print(mac)
                # hostname = socket.sethostname(host_ip)
                try:
                    hersteller = Lookup.search(mac)
                    port_list = []
                    for n in range(1, 100):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
                except:
                    port_list = []
                    for n in range(1, 1001):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, ports])

        def Hard(i, Ip, op_verbose):
            host_ip = Ip + str(i)
            print(host_ip)
            response = ping(host_ip, timeout=0.5)
            if response == None:
                pass

            else:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                print(mac)
                # hostname = socket.sethostname(host_ip)
                try:
                    hersteller = Lookup.search(mac)
                    port_list = []
                    for n in range(1, 100):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
                except:
                    port_list = []
                    for n in range(1, 65536):
                        port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.5)
                        if port_response:
                            if port_response[TCP].flags == 18:
                                print(str(n) + " Port open")
                                port_list.append(str(n) + ";")
                            else:
                                print(str(n) + " Port not open")
                    ports = "".join(port_list)
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, ports])

        def Ping(i, Ip):
            host_ip = Ip + str(i)
            print(host_ip)
            response = ping(host_ip, timeout=0.5)
            if response == None:
                pass

            else:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                print(mac)
                # hostname = socket.sethostname(host_ip)
                try:
                    hersteller = Lookup.search(mac)
                    port_list = []
                    with open('rangescan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, " "])
                except:
                    with open('range_scan.csv', 'a', newline='') as Scan_file:
                        writer = csv.writer(Scan_file)
                        writer.writerow([host_ip, mac, "Hostname", hersteller, " "])












