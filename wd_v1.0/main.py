from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from MainWin import *
import sys
#import connect
#import time
#import spi

class MyMainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.setupUi(self)


class MainThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
    def run(self):
        spi.SPI_init()
        
        while True:
            st, at, h = spi.SPI_read([0xA0])
            print('soil temp:', st)
            print('air temp:', at)
            print('humidity:', h)
            
            myWin.num1.display(round(float(st), 1))
            myWin.num2.display(round(float(at), 1))
            myWin.num3.display(round(float(h), 1))
            
            time.sleep(5) #at least 2s  10s is ok


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    myWin.setFixedSize(myWin.width(), myWin.height())
    myWin.showFullScreen()
    myWin.move(0, 0)
    myWin.show()
    
    t = MainThread()
    #t.start()
    sys.exit(app.exec_())
