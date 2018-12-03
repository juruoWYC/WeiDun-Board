from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from MainWin import *
import sys
import connect
import time
import spi

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
            h, t, l = spi.SPI_read()
            print('humidity:', h)
            print('air temp:', t)
            print('light:', l)
            
            myWin.num1_1.display(round(float(h), 1))
            myWin.num1_2.display(round(float(t), 1))
            myWin.num1_3.display(round(float(l), 1))
            
            time.sleep(5) #at least 2s  10s is ok


if __name__ == '__main__':
    connect.NB_IOT_INIT()
    
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    myWin.showFullScreen()
    myWin.move(0, 0)
    myWin.show()
    
    main_pic = QtGui.QPixmap('weidun.png')
    myWin.main_pic.setPixmap(main_pic)
    
    t = MainThread()
    t.start()
    sys.exit(app.exec_())
