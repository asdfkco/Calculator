import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tkinter.messagebox as msgbox

form_class = uic.loadUiType("ui.ui")[0]

global result
fir_value = 0
sec_value = 0


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.value.setText("0")
        self.one.clicked.connect(self.one_value)
        self.two.clicked.connect(self.two_value)
        self.three.clicked.connect(self.three_value)
        self.four.clicked.connect(self.four_value)
        self.five.clicked.connect(self.five_value)
        self.six.clicked.connect(self.six_value)
        self.seven.clicked.connect(self.seven_value)
        self.eight.clicked.connect(self.eight_value)
        self.nine.clicked.connect(self.nine_value)
        self.zero.clicked.connect(self.zero_value)
        self.clear.clicked.connect(self.clear_button)

    def clear_button(self):
        fir_value = 0
        sec_value = 0
        result = 0
        self.value.setText(str(fir_value))
        
        
    def error_message(self, title, message):
        msgbox.showerror(title, message)

    def number(self, number):
        global fir_value, sec_value
        if(fir_value == 0):
            if(number == 0):
                self.error_message("error", "0으로 시작할 수 없습니다.")
            else:
                fir_value = number
        else:
            fir_value = fir_value * 10 + number
        self.value.setText(str(fir_value))
        print(fir_value)

    def one_value(self):
        self.number(1)

    def two_value(self):
        self.number(2)

    def three_value(self):
        self.number(3)

    def four_value(self):
        self.number(4)

    def five_value(self):
        self.number(5)

    def six_value(self):
        self.number(6)

    def seven_value(self):
        self.number(7)

    def eight_value(self):
        self.number(8)

    def nine_value(self):
        self.number(9)

    def zero_value(self):
        self.number(0)

        #계산할때 변수한개에 저장하거나 배열에 저장하기 ㅋ


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
