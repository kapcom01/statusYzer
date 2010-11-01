# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusyzer.ui'
#
# Created: Sun Nov 22 01:03:31 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_statusyzer(object):
    def setupUi(self, statusyzer):
        statusyzer.setObjectName("statusyzer")
        statusyzer.resize(563, 521)
        self.centralWidget = QtGui.QWidget(statusyzer)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.combobox_interfaces = QtGui.QComboBox(self.centralWidget)
        self.combobox_interfaces.setObjectName("combobox_interfaces")
        self.gridLayout.addWidget(self.combobox_interfaces, 0, 0, 1, 1)
        self.pushButton_start_sniffer = QtGui.QPushButton(self.centralWidget)
        self.pushButton_start_sniffer.setObjectName("pushButton_start_sniffer")
        self.gridLayout.addWidget(self.pushButton_start_sniffer, 0, 1, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.centralWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtGui.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_all = QtGui.QPushButton(self.layoutWidget)
        self.pb_all.setObjectName("pb_all")
        self.verticalLayout.addWidget(self.pb_all)
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab0 = QtGui.QWidget()
        self.tab0.setObjectName("tab0")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_statuses = QtGui.QListWidget(self.tab0)
        self.list_statuses.setObjectName("list_statuses")
        self.gridLayout_2.addWidget(self.list_statuses, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab0, "")
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 2)
        self.pb_whatisfln = QtGui.QPushButton(self.centralWidget)
        self.pb_whatisfln.setObjectName("pb_whatisfln")
        self.gridLayout.addWidget(self.pb_whatisfln, 2, 0, 1, 1)
        self.pb_about = QtGui.QPushButton(self.centralWidget)
        self.pb_about.setObjectName("pb_about")
        self.gridLayout.addWidget(self.pb_about, 2, 1, 1, 1)
        statusyzer.setCentralWidget(self.centralWidget)

        self.retranslateUi(statusyzer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(statusyzer)

    def retranslateUi(self, statusyzer):
        statusyzer.setWindowTitle(QtGui.QApplication.translate("statusyzer", "statusYzer (www.kapcom.gr)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start_sniffer.setText(QtGui.QApplication.translate("statusyzer", "Έναρξη ", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_all.setText(QtGui.QApplication.translate("statusyzer", "Όλα", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("statusyzer", "Επαφές", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("statusyzer", "Μπινιές", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), QtGui.QApplication.translate("statusyzer", "Όλα", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_whatisfln.setText(QtGui.QApplication.translate("statusyzer", "Τι είναι το πακέτο FLN", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_about.setText(QtGui.QApplication.translate("statusyzer", "Σχετικά με το πρόγραμμα", None, QtGui.QApplication.UnicodeUTF8))

