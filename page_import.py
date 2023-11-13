# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:16:24 2021

@author: Christopher.Willacy
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

#----------------------------------------------------------------------
#  IMPORT SPS PAGE
#----------------------------------------------------------------------
def PageImport(self,Wizard,icons,tipstyle,groupstyle,labelstyle):  
    
    self.wizardPage3 = QtWidgets.QWizardPage()
    self.wizardPage3.setObjectName("wizardPage3")
    self.wizardPage3.setTitle("Navigation Import")
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage3)
    self.verticalLayout_2.setObjectName("verticalLayout_2")
    self.groupBox_3 = QtWidgets.QGroupBox(self.wizardPage3)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.groupBox_3.setFont(font)
    self.groupBox_3.setStyleSheet(groupstyle)
    self.groupBox_3.setObjectName("groupBox_3")
    self.groupBox_3.setTitle("SPS Files")
    self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
    self.verticalLayout_3.setObjectName("verticalLayout_3")
    self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_9.setObjectName("horizontalLayout_9")
    self.label_10 = QtWidgets.QLabel(self.groupBox_3)
    self.label_10.setBaseSize(QtCore.QSize(0, 0))
    self.label_10.setObjectName("label_10")
    self.label_10.setStyleSheet(labelstyle)
    self.label_10.setText("SPS source:")
    self.label_10.setFixedWidth(125)
    self.horizontalLayout_9.addWidget(self.label_10)
    self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
    self.lineEdit_5.setObjectName("lineEdit_5")
    self.lineEdit_5.setText('')
    self.horizontalLayout_9.addWidget(self.lineEdit_5)       
    self.lineEdit_5.setToolTip("enter the SPS source file")
    self.lineEdit_5.setStyleSheet(tipstyle)
    self.lineEdit_5.textChanged[str].connect(self.changestate_spssrc)    
    self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
    self.pushButton_3.setObjectName("pushButton_3")
    self.pushButton_3.setStyleSheet("border: none")
    self.pushButton_3.setIcon(QIcon(icons[3])) 
    self.horizontalLayout_9.addWidget(self.pushButton_3)
    self.verticalLayout_3.addLayout(self.horizontalLayout_9)
    self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_10.setObjectName("horizontalLayout_10")
    self.label_11 = QtWidgets.QLabel(self.groupBox_3)
    self.label_11.setObjectName("label_11")
    self.label_11.setStyleSheet(labelstyle)
    self.label_11.setText("SPS receiver:")
    self.label_11.setFixedWidth(125)
    self.horizontalLayout_10.addWidget(self.label_11)
    self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
    self.lineEdit_6.setObjectName("lineEdit_6")
    self.lineEdit_6.setText('')
    self.horizontalLayout_10.addWidget(self.lineEdit_6)
    self.lineEdit_6.setToolTip("enter the SPS receiver file")
    self.lineEdit_6.setStyleSheet(tipstyle)
    self.lineEdit_6.textChanged[str].connect(self.changestate_spsrec) 
    self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
    self.pushButton_4.setObjectName("pushButton_4")
    self.pushButton_4.setStyleSheet("border: none")
    self.pushButton_4.setIcon(QIcon(icons[3]))
    self.horizontalLayout_10.addWidget(self.pushButton_4)
    self.verticalLayout_3.addLayout(self.horizontalLayout_10)
    self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_11.setObjectName("horizontalLayout_11")
    self.label_12 = QtWidgets.QLabel(self.groupBox_3)
    self.label_12.setObjectName("label_12")
    self.label_12.setStyleSheet(labelstyle)
    self.label_12.setText("SPS relational:")
    self.label_12.setFixedWidth(125)
    self.horizontalLayout_11.addWidget(self.label_12)
    self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
    self.lineEdit_7.setObjectName("lineEdit_7")
    self.lineEdit_7.setText('')
    self.horizontalLayout_11.addWidget(self.lineEdit_7)
    self.lineEdit_7.setToolTip("enter the SPS relational file")
    self.lineEdit_7.setStyleSheet(tipstyle)
    self.lineEdit_7.textChanged[str].connect(self.changestate_spsrel) 
    self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
    self.pushButton_5.setObjectName("pushButton_5")
    self.pushButton_5.setStyleSheet("border: none")
    self.pushButton_5.setIcon(QIcon(icons[3]))
    self.horizontalLayout_11.addWidget(self.pushButton_5)
    self.verticalLayout_3.addLayout(self.horizontalLayout_11)
    self.verticalLayout_2.addWidget(self.groupBox_3)
    self.groupBox_4 = QtWidgets.QGroupBox(self.wizardPage3)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.groupBox_4.setFont(font)
    self.groupBox_4.setStyleSheet(groupstyle)
    self.groupBox_4.setObjectName("groupBox_4")
    self.groupBox_4.setTitle("Coordinate Translation")
    self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
    self.verticalLayout_4.setObjectName("verticalLayout_4")
    self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_12.setObjectName("horizontalLayout_12")
    self.label_13 = QtWidgets.QLabel(self.groupBox_4)
    self.label_13.setObjectName("label_13")
    self.label_13.setStyleSheet(labelstyle)
    self.label_13.setText("Apply bulk coordinate shift?:")
    self.horizontalLayout_12.addWidget(self.label_13)
    self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_4)
    self.checkBox_4.setText("")
    self.checkBox_4.setChecked(False)
    self.checkBox_4.setObjectName("checkBox_4")
    self.horizontalLayout_12.addWidget(self.checkBox_4)
    self.checkBox_4.setToolTip("select option to apply a bulk shift the the x,y coordinates")
    self.checkBox_4.setStyleSheet(tipstyle)
   
    self.verticalLayout_4.addLayout(self.horizontalLayout_12)
    self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_14.setObjectName("horizontalLayout_14")
    self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_13.setObjectName("horizontalLayout_13")
    
    self.label_14 = QtWidgets.QLabel(self.groupBox_4)
    self.label_14.setObjectName("label_14")
    self.label_14.setStyleSheet(labelstyle)
    self.label_14.setText("X0:")        
    spacerItem_14 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_13.addItem(spacerItem_14)        
    self.horizontalLayout_13.addWidget(self.label_14)
    self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
    self.lineEdit_8.setSizePolicy(sizePolicy)
    self.lineEdit_8.setObjectName("lineEdit_8")
    self.lineEdit_8.setDisabled(True)       
    self.horizontalLayout_13.addWidget(self.lineEdit_8)
    self.lineEdit_8.setToolTip("horizontal shift to apply to the X coordinate")
    self.lineEdit_8.setStyleSheet(tipstyle) 
    self.lineEdit_8.setFixedWidth(75)
    self.lineEdit_8.textChanged[str].connect(self.changestate_x0) 
    spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_13.addItem(spacerItem3)
    self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
    self.label_15 = QtWidgets.QLabel(self.groupBox_4)
    self.label_15.setObjectName("label_15")
    self.label_15.setStyleSheet(labelstyle)
    self.label_15.setText("Y0:")
    self.horizontalLayout_14.addWidget(self.label_15)
    self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
    self.lineEdit_9.setSizePolicy(sizePolicy)
    self.lineEdit_9.setObjectName("lineEdit_9")
    self.lineEdit_9.setDisabled(True)
    self.horizontalLayout_14.addWidget(self.lineEdit_9)
    self.lineEdit_9.setToolTip("vertical shift to apply to the Y coordinate")
    self.lineEdit_9.setStyleSheet(tipstyle)  
    self.lineEdit_9.setFixedWidth(75)
    self.lineEdit_9.textChanged[str].connect(self.changestate_y0) 
    spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout_14.addItem(spacerItem4)
    self.verticalLayout_4.addLayout(self.horizontalLayout_14)
    self.verticalLayout_2.addWidget(self.groupBox_4)
    
    self.checkBox_4.clicked.connect(self.changestate_bshift)
    Wizard.setPage(3,self.wizardPage3) 