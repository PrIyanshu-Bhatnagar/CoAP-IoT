# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppUI.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 691)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(520, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_get_client1 = QtWidgets.QPushButton(Form)
        self.pushButton_get_client1.setGeometry(QtCore.QRect(20, 200, 113, 32))
        self.pushButton_get_client1.setObjectName("pushButton_get_client1")
        self.pushButton_put_client1 = QtWidgets.QPushButton(Form)
        self.pushButton_put_client1.setGeometry(QtCore.QRect(20, 240, 113, 32))
        self.pushButton_put_client1.setObjectName("pushButton_put_client1")
        self.pushButton_post_client1 = QtWidgets.QPushButton(Form)
        self.pushButton_post_client1.setGeometry(QtCore.QRect(20, 280, 113, 32))
        self.pushButton_post_client1.setObjectName("pushButton_post_client1")
        self.pushButton_delete_client1 = QtWidgets.QPushButton(Form)
        self.pushButton_delete_client1.setGeometry(QtCore.QRect(20, 320, 113, 32))
        self.pushButton_delete_client1.setObjectName("pushButton_delete_client1")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.payloadLabel_client1 = QtWidgets.QLabel(Form)
        self.payloadLabel_client1.setGeometry(QtCore.QRect(110, 90, 111, 31))
        self.payloadLabel_client1.setObjectName("payloadLabel_client1")
        self.typeLabel_client1 = QtWidgets.QLabel(Form)
        self.typeLabel_client1.setGeometry(QtCore.QRect(110, 130, 111, 31))
        self.typeLabel_client1.setObjectName("typeLabel_client1")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 130, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.midLabel_client1 = QtWidgets.QLabel(Form)
        self.midLabel_client1.setGeometry(QtCore.QRect(110, 170, 111, 31))
        self.midLabel_client1.setObjectName("midLabel_client1")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 170, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.payloadLabel_server = QtWidgets.QLabel(Form)
        self.payloadLabel_server.setGeometry(QtCore.QRect(550, 280, 111, 31))
        self.payloadLabel_server.setObjectName("payloadLabel_server")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(470, 360, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(470, 320, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(470, 280, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.midLabel_server = QtWidgets.QLabel(Form)
        self.midLabel_server.setGeometry(QtCore.QRect(550, 360, 111, 31))
        self.midLabel_server.setObjectName("midLabel_server")
        self.typeLabel_server = QtWidgets.QLabel(Form)
        self.typeLabel_server.setGeometry(QtCore.QRect(550, 320, 111, 31))
        self.typeLabel_server.setObjectName("typeLabel_server")
        self.pushButton_client1 = QtWidgets.QPushButton(Form)
        self.pushButton_client1.setGeometry(QtCore.QRect(110, 50, 111, 41))
        self.pushButton_client1.setObjectName("pushButton_client1")
        self.pushButton_server = QtWidgets.QPushButton(Form)
        self.pushButton_server.setGeometry(QtCore.QRect(590, 230, 111, 41))
        self.pushButton_server.setObjectName("pushButton_server")
        self.textEdit_put_client1 = QtWidgets.QPlainTextEdit(Form)
        self.textEdit_put_client1.setGeometry(QtCore.QRect(170, 240, 201, 31))
        self.textEdit_put_client1.setObjectName("textEdit_put_client1")
        self.textEdit_post_client1 = QtWidgets.QPlainTextEdit(Form)
        self.textEdit_post_client1.setGeometry(QtCore.QRect(170, 280, 201, 31))
        self.textEdit_post_client1.setObjectName("textEdit_post_client1")
        self.pushButton_delete_client2 = QtWidgets.QPushButton(Form)
        self.pushButton_delete_client2.setGeometry(QtCore.QRect(20, 640, 113, 32))
        self.pushButton_delete_client2.setObjectName("pushButton_delete_client2")
        self.pushButton_get_client2 = QtWidgets.QPushButton(Form)
        self.pushButton_get_client2.setGeometry(QtCore.QRect(20, 520, 113, 32))
        self.pushButton_get_client2.setObjectName("pushButton_get_client2")
        self.payloadLabel_client2 = QtWidgets.QLabel(Form)
        self.payloadLabel_client2.setGeometry(QtCore.QRect(110, 410, 111, 31))
        self.payloadLabel_client2.setObjectName("payloadLabel_client2")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(30, 490, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(30, 450, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_put_client2 = QtWidgets.QPushButton(Form)
        self.pushButton_put_client2.setGeometry(QtCore.QRect(20, 560, 113, 32))
        self.pushButton_put_client2.setObjectName("pushButton_put_client2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 410, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.midLabel_client2 = QtWidgets.QLabel(Form)
        self.midLabel_client2.setGeometry(QtCore.QRect(110, 490, 111, 31))
        self.midLabel_client2.setObjectName("midLabel_client2")
        self.textEdit_put_client2 = QtWidgets.QPlainTextEdit(Form)
        self.textEdit_put_client2.setGeometry(QtCore.QRect(170, 560, 201, 31))
        self.textEdit_put_client2.setObjectName("textEdit_put_client2")
        self.typeLabel_client2 = QtWidgets.QLabel(Form)
        self.typeLabel_client2.setGeometry(QtCore.QRect(110, 450, 111, 31))
        self.typeLabel_client2.setObjectName("typeLabel_client2")
        self.textEdit_post_client2 = QtWidgets.QPlainTextEdit(Form)
        self.textEdit_post_client2.setGeometry(QtCore.QRect(170, 600, 201, 31))
        self.textEdit_post_client2.setObjectName("textEdit_post_client2")
        self.pushButton_client2 = QtWidgets.QPushButton(Form)
        self.pushButton_client2.setGeometry(QtCore.QRect(110, 370, 111, 41))
        self.pushButton_client2.setObjectName("pushButton_client2")
        self.pushButton_post_client2 = QtWidgets.QPushButton(Form)
        self.pushButton_post_client2.setGeometry(QtCore.QRect(20, 600, 113, 32))
        self.pushButton_post_client2.setObjectName("pushButton_post_client2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Constraind Application Protocol"))
        self.label_2.setText(_translate("Form", "Server"))
        self.label_3.setText(_translate("Form", "Client 1"))
        self.pushButton_get_client1.setText(_translate("Form", "GET"))
        self.pushButton_put_client1.setText(_translate("Form", "PUT"))
        self.pushButton_post_client1.setText(_translate("Form", "POST"))
        self.pushButton_delete_client1.setText(_translate("Form", "DELETE"))
        self.label_5.setText(_translate("Form", "Payload"))
        self.payloadLabel_client1.setText(_translate("Form", "Basic Resource"))
        self.typeLabel_client1.setText(_translate("Form", "ACK"))
        self.label_10.setText(_translate("Form", "Type"))
        self.midLabel_client1.setText(_translate("Form", "0"))
        self.label_12.setText(_translate("Form", "MID"))
        self.payloadLabel_server.setText(_translate("Form", "Basic Resource"))
        self.label_18.setText(_translate("Form", "MID"))
        self.label_19.setText(_translate("Form", "Type"))
        self.label_20.setText(_translate("Form", "Payload"))
        self.midLabel_server.setText(_translate("Form", "0"))
        self.typeLabel_server.setText(_translate("Form", "ACK"))
        self.pushButton_client1.setText(_translate("Form", "ON"))
        self.pushButton_server.setText(_translate("Form", "ON"))
        self.textEdit_put_client1.setPlaceholderText(_translate("Form", "Enter payload"))
        self.textEdit_post_client1.setPlaceholderText(_translate("Form", "Enter payload"))
        self.pushButton_delete_client2.setText(_translate("Form", "DELETE"))
        self.pushButton_get_client2.setText(_translate("Form", "GET"))
        self.payloadLabel_client2.setText(_translate("Form", "Basic Resource"))
        self.label_13.setText(_translate("Form", "MID"))
        self.label_14.setText(_translate("Form", "Type"))
        self.label_4.setText(_translate("Form", "Client 2"))
        self.pushButton_put_client2.setText(_translate("Form", "PUT"))
        self.label_8.setText(_translate("Form", "Payload"))
        self.midLabel_client2.setText(_translate("Form", "0"))
        self.textEdit_put_client2.setPlaceholderText(_translate("Form", "Enter payload"))
        self.typeLabel_client2.setText(_translate("Form", "ACK"))
        self.textEdit_post_client2.setPlaceholderText(_translate("Form", "Enter payload"))
        self.pushButton_client2.setText(_translate("Form", "ON"))
        self.pushButton_post_client2.setText(_translate("Form", "POST"))

