# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atividade.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cadastro import Ui_CadastroWindow
from telaPrincipal import Ui_TelaPrincipal
from telaPrincipalDois import Ui_TelaPrincipalDois
import sqlite3
from CustomDialogLoginError import CustomDialogLoginError


class Ui_login(object):
    def telaCadastro(self):
        self.novaJanela = QtWidgets.QMainWindow()
        self.ui = Ui_CadastroWindow()
        self.ui.setupUi(self.novaJanela)
        self.novaJanela.show()

    def telaPrincipal(self):
        self.novaJanela = QtWidgets.QMainWindow()
        self.ui = Ui_TelaPrincipalDois()
        self.ui.setupUi(self.novaJanela)
        self.novaJanela.show()
    def Login(self):
        email = self.EditEmail. text()
        senha = self.EditPassword.text()
        conn = sqlite3.connect('login.db')

        emailDb = conn.cursor()
        emailDb.execute("SELECT email FROM cadastrados WHERE email='{}'".format(email))
        emailDb = emailDb.fetchall()

        senhaDb = conn.cursor()
        senhaDb.execute("SELECT senha FROM cadastrados WHERE senha='{}'".format(senha))
        senhaDb = senhaDb.fetchall()

        if not emailDb:
            dlg = CustomDialogLoginError()
            dlg.exec()
        else:

            if not senhaDb:
                print("A senha esta errada mas o email certo")
                dlg = CustomDialogLoginError()
                dlg.exec()
            else:
                print("O email e a senha estão corretos")
                self.uiPrincipal.tabom(emailDb[0])
                MainWindow.close()
                self.telaPrincipal()

    def setupUi(self, MainWindow):
        self.novaJanela = QtWidgets.QMainWindow()
        self.uiPrincipal = Ui_TelaPrincipalDois()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 408)
        MainWindow.setStyleSheet("background-color: pink;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLogin.setGeometry(QtCore.QRect(120, 280, 151, 61))
        font = QtGui.QFont()
        font.setFamily("verdana")
        self.BtnLogin.setFont(font)
        self.BtnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnLogin.setStyleSheet("background-color: white;\n"
"font-family: verdana;\n"
"border: 1px solid;\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color : lightgreen;\n"
"}")
        self.BtnLogin.setObjectName("BtnLogin")
        self.BtnLogin.clicked.connect(self.Login)


        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(30, 100, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("image: url(:/img/user.png);")
        self.label_login.setText("")
        self.label_login.setObjectName("label_login")
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setGeometry(QtCore.QRect(30, 190, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_senha.setFont(font)
        self.label_senha.setStyleSheet("image: url(:/img/lock.png);")
        self.label_senha.setText("")
        self.label_senha.setObjectName("label_senha")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(100, 30, 211, 51))
        self.titulo.setObjectName("titulo")
        self.EditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.EditEmail.setGeometry(QtCore.QRect(100, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EditEmail.setFont(font)
        self.EditEmail.setStyleSheet("background-color: white;")
        self.EditEmail.setObjectName("EditEmail")

        self.EditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.EditPassword.setGeometry(QtCore.QRect(100, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EditPassword.setFont(font)
        self.EditPassword.setStyleSheet("background-color: white;")
        self.EditPassword.setInputMask("")
        self.EditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EditPassword.setObjectName("EditPassword")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 360, 211, 23))
        self.pushButton.setStyleSheet("\n"
"color: blue;\n"
"text-decoration: underline;\n"
"font-size: 12pt;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.telaCadastro)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.BtnLogin.setText(_translate("MainWindow", "ENTRAR"))
        self.titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">CONTROLE DE ESTOQUE</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Não tem conta? Cadastre-se"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
