# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_file.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import rpy2.robjects as robjects  
from rpy2.robjects import *

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

class Ui_import_file(object):
    def setupUi(self, import_file):
        import_file.setObjectName(_fromUtf8("import_file"))
        import_file.resize(222, 161)
        import_file.setFrameShape(QtGui.QFrame.StyledPanel)
        import_file.setFrameShadow(QtGui.QFrame.Raised)
        self.label = QtGui.QLabel(import_file)
        self.label.setGeometry(QtCore.QRect(20, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(import_file)
        self.pushButton.setGeometry(QtCore.QRect(90, 50, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("Browse"))

        self.retranslateUi(import_file)
        QtCore.QMetaObject.connectSlotsByName(import_file)

    def retranslateUi(self, import_file):
        import_file.setWindowTitle(_translate("import_file", "Frame", None))
        self.label.setText(_translate("import_file", "Open File", None))
        self.pushButton.setText(_translate("import_file", "Browse", None))
        self.pushButton.clicked.connect(self.file_path)


    def file_path(self):
    	
		#path = r('file.choose()')
		#print (path)
		#path = str(path)
		#print (path)
		myData = robjects.r['read.csv'](r('file.choose()'))
		#myData = robjects.r['read.csv']("C:\\Users\\CoEA\\Downloads\\bank\\bank.csv")

		#myData = robjects.r['read.csv']("/Users/CoEA/Downloads/bank/bank.csv")
		print myData
		print robjects.r['summary'](myData)
		    	

	# def save_file(self):
	# 	import rpy2.robjects as robjects
	# 	myData = robjects.r.path
	# 	print myData
		



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    import_file = QtGui.QFrame()
    ui = Ui_import_file()
    ui.setupUi(import_file)
    import_file.show()
    sys.exit(app.exec_())

