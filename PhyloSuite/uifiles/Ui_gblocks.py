# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\codes\PhyloSuite\uifiles\gblocks.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Gblocks(object):
    def setupUi(self, Gblocks):
        Gblocks.setObjectName("Gblocks")
        Gblocks.resize(702, 546)
        self.verticalLayout = QtWidgets.QVBoxLayout(Gblocks)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(Gblocks)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox_4 = ListQCombobox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setAcceptDrops(True)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_4.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_7 = ClickedLableGif(self.groupBox_4)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(Gblocks)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout.addWidget(self.comboBox_10, 1, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setMinimum(2)
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setProperty("value", 8)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 3, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 2, 1, 2)
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_13.sizePolicy().hasHeightForWidth())
        self.comboBox_13.setSizePolicy(sizePolicy)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.gridLayout.addWidget(self.comboBox_13, 3, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout.addWidget(self.comboBox_5, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_12.raise_()
        self.comboBox_10.raise_()
        self.comboBox_5.raise_()
        self.label_3.raise_()
        self.comboBox_2.raise_()
        self.label_11.raise_()
        self.label_2.raise_()
        self.spinBox_2.raise_()
        self.label_22.raise_()
        self.comboBox_13.raise_()
        self.spinBox_3.raise_()
        self.label_6.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Gblocks)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(50)
        self.spinBox.setMaximum(500)
        self.spinBox.setProperty("value", 60)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_6, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 2, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_12, 1, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_7, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 2, 2, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_11, 2, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_8, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_9, 3, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Gblocks)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = ArrowPushButton(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_6 = QtWidgets.QGroupBox(Gblocks)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/Eye_Care_Services-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_6)

        self.retranslateUi(Gblocks)
        self.radioButton_2.toggled['bool'].connect(self.comboBox_13.setEnabled)
        self.radioButton_3.toggled['bool'].connect(self.comboBox_13.setDisabled)
        self.radioButton.toggled['bool'].connect(self.comboBox_13.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Gblocks)
        Gblocks.setTabOrder(self.radioButton, self.pushButton_3)
        Gblocks.setTabOrder(self.pushButton_3, self.spinBox_3)
        Gblocks.setTabOrder(self.spinBox_3, self.comboBox_4)
        Gblocks.setTabOrder(self.comboBox_4, self.comboBox_2)
        Gblocks.setTabOrder(self.comboBox_2, self.comboBox_5)
        Gblocks.setTabOrder(self.comboBox_5, self.comboBox_13)
        Gblocks.setTabOrder(self.comboBox_13, self.comboBox_10)
        Gblocks.setTabOrder(self.comboBox_10, self.pushButton)
        Gblocks.setTabOrder(self.pushButton, self.pushButton_2)
        Gblocks.setTabOrder(self.pushButton_2, self.pushButton_9)
        Gblocks.setTabOrder(self.pushButton_9, self.spinBox_2)
        Gblocks.setTabOrder(self.spinBox_2, self.radioButton_2)
        Gblocks.setTabOrder(self.radioButton_2, self.radioButton_3)
        Gblocks.setTabOrder(self.radioButton_3, self.lineEdit_3)
        Gblocks.setTabOrder(self.lineEdit_3, self.comboBox_6)
        Gblocks.setTabOrder(self.comboBox_6, self.comboBox_7)
        Gblocks.setTabOrder(self.comboBox_7, self.comboBox_8)
        Gblocks.setTabOrder(self.comboBox_8, self.comboBox_11)
        Gblocks.setTabOrder(self.comboBox_11, self.spinBox)
        Gblocks.setTabOrder(self.spinBox, self.comboBox_12)
        Gblocks.setTabOrder(self.comboBox_12, self.comboBox_9)

    def retranslateUi(self, Gblocks):
        _translate = QtCore.QCoreApplication.translate
        Gblocks.setWindowTitle(_translate("Gblocks", "Gblocks"))
        self.groupBox_4.setTitle(_translate("Gblocks", "Input"))
        self.label_4.setText(_translate("Gblocks", "Input:"))
        self.label_5.setText(_translate("Gblocks", "<html><head/><body><p>Try to drag your <span style=\" font-weight:600; color:#ff0000;\">FASTA</span> or <span style=\" font-weight:600; color:#ff0000;\">NBRF/PIR</span> file and drop here if you want to use custom files</p></body></html>"))
        self.label_8.setText(_translate("Gblocks", "Demo:"))
        self.label_7.setToolTip(_translate("Gblocks", "Brief example"))
        self.groupBox.setTitle(_translate("Gblocks", "Parameters"))
        self.label_11.setText(_translate("Gblocks", "Minimum Number Of Sequences For A Conserved Position:"))
        self.label_2.setText(_translate("Gblocks", "Minimum Number Of Sequences For A Flank Position:"))
        self.label_12.setText(_translate("Gblocks", "Allowed Gap Positions:"))
        self.label_3.setText(_translate("Gblocks", "Maximum Number Of Contiguous Nonconserved Positions:"))
        self.label_22.setText(_translate("Gblocks", "Use Similarity Matrices:"))
        self.comboBox_13.setItemText(0, _translate("Gblocks", "Yes"))
        self.comboBox_13.setItemText(1, _translate("Gblocks", "No"))
        self.label_13.setText(_translate("Gblocks", "Data Type:"))
        self.radioButton.setText(_translate("Gblocks", "Nucleotide"))
        self.radioButton_2.setText(_translate("Gblocks", "Protein"))
        self.radioButton_3.setText(_translate("Gblocks", "Codons"))
        self.comboBox_5.setItemText(0, _translate("Gblocks", "With Half"))
        self.comboBox_5.setItemText(1, _translate("Gblocks", "All"))
        self.comboBox_5.setItemText(2, _translate("Gblocks", "None"))
        self.label_6.setText(_translate("Gblocks", "Minimum Length Of A Block:"))
        self.groupBox_2.setTitle(_translate("Gblocks", "Save Options"))
        self.label_18.setText(_translate("Gblocks", "Generic File Extension:"))
        self.lineEdit_3.setText(_translate("Gblocks", "-gb"))
        self.label_19.setText(_translate("Gblocks", "Characters Per Line In Results And Parameters File:"))
        self.label_14.setText(_translate("Gblocks", "Selected Blocks:"))
        self.comboBox_6.setItemText(0, _translate("Gblocks", "Save"))
        self.comboBox_6.setItemText(1, _translate("Gblocks", "Don\'t Save"))
        self.label_21.setText(_translate("Gblocks", "Results And Parameters File:"))
        self.comboBox_12.setItemText(0, _translate("Gblocks", "Save"))
        self.comboBox_12.setItemText(1, _translate("Gblocks", "Save Text"))
        self.comboBox_12.setItemText(2, _translate("Gblocks", "Save Short"))
        self.comboBox_12.setItemText(3, _translate("Gblocks", "Don\'t Save"))
        self.label_15.setText(_translate("Gblocks", "Nonconserved Blocks:"))
        self.comboBox_7.setItemText(0, _translate("Gblocks", "Don\'t Save"))
        self.comboBox_7.setItemText(1, _translate("Gblocks", "Save"))
        self.label_17.setText(_translate("Gblocks", "Mask File With The Selected Blocks:"))
        self.comboBox_11.setItemText(0, _translate("Gblocks", "Don\'t Save"))
        self.comboBox_11.setItemText(1, _translate("Gblocks", "Save"))
        self.label_16.setText(_translate("Gblocks", "Ungapped Alignment:"))
        self.comboBox_8.setItemText(0, _translate("Gblocks", "Don\'t Save"))
        self.comboBox_8.setItemText(1, _translate("Gblocks", "Save"))
        self.label_20.setText(_translate("Gblocks", "Postscript File With The Selected Blocks:"))
        self.comboBox_9.setItemText(0, _translate("Gblocks", "Don\'t Save"))
        self.comboBox_9.setItemText(1, _translate("Gblocks", "Save"))
        self.groupBox_3.setTitle(_translate("Gblocks", "Run"))
        self.pushButton.setText(_translate("Gblocks", "Start"))
        self.pushButton_2.setText(_translate("Gblocks", "Stop"))
        self.groupBox_6.setTitle(_translate("Gblocks", "Progress"))
        self.pushButton_9.setText(_translate("Gblocks", "Show log"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, ListQCombobox
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gblocks = QtWidgets.QDialog()
    ui = Ui_Gblocks()
    ui.setupUi(Gblocks)
    Gblocks.show()
    sys.exit(app.exec_())

