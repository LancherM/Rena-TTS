# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rena_voice_generator(object):
    def setupUi(self, rena_voice_generator):
        rena_voice_generator.setObjectName("rena_voice_generator")
        rena_voice_generator.resize(600, 635)
        rena_voice_generator.setStyleSheet("QToolButton {\n"
"      /* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 4px 8px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"QToolButton:hover {\n"
"      background-color: #008CBA;\n"
"      color: white;\n"
"    transition:all 1s;\n"
"}\n"
"QTextEdit{\n"
"/* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 4px 8px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"\n"
"QPushButton {\n"
"      /* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 4px 8px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"QPushButton:hover {\n"
"      background-color: #008CBA;\n"
"      color: white;\n"
"    transition:all 1s;\n"
"}\n"
"QLineEdit{\n"
"/* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 4px 8px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"QDoubleSpinBox{\n"
"/* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 4px 8px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}")
        self.label = QtWidgets.QLabel(rena_voice_generator)
        self.label.setGeometry(QtCore.QRect(80, 260, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(rena_voice_generator)
        self.pushButton.setGeometry(QtCore.QRect(470, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(rena_voice_generator)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(rena_voice_generator)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn = QtWidgets.QToolButton(rena_voice_generator)
        self.btn.setGeometry(QtCore.QRect(470, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn.setFont(font)
        self.btn.setStyleSheet(".btn {\n"
"      /* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 16px 32px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      -webkit-transition-duration: 0.4s; /* Safari */\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"      text-transform: uppercase;\n"
"}\n"
".btn {\n"
"      background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"/* 悬停样式 */\n"
".btn:hover {\n"
"      background-color: #008CBA;\n"
"      color: white;\n"
"}")
        self.btn.setObjectName("btn")
        self.btn_2 = QtWidgets.QToolButton(rena_voice_generator)
        self.btn_2.setGeometry(QtCore.QRect(470, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(".btn {\n"
"      /* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 16px 32px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      -webkit-transition-duration: 0.4s; /* Safari */\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"      text-transform: uppercase;\n"
"}\n"
".btn {\n"
"      background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"/* 悬停样式 */\n"
".btn:hover {\n"
"      background-color: #008CBA;\n"
"      color: white;\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.label_8 = QtWidgets.QLabel(rena_voice_generator)
        self.label_8.setGeometry(QtCore.QRect(490, 580, 101, 51))
        font = QtGui.QFont()
        font.setFamily("默陌绿妖体")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(rena_voice_generator)
        self.label_9.setGeometry(QtCore.QRect(60, 90, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btn_3 = QtWidgets.QToolButton(rena_voice_generator)
        self.btn_3.setGeometry(QtCore.QRect(470, 70, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(".btn {\n"
"      /* 文字颜色 */\n"
"      color: #0099CC; \n"
"      /* 清除背景色 */\n"
"      background: transparent; \n"
"      /* 边框样式、颜色、宽度 */\n"
"      border: 2px solid #0099CC;\n"
"      /* 给边框添加圆角 */\n"
"      border-radius: 6px; \n"
"      /* 字母转大写 */\n"
"      border: none;\n"
"      color: white;\n"
"      padding: 16px 32px;\n"
"      text-align: center;\n"
"      display: inline-block;\n"
"      font-size: 16px;\n"
"      margin: 4px 2px;\n"
"      -webkit-transition-duration: 0.4s; /* Safari */\n"
"      transition-duration: 0.4s;\n"
"      cursor: pointer;\n"
"      text-decoration: none;\n"
"      text-transform: uppercase;\n"
"}\n"
".btn {\n"
"      background-color: white; \n"
"      color: black; \n"
"      border: 2px solid #008CBA;\n"
"}\n"
"/* 悬停样式 */\n"
".btn:hover {\n"
"      background-color: #008CBA;\n"
"      color: white;\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.label_4 = QtWidgets.QLabel(rena_voice_generator)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(rena_voice_generator)
        self.textBrowser.setGeometry(QtCore.QRect(140, 400, 451, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(rena_voice_generator)
        self.label_5.setGeometry(QtCore.QRect(80, 480, 72, 15))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(rena_voice_generator)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(rena_voice_generator)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(rena_voice_generator)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 130, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(rena_voice_generator)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 190, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(rena_voice_generator)
        self.doubleSpinBox.setGeometry(QtCore.QRect(470, 291, 111, 41))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_6 = QtWidgets.QLabel(rena_voice_generator)
        self.label_6.setGeometry(QtCore.QRect(490, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(rena_voice_generator)
        self.label_7.setGeometry(QtCore.QRect(480, 270, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(rena_voice_generator)
        self.textEdit.setGeometry(QtCore.QRect(140, 250, 321, 141))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(rena_voice_generator)
        QtCore.QMetaObject.connectSlotsByName(rena_voice_generator)

    def retranslateUi(self, rena_voice_generator):
        _translate = QtCore.QCoreApplication.translate
        rena_voice_generator.setWindowTitle(_translate("rena_voice_generator", "VITS-TTS"))
        self.label.setText(_translate("rena_voice_generator", "文本："))
        self.pushButton.setText(_translate("rena_voice_generator", "开始合成"))
        self.label_2.setText(_translate("rena_voice_generator", "输出目录："))
        self.label_3.setText(_translate("rena_voice_generator", "VITS 模型："))
        self.btn.setText(_translate("rena_voice_generator", "浏览文件"))
        self.btn_2.setText(_translate("rena_voice_generator", "浏览目录"))
        self.label_8.setText(_translate("rena_voice_generator", "By Lancher"))
        self.label_9.setText(_translate("rena_voice_generator", "配置文件："))
        self.btn_3.setText(_translate("rena_voice_generator", "浏览文件"))
        self.label_4.setText(_translate("rena_voice_generator", "Symbols："))
        self.textBrowser.setHtml(_translate("rena_voice_generator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">.</span></p></body></html>"))
        self.label_5.setText(_translate("rena_voice_generator", "输出："))
        self.lineEdit_4.setText(_translate("rena_voice_generator", "!\"&*,-.?ABCINU[]abcdefghijklmnoprstuwyz{}()~"))
        self.label_6.setText(_translate("rena_voice_generator", "语速倍率"))
        self.label_7.setText(_translate("rena_voice_generator", "（默认为1）"))
