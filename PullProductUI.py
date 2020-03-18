# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PullProductUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys
import PullProductFunsUI
conffile='pullproductconfigui.txt'

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(637, 609)
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
        self.tb_showmsg = QtWidgets.QTextBrowser(Form)
        self.tb_showmsg.setGeometry(QtCore.QRect(10, 380, 611, 201))
        self.tb_showmsg.setObjectName("tb_showmsg")
        self.btn_saveconfig = QtWidgets.QPushButton(Form)
        self.btn_saveconfig.setGeometry(QtCore.QRect(390, 340, 75, 23))
        self.btn_saveconfig.setObjectName("btn_saveconfig")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.btn_pullitnow.raise_()
        self.edit_egalaxyurl.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.edit_pricingurl.raise_()
        self.label_3.raise_()
        self.edit_galaxyuser.raise_()
        self.tb_showmsg.raise_()
        self.btn_saveconfig.raise_()

        

        self.retranslateUi(Form)
        self.btn_pullitnow.clicked.connect(self.pullitnow)
        self.btn_saveconfig.clicked.connect(self.saveConfig)

        self.initAll()


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

    def saveConfig(self):
        user = self.edit_galaxyuser.text()
        passwd = self.edit_galaxypwd.text()
        auth = PullProductFunsUI.ToBase64Encode(user + ':' + passwd)
        sdate = self.edit_startdate.date().toString('yyyy-MM-dd')
        edate = self.edit_enddate.date().toString('yyyy-MM-dd')
        with open(conffile,'w') as f:
            f.write(self.edit_egalaxyurl.text())
            f.write('\n')
            f.write(self.edit_pricingurl.text())
            f.write('\n')
            f.write(auth)
            f.write('\n')
            f.write(self.edit_plus.text())
            f.write('\n')
            f.write(sdate)
            f.write('\n')
            f.write(edate)
            f.write('\n')
            f.write(self.edit_customerid.text())
            f.write('\n')
            f.write(self.edit_galaxytimeout.text())
            self.tb_showmsg.append('config file saved...')

    def pullitnow(self):
        egalurl = self.edit_egalaxyurl.text()
        priurl = self.edit_pricingurl.text()
        custid = self.edit_customerid.text()
        timeout = self.edit_galaxytimeout.text()
        plulist = self.edit_plus.text()
        user = self.edit_galaxyuser.text()
        passwd = self.edit_galaxypwd.text()
        auth = 'Basic ' + PullProductFunsUI.ToBase64Encode(user + ':' + passwd)
        sdate = self.edit_startdate.date().toString('yyyy-MM-dd')
        edate = self.edit_enddate.date().toString('yyyy-MM-dd')

        self.btn_pullitnow.setDisabled(True)

        self.threadpool = QtCore.QThreadPool()
        worker = Work(egalurl,priurl,auth,plulist,custid,timeout,sdate,edate)

        worker.sig.cleanlog.connect(lambda:self.showMSG('log cleaned...'))

        worker.sig.querycustomer.connect(lambda :self.showMSG('querying customer {0} items {1}'.format(custid,plulist)))

        worker.sig.queryevents.connect(lambda :self.showMSG('querying events from {0} to {1}...'.format(sdate,edate)))

        worker.sig.querypricing.connect(lambda :self.showMSG('querying items prices...'))

        worker.sig.writing.connect(lambda :self.showMSG('writing items results...'))

        worker.sig.complete.connect(lambda :self.showMSG('pull products completed...'))

        worker.sig.errorquerycustomer.connect(lambda : self.showMSG('query customer error occurred, see log...'))

        worker.sig.errorqueryevents.connect(lambda : self.showMSG('query events error occurred, see log...'))

        self.threadpool.start(worker)
    

    def showMSG(self,strings):
        import re
        if re.findall('error',strings) or re.findall('completed',strings):
            self.btn_pullitnow.setDisabled(False)
        self.tb_showmsg.append(strings)

    def pullitnow1(self):
        egalurl = self.edit_egalaxyurl.text()
        priurl = self.edit_pricingurl.text()
        custid = self.edit_customerid.text()
        timeout = self.edit_galaxytimeout.text()
        plulist = self.edit_plus.text()
        user = self.edit_galaxyuser.text()
        passwd = self.edit_galaxypwd.text()
        auth = 'Basic ' + PullProductFunsUI.ToBase64Encode(user + ':' + passwd)
        sdate = self.edit_startdate.date().toString('yyyy-MM-dd')
        edate = self.edit_enddate.date().toString('yyyy-MM-dd')

        self.tb_showmsg.append(PullProductFunsUI.CleanLogFile())

        self.tb_showmsg.append('querying customer {0} items {1}'.format(custid,plulist))
        customeritems = PullProductFunsUI.QueryCustomer(egalurl,timeout,plulist,custid)
        if isinstance(customeritems,dict):
            self.tb_showmsg.append('error: '+customeritems['error'])
        else:
            self.tb_showmsg.append('querying events from {0} to {1}...'.format(sdate,edate))
            eventids,products = PullProductFunsUI.QueryEventID(customeritems,sdate,edate,egalurl,timeout,custid)
            errormsg = ''
            if isinstance(eventids,dict):
                errormsg = eventids['error']
            if isinstance(products,dict):
                errormsg = errormsg + ' ' + products['error']
            if errormsg: 
                self.tb_showmsg.append('error in query event: ' + errormsg)
            else:
                reorgedeventid = PullProductFunsUI.ReOrgEventIDandVisitDate(eventids)
            

                self.tb_showmsg.append('querying items prices...')
                pricingcmds = PullProductFunsUI.MakePricingRequest(reorgedeventid,products,customeritems,custid)
        
                self.tb_showmsg.append('writing items results...')
                PullProductFunsUI.ExecQueryPricing(pricingcmds,priurl,timeout,auth)
                PullProductFunsUI.WriteGAProducts(customeritems)
                self.tb_showmsg.append('pull products completed...')


    def initAll(self):
        self.edit_startdate.setDisplayFormat('yyyy-MM-dd')
        self.edit_enddate.setDisplayFormat('yyyy-MM-dd')
        self.initConfig()

    def initConfig(self):
        if not os.path.exists(conffile):
            self.tb_showmsg.append("config file not found...")
        else:
            with open(conffile,"r") as f:
                egalaxyurl = f.readline().replace("\n","")
                pricingurl = f.readline().replace("\n","")
                authmiwen = f.readline().replace("\n","")
                plulist = f.readline().replace("\n","")
                startdate = f.readline().replace("\n","")
                enddate = f.readline().replace("\n","")
                customerid = f.readline().replace("\n","")
                timeout = f.readline().replace("\n","")
            sdate = startdate.split('-')
            edate = enddate.split('-')
            authmingwen = PullProductFunsUI.ToPlainText(authmiwen)

            if authmingwen:
                auth = authmingwen.split(':')

            self.edit_egalaxyurl.setText(egalaxyurl)
            self.edit_pricingurl.setText(pricingurl)
            self.edit_galaxyuser.setText(auth[0])
            self.edit_galaxypwd.setText(auth[1])
            self.edit_galaxytimeout.setText(timeout)
            self.edit_plus.setText(plulist)
            self.edit_customerid.setText(customerid)
            self.edit_startdate.setDate(QtCore.QDate(int(sdate[0]),int(sdate[1]),int(sdate[2])))
            self.edit_enddate.setDate(QtCore.QDate(int(edate[0]),int(edate[1]),int(edate[2])))
            self.tb_showmsg.append('config initialized...')

