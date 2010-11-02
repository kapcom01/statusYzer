# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Mon Dec 14 20:22:46 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(714, 520)
        self.gridLayout = QtGui.QGridLayout(aboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(aboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(aboutDialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), aboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "Σχετικά με το πρόγραμμα", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("aboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600; text-decoration: underline;\">statusYzer</span><span style=\" font-size:x-large;\"> <br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large;\">Το πρόγραμμα καταγράφει όλες τις καταστάσεις</span> των επαφών σας και <span style=\" color:#ff0000;\">τονίζει με κόκκινο τις ύποπτες καταστάσεις</span> χαρης σε ένα bug του msn. Έτσι μπορείτε να δείτε πότε μπήκε και πότε βγήκε κάποια επαφή σας αναλυτικά. <br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Για παράδειγμα, όταν ληφθεί κατάσταση <span style=\" color:#3d85c6; background-color:#ffffff;\">\"Εκτος Σύνδεσης</span><span style=\" color:#3d85c6;\">\"\'</span> για κάποια επαφή σας η οποία ΔΕΝ ηταν συνδεδεμένη, τότε αυτο <span style=\" background-color:#fff2cc;\">πιθανοντατα*</span> σημαίνει ότι μόλις τώρα συνδέθηκε με κατάσταση \"<span style=\" font-style:italic;\">Εμφάνιση Εκτος Σύνδεσης</span>\" οπότε η κατάσταση αυτή τονίζεται με κόκκινο χρώμα στο πρόγραμμα!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#fff2cc;\">*πιθανότατα</span>: βέβαια μπορεί να ισχύει το άλλο σενάριο, να βγήκε πραγματικά απο το msn αλλά τόση ώρα να ήταν σε \"<span style=\" font-style:italic;\">Εμφάνιση Εκτος Σύνδεσης</span>\". Όπως και να\'χει αυτό πρέπει να σημειωθεί με κόκκινο!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">-<span style=\" font-style:italic;\">Το σίγουρο είναι οτι το πρόγραμμα δεν γίνεται να ανεφέρει λάθος κατάσταση! Ο server της microsoft μπορει..</span></p>\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:small;\">Μανώλης (kapcom01) 2009</span></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:small;\"></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Το statusYzer είναι ένα μέρος του αναλυτή kapcomYzer που ακόμα βρίσκεται υπο κατασκευή...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

