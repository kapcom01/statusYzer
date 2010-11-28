# -*- coding: utf-8 -*-

#  Copyright 2009-2010 Emmanouel Kapernaros <manolis@kapcom.gr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3 as published by
#    the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import gettext
t = gettext.translation('statusyzer', 'locale', fallback=True)
_ = t.ugettext

from PyQt4 import QtCore, QtGui
import pcapy
import time
from fln_n_msn_ui import Ui_flnDialog
from about_ui import Ui_aboutDialog
from statusyzer_ui import Ui_statusyzer

class flnForm(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.fln = Ui_flnDialog()
		self.fln.setupUi(self)

class aboutForm(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.about = Ui_aboutDialog()
		self.about.setupUi(self)

class StatusyzerForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_statusyzer()
		self.ui.setupUi(self)
		#αρχικοποίηση strings
		self.ui.pushButton_start_sniffer.setText(_('Start Analyzing'))
		self.ui.pb_all.setText(_('All'))
		self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab0),_('All'))
		self.ui.tableWidget.horizontalHeaderItem(0).setText(_('Contacts'))
		self.ui.tableWidget.horizontalHeaderItem(1).setText(_('Fakes'))
		self.ui.pb_whatisfln.setText(_('FLN and MSN program'))
		self.ui.pb_about.setText(_('About statusYzer'))
		#-----------------
		self.test_findalldevs()
		self.ctimer = QtCore.QTimer()
		QtCore.QObject.connect(self.ui.pushButton_start_sniffer, QtCore.SIGNAL("released()"), self.start_button_check)
		QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.constantUpdate)
		QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.show_item_tabs)
		QtCore.QObject.connect(self.ui.pb_whatisfln, QtCore.SIGNAL("released()"), self.show_fln)
		QtCore.QObject.connect(self.ui.pb_about, QtCore.SIGNAL("released()"), self.show_about)
		self.mpinies = {}
		self.buddies = {}

	def show_fln(self):
		self.dlg = flnForm()
		self.dlg.show()

	def show_about(self):
		self.dlg = aboutForm()
		self.dlg.show()

	def show_item_tabs(self):
		tmpindex = self.ui.tableWidget.currentRow()
		self.ui.tabWidget.setCurrentIndex(tmpindex+1)

	def test_findalldevs(self):
		try:
			for ifname in pcapy.findalldevs():
				self.ui.combobox_interfaces.addItem(ifname)
		except:
			pass
		if self.ui.combobox_interfaces.count() == 0 :
			self.ui.list_statuses.addItem(_('ERROR: Could not find a network device. Are you Administrator?'))
			tablistrow = self.ui.list_statuses.count()-1
			self.ui.list_statuses.item(tablistrow).setTextColor(QtGui.QColor('red'))
	def constantUpdate(self):
		try:
			(header, payload) = self.cap.next()
		except:
			return
		if header != None : self.print_packet(header.getlen(),payload,time.strftime('%d-%m-%Y, %H:%M:%S'))

	def start_button_check(self):
		self.ifname = self.ui.combobox_interfaces.currentText()
		if self.ui.pushButton_start_sniffer.text() == _('Start Analyzing'):
			new_text = '%s %s...' % (_('Stop Analyzing'), self.ifname)
			self.ui.pushButton_start_sniffer.setText(new_text)
			self.start_sniffer()
		else:
			new_text = _('Start Analyzing')
			self.ui.pushButton_start_sniffer.setText(new_text)
			tmpstr = _('Analyzing Stopped')

			self.ui.list_statuses.addItem(tmpstr)
			self.ctimer.stop()

	def on_pb_all_released(self):
		self.ui.tabWidget.setCurrentIndex(0)

	def decode_ip_packet(self,s):
		d={}
		d['version']=(ord(s[0]) & 0xf0) >> 4
		d['header_len']=ord(s[0]) & 0x0f
		if d['header_len']>5:
			d['options']=s[20:4*(d['header_len']-5)]
		else:
			d['options']=None
		d['data']=s[4*d['header_len']:]
		return d

	def decode_tcp_packet(self,s):
		t={}
		t['header_len']=(ord(s[12]) & 0xf0) >> 4
		t['data']=s[4*t['header_len']:]
		return t

	def print_packet(self,pktlen, data, timestamp):
		if not data:
			return
		if data[12:14]=='\x08\x00':
			decoded_ip=self.decode_ip_packet(data[14:])
			#print 'IP: %s' % decoded_ip
			ip_header_bytes=4*decoded_ip['header_len']
			decoded_tcp=self.decode_tcp_packet(data[(14+ip_header_bytes):])
			data_str=decoded_tcp['data']
			#print 'TCP payload: %s' % data_str
			command=data_str.split()
			if len(command)>1:
				if 'ILN'==command[0]: self.buddy_status_change(command[3],'Online')
				elif 'NLN'==command[0]: self.buddy_status_change(command[2],'Online')
				elif 'FLN'==command[0]: self.buddy_status_change(command[1],'Offline')
				elif 'XFR'==command[0] and 'NS'==command[2]: self.ns_redirection(command[3])
				elif 'RNG'==command[0]: print 'RNG: ' + command[5] + ' ' + command[6]
				elif 'BYE'==command[0]: print 'BYE: ' + command[1]

	def buddy_status_change(self,email,status):
		status_color = {}
		status_color['Online'] = QtGui.QColor('green')
		status_color['Offline'] = QtGui.QColor('black')

		colon = email.find(':')
		if colon!=-1:
			if email[0:colon]=='32': return
			else: email = email[colon+1:]
		
		colon = email.find(';')
		if colon!=-1:
			email = '[G]' + email[:colon]
		
		#ελέγχουμε αν υπάρχει ήδη αυτη η επαφή
		if email in self.buddies:
			if self.buddies[email].getStatus() == 'Online' and status == 'Online': return
			tmplist0row = self.ui.list_statuses.count()
			self.ui.list_statuses.addItem('(%s): [%s] %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), email, status))
			tmpindex = self.buddies[email].getIndex()
			self.buddies[email].tablist.addItem('(%s): %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), status))
			tablistrow = self.buddies[email].tablist.count()-1
			self.buddies[email].tablist.item(tablistrow).setTextColor(status_color[status])
			self.ui.list_statuses.item(tmplist0row).setTextColor(status_color[status])
			self.ui.tableWidget.item(tmpindex,0).setTextColor(status_color[status])
			if self.buddies[email].getStatus() == 'Offline':
				if status == 'Offline':
					self.buddies[email].addMpinia()
					self.ui.tableWidget.item(tmpindex,1).setTextColor(QtGui.QColor('red'))
					self.buddies[email].tablist.item(tablistrow).setTextColor(QtGui.QColor('red'))
					self.ui.list_statuses.item(tmplist0row).setTextColor(QtGui.QColor('red'))
			mpinies = self.buddies[email].getMpinies()
			self.ui.tableWidget.item(tmpindex,1).setText(mpinies)
			self.buddies[email].setStatus(status)
			return
		
		#δημιουργούμε αντικείμενο για τη νέα επαφή και το προσθέτουμε στους buddies
		tmpbuddy = MSN_Buddy(email)
		self.buddies[email]=tmpbuddy
		self.buddies[email].setStatus(status)
		if status == 'Offline': self.buddies[email].addMpinia()

		#δημιουργούμε νέα καρτέλα και λίστα για τις καταστάσεις της επαφής
		newtab = QtGui.QWidget()
		self.ui.tabWidget.addTab(newtab,email)
		newlist = QtGui.QListWidget(newtab)
		newlist.addItem(('(%s): %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), status)))
		newlist.item(0).setTextColor(status_color[status])
		self.buddies[email].tablist = newlist
		#προσθέτουμε το γεγονος και στην καρτέλα "Όλα"
		tmplist0row = self.ui.list_statuses.count()
		self.ui.list_statuses.addItem('(%s): [%s] %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), email, status))
		self.ui.list_statuses.item(tmplist0row).setTextColor(status_color[status])
		#τοποθετούμε τη νέα λίστα σε grid layout με την νέα καρτέλα
		newLayout = QtGui.QGridLayout()
		newLayout.addWidget(self.buddies[email].tablist)
		newtab.setLayout(newLayout)
		#εισάγουμε νέα γραμμή στο πίνακα αριστερά
		cnt = self.ui.tableWidget.rowCount()
		self.ui.tableWidget.insertRow(cnt)
		self.buddies[email].setIndex(cnt)

		tmpitem0 = QtGui.QTableWidgetItem(email)
		self.ui.tableWidget.setItem(cnt,0,tmpitem0)
		self.ui.tableWidget.item(cnt,0).setTextColor(status_color[status])
		
		mpinies = self.buddies[email].getMpinies()
		tmpitem1 = QtGui.QTableWidgetItem(mpinies)
		self.ui.tableWidget.setItem(cnt,1,tmpitem1)

		if mpinies =='1':
			self.ui.tableWidget.item(cnt,1).setTextColor(QtGui.QColor('red'))
			self.buddies[email].tablist.item(0).setTextColor(QtGui.QColor('red'))
			self.ui.list_statuses.item(tmplist0row).setTextColor(QtGui.QColor('red'))

	def ns_redirection(self,address):
		self.ui.list_statuses.addItem('(%s): %s %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), _('Detected Connecting to Notification Server at'), address))
		tablistrow = self.ui.list_statuses.count()-1
		self.ui.list_statuses.item(tablistrow).setTextColor(QtGui.QColor('orange'))

		for email in self.buddies:
			tmpindex = self.buddies[email].getIndex() #fuzyy.. δεν θυμάμαι γιατί το έγραψα...
			self.buddies[email].tablist.addItem('(%s): %s %s' % (time.strftime('%d-%m-%Y, %H:%M:%S'), _('Detected Connecting to Notification Server at'), address))
			tablistrow = self.buddies[email].tablist.count()-1
			self.buddies[email].tablist.item(tablistrow).setTextColor(QtGui.QColor('orange'))

	def start_sniffer(self):
		self.ifname = str(self.ifname)
		tmpstr = '%s %s' % (_('Opening'), self.ifname)
		self.ui.list_statuses.addItem(tmpstr)
		try:
			self.cap = pcapy.open_live(self.ifname, 1600, 1, 5)
		except:
			self.ui.list_statuses.addItem(_('ERROR'))
			return
		self.cap.setfilter('tcp port 1863')
		tmpstr = '%s' % _('Analyzing Notifications...')
		self.ui.list_statuses.addItem(tmpstr)
		self.ctimer.start(10)
		tmpstr = '%s' % _('Now you can start your MSN program...')
		self.ui.list_statuses.addItem(tmpstr)
		tablistrow = self.ui.list_statuses.count()-1
		self.ui.list_statuses.item(tablistrow).setTextColor(QtGui.QColor('green'))


class MSN_Buddy():
	
	def __init__(self,email):
		self.email = email
		self.mpinies = 0
		self.tablist = QtGui.QListWidget()

	def getEmail(self):
		return self.email

	def setIndex(self,index):
		self.index=index

	def getIndex(self):
		return self.index

	def setStatus(self,status):
		self.status=status

	def getStatus(self):
		return self.status

	def addMpinia(self):
		self.mpinies = self.mpinies+1

	def getMpinies(self):
		return str(self.mpinies)


try:
	# Change the process name.
	import ctypes
	libc = ctypes.CDLL('libc.so.6')
	libc.prctl(15, 'statusYzer', 0, 0)
except:
	pass

if __name__ == "__main__":
	app = QtGui.QApplication([])

	myapp = StatusyzerForm()
	myapp.show()

	app.exec_()