class Work(QtCore.QRunnable):
    def __init__(self,egalurl,priurl,auth,plulist,custid,timeout,sdate,edate):
        super(Work,self).__init__()
        self.egalurl = egalurl
        self.priurl = priurl
        self.auth = auth
        self.plulist = plulist
        self.custid = custid
        self.timeout = timeout
        self.sdate = sdate
        self.edate = edate

        self.sig = WorkerSigals()

    def run(self):
        egalurl = self.egalurl
        priurl = self.priurl
        custid = self.custid
        timeout = self.timeout
        plulist = self.plulist
        sdate = self.sdate
        edate = self.edate
        auth = self.auth

        PullProductFunsUI.CleanLogFile()

        self.sig.cleanlog.emit()


        self.sig.querycustomer.emit()
        customeritems = PullProductFunsUI.QueryCustomer(egalurl,timeout,plulist,custid)
        errormsg = ''
        if isinstance(customeritems,dict):
            errormsg = errormsg + 'error: '+customeritems['error']
            self.sig.errorquerycustomer.emit()
        else:
            self.sig.queryevents.emit()
            eventids,products = PullProductFunsUI.QueryEventID(customeritems,sdate,edate,egalurl,timeout,custid)
            errormsg = ''
            if isinstance(eventids,dict):
                errormsg = eventids['error']
            if isinstance(products,dict):
                errormsg = errormsg + ' ' + products['error']
            if errormsg:
                self.sig.errorqueryevents.emit()
            else:
                reorgedeventid = PullProductFunsUI.ReOrgEventIDandVisitDate(eventids)
            

                self.sig.querypricing.emit()
                pricingcmds = PullProductFunsUI.MakePricingRequest(reorgedeventid,products,customeritems,custid)
        
                self.sig.writing.emit()
                PullProductFunsUI.ExecQueryPricing(pricingcmds,priurl,timeout,auth)
                PullProductFunsUI.WriteGAProducts(customeritems)
                self.sig.complete.emit()

class WorkerSigals(QtCore.QObject):
    cleanlog = QtCore.pyqtSignal()
    querycustomer = QtCore.pyqtSignal()
    queryevents = QtCore.pyqtSignal()
    querypricing = QtCore.pyqtSignal()
    writing = QtCore.pyqtSignal()
    complete = QtCore.pyqtSignal()
    errorquerycustomer = QtCore.pyqtSignal()
    errorqueryevents = QtCore.pyqtSignal()


