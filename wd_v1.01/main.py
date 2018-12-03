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
            st1, at1, h1, st2, at2, h2 = spi.SPI_read([0xA0])
            print('1 - soil temp:', st1)
            print('1 - air temp:', at1)
            print('1 - humidity:', h1)
            print('2 - soil temp:', st2)
            print('2 - air temp:', at2)
            print('2 - humidity:', h2)
            
            myWin.num1_1.display(round(float(st1), 1))
            myWin.num1_2.display(round(float(at1), 1))
            myWin.num1_3.display(round(float(h1), 1))
            myWin.num2_1.display(round(float(st2), 1))
            myWin.num2_2.display(round(float(at2), 1))
            myWin.num2_3.display(round(float(h2), 1))
            
            time.sleep(5) #at least 2s  10s is ok


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    #myWin.showFullScreen()
    myWin.move(0, 0)
    myWin.show()
    
    main_pic = QtGui.QPixmap('weidun-10%.png')
    myWin.main_pic.setPixmap(main_pic)
    
    t = MainThread()
    #t.start()
    sys.exit(app.exec_())
