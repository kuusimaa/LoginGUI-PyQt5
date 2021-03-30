import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 350)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("QMainWindow {background: transparent; }\n"
                           "QToolTip {\n"
                           "    color: #ffffff;\n"
                           "    background-color: rgba(27, 29, 35, 160);\n"
                           "    border: 1px solid rgb(100, 100, 100);\n"
                           "}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background: transparent;\n"
                                         "color: rgb(210, 210, 210);\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")

        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        self.frame_top = TopBar(self, self.frame_main)

        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setGeometry(QtCore.QRect(0, 30, 400, 350))
        self.frame_center.setStyleSheet("background-color: rgb(44, 49, 60);\n"
                                        "")
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")

        self.password_box = QtWidgets.QFrame(self.frame_center)
        self.password_box.setGeometry(QtCore.QRect(100, 135, 200, 35))
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
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.username_box = QtWidgets.QFrame(self.frame_center)
        self.username_box.setGeometry(QtCore.QRect(100, 80, 200, 35))
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

        self.Login_btn = QtWidgets.QPushButton(self.frame_center)
        self.Login_btn.setGeometry(QtCore.QRect(125, 190, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Login_btn.setFont(font)
        self.Login_btn.setMouseTracking(False)
        self.Login_btn.setAutoFillBackground(False)
        self.Login_btn.setStyleSheet("QPushButton {\n"
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
        self.Login_btn.setCheckable(False)
        self.Login_btn.setFlat(False)
        self.Login_btn.setObjectName("Login_btn")

        self.register_button = QtWidgets.QPushButton(self.frame_center)
        self.register_button.setGeometry(QtCore.QRect(150, 230, 100, 23))
        self.register_button.setMouseTracking(False)
        self.register_button.setStyleSheet("QPushButton {\n"
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
        self.register_button.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
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

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main", "main"))
        self.lineEdit_password.setPlaceholderText(
            _translate("main", "Password"))
        self.lineEdit_username.setPlaceholderText(
            _translate("main", "Username"))
        self.Login_btn.setText(_translate("main", "Login"))
        self.register_button.setText(_translate("main", "Register"))


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
        self.label.setText("LoginGUI")
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
        self.btn_close.clicked.connect(lambda: self.close_window())

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
        self.btn_minimize.clicked.connect(lambda: self.minimize_window())

    def minimize_window(self):
        self.parent.showMinimized()

    def close_window(self):
        self.parent.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
