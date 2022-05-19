import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tkinter.messagebox as msgbox

form_class = uic.loadUiType("ui.ui")[0]

global result, plus_minuse
fir_sec = 0
fir_value = 0.0
sec_value = 0.0
result = 0.0
operation = 0
plus_minuse = 0

#번호로 1 더하기 2 빼기 3 나누기 4 곱하기 = 했을때 번호에 따라 결과값
#번호로 if줘서 1일때 더하고 하기 ㅋ
#plus_minuse 가 0일땐 + 1일땐 마이너스로


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
        self.plus.clicked.connect(self.plus_)
        self.minus.clicked.connect(self.minus_)
        self.times.clicked.connect(self.times_)
        self.division.clicked.connect(self.division_)
        self.result.clicked.connect(self.result__)

    def result__(self):
        if(sec_value != 0):
            self.result_()
            self.value.setText(str(fir_value))
        else:
            self.error_message("error", "값을 입력해주세요")
    def result_(self):
        global fir_value, operation, fir_sec, sec_value

        if(operation == 1):
            value = fir_value + sec_value
            fir_value = value
        elif(operation == 2):
            value = fir_value - sec_value
            fir_value = value
        elif(operation == 3):
            value = fir_value / sec_value
            fir_value = value
        elif(operation == 4):
            value = fir_value * sec_value
            fir_value = value
        value = 0
        fir_sec = 0
        operation = 0
        sec_value = 0

    def Operator(self, message, operation_):
        global fir_sec, operation
        if(sec_value == 0):
            if(fir_value == 0):
                self.error_message("error", message+"를 입력해주세요. ")
            else:
                fir_sec = 1
                operation = operation_
                self.value.setText(str(float(sec_value)))
        else:
            self.error_message("error", "결과 값을 내주세요")

    def plus_(self):
        self.Operator("더할 수", 1)
    def minus_(self):
        self.Operator("뺄셈", 2)
    def division_(self):
        self.Operator("나눌 수", 3)
    def times_(self):
        self.Operator("곱할 수", 4)
    def clear_button(self):
        global fir_value, sec_value, result, fir_sec
        fir_value = 0
        sec_value = 0
        result = 0
        self.value.setText(str(float(sec_value)))
        fir_sec = 0

    def error_message(self, title, message):
        msgbox.showerror(title, message)

    def number(self, number):
        global fir_value, sec_value
        if(fir_sec == 1):
            if(sec_value == 0):
                if(number == 0):
                    self.error_message("error", "0으로 시작할 수 없습니다.")
                else:
                    sec_value = number
            else:
                sec_value = sec_value * 10 + number
                self.value.setText(str(float(sec_value)))
                

        else:
            if(fir_value == 0):
                if(number == 0):
                    self.error_message("error", "0으로 시작할 수 없습니다.")
                else:
                    fir_value = number
            else:
                fir_value = fir_value * 10 + number
                self.value.setText(str(float(sec_value))) 
                

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
