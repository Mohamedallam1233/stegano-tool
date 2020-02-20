from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *
import time
import allam_program
from os import path
import sys
LIMIT_TIME = 100
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), 'first_page.ui'))
class Ex(QThread):
    countChanged = pyqtSignal(int)
    def run(self):
        count = 0
        while count < LIMIT_TIME:
            count += 1
            time.sleep(0.04)
            self.countChanged.emit(count)
class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.progressBar.setValue(0)
        self.onStart()
    def handel_ui(self):
        self.setFixedSize(800,600)
        self.setWindowIcon(QIcon('photos/lock.png'))
    def onStart(self):
        self.calc = Ex()
        self.calc.countChanged.connect(self.countChangedProcess)
        self.calc.start()
    def countChangedProcess(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            time.sleep(0.04)
            self.closeCurrentApp_OpenNewApp()
    def closeCurrentApp_OpenNewApp(self):
        self.close()
        self.open = allam_program.mainApp1()
        self.open.show()
def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()