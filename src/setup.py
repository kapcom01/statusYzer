#ENGLISH:
#This file is for making an exe (portable) version for Windows
#
#ΕΛΛΗΝΙΚΑ:
#Αυτό το αρχείο είναι για τη δημιουργία μιας exe (φορητής) έκδοσης για Windows

from distutils.core import setup
import py2exe

setup(windows=['statusyzer.pyw'])

