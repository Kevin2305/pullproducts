# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PullProductUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(637, 593)
        self.btn_pullitnow = QtWidgets.QPushButton(Form)
        self.btn_pullitnow.setGeometry(QtCore.QRect(190, 340, 75, 23))
        self.btn_pullitnow.setObjectName("btn_pullitnow")
        self.edit_egalaxyurl = QtWidgets.QLineEdit(Form)
        self.edit_egalaxyurl.setGeometry(QtCore.QRect(100, 30, 491, 20))
        self.edit_egalaxyurl.setObjectName("edit_egalaxyurl")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_2.setObjectName("label_2")
        self.edit_pricingurl = QtWidgets.QLineEdit(Form)
        self.edit_pricingurl.setGeometry(QtCore.QRect(100, 70, 491, 20))
        self.edit_pricingurl.setObjectName("edit_pricingurl")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_3.setObjectName("label_3")
        self.edit_galaxyuser = QtWidgets.QLineEdit(Form)
        self.edit_galaxyuser.setGeometry(QtCore.QRect(100, 110, 71, 20))
        self.edit_galaxyuser.setObjectName("edit_galaxyuser")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 611, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(450, 100, 61, 21))
        self.label_5.setObjectName("label_5")
        self.edit_galaxytimeout = QtWidgets.QLineEdit(self.groupBox)
        self.edit_galaxytimeout.setGeometry(QtCore.QRect(520, 100, 61, 20))
        self.edit_galaxytimeout.setObjectName("edit_galaxytimeout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.edit_galaxypwd = QtWidgets.QLineEdit(self.groupBox)
        self.edit_galaxypwd.setGeometry(QtCore.QRect(290, 100, 141, 20))
        self.edit_galaxypwd.setStatusTip("")
        self.edit_galaxypwd.setInputMask("")
        self.edit_galaxypwd.setText("")
        self.edit_galaxypwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_galaxypwd.setObjectName("edit_galaxypwd")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 611, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_6.setObjectName("label_6")
        self.edit_plus = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_plus.setGeometry(QtCore.QRect(90, 40, 491, 20))
        self.edit_plus.setObjectName("edit_plus")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(210, 90, 71, 21))
        self.label_7.setObjectName("label_7")
        self.edit_startdate = QtWidgets.QDateEdit(self.groupBox_2)
        self.edit_startdate.setGeometry(QtCore.QRect(280, 90, 110, 22))
        self.edit_startdate.setObjectName("edit_startdate")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(420, 90, 61, 21))
        self.label_8.setObjectName("label_8")
        self.edit_enddate = QtWidgets.QDateEdit(self.groupBox_2)
        self.edit_enddate.setGeometry(QtCore.QRect(480, 90, 110, 22))
        self.edit_enddate.setObjectName("edit_enddate")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_9.setObjectName("label_9")
        self.edit_customerid = QtWidgets.QLineEdit(self.groupBox_2)
        self.edit_customerid.setGeometry(QtCore.QRect(90, 90, 91, 20))
        self.edit_customerid.setObjectName("edit_customerid")
        self.btn_saveconfig = QtWidgets.QPushButton(Form)
        self.btn_saveconfig.setGeometry(QtCore.QRect(390, 340, 75, 23))
        self.btn_saveconfig.setObjectName("btn_saveconfig")
        self.tb_showmsg = QtWidgets.QTextBrowser(Form)
        self.tb_showmsg.setGeometry(QtCore.QRect(10, 380, 611, 201))
        self.tb_showmsg.setObjectName("tb_showmsg")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.btn_pullitnow.raise_()
        self.edit_egalaxyurl.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.edit_pricingurl.raise_()
        self.label_3.raise_()
        self.edit_galaxyuser.raise_()
        self.btn_saveconfig.raise_()
        self.tb_showmsg.raise_()

        self.retranslateUi(Form)
        self.btn_pullitnow.clicked.connect(self.edit_startdate.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Galaxy Pull Products"))
        self.btn_pullitnow.setText(_translate("Form", "pull it now"))
        self.label.setText(_translate("Form", "eGalaxy URL"))
        self.label_2.setText(_translate("Form", " Pricing URL"))
        self.label_3.setText(_translate("Form", "Galaxy User"))
        self.groupBox.setTitle(_translate("Form", "Galaxy Information"))
        self.label_5.setText(_translate("Form", "Timeout (s)"))
        self.label_4.setText(_translate("Form", "Galaxy Password"))
        self.groupBox_2.setTitle(_translate("Form", "Pull Products"))
        self.label_6.setText(_translate("Form", "PLU List (,)"))
        self.label_7.setText(_translate("Form", "Start Date"))
        self.label_8.setText(_translate("Form", "End Date"))
        self.label_9.setText(_translate("Form", "CustomerID"))
        self.btn_saveconfig.setText(_translate("Form", "save config"))

