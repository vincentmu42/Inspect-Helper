# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Graphical_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 875)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\resources/LOGO-128p.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(37, 37, 38)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Status_Label = QtWidgets.QLabel(self.centralwidget)
        self.Status_Label.setGeometry(QtCore.QRect(10, 90, 215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Status_Label.setFont(font)
        self.Status_Label.setStyleSheet("color: #ffffff;")
        self.Status_Label.setObjectName("Status_Label")
        self.Progress_Bar = QtWidgets.QProgressBar(self.centralwidget)
        self.Progress_Bar.setGeometry(QtCore.QRect(230, 95, 360, 15))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.Progress_Bar.setFont(font)
        self.Progress_Bar.setStyleSheet("color: rgb(255, 255, 255);")
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 845, 701, 2))
        self.line.setStyleSheet("background-color: rgb(51, 51, 55);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Version_Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Version_Title_Label.setGeometry(QtCore.QRect(10, 813, 85, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Version_Title_Label.setFont(font)
        self.Version_Title_Label.setObjectName("Version_Title_Label")
        self.Version_Display_Label = QtWidgets.QLabel(self.centralwidget)
        self.Version_Display_Label.setGeometry(QtCore.QRect(100, 813, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Version_Display_Label.setFont(font)
        self.Version_Display_Label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Version_Display_Label.setObjectName("Version_Display_Label")
        self.dayTime_Display = QtWidgets.QLineEdit(self.centralwidget)
        self.dayTime_Display.setGeometry(QtCore.QRect(335, 5, 255, 28))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dayTime_Display.setFont(font)
        self.dayTime_Display.setMouseTracking(False)
        self.dayTime_Display.setAutoFillBackground(False)
        self.dayTime_Display.setStyleSheet("background-color:#000000; color:#00ff00")
        self.dayTime_Display.setText("")
        self.dayTime_Display.setAlignment(QtCore.Qt.AlignCenter)
        self.dayTime_Display.setReadOnly(True)
        self.dayTime_Display.setObjectName("dayTime_Display")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(10, 40, 285, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Label.setFont(font)
        self.Title_Label.setObjectName("Title_Label")
        self.Select_File_Label = QtWidgets.QLabel(self.centralwidget)
        self.Select_File_Label.setGeometry(QtCore.QRect(10, 170, 180, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Select_File_Label.setFont(font)
        self.Select_File_Label.setObjectName("Select_File_Label")
        self.File_Path_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.File_Path_Edit.setGeometry(QtCore.QRect(10, 200, 425, 25))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.File_Path_Edit.setFont(font)
        self.File_Path_Edit.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"color: rgb(255, 255, 255);")
        self.File_Path_Edit.setText("")
        self.File_Path_Edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.File_Path_Edit.setObjectName("File_Path_Edit")
        self.Select_File_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Select_File_Button.setGeometry(QtCore.QRect(450, 197, 101, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Select_File_Button.setFont(font)
        self.Select_File_Button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Select_File_Button.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(139, 195, 74);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(139, 195, 74);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(139, 195, 74);\n"
"color: rgb(49, 54, 59);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Select_File_Button.setObjectName("Select_File_Button")
        self.Scripts_Label = QtWidgets.QLabel(self.centralwidget)
        self.Scripts_Label.setGeometry(QtCore.QRect(10, 297, 380, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Scripts_Label.setFont(font)
        self.Scripts_Label.setObjectName("Scripts_Label")
        self.Scripts_Edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Scripts_Edit.setGeometry(QtCore.QRect(10, 327, 425, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Scripts_Edit.setFont(font)
        self.Scripts_Edit.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"color: rgb(255, 255, 255);")
        self.Scripts_Edit.setPlainText("")
        self.Scripts_Edit.setObjectName("Scripts_Edit")
        self.Start_Main_Task_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Main_Task_Button.setEnabled(True)
        self.Start_Main_Task_Button.setGeometry(QtCore.QRect(150, 497, 300, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Start_Main_Task_Button.setFont(font)
        self.Start_Main_Task_Button.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(139, 195, 74);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(139, 195, 74);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(139, 195, 74);\n"
"color: rgb(49, 54, 59);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Start_Main_Task_Button.setObjectName("Start_Main_Task_Button")
        self.Message_Display_Label = QtWidgets.QLabel(self.centralwidget)
        self.Message_Display_Label.setGeometry(QtCore.QRect(10, 567, 130, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Message_Display_Label.setFont(font)
        self.Message_Display_Label.setObjectName("Message_Display_Label")
        self.Message_Display_Edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Message_Display_Edit.setGeometry(QtCore.QRect(10, 594, 425, 202))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Message_Display_Edit.setFont(font)
        self.Message_Display_Edit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Message_Display_Edit.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"color: rgb(255, 255, 255);")
        self.Message_Display_Edit.setReadOnly(True)
        self.Message_Display_Edit.setPlainText("")
        self.Message_Display_Edit.setObjectName("Message_Display_Edit")
        self.Open_Saved_Dir_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Open_Saved_Dir_Button.setGeometry(QtCore.QRect(450, 764, 140, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Open_Saved_Dir_Button.setFont(font)
        self.Open_Saved_Dir_Button.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(139, 195, 74);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(139, 195, 74);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(139, 195, 74);\n"
"color: rgb(49, 54, 59);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Open_Saved_Dir_Button.setObjectName("Open_Saved_Dir_Button")
        self.Connect_By_Telnet_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Connect_By_Telnet_Button.setEnabled(True)
        self.Connect_By_Telnet_Button.setGeometry(QtCore.QRect(330, 253, 160, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_By_Telnet_Button.setFont(font)
        self.Connect_By_Telnet_Button.setStyleSheet("color: rgb(255, 255, 127);")
        self.Connect_By_Telnet_Button.setChecked(False)
        self.Connect_By_Telnet_Button.setObjectName("Connect_By_Telnet_Button")
        self.Connect_By_SSH_Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Connect_By_SSH_Button.setEnabled(True)
        self.Connect_By_SSH_Button.setGeometry(QtCore.QRect(170, 253, 150, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_By_SSH_Button.setFont(font)
        self.Connect_By_SSH_Button.setStyleSheet("color: rgb(255, 255, 127);")
        self.Connect_By_SSH_Button.setChecked(True)
        self.Connect_By_SSH_Button.setObjectName("Connect_By_SSH_Button")
        self.Select_Protocol_Label = QtWidgets.QLabel(self.centralwidget)
        self.Select_Protocol_Label.setGeometry(QtCore.QRect(10, 249, 150, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Select_Protocol_Label.setFont(font)
        self.Select_Protocol_Label.setObjectName("Select_Protocol_Label")
        self.Message_Display_Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Message_Display_Clear_Button.setEnabled(True)
        self.Message_Display_Clear_Button.setGeometry(QtCore.QRect(450, 717, 140, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Message_Display_Clear_Button.setFont(font)
        self.Message_Display_Clear_Button.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(255, 0, 0);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 0, 0);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Message_Display_Clear_Button.setCheckable(False)
        self.Message_Display_Clear_Button.setChecked(False)
        self.Message_Display_Clear_Button.setObjectName("Message_Display_Clear_Button")
        self.Start_Main_Task_Button_Fake = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Main_Task_Button_Fake.setEnabled(False)
        self.Start_Main_Task_Button_Fake.setGeometry(QtCore.QRect(150, 497, 300, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Start_Main_Task_Button_Fake.setFont(font)
        self.Start_Main_Task_Button_Fake.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(139, 195, 74);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(139, 195, 74);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(139, 195, 74);\n"
"color: rgb(49, 54, 59);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Start_Main_Task_Button_Fake.setObjectName("Start_Main_Task_Button_Fake")
        self.Message_Display_Clear_Button_Fake = QtWidgets.QPushButton(self.centralwidget)
        self.Message_Display_Clear_Button_Fake.setEnabled(False)
        self.Message_Display_Clear_Button_Fake.setGeometry(QtCore.QRect(450, 717, 140, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Message_Display_Clear_Button_Fake.setFont(font)
        self.Message_Display_Clear_Button_Fake.setStyleSheet("QPushButton{\n"
"background-color: rgb(49, 54, 59);\n"
"border: 2px;\n"
"border-color: rgb(255, 0, 0);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px;\n"
"border-color: rgb(255, 0, 0);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(79, 91, 98);\n"
"border: 2px;\n"
"border-color: rgb(49, 54, 59);\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"color: rgb(49, 54, 59);\n"
"}")
        self.Message_Display_Clear_Button_Fake.setCheckable(False)
        self.Message_Display_Clear_Button_Fake.setChecked(False)
        self.Message_Display_Clear_Button_Fake.setObjectName("Message_Display_Clear_Button_Fake")
        self.Version_Title_Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Version_Title_Label_2.setGeometry(QtCore.QRect(405, 813, 185, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.Version_Title_Label_2.setFont(font)
        self.Version_Title_Label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Version_Title_Label_2.setObjectName("Version_Title_Label_2")
        self.Count_Status_Label = QtWidgets.QLabel(self.centralwidget)
        self.Count_Status_Label.setGeometry(QtCore.QRect(64, 130, 350, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Count_Status_Label.setFont(font)
        self.Count_Status_Label.setStyleSheet("color: #8bc34a;")
        self.Count_Status_Label.setText("")
        self.Count_Status_Label.setObjectName("Count_Status_Label")
        self.Message_Display_Clear_Button_Fake.raise_()
        self.Start_Main_Task_Button_Fake.raise_()
        self.Status_Label.raise_()
        self.Progress_Bar.raise_()
        self.line.raise_()
        self.Version_Title_Label.raise_()
        self.Version_Display_Label.raise_()
        self.dayTime_Display.raise_()
        self.Title_Label.raise_()
        self.Select_File_Label.raise_()
        self.File_Path_Edit.raise_()
        self.Select_File_Button.raise_()
        self.Scripts_Label.raise_()
        self.Scripts_Edit.raise_()
        self.Start_Main_Task_Button.raise_()
        self.Message_Display_Label.raise_()
        self.Message_Display_Edit.raise_()
        self.Open_Saved_Dir_Button.raise_()
        self.Connect_By_Telnet_Button.raise_()
        self.Connect_By_SSH_Button.raise_()
        self.Select_Protocol_Label.raise_()
        self.Message_Display_Clear_Button.raise_()
        self.Version_Title_Label_2.raise_()
        self.Count_Status_Label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inspect Helper GUI"))
        self.Status_Label.setText(_translate("MainWindow", "状态：等待执行"))
        self.Version_Title_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">程序版本：</span></p></body></html>"))
        self.Version_Display_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.Title_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#8bc34a;\">R&amp;S设备批量运维</span></p></body></html>"))
        self.Select_File_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">选择设备信息文件：</span></p></body></html>"))
        self.Select_File_Button.setText(_translate("MainWindow", "选择文件"))
        self.Scripts_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">输入需要按顺序执行的命令（一行一个）：</span></p></body></html>"))
        self.Start_Main_Task_Button.setText(_translate("MainWindow", "开始执行"))
        self.Message_Display_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">运行状态信息：</span></p></body></html>"))
        self.Open_Saved_Dir_Button.setText(_translate("MainWindow", "浏览保存目录"))
        self.Connect_By_Telnet_Button.setText(_translate("MainWindow", "使用Telnet连接"))
        self.Connect_By_SSH_Button.setText(_translate("MainWindow", "使用SSH连接"))
        self.Select_Protocol_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">选择连接方式：</span></p></body></html>"))
        self.Message_Display_Clear_Button.setText(_translate("MainWindow", "清空状态信息"))
        self.Start_Main_Task_Button_Fake.setText(_translate("MainWindow", "开始执行"))
        self.Message_Display_Clear_Button_Fake.setText(_translate("MainWindow", "清空状态信息"))
        self.Version_Title_Label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">© 2022-2023 Vincent慕远</span></p></body></html>"))
