import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_class = uic.loadUiType("installing.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    os.system('dir')
    path = os.path.dirname(os.path.abspath(__file__))
    path = 'regedit /s ' + path + '\\sources\\SKIPTPMCHK.reg'
    print(path)
    os.system(path)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.showFullScreen()
    app.exec_()