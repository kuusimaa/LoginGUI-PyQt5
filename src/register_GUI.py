import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.resize(400, 350)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        self.frame_top = TopBar(self, self.frame_main)

        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setGeometry(QtCore.QRect(0, 30, 400, 320))
        self.frame_center.setStyleSheet("QFrame {\n"
                                        "    background-color: rgb(44, 49, 60);\n"
                                        "}")
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.register_label = QtWidgets.QLabel(self.frame_center)
        self.register_label.setGeometry(QtCore.QRect(0, 20, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_label.setFont(font)
        self.register_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_label.setObjectName("register_label")
        self.username_box = QtWidgets.QFrame(self.frame_center)
        self.username_box.setGeometry(QtCore.QRect(100, 60, 200, 35))
        self.username_box.setStyleSheet("background-color: rgb(28, 29, 32);\n"
                                        "border-radius: 15;\n"
                                        "")
        self.username_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_box.setObjectName("username_box")
        self.lineEdit_username = QtWidgets.QLineEdit(self.username_box)
        self.lineEdit_username.setGeometry(QtCore.QRect(0, 0, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("QLineEdit {\n"
                                             "    color: rgb(195, 203, 221);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(64, 71, 88);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(91, 101, 124);\n"
                                             "}")
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.email_box = QtWidgets.QFrame(self.frame_center)
        self.email_box.setGeometry(QtCore.QRect(100, 110, 200, 35))
        self.email_box.setStyleSheet("background-color: rgb(28, 29, 32);\n"
                                     "border-radius: 15;\n"
                                     "")
        self.email_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email_box.setObjectName("email_box")
        self.lineEdit_email = QtWidgets.QLineEdit(self.email_box)
        self.lineEdit_email.setGeometry(QtCore.QRect(0, 0, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("QLineEdit {\n"
                                          "    color: rgb(195, 203, 221);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:hover {\n"
                                          "    border: 2px solid rgb(64, 71, 88);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:focus {\n"
                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                          "}")
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.password_box = QtWidgets.QFrame(self.frame_center)
        self.password_box.setGeometry(QtCore.QRect(100, 160, 200, 35))
        self.password_box.setStyleSheet("background-color: rgb(28, 29, 32);\n"
                                        "border-radius: 15;\n"
                                        "")
        self.password_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_box.setObjectName("password_box")
        self.lineEdit_password = QtWidgets.QLineEdit(self.password_box)
        self.lineEdit_password.setGeometry(QtCore.QRect(0, 0, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    color: rgb(195, 203, 221);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(64, 71, 88);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(91, 101, 124);\n"
                                             "}")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.register_btn = QtWidgets.QPushButton(self.frame_center)
        self.register_btn.setGeometry(QtCore.QRect(125, 210, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setMouseTracking(False)
        self.register_btn.setAutoFillBackground(False)
        self.register_btn.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid rgb(52, 59, 72);\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(57, 65, 80);\n"
                                        "    border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(35, 40, 49);\n"
                                        "    border: 2px solid rgb(43, 50, 61);\n"
                                        "}")
        self.register_btn.setCheckable(False)
        self.register_btn.setFlat(False)
        self.register_btn.setObjectName("Login_btn")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.offset = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.register_label.setText(_translate("MainWindow", "Registration"))
        self.lineEdit_username.setPlaceholderText(
            _translate("MainWindow", "Username"))
        self.lineEdit_email.setPlaceholderText(
            _translate("MainWindow", "Email"))
        self.lineEdit_password.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.register_btn.setText(_translate("MainWindow", "Register"))


class TopBar(QWidget):
    def __init__(self, parent, frame_main):
        super(TopBar, self).__init__()
        self.parent = parent
        self.frame_main = frame_main

        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.frame_top.setStyleSheet("background-color: rgb(37, 39, 44);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label = QtWidgets.QLabel(self.frame_top)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setText("RegisterGUI")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_close = QtWidgets.QPushButton(self.frame_top)
        self.btn_close.setGeometry(QtCore.QRect(370, 0, 30, 30))
        self.btn_close.setStyleSheet("QPushButton {    \n"
                                     "    border: none;\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "}")
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cil-x.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_top)
        self.btn_minimize.setGeometry(QtCore.QRect(340, 0, 30, 30))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_minimize.setAutoFillBackground(False)
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
                                        "    border: none;\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.btn_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/cil-window-minimize.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QtCore.QSize(24, 24))
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_close.clicked.connect(lambda: self.close_window())
        self.btn_minimize.clicked.connect(lambda: self.minimize_window())

    def minimize_window(self):
        self.parent.showMinimized()

    def close_window(self):
        self.parent.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    rw = RegisterWindow()
    rw.show()
    sys.exit(app.exec_())
