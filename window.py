# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 219)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 261, 160))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(42)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGen = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnGen.setObjectName("btnGen")
        self.gridLayout.addWidget(self.btnGen, 5, 1, 1, 1)
        self.rdSpecialChar = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rdSpecialChar.setAutoExclusive(False)
        self.rdSpecialChar.setObjectName("rdSpecialChar")
        self.gridLayout.addWidget(self.rdSpecialChar, 4, 1, 1, 1)
        self.slLength = QtWidgets.QSlider(self.gridLayoutWidget)
        self.slLength.setMinimum(6)
        self.slLength.setMaximum(36)
        self.slLength.setPageStep(3)
        self.slLength.setOrientation(QtCore.Qt.Horizontal)
        self.slLength.setObjectName("slLength")
        self.gridLayout.addWidget(self.slLength, 1, 1, 1, 1)
        self.rdUpLowCase = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rdUpLowCase.setAutoExclusive(False)
        self.rdUpLowCase.setObjectName("rdUpLowCase")
        self.gridLayout.addWidget(self.rdUpLowCase, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 2, 2, 1, 1)
        self.rdNumbers = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rdNumbers.setAutoExclusive(False)
        self.rdNumbers.setObjectName("rdNumbers")
        self.gridLayout.addWidget(self.rdNumbers, 3, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.lbLength = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbLength.setObjectName("lbLength")
        self.gridLayout.addWidget(self.lbLength, 0, 1, 1, 1)
        self.lbPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lbPassword.setGeometry(QtCore.QRect(4, 180, 251, 20))
        self.lbPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPassword.setObjectName("lbPassword")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.slLength.valueChanged.connect(lambda: self.lbLength.setText("Password lenght: "+str(self.slLength.value()))) # Update the line displaying the length everytime the slider value changes
        self.btnGen.clicked.connect(lambda: self.generate()) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.btnGen.setText(_translate("MainWindow", "Generate"))
        self.rdSpecialChar.setText(_translate("MainWindow", "Special Characters"))
        self.rdUpLowCase.setText(_translate("MainWindow", "Upper and Lower case"))
        self.lbPassword.setText(_translate("MainWindow", "Your password will appear here"))
        self.rdNumbers.setText(_translate("MainWindow", "Numbers"))
        self.lbLength.setText(_translate("MainWindow", "Password lenght: "+str(self.slLength.value())))
    
    def generate(self):
        import string
        import random
        random.seed()

        options = [] # List to push checked radios

        if self.rdUpLowCase.isChecked(): options.append('Aa') # Check if user wants lower and upper cases
        if self.rdNumbers.isChecked(): options.append('123') # Check if user wants numbers
        if self.rdSpecialChar.isChecked(): options.append('&') # Check if user wants special characters
        # A full password list would be ['Aa', '123', '&']
        # We will later check for each item to see what the user wants to include

        i = 0
        passwd = '' # defining password string
        while i != self.slLength.value(): # Repeat a while loop until the password reaches the length set by the slider 
            if options: # If there is at least one checked radio
                x = random.randint(0, len(options)-1)
                if options[x] == 'Aa': char = random.choice(string.ascii_letters) # Randomily choose a letter from the ascii code
                elif options[x] == '123': char = str(random.randrange(0, 9)) # Randomly chooses a number from 0 to 9
                elif options[x] == '&': char = random.choice(string.punctuation) # Randomly choose a special character
                
            else: # If there is no checked radio
                char = random.choice(string.ascii_letters) 

            passwd = passwd + char # Put the latest char to our password
            i += 1

        if 'Aa' not in options: passwd = passwd.lower() # Lower case everything if user do not check the letters radio
        self.lbPassword.setText(passwd)


if __name__ == "__main__":
    import sys
            
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())