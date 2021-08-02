import os, sys, shutil , os.path, tkinter
from xml.etree.ElementTree import XML
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import *
from tkinter import messagebox, Tk, filedialog

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_class = uic.loadUiType("select.ui")[0]
ver, disk, usb = '\0', '\0' , '\0'

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.Versionlist.itemClicked.connect(self.selectversion)
        self.Disklist.itemClicked.connect(self.selectdisk)
        self.USB.clicked.connect(self.usblist)
        self.agreebutton.clicked.connect(self.Afterpushbutton)
        self.checkdisknumber.clicked.connect(self.checkdisknum)
        

    def selectversion(self):
        global ver
        ver = self.Versionlist.currentRow()
        
    def selectdisk(self):
        global disk
        disk = self.Disklist.currentRow()

    def checkdisknum(self):
        lisdisk = os.popen('wmic diskdrive get size,model,deviceID').read()
        Tk().withdraw()
        messagebox.showinfo('DeviceID의 PHYSICALDRIVE(숫자)가 사용자 PC에 있는 디스크 번호입니다.', f'{lisdisk}')

    def usblist(self):
        global usb
        root = tkinter.Tk()
        root.withdraw()
        usb = filedialog.askdirectory(parent=root,initialdir="/",title='윈도우 설치 USB의 드라이브(C,D,E...)를 선택해주세요.')
        usb = usb.replace("/","\\")
        self.USB.setText(f'현재 선택된 드라이브 경로 : {usb}')
    
    def Afterpushbutton(self):
        if(ver == '\0' or disk == '\0' or usb == '\0'):
            Tk().withdraw()
            messagebox.showerror('오류',"1개 이상의 항목이나 드라이브를 선택하지 않으셨습니다.")

        else:
            if os.path.isdir(usb) == False:
                Tk().withdraw()
                messagebox.showerror('오류',"올바르지 않은 USB 경로입니다. 다시 확인해 주십시오. 프로그램이 종료됩니다.")
            path = os.getcwd()
            global unattendxml
            unattendxml = str(disk)+str(ver)
            xmlpath = path + '\\xml\\' + unattendxml + '.xml'
            copypath = usb + 'sources\\unattend.xml'
            shutil.copy(xmlpath, copypath)
            regpath = path + '\\reg\\SKIPTPMCHK.reg'
            copypath = usb + 'sources\\SKIPTPMCHK.reg'
            shutil.copy(regpath, copypath)

            Tk().withdraw()
            messagebox.showinfo('성공!',"필요한 파일이 전부 복사되었습니다. USB로 재부팅시 자동으로 설치과정이 진행됩니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()