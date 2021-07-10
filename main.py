import os
import socket
import sys
import threading
import time
import webbrowser
from datetime import datetime

import scapy.layers.l2
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QTableWidgetItem
)
from PyQt6.uic import loadUi
from scapy.layers.inet import TCP,IP
from scapy.sendrecv import sr1
from mac_vendor_lookup import MacLookup
from ping3 import ping
import csv
# import schedule
from Gui.main_window_ui import Ui_MainWindow
from Gui.make_config_dia import Ui_Form
from PyQt6.QtCore import QObject, QThread, pyqtSignal


op_verbose=False

timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
url = "https://realpython.com/qt-designer-python/"


def statup():
    with open('range_scan.csv', 'w', newline='') as Scan_file:
        writer = csv.writer(Scan_file)
        writer.writerow(["header", "header", "header", "header", "header"])
    with open('scan.csv', 'w', newline='') as Scan_file:
        writer = csv.writer(Scan_file)
        writer.writerow(["header", "header", "header", "header", "header"])


class Worker(QObject, Ui_MainWindow):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    mac_addr = pyqtSignal(str)

    def run(self):
        for i in range(1, 255):
            print(i)
            th = threading.Thread(target=self.Ping(i), args=(1,))
            th.start()
            self.progress.emit(i + 1)

        self.finished.emit()

    def runBasic(self):
        for i in range(1, 255):
            print(i)
            th = threading.Thread(target=self.Basic(i), args=(1,))
            th.start()
            self.progress.emit(i + 1)

        self.finished.emit()

    def runNormal(self):
        # os.remove("scan.csv")
        for i in range(1, 255):
            print(i)
            th = threading.Thread(target=self.Normal(i), args=(1,))
            th.start()
            self.progress.emit(i + 1)

        self.finished.emit()

    def runHard(self):
        # os.remove("scan.csv")
        for i in range(1, 255):
            print(i)
            th = threading.Thread(target=self.Hard(i), args=(1,))
            th.start()
            self.progress.emit(i + 1)

        self.finished.emit()

    def Basic(self, i):
        host_ip = "192.168.1." + str(i)
        print(host_ip)
        response=ping(host_ip,timeout=0.2)
        if response == None:
            print('hallo')
        else:
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            # hostname = socket.sethostname(host_ip)
            try:
                #print("test")
                hersteller = MacLookup().lookup(mac)
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
                self.mac_addr.emit(mac)
                # print(host_ip)
            except KeyError:
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", "None", ports])
                self.mac_addr.emit(mac)

    def Ping(self, i):
        host_ip = "192.168.1." + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        if response == None:
            pass
        else:
            # hostname = socket.sethostname(host_ip)
            try:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                print("test")
                hersteller = MacLookup().lookup(mac)
                print(hersteller)
                with open('scan.csv', 'a', newline='') as Temperatur_file:
                    print("thread fertig")
                    writer = csv.writer(Temperatur_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, "Offene_ports"])
                    self.mac_addr.emit(mac)

            except KeyError:
                mac = scapy.layers.l2.getmacbyip(host_ip)
                with open('scan.csv', 'a', newline='') as Temperatur_file:
                    writer = csv.writer(Temperatur_file)
                    writer.writerow([host_ip, mac, "Hostname", "None", "Offene_ports"])
                    self.mac_addr.emit(mac)

    def Normal(self, i):

        host_ip = "192.168.1." + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        print(response)
        if response == None:
            print('hallo')
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            socket.gethostbyaddr(host_ip)
            try:

                hersteller = MacLookup().lookup(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n) + ";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('rscan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
                self.mac_addr.emit(mac)
            except KeyError:
                pass

    def Hard(self, i):
        host_ip = "192.168.1." + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        print(response)
        if response == None:
            print('hallo')
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            try:
                hersteller = MacLookup().lookup(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
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
                    # print(host_ip)
                self.mac_addr.emit(mac)
            except KeyError:
                pass



class MainWindow(QMainWindow, Ui_MainWindow):

    global ipaddr
    def __init__(self, parent=None):
        super().__init__(parent)
        self.worker = Worker()
        self.thread = QThread()
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setWindowTitle('Net Scan')

    def connectSignalsSlots(self):
        self.action_New_cofig.triggered.connect(self.Scan)
        self.actionDoc.triggered.connect(self.doc)
        self.aktualisieren.clicked.connect(self.csvreader)
        self.actionputty.triggered.connect(self.ssh)
        self.pingScan.clicked.connect(self.Pingscan)
        self.basicScan.clicked.connect(self.BasicScan)
        self.NormalScan.clicked.connect(self.normalScan)
        self.HardScan.clicked.connect(self.hardScan)
        self.tabel.cellDoubleClicked.connect(self.click)

    def click(self, row, colum):
        #print(row)
        #print(colum)
        test=self.tabel.item(row,0)
        cell=test.text()
        os.system("putty.exe "+cell)
        print(cell)
    def ssh(self,row, col):

        print(self.tabel.item(row,col))

    def csvreader(self):
        self.tabel.setRowCount(0)
        with open("range_scan.csv", 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.tabel.rowCount()
                self.tabel.insertRow(row)
                self.tabel.setItem(row, 0, QTableWidgetItem(line[0]))
                self.tabel.setItem(row, 1, QTableWidgetItem(line[1]))
                self.tabel.setItem(row, 2, QTableWidgetItem(line[2]))
                self.tabel.setItem(row, 3, QTableWidgetItem(line[3]))
                self.tabel.setItem(row, 4, QTableWidgetItem(line[4]))

    def readping(self):
        self.tabel.setRowCount(0)
        with open("scan.csv", 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.tabel.rowCount()
                self.tabel.insertRow(row)
                self.tabel.setItem(row, 0, QTableWidgetItem(line[0]))
                self.tabel.setItem(row, 1, QTableWidgetItem(line[1]))
                self.tabel.setItem(row, 2, QTableWidgetItem(line[2]))
                self.tabel.setItem(row, 3, QTableWidgetItem(line[3]))

    def readbasic(self):
        print('hallo')
        self.tabel.setRowCount(0)
        with open("scan.csv", 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.tabel.rowCount()
                self.tabel.insertRow(row)
                self.tabel.setItem(row, 0, QTableWidgetItem(line[0]))
                self.tabel.setItem(row, 1, QTableWidgetItem(line[1]))
                self.tabel.setItem(row, 2, QTableWidgetItem(line[2]))
                self.tabel.setItem(row, 3, QTableWidgetItem(line[3]))
                self.tabel.setItem(row, 4, QTableWidgetItem(line[4]))

    def readnormal(self):
        print('hallo')
        self.tabel.setRowCount(0)
        with open("scan.csv", 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.tabel.rowCount()
                self.tabel.insertRow(row)
                self.tabel.setItem(row, 0, QTableWidgetItem(line[0]))
                self.tabel.setItem(row, 1, QTableWidgetItem(line[1]))
                self.tabel.setItem(row, 2, QTableWidgetItem(line[2]))
                self.tabel.setItem(row, 3, QTableWidgetItem(line[3]))
                self.tabel.setItem(row, 4, QTableWidgetItem(line[4]))

    def Pingscan(self):
        #os.remove("scan.csv")
        print("start ping")
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        self.worker.mac_addr.connect(self.readping)
        # Step 6: Start the thread
        self.thread.start()
    def BasicScan(self):
        # os.remove("scan.csv")
        # Step 2: Create a QThread object
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.runBasic)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        self.worker.mac_addr.connect(self.readbasic)
        # Step 6: Start the thread
        self.thread.start()

    def normalScan(self):
        # os.remove("scan.csv")
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.runNormal)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        self.worker.mac_addr.connect(self.readnormal)
        # Step 6: Start the thread
        self.thread.start()

    def hardScan(self):
        # os.remove("scan.csv")
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.runHard)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        self.worker.mac_addr.connect(self.csvreader)
        # Step 6: Start the thread
        self.thread.start()

    def doc(self):
        webbrowser.open_new(url)

    def Scan(self):
        new = Scan(self)
        new.exec()


class Scan(QDialog, Ui_Form, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi("Gui/config.ui")
        loadUi("Gui/config.ui", self)
        self.connection()
        self.setWindowTitle("Make Config")

    def connection(self):
        self.cancel.clicked.connect(self.close)
        self.create_buttton.clicked.connect(self.config)
        # self.act

    def basic_scan(self, i):
        host_ip = ipaddr + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        if response == None:
            pass
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            try:
                hersteller = MacLookup().lookup(mac)
                port_list=[]
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
                    if port_response:
                        if port_response[TCP].flags == 18:
                            print(str(n) + " Port open")
                            port_list.append(str(n)+";")
                        else:
                            print(str(n) + " Port not open")
                ports = "".join(port_list)
                with open('range_scan.csv', 'a', newline='') as Scan_file:
                    writer = csv.writer(Scan_file)
                    writer.writerow([host_ip, mac, "Hostname", hersteller, ports])
                print(ports)
                # print(host_ip)
            except KeyError:
                pass

    def Normal_scan(self, i, port):
        host_ip = ipaddr + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        if response == None:
            pass
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            socket.gethostbyaddr(host_ip)
            try:
                hersteller = MacLookup().lookup(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
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

            except KeyError:
                pass

    def hard_scan(self, i):
        print(i)
        host_ip = ipaddr + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        print(response)
        if response == None:
            print('hallo')
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            try:
                hersteller = MacLookup().lookup(mac)
                port_list = []
                for n in range(1, 100):
                    port_response = sr1(IP(dst=host_ip) / TCP(dport=n, flags="S"), verbose=op_verbose, timeout=0.2)
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

            except KeyError:
                pass

    def ping_scan(self, i):
        # print(i)
        host_ip = ipaddr + str(i)
        print(host_ip)
        response = ping(host_ip,timeout=0.2)
        # print(response)
        if response == None:
            print('hallo')
        else:
            print(host_ip)
            mac = scapy.layers.l2.getmacbyip(host_ip)
            print(mac)
            try:
                hersteller = MacLookup().lookup(mac)
                print(hersteller)
                print("thread fertig")
                time.sleep(0.5)
            except KeyError:
                time.sleep(0.2)

    def config(self):
        global ipaddr
        if self.basic.isChecked() == True:
            ipaddr = self.ip_1_1.text() + '.' + self.ip_1_2.text() + '.' + self.ip_1_3.text() + '.'
            self.close()
            ip1 = int(self.ip_1_4.text())
            ip2 = int(self.ip_2_4.text()) + 1
            print(ip1)
            for i in range(ip1, ip2):
                th = threading.Thread(target=self.basic_scan(i), args=(1,))
                th.start()
        elif self.normal.isChecked() == True:
            ipaddr = self.ip_1_1.text() + '.' + self.ip_1_2.text() + '.' + self.ip_1_3.text() + '.'
            self.close()
            ip1 = int(self.ip_1_4.text())
            ip2 = int(self.ip_2_4.text()) + 1
            print(ip1)
            for i in range(ip1, ip2):

                th = threading.Thread(target=self.Normal_scan(i=i), args=(1,))
                th.start()
                print("create thread")
        elif self.Hard.isChecked() == True:
            ipaddr = self.ip_1_1.text() + '.' + self.ip_1_2.text() + '.' + self.ip_1_3.text() + '.'
            self.close()
            ip1 = int(self.ip_1_4.text())
            ip2 = int(self.ip_2_4.text()) + 1
            print(ip1)
            for i in range(ip1, ip2):
                th = threading.Thread(target=self.hard_scan(i), args=(1,))
                th.start()
        elif self.ping.isChecked() == True:
            ipaddr = self.ip_1_1.text() + '.' + self.ip_1_2.text() + '.' + self.ip_1_3.text() + '.'
            self.close()
            ip1 = int(self.ip_1_4.text())
            ip2 = int(self.ip_2_4.text()) + 1
            print(ip1)
            for i in range(ip1, ip2):
                th = threading.Thread(target=self.ping_scan(i=i), args=(1,))
                th.start()
        else:
            pass


class test(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi("Gui/config.ui")
        # loadUi("Gui/config.ui", self)
        self.setupUi(self)


if __name__ == "__main__":
    statup()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())