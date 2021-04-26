# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:49:27 2021

@author: Christopher.Willacy
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

#----------------------------------------------------------------------
#  SIDEBAR FUNCTIONALITY
#----------------------------------------------------------------------
def sideBar(self, icons, Wizard):

    # button style        
    side_style = str("QPushButton {\n"
" text-align:left;"
"  color: black;\n"
"  font-size: 14px;\n"
" background-color: #4000FF99;"
"}")
   
    self.centralwidget = QtWidgets.QWidget()
    self.centralwidget.setObjectName("centralwidget")
    self.widget_mside = QtWidgets.QWidget(self.centralwidget)
    self.widget_mside.setGeometry(QtCore.QRect(150, 120, 115, 85))
    self.widget_mside.setObjectName("widget_mside")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_mside)
    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout.setObjectName("verticalLayout")
    self.pushButton_1s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_1s.setObjectName("pushButton_1s")
    self.pushButton_1s.setText("1. Introduction")       
    self.pushButton_1s.setStyleSheet(side_style)
    self.pushButton_1s.setIcon(QIcon(icons[1]))
    self.pushButton_1s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_1s)                
    self.pushButton_2s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_2s.setObjectName("pushButton_2s")
    self.pushButton_2s.setText("2. Workflow Setup") 
    self.pushButton_2s.setStyleSheet(side_style)
    self.pushButton_2s.setIcon(QIcon(icons[2]))
    self.pushButton_2s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_2s)        
    self.pushButton_3s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_3s.setObjectName("pushButton_3s")
    self.pushButton_3s.setText("3. SPS Import")   
    self.pushButton_3s.setStyleSheet(side_style)
    self.pushButton_3s.setIcon(QIcon(icons[2]))
    self.pushButton_3s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_3s)
    self.pushButton_4s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_4s.setObjectName("pushButton_4s")
    self.pushButton_4s.setText("4. Geometry Build")  
    self.pushButton_4s.setStyleSheet(side_style)
    self.pushButton_4s.setIcon(QIcon(icons[2]))
    self.pushButton_4s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_4s)
    self.pushButton_5s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_5s.setObjectName("pushButton_5s")
    self.pushButton_5s.setText("5. Wavelet + Noise") 
    self.pushButton_5s.setStyleSheet(side_style)
    self.pushButton_5s.setIcon(QIcon(icons[2]))
    self.pushButton_5s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_5s)
    self.pushButton_6s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_6s.setObjectName("pushButton_6s")
    self.pushButton_6s.setText("6. Blending")   
    self.pushButton_6s.setStyleSheet(side_style)
    self.pushButton_6s.setIcon(QIcon(icons[2]))
    self.pushButton_6s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_6s)
    self.pushButton_7s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_7s.setObjectName("pushButton_8s")
    self.pushButton_7s.setText("7. Deblending") 
    self.pushButton_7s.setStyleSheet(side_style)
    self.pushButton_7s.setIcon(QIcon(icons[2]))
    self.pushButton_7s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_7s)
    self.pushButton_8s = QtWidgets.QPushButton(self.widget_mside)
    self.pushButton_8s.setObjectName("pushButton_8s")
    self.pushButton_8s.setText("8. Output Options") 
    self.pushButton_8s.setStyleSheet(side_style)
    self.pushButton_8s.setIcon(QIcon(icons[2]))
    self.pushButton_8s.setEnabled(True)
    self.verticalLayout.addWidget(self.pushButton_8s)
    
    Wizard.setSideWidget(self.widget_mside)