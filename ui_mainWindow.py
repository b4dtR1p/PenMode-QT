# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Penmode-Qt/mainWindow.ui'
#
# Created: Sun Jul 14 15:39:57 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 425)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_whatweb = QtGui.QWidget()
        self.tab_whatweb.setObjectName(_fromUtf8("tab_whatweb"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_whatweb)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.pushStartWhatWeb = QtGui.QPushButton(self.tab_whatweb)
        self.pushStartWhatWeb.setObjectName(_fromUtf8("pushStartWhatWeb"))
        self.gridLayout_5.addWidget(self.pushStartWhatWeb, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_whatweb)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.whatwebTarget = QtGui.QLineEdit(self.tab_whatweb)
        self.whatwebTarget.setAcceptDrops(False)
        self.whatwebTarget.setObjectName(_fromUtf8("whatwebTarget"))
        self.gridLayout_3.addWidget(self.whatwebTarget, 0, 1, 1, 1)
        self.labelParameter_1 = QtGui.QLabel(self.tab_whatweb)
        self.labelParameter_1.setEnabled(False)
        self.labelParameter_1.setObjectName(_fromUtf8("labelParameter_1"))
        self.gridLayout_3.addWidget(self.labelParameter_1, 1, 0, 1, 1)
        self.whatwebParameter = QtGui.QLineEdit(self.tab_whatweb)
        self.whatwebParameter.setEnabled(False)
        self.whatwebParameter.setObjectName(_fromUtf8("whatwebParameter"))
        self.gridLayout_3.addWidget(self.whatwebParameter, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.shellWhatWeb = QtGui.QTextEdit(self.tab_whatweb)
        self.shellWhatWeb.setEnabled(True)
        self.shellWhatWeb.setAcceptDrops(False)
        self.shellWhatWeb.setAutoFillBackground(False)
        self.shellWhatWeb.setStyleSheet(_fromUtf8(""))
        self.shellWhatWeb.setObjectName(_fromUtf8("shellWhatWeb"))
        self.gridLayout_4.addWidget(self.shellWhatWeb, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_whatweb, _fromUtf8(""))
        self.tab_nmap = QtGui.QWidget()
        self.tab_nmap.setObjectName(_fromUtf8("tab_nmap"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_nmap)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.nmapTarget = QtGui.QLineEdit(self.tab_nmap)
        self.nmapTarget.setAcceptDrops(False)
        self.nmapTarget.setObjectName(_fromUtf8("nmapTarget"))
        self.gridLayout_6.addWidget(self.nmapTarget, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_nmap)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushStartNmap = QtGui.QPushButton(self.tab_nmap)
        self.pushStartNmap.setObjectName(_fromUtf8("pushStartNmap"))
        self.gridLayout_7.addWidget(self.pushStartNmap, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 2, 1, 1, 1)
        self.labelParameter_2 = QtGui.QLabel(self.tab_nmap)
        self.labelParameter_2.setObjectName(_fromUtf8("labelParameter_2"))
        self.gridLayout_6.addWidget(self.labelParameter_2, 1, 0, 1, 1)
        self.nmapParameter = QtGui.QLineEdit(self.tab_nmap)
        self.nmapParameter.setObjectName(_fromUtf8("nmapParameter"))
        self.gridLayout_6.addWidget(self.nmapParameter, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.shellNmap = QtGui.QTextEdit(self.tab_nmap)
        self.shellNmap.setAcceptDrops(False)
        self.shellNmap.setObjectName(_fromUtf8("shellNmap"))
        self.gridLayout_8.addWidget(self.shellNmap, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_nmap, _fromUtf8(""))
        self.tab_nikto = QtGui.QWidget()
        self.tab_nikto.setObjectName(_fromUtf8("tab_nikto"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_nikto)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_5 = QtGui.QLabel(self.tab_nikto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.pushStartNikto = QtGui.QPushButton(self.tab_nikto)
        self.pushStartNikto.setObjectName(_fromUtf8("pushStartNikto"))
        self.gridLayout_10.addWidget(self.pushStartNikto, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 2, 1, 1, 1)
        self.niktoTarget = QtGui.QLineEdit(self.tab_nikto)
        self.niktoTarget.setAcceptDrops(False)
        self.niktoTarget.setObjectName(_fromUtf8("niktoTarget"))
        self.gridLayout_9.addWidget(self.niktoTarget, 0, 1, 1, 1)
        self.labelParameter_3 = QtGui.QLabel(self.tab_nikto)
        self.labelParameter_3.setEnabled(False)
        self.labelParameter_3.setObjectName(_fromUtf8("labelParameter_3"))
        self.gridLayout_9.addWidget(self.labelParameter_3, 1, 0, 1, 1)
        self.niktoParameter = QtGui.QLineEdit(self.tab_nikto)
        self.niktoParameter.setEnabled(False)
        self.niktoParameter.setObjectName(_fromUtf8("niktoParameter"))
        self.gridLayout_9.addWidget(self.niktoParameter, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.shellNikto = QtGui.QTextEdit(self.tab_nikto)
        self.shellNikto.setAcceptDrops(False)
        self.shellNikto.setObjectName(_fromUtf8("shellNikto"))
        self.gridLayout_11.addWidget(self.shellNikto, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_nikto, _fromUtf8(""))
        self.tab_joomscan = QtGui.QWidget()
        self.tab_joomscan.setObjectName(_fromUtf8("tab_joomscan"))
        self.gridLayout_17 = QtGui.QGridLayout(self.tab_joomscan)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.joomscanTarget = QtGui.QLineEdit(self.tab_joomscan)
        self.joomscanTarget.setAcceptDrops(False)
        self.joomscanTarget.setObjectName(_fromUtf8("joomscanTarget"))
        self.gridLayout_15.addWidget(self.joomscanTarget, 0, 1, 1, 1)
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.pushStartJoomScan = QtGui.QPushButton(self.tab_joomscan)
        self.pushStartJoomScan.setObjectName(_fromUtf8("pushStartJoomScan"))
        self.gridLayout_16.addWidget(self.pushStartJoomScan, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_16, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_joomscan)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)
        self.labelParameter_4 = QtGui.QLabel(self.tab_joomscan)
        self.labelParameter_4.setEnabled(False)
        self.labelParameter_4.setObjectName(_fromUtf8("labelParameter_4"))
        self.gridLayout_15.addWidget(self.labelParameter_4, 1, 0, 1, 1)
        self.joomscanParameter = QtGui.QLineEdit(self.tab_joomscan)
        self.joomscanParameter.setEnabled(False)
        self.joomscanParameter.setObjectName(_fromUtf8("joomscanParameter"))
        self.gridLayout_15.addWidget(self.joomscanParameter, 1, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.shellJoomScan = QtGui.QTextEdit(self.tab_joomscan)
        self.shellJoomScan.setAcceptDrops(False)
        self.shellJoomScan.setObjectName(_fromUtf8("shellJoomScan"))
        self.gridLayout_17.addWidget(self.shellJoomScan, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_joomscan, _fromUtf8(""))
        self.tab_wpscan = QtGui.QWidget()
        self.tab_wpscan.setObjectName(_fromUtf8("tab_wpscan"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_wpscan)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.label_10 = QtGui.QLabel(self.tab_wpscan)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_18.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem4, 0, 1, 1, 1)
        self.pushStartWpScan = QtGui.QPushButton(self.tab_wpscan)
        self.pushStartWpScan.setObjectName(_fromUtf8("pushStartWpScan"))
        self.gridLayout_19.addWidget(self.pushStartWpScan, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_19, 2, 1, 1, 1)
        self.wpscanTarget = QtGui.QLineEdit(self.tab_wpscan)
        self.wpscanTarget.setAcceptDrops(False)
        self.wpscanTarget.setObjectName(_fromUtf8("wpscanTarget"))
        self.gridLayout_18.addWidget(self.wpscanTarget, 0, 1, 1, 1)
        self.labelParameter_5 = QtGui.QLabel(self.tab_wpscan)
        self.labelParameter_5.setEnabled(False)
        self.labelParameter_5.setObjectName(_fromUtf8("labelParameter_5"))
        self.gridLayout_18.addWidget(self.labelParameter_5, 1, 0, 1, 1)
        self.wpscanParameter = QtGui.QLineEdit(self.tab_wpscan)
        self.wpscanParameter.setEnabled(False)
        self.wpscanParameter.setObjectName(_fromUtf8("wpscanParameter"))
        self.gridLayout_18.addWidget(self.wpscanParameter, 1, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.shellWpScan = QtGui.QTextEdit(self.tab_wpscan)
        self.shellWpScan.setAcceptDrops(False)
        self.shellWpScan.setObjectName(_fromUtf8("shellWpScan"))
        self.gridLayout_20.addWidget(self.shellWpScan, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_wpscan, _fromUtf8(""))
        self.tab_skipfish = QtGui.QWidget()
        self.tab_skipfish.setObjectName(_fromUtf8("tab_skipfish"))
        self.gridLayout_23 = QtGui.QGridLayout(self.tab_skipfish)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.gridLayout_21 = QtGui.QGridLayout()
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.skipfishTarget = QtGui.QLineEdit(self.tab_skipfish)
        self.skipfishTarget.setAcceptDrops(False)
        self.skipfishTarget.setObjectName(_fromUtf8("skipfishTarget"))
        self.gridLayout_21.addWidget(self.skipfishTarget, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_skipfish)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_21.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout_22 = QtGui.QGridLayout()
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem5, 0, 1, 1, 1)
        self.pushStartSkipFish = QtGui.QPushButton(self.tab_skipfish)
        self.pushStartSkipFish.setObjectName(_fromUtf8("pushStartSkipFish"))
        self.gridLayout_22.addWidget(self.pushStartSkipFish, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_22, 2, 1, 1, 1)
        self.labelParameter_6 = QtGui.QLabel(self.tab_skipfish)
        self.labelParameter_6.setEnabled(False)
        self.labelParameter_6.setObjectName(_fromUtf8("labelParameter_6"))
        self.gridLayout_21.addWidget(self.labelParameter_6, 1, 0, 1, 1)
        self.skipfishParameter = QtGui.QLineEdit(self.tab_skipfish)
        self.skipfishParameter.setEnabled(False)
        self.skipfishParameter.setObjectName(_fromUtf8("skipfishParameter"))
        self.gridLayout_21.addWidget(self.skipfishParameter, 1, 1, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.shellSkipFish = QtGui.QTextEdit(self.tab_skipfish)
        self.shellSkipFish.setAcceptDrops(False)
        self.shellSkipFish.setObjectName(_fromUtf8("shellSkipFish"))
        self.gridLayout_23.addWidget(self.shellSkipFish, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_skipfish, _fromUtf8(""))
        self.tab_sqlmap = QtGui.QWidget()
        self.tab_sqlmap.setObjectName(_fromUtf8("tab_sqlmap"))
        self.gridLayout_26 = QtGui.QGridLayout(self.tab_sqlmap)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.gridLayout_24 = QtGui.QGridLayout()
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.sqlmapTarget = QtGui.QLineEdit(self.tab_sqlmap)
        self.sqlmapTarget.setAcceptDrops(False)
        self.sqlmapTarget.setObjectName(_fromUtf8("sqlmapTarget"))
        self.gridLayout_24.addWidget(self.sqlmapTarget, 0, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_sqlmap)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_24.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_25 = QtGui.QGridLayout()
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem6, 0, 1, 1, 1)
        self.pushStartSqlMap = QtGui.QPushButton(self.tab_sqlmap)
        self.pushStartSqlMap.setObjectName(_fromUtf8("pushStartSqlMap"))
        self.gridLayout_25.addWidget(self.pushStartSqlMap, 0, 0, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_25, 3, 1, 1, 1)
        self.labelParameter_7 = QtGui.QLabel(self.tab_sqlmap)
        self.labelParameter_7.setEnabled(False)
        self.labelParameter_7.setObjectName(_fromUtf8("labelParameter_7"))
        self.gridLayout_24.addWidget(self.labelParameter_7, 1, 0, 1, 1)
        self.sqlmapParameter = QtGui.QLineEdit(self.tab_sqlmap)
        self.sqlmapParameter.setEnabled(False)
        self.sqlmapParameter.setObjectName(_fromUtf8("sqlmapParameter"))
        self.gridLayout_24.addWidget(self.sqlmapParameter, 1, 1, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.shellSqlmap = QtGui.QTextEdit(self.tab_sqlmap)
        self.shellSqlmap.setAcceptDrops(False)
        self.shellSqlmap.setObjectName(_fromUtf8("shellSqlmap"))
        self.gridLayout_26.addWidget(self.shellSqlmap, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_sqlmap, _fromUtf8(""))
        self.tab_slowloris = QtGui.QWidget()
        self.tab_slowloris.setObjectName(_fromUtf8("tab_slowloris"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_slowloris)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.spinRequest = QtGui.QSpinBox(self.tab_slowloris)
        self.spinRequest.setMaximum(99999)
        self.spinRequest.setObjectName(_fromUtf8("spinRequest"))
        self.gridLayout_12.addWidget(self.spinRequest, 1, 1, 1, 1)
        self.slowlorisTarget = QtGui.QLineEdit(self.tab_slowloris)
        self.slowlorisTarget.setAcceptDrops(False)
        self.slowlorisTarget.setObjectName(_fromUtf8("slowlorisTarget"))
        self.gridLayout_12.addWidget(self.slowlorisTarget, 0, 1, 1, 1)
        self.spinTimeout = QtGui.QSpinBox(self.tab_slowloris)
        self.spinTimeout.setObjectName(_fromUtf8("spinTimeout"))
        self.gridLayout_12.addWidget(self.spinTimeout, 2, 1, 1, 1)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem7, 0, 1, 1, 1)
        self.pushStartSlowLoris = QtGui.QPushButton(self.tab_slowloris)
        self.pushStartSlowLoris.setObjectName(_fromUtf8("pushStartSlowLoris"))
        self.gridLayout_13.addWidget(self.pushStartSlowLoris, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_13, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_slowloris)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_12.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_slowloris)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_slowloris)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_12.addWidget(self.label_7, 1, 0, 1, 1)
        self.labelParameter_8 = QtGui.QLabel(self.tab_slowloris)
        self.labelParameter_8.setEnabled(False)
        self.labelParameter_8.setObjectName(_fromUtf8("labelParameter_8"))
        self.gridLayout_12.addWidget(self.labelParameter_8, 3, 0, 1, 1)
        self.slowlorisParameter = QtGui.QLineEdit(self.tab_slowloris)
        self.slowlorisParameter.setEnabled(False)
        self.slowlorisParameter.setObjectName(_fromUtf8("slowlorisParameter"))
        self.gridLayout_12.addWidget(self.slowlorisParameter, 3, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.shellSlowLoris = QtGui.QTextEdit(self.tab_slowloris)
        self.shellSlowLoris.setAcceptDrops(False)
        self.shellSlowLoris.setObjectName(_fromUtf8("shellSlowLoris"))
        self.gridLayout_14.addWidget(self.shellSlowLoris, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_slowloris, _fromUtf8(""))
        self.tab_exploit = QtGui.QWidget()
        self.tab_exploit.setObjectName(_fromUtf8("tab_exploit"))
        self.tabWidget.addTab(self.tab_exploit, _fromUtf8(""))
        self.tab_dork = QtGui.QWidget()
        self.tab_dork.setObjectName(_fromUtf8("tab_dork"))
        self.tabWidget.addTab(self.tab_dork, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushSocat = QtGui.QPushButton(self.centralwidget)
        self.pushSocat.setEnabled(False)
        self.pushSocat.setObjectName(_fromUtf8("pushSocat"))
        self.gridLayout_2.addWidget(self.pushSocat, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushTor = QtGui.QPushButton(self.centralwidget)
        self.pushTor.setEnabled(True)
        self.pushTor.setObjectName(_fromUtf8("pushTor"))
        self.gridLayout_2.addWidget(self.pushTor, 0, 3, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 5, 1, 1)
        self.labelResolve = QtGui.QLabel(self.centralwidget)
        self.labelResolve.setText(_fromUtf8(""))
        self.labelResolve.setObjectName(_fromUtf8("labelResolve"))
        self.gridLayout_2.addWidget(self.labelResolve, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSocat = QtGui.QAction(MainWindow)
        self.actionSocat.setObjectName(_fromUtf8("actionSocat"))
        self.actionTor = QtGui.QAction(MainWindow)
        self.actionTor.setObjectName(_fromUtf8("actionTor"))
        self.actionWhatWeb = QtGui.QAction(MainWindow)
        self.actionWhatWeb.setObjectName(_fromUtf8("actionWhatWeb"))
        self.actionNmap = QtGui.QAction(MainWindow)
        self.actionNmap.setObjectName(_fromUtf8("actionNmap"))
        self.actionNikto = QtGui.QAction(MainWindow)
        self.actionNikto.setObjectName(_fromUtf8("actionNikto"))
        self.actionJoomScan = QtGui.QAction(MainWindow)
        self.actionJoomScan.setObjectName(_fromUtf8("actionJoomScan"))
        self.actionWpScan = QtGui.QAction(MainWindow)
        self.actionWpScan.setObjectName(_fromUtf8("actionWpScan"))
        self.actionSkipFish = QtGui.QAction(MainWindow)
        self.actionSkipFish.setObjectName(_fromUtf8("actionSkipFish"))
        self.actionSqlmap = QtGui.QAction(MainWindow)
        self.actionSqlmap.setObjectName(_fromUtf8("actionSqlmap"))
        self.actionAbout_Penmode = QtGui.QAction(MainWindow)
        self.actionAbout_Penmode.setObjectName(_fromUtf8("actionAbout_Penmode"))
        self.actionAbout_Phos = QtGui.QAction(MainWindow)
        self.actionAbout_Phos.setObjectName(_fromUtf8("actionAbout_Phos"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.menuHelp.addAction(self.actionSocat)
        self.menuHelp.addAction(self.actionTor)
        self.menuHelp.addAction(self.actionWhatWeb)
        self.menuHelp.addAction(self.actionNmap)
        self.menuHelp.addAction(self.actionNikto)
        self.menuHelp.addAction(self.actionJoomScan)
        self.menuHelp.addAction(self.actionWpScan)
        self.menuHelp.addAction(self.actionSkipFish)
        self.menuHelp.addAction(self.actionSqlmap)
        self.menuAbout.addAction(self.actionAbout_Penmode)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Phos)
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushStartWhatWeb.setText(_translate("MainWindow", "Start", None))
        self.label_3.setText(_translate("MainWindow", "Target", None))
        self.labelParameter_1.setText(_translate("MainWindow", "Parameter", None))
        self.shellWhatWeb.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Oxygen\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_whatweb), _translate("MainWindow", "WhatWeb", None))
        self.label_4.setText(_translate("MainWindow", "Target", None))
        self.pushStartNmap.setText(_translate("MainWindow", "Start", None))
        self.labelParameter_2.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nmap), _translate("MainWindow", "Nmap", None))
        self.label_5.setText(_translate("MainWindow", "Target", None))
        self.pushStartNikto.setText(_translate("MainWindow", "Start", None))
        self.labelParameter_3.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nikto), _translate("MainWindow", "Nikto", None))
        self.pushStartJoomScan.setText(_translate("MainWindow", "Start", None))
        self.label_9.setText(_translate("MainWindow", "Target", None))
        self.labelParameter_4.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_joomscan), _translate("MainWindow", "JoomScan", None))
        self.label_10.setText(_translate("MainWindow", "Target", None))
        self.pushStartWpScan.setText(_translate("MainWindow", "Start", None))
        self.labelParameter_5.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wpscan), _translate("MainWindow", "WpScan", None))
        self.label_11.setText(_translate("MainWindow", "Target", None))
        self.pushStartSkipFish.setText(_translate("MainWindow", "Start", None))
        self.labelParameter_6.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skipfish), _translate("MainWindow", "SkipFish", None))
        self.label_12.setText(_translate("MainWindow", "Target", None))
        self.pushStartSqlMap.setText(_translate("MainWindow", "Start", None))
        self.labelParameter_7.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sqlmap), _translate("MainWindow", "SqlMap", None))
        self.pushStartSlowLoris.setText(_translate("MainWindow", "Start", None))
        self.label_8.setText(_translate("MainWindow", "TimeOut (sec)", None))
        self.label_6.setText(_translate("MainWindow", "Target", None))
        self.label_7.setText(_translate("MainWindow", "Requests Number", None))
        self.labelParameter_8.setText(_translate("MainWindow", "Parameter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_slowloris), _translate("MainWindow", "SlowLoris", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_exploit), _translate("MainWindow", "Exploit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dork), _translate("MainWindow", "Dork", None))
        self.pushSocat.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "Socat", None))
        self.label_2.setText(_translate("MainWindow", "Tor", None))
        self.pushTor.setText(_translate("MainWindow", "Start", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionSocat.setText(_translate("MainWindow", "Socat", None))
        self.actionTor.setText(_translate("MainWindow", "Tor", None))
        self.actionWhatWeb.setText(_translate("MainWindow", "WhatWeb", None))
        self.actionNmap.setText(_translate("MainWindow", "Nmap", None))
        self.actionNikto.setText(_translate("MainWindow", "Nikto", None))
        self.actionJoomScan.setText(_translate("MainWindow", "JoomScan", None))
        self.actionWpScan.setText(_translate("MainWindow", "WpScan", None))
        self.actionSkipFish.setText(_translate("MainWindow", "SkipFish", None))
        self.actionSqlmap.setText(_translate("MainWindow", "Sqlmap", None))
        self.actionAbout_Penmode.setText(_translate("MainWindow", "About Penmode", None))
        self.actionAbout_Phos.setText(_translate("MainWindow", "About Ph#os", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))

