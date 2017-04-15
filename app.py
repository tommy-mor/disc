import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initScreen()
    def initScreen(self):
        act = QAction(QIcon('icon.png'), 'Exit', self)
        act.setStatusTip('exit the app')
        act.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(act)

        self.toolbar = self.addToolBar('exit')
        self.toolbar.addAction(act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('disc')
        self.statusBar().showMessage('Ready')

        #btn = QPushButton('click me pls', self)
        #btn.resize(btn.sizeHint())
        #btn.move(20, 100)

        self.show()
    def keyPressEvent(self, e):
        print(e.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginScreen()
    sys.exit(app.exec_())
