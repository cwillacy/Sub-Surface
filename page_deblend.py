# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:26:06 2021

@author: Christopher.Willacy
"""
from PyQt5 import QtGui, QtWidgets

#----------------------------------------------------------------------
#   DEBLEND
#----------------------------------------------------------------------
def PageDeblend(self,Wizard,icons,df,tipstyle,groupstyle):          
    self.wizardPage7 = QtWidgets.QWizardPage()
    self.wizardPage7.setObjectName("wizardPage7")
    self.wizardPage7.setTitle('Deblending')
    self.verticalLayout_dbl = QtWidgets.QVBoxLayout(self.wizardPage7)
    self.verticalLayout_dbl.setObjectName("verticalLayout_dbl")
    self.groupBox_dbl = QtWidgets.QGroupBox(self.wizardPage7)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.groupBox_dbl.sizePolicy().hasHeightForWidth())
    self.groupBox_dbl.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.groupBox_dbl.setFont(font)
    self.groupBox_dbl.setStyleSheet(groupstyle)
    self.groupBox_dbl.setObjectName("groupBox_dbl")
    self.groupBox_dbl.setTitle("Deblending Options")
    self.verticalLayout_dbl2 = QtWidgets.QVBoxLayout(self.groupBox_dbl)
    self.verticalLayout_dbl2.setObjectName("verticalLayout_dbl2")
    self.horizontalLayout_dbl = QtWidgets.QHBoxLayout()
    self.horizontalLayout_dbl.setObjectName("horizontalLayout_dbl")
    
    self.gridLayout_dbl = QtWidgets.QGridLayout()
    self.gridLayout_dbl.setObjectName("gridLayout_dbl")
        
    self.label_dbl = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl.setObjectName("label_dbl")
    self.label_dbl.setText("Generate deblending skl's?")
    self.label_dbl.setFixedWidth(225)  
    self.horizontalLayout_dbl.addWidget(self.label_dbl)
    self.checkBox_dbl = QtWidgets.QCheckBox(self.groupBox_dbl)
    self.checkBox_dbl.setText("")
    self.checkBox_dbl.setChecked(False)
    self.checkBox_dbl.setObjectName("checkBox_dbl")
    self.horizontalLayout_dbl.addWidget(self.checkBox_dbl)
    self.checkBox_dbl.setToolTip("select option to generate the deblending skeletons based on OBNPTY")
    self.checkBox_dbl.setStyleSheet(tipstyle)
    self.checkBox_dbl.clicked.connect(self.changestate_checkdbl)
    
    self.verticalLayout_dbl2.addLayout(self.horizontalLayout_dbl)    
    self.verticalLayout_dbl.addWidget(self.groupBox_dbl)   
    #-----------------------

    self.label_dbl2a = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl2a.setObjectName("label_dbl2a")
    self.label_dbl2a.setText("fmax:")
    self.label_dbl2a.setFixedWidth(100)
    self.lineEdit_dbl2a = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl2a.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl2a.setSizePolicy(sizePolicy)
    self.lineEdit_dbl2a.setObjectName("lineEdit_dbl2a")
    self.lineEdit_dbl2a.setDisabled(True)
    self.lineEdit_dbl2a.setToolTip("maximum frequency to deblend")
    self.lineEdit_dbl2a.setFixedWidth(100)
    self.lineEdit_dbl2a.setStyleSheet(tipstyle)  
    val = df.loc[38,"VALUE"]
    self.lineEdit_dbl2a.setText(str(val))
    self.lineEdit_dbl2a.textChanged[str].connect(self.changestate_fmax) 
      
    self.gridLayout_dbl.addWidget(self.label_dbl2a,0,0)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl2a,0,1)
       
    self.label_dbl2b = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl2b.setObjectName("label_dbl2b")
    self.label_dbl2b.setText("ndip:")
    self.label_dbl2b.setFixedWidth(100)
    self.lineEdit_dbl2b = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl2b.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl2b.setSizePolicy(sizePolicy)
    self.lineEdit_dbl2b.setObjectName("lineEdit_dbl2b")
    self.lineEdit_dbl2b.setDisabled(True)
    self.lineEdit_dbl2b.setToolTip("number of dips required for the final output")
    self.lineEdit_dbl2b.setFixedWidth(100)
    self.lineEdit_dbl2b.setStyleSheet(tipstyle)    
    val = df.loc[39,"VALUE"]
    self.lineEdit_dbl2b.setText(str(val))
    self.lineEdit_dbl2b.textChanged[str].connect(self.changestate_ndip) 

    self.gridLayout_dbl.addWidget(self.label_dbl2b,0,2)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl2b,0,3)
          
    #--------------------
 
    self.label_dbl3a = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl3a.setObjectName("label_dbl3a")
    self.label_dbl3a.setText("pmax:")
    self.label_dbl3a.setFixedWidth(100)
    self.lineEdit_dbl3a = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl3a.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl3a.setSizePolicy(sizePolicy)
    self.lineEdit_dbl3a.setObjectName("lineEdit_dbl3a")
    self.lineEdit_dbl3a.setDisabled(True)
    self.lineEdit_dbl3a.setToolTip("max dip to be modelled in units of sec/xyunit")
    self.lineEdit_dbl3a.setFixedWidth(100)
    self.lineEdit_dbl3a.setStyleSheet(tipstyle)  
    val = df.loc[40,"VALUE"]
    self.lineEdit_dbl3a.setText(str(val))   
    self.lineEdit_dbl3a.textChanged[str].connect(self.changestate_pmax)   
    self.gridLayout_dbl.addWidget(self.label_dbl3a,1,0)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl3a,1,1)

    
    self.label_dbl3b = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl3b.setObjectName("label_dbl3b")
    self.label_dbl3b.setText("mxblnd:")
    self.label_dbl3b.setFixedWidth(100)
    self.lineEdit_dbl3b = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl3b.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl3b.setSizePolicy(sizePolicy)
    self.lineEdit_dbl3b.setObjectName("lineEdit_dbl3b")
    self.lineEdit_dbl3b.setDisabled(True)
    self.lineEdit_dbl3b.setToolTip("max number of blended traces on which a given shot can appear")
    self.lineEdit_dbl3b.setFixedWidth(100)
    self.lineEdit_dbl3b.setStyleSheet(tipstyle)   
    val = df.loc[41,"VALUE"]
    self.lineEdit_dbl3b.setText(str(val))
    self.lineEdit_dbl3b.textChanged[str].connect(self.changestate_mxblnd) 
       
    self.gridLayout_dbl.addWidget(self.label_dbl3b,1,2)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl3b,1,3)

    #--------------------


    self.label_dbl4a = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl4a.setObjectName("label_dbl4a")
    self.label_dbl4a.setText("xywindow:")
    self.label_dbl4a.setFixedWidth(100)
    self.lineEdit_dbl4a = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl4a.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl4a.setSizePolicy(sizePolicy)
    self.lineEdit_dbl4a.setObjectName("lineEdit_dbl4a")
    self.lineEdit_dbl4a.setDisabled(True)
    self.lineEdit_dbl4a.setToolTip("half width of OBNPTY window in XYUNITs")
    self.lineEdit_dbl4a.setFixedWidth(100)
    self.lineEdit_dbl4a.setStyleSheet(tipstyle)  
    val = df.loc[42,"VALUE"]
    self.lineEdit_dbl4a.setText(str(val))
    self.lineEdit_dbl4a.textChanged[str].connect(self.changestate_xywindow)  
 
    self.gridLayout_dbl.addWidget(self.label_dbl4a,2,0)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl4a,2,1)
    
    self.label_dbl4b = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl4b.setObjectName("label_dbl4b")
    self.label_dbl4b.setText("twindow:")
    self.label_dbl4b.setFixedWidth(100)
    self.lineEdit_dbl4b = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl4b.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl4b.setSizePolicy(sizePolicy)
    self.lineEdit_dbl4b.setObjectName("lineEdit_dbl4b")
    self.lineEdit_dbl4b.setDisabled(True)
    self.lineEdit_dbl4b.setToolTip("half width of OBNPTY time window in TUNITS")
    self.lineEdit_dbl4b.setFixedWidth(100)
    self.lineEdit_dbl4b.setStyleSheet(tipstyle)   
    val = df.loc[43,"VALUE"]
    self.lineEdit_dbl4b.setText(str(val))
    self.lineEdit_dbl4b.textChanged[str].connect(self.changestate_twindow)     

    self.gridLayout_dbl.addWidget(self.label_dbl4b,2,2)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl4b,2,3)

    #--------------------

    self.label_dbl5a = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl5a.setObjectName("label_dbl5a")
    self.label_dbl5a.setText("niters:")
    self.label_dbl5a.setFixedWidth(100)
    self.lineEdit_dbl5a = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl5a.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl5a.setSizePolicy(sizePolicy)
    self.lineEdit_dbl5a.setObjectName("lineEdit_dbl5a")
    self.lineEdit_dbl5a.setDisabled(True)
    self.lineEdit_dbl5a.setToolTip("number of outer loop iterations")
    self.lineEdit_dbl5a.setFixedWidth(100)
    self.lineEdit_dbl5a.setStyleSheet(tipstyle)
    val = df.loc[44,"VALUE"]
    self.lineEdit_dbl5a.setText(str(val))
    self.lineEdit_dbl5a.textChanged[str].connect(self.changestate_niters)   

    self.gridLayout_dbl.addWidget(self.label_dbl5a,3,0)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl5a,3,1)
    
    self.label_dbl5b = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl5b.setObjectName("label_dbl5b")
    self.label_dbl5b.setText("nshot:")
    self.label_dbl5b.setFixedWidth(100)
    self.lineEdit_dbl5b = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl5b.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl5b.setSizePolicy(sizePolicy)
    self.lineEdit_dbl5b.setObjectName("lineEdit_dbl5b")
    self.lineEdit_dbl5b.setDisabled(True)
    self.lineEdit_dbl5b.setToolTip("number of thousand shots in survey")
    self.lineEdit_dbl5b.setFixedWidth(100)
    self.lineEdit_dbl5b.setStyleSheet(tipstyle) 
    val = df.loc[45,"VALUE"]
    self.lineEdit_dbl5b.setText(str(val))
    self.lineEdit_dbl5b.textChanged[str].connect(self.changestate_nshot) 
    self.gridLayout_dbl.addWidget(self.label_dbl5b,3,2)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl5b,3,3)

    #--------------------

    self.label_dbl6a = QtWidgets.QLabel(self.groupBox_dbl)
    self.label_dbl6a.setObjectName("label_dbl6a")
    self.label_dbl6a.setText("nwavit:")
    self.label_dbl6a.setFixedWidth(100)
    self.lineEdit_dbl6a = QtWidgets.QLineEdit(self.groupBox_dbl)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit_dbl5a.sizePolicy().hasHeightForWidth())
    self.lineEdit_dbl6a.setSizePolicy(sizePolicy)
    self.lineEdit_dbl6a.setObjectName("lineEdit_dbl5a")
    self.lineEdit_dbl6a.setDisabled(True)
    self.lineEdit_dbl6a.setToolTip("number of wavelet iterations per dip ")
    self.lineEdit_dbl6a.setFixedWidth(100)
    self.lineEdit_dbl6a.setStyleSheet(tipstyle)  
    val = df.loc[46,"VALUE"]
    self.lineEdit_dbl6a.setText(str(val))
    self.lineEdit_dbl6a.textChanged[str].connect(self.changestate_nwavit)   

    self.gridLayout_dbl.addWidget(self.label_dbl6a,4,0)
    self.gridLayout_dbl.addWidget(self.lineEdit_dbl6a,4,1)
    
    self.verticalLayout_dbl2.addLayout(self.gridLayout_dbl)
    
    
    Wizard.setPage(7,self.wizardPage7)
