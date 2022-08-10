import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindow import Ui_rena_voice_generator
import os
from initial import *
import json


class MainForm(QMainWindow, Ui_rena_voice_generator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if os.path.exists('./configs.json'):
            with open('./configs.json', 'r', encoding='utf-8') as f:
                a = json.load(f)
            self.model_dir = a['model_dir']
            self.lineEdit.setText(a['model_dir'])
            self.json_dir = a['json_dir']
            self.lineEdit_2.setText(a['json_dir'])
            self.out_dir = a['out_dir']
            self.lineEdit_3.setText(a['out_dir'])
            self.length = a['length']
            self.doubleSpinBox.setValue(a['length'])
            self.symbols = a['symbols']
            self.lineEdit_4.setText("".join(a['symbols']))
        else:
            self.symbols = list(' !"&*,-.?ABCINU[]abcdefghijklmnoprstuwyz{}()~')
            self.model_dir = ""
            self.json_dir = ""
            self.out_dir = ""
            self.text = ""
            self.length = 1.0

        self.btn.clicked.connect(self.open_file_1)
        self.btn_3.clicked.connect(self.open_file_2)
        self.btn_2.clicked.connect(self.choose_dir)
        self.lineEdit_4.textEdited.connect(self.change_symbols)
        self.pushButton.clicked.connect(self.start_generate)
        self.doubleSpinBox.textChanged.connect(self.change_length)

    def open_file_1(self):
        _translate = QtCore.QCoreApplication.translate
        filename, filetype = QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                         "All Files(*);;Text Files(*.txt)")
        self.model_dir = filename
        self.lineEdit.setText(filename)

    def open_file_2(self):
        _translate = QtCore.QCoreApplication.translate
        filename, filetype = QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                         "All Files(*);;Text Files(*.txt)")
        self.json_dir = filename
        self.lineEdit_2.setText(filename)

    def choose_dir(self):
        dirname = QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")
        self.out_dir = dirname
        self.lineEdit_3.setText(dirname)

    def change_symbols(self):
        self.symbols = list(self.lineEdit_4.text())

    def change_text(self):
        self.text = list(self.textEdit.text())

    def change_length(self):
        self.length = float(self.doubleSpinBox.text())
        print(self.doubleSpinBox.text())

    def start_generate(self):
        self.text = self.textEdit.toPlainText()
        with open("./configs.json","w",encoding='utf-8') as f:
            json.dump({'model_dir': self.model_dir, 'out_dir': self.out_dir, 'json_dir': self.json_dir,
                       'length': self.length, 'symbols': self.symbols}, f, sort_keys=True, indent=4, separators=(',', ': '))
        self.textBrowser.setText("")
        if self.text == "":
            self.textBrowser.append("未输入要转化的文本")
            return
        if self.out_dir == "":
            self.textBrowser.append("未选择输出文件夹")
            return
        if self.json_dir == "":
            self.textBrowser.append("未选择配置文件")
            return
        if self.model_dir == "":
            self.textBrowser.append("未选择模型")
            return
        self.textBrowser.append("正在初始化……")
        try:
            n, h = init(self.symbols, self.json_dir)
        except Exception as e:
            print(e)
            self.textBrowser.append("初始化失败！")
            self.textBrowser.append(str(e))
            return
        self.textBrowser.setText("初始化已完成！")
        try:
            self.textBrowser.append("正在加载模型……")
            load_model(self.model_dir, n)
        except Exception as e1:
            print(e1)
            self.textBrowser.append("模型加载失败！")
            self.textBrowser.append(str(e1))
            return
        self.textBrowser.append("模型加载成功！")
        try:
            self.textBrowser.append("开始合成……")
            jtts(self.text, n, h, self.out_dir, self.length)
        except Exception as e2:
            print(e2)
            self.textBrowser.append("合成失败！")
            self.textBrowser.append(str(e2))
            return
        self.textBrowser.append("音频已保存至{}".format(self.out_dir + \
                                                  '/' + (self.text[:10] if len(self.text) > 10 else self.text)+'.wav'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.show()
    sys.exit(app.exec_())
