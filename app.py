import sys
from PyQt5.QtWidgets import *
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

        win = QWidget()

        usrIn = QLineEdit()

        pswdIn = QLineEdit()
        pswdIn.setEchoMode(QLineEdit.Password)

        btn = QPushButton('Login', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda:print(usrIn.text()))

        flo = QFormLayout()
        flo.addRow("Username", usrIn)
        flo.addRow("Password", pswdIn)
        flo.addRow(btn)
        
        win.setLayout(flo)
        self.setCentralWidget(win)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('disc')
        self.statusBar().showMessage('Ready')

        print(self.centralWidget())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginScreen()
    sys.exit(app.exec_())
