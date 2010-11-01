# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whatisfln.ui'
#
# Created: Mon Nov 16 16:19:14 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_flnDialog(object):
    def setupUi(self, flnDialog):
        flnDialog.setObjectName("flnDialog")
        flnDialog.resize(773, 699)
        self.gridLayout = QtGui.QGridLayout(flnDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(flnDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(flnDialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.retranslateUi(flnDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), flnDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), flnDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(flnDialog)

    def retranslateUi(self, flnDialog):
        flnDialog.setWindowTitle(QtGui.QApplication.translate("flnDialog", "Τι είναι το πακέτο FLN", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("flnDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">Πολύ γενικά, </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; font-weight:600;\">πακέτο</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> ονομάζεται το στοιχειώδης αυτοδύναμο κομμάτι δεδομένων της πληροφορίας που μεταφέρεται στο διαδίκτυο.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">Για παράδειγμα όταν στέλνουμε μία φωτογραφία, αυτή πριν μεταδωθεί διασπάται σε πακέτα συγκεκριμένης μορφής που περιέχουν κάποιες επιπλέον πληροφορίες όπως τα στοιχεία του παραλήπτη. Έτσι λοιπόν, τα μηχανήματα που βρίσκονται ανάμεσα στον υπολογιστή μας και στον υπολογιστή του παραλήπτη, όπως πχ τα μηχανήματα του ΟΤΕ, θα μπορέσουν να καταλάβουν για ποιόν είναι το πακέτο και θα το προωθήσουν. Το MSN (Windows Live Messenger) χρησιμοποιεί ένα δικό του πρωτόκολλο για την επικοινωνία. Το πρωτόκολλο αυτό ορίζει κάποιες εντολές επιπρόσθετα στο πακέτο εκτός απο το κείμενο της συνομιλίας που πληκτρολογούμε εμείς όταν μιλάμε. Αναφορικά μερικές εντολές είναι οι: </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">ILN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">, </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">MSG </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\">και</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">FLN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">Πολύ χοντρικά ο σέρβερ στέλνει την εντολή </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">ILN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> για να μας ενημερώσει οτι κάποιος φίλος μας μόλις εισήλθε, την </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">MSG</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> όταν κάποιος μας στέλνει κάποιο μήνυνα και τη </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#ffaa00;\">FLN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> όταν κάποιος αποσυνδέεται.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">πχ1: \"</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#0000ff;\">ILN manolis@kapcom.gr</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">\" αυτό σημαίνει οτι ο χρήστης με email </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\">manolis@kapcom.gr</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> μόλις συνδέθηκε.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">πχ2: \"</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#0000ff;\">FLN manolis@kapcom.gr</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">\" αυτό σημαίνει οτι ο χρήστης με email </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\">manolis@kapcom.gr</span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\"> μόλις αποσυνδέθηκε.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'FreeSans\'; font-size:11pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt; font-weight:600; text-decoration: underline;\">Το BUG</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">Όταν κάποιος αλλάζει κατάσταση σε \"Εμφάνιση Εκτός Σύνδεσης\" ο σέρβερ της microsoft στέλνει κανονικά ένα </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; font-weight:600;\">πακέτο FLN </span><span style=\" font-family:\'FreeSans\'; font-size:11pt;\">για να νομίζουν όλοι οι φίλοι του οτι αποσυνδέθηκε. Μέχρι εδώ καλά. Το πρόβλημα είναι ότι όταν αυτός αποσυνδεθεί πραγματικά (πχ κλείσει τον υπολογιστη του) τότε ο σέρβερ </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; font-weight:600; color:#ff0000;\">ΞΑΝΑΣΤΕΛΝΕΙ πακέτο FLN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\">. Το MSN βέβαια αγνοεί το δεύτερο πακέτο FLN αλλά το πρόγραμμά μας ΟΧΙ !! :) </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; text-decoration: underline; color:#000000;\">Έτσι καταλαβαίνουμε ότι ο χρήστης πριν το δεύτερο FLN ήταν μέσα!</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\"> (σε κατάσταση \"Εμφάνιση Εκτός Σύνδεσης\") Και δεν έφτανε αυτό, στις νέες εκδόσεις του Live Messenger, το bug εγινε χειρότερο! Εκτός από τα παραπάνω, </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; text-decoration: underline; color:#000000;\">τώρα στέλνει πακέτο FLN</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\"> και όταν ο χρήστης συνδεθεί στο messenger </span><span style=\" font-family:\'FreeSans\'; font-size:11pt; text-decoration: underline; color:#000000;\">έχοντας πρεπιλεγμένη την κατάσταση \"εμφάνιση εκτός σύνδεσης\"</span><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#000000;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'FreeSans\'; font-size:11pt; color:#000000;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'FreeSans\'; font-size:11pt; color:#00aa00;\">Σκοπός είναι η microsoft να διορθώσει αυτό το bug γιατί όπως και να το κάνουμε είναι ιδιωτική πληροφορία. Μέχρι τότε όμως καλό χακερικό κουτσομπολιό! :)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

