import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tkinter.messagebox as msgbox

form_class = uic.loadUiType("ui.ui")[0]

global result, plus_minuse
fir_sec = 0
fir_value = 0
sec_value = 0
result = 0
operation = 0
plus_minuse = 0
fir_exp_value = 0
sec_exp_value = 0
op_exp_value = 0


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.plus_minus.clicked.connect(self.switch_plus_minus)

    def op_text(self):
        if(operation == 1):
            self.value.setText(
                str(fir_value)+" + "+"\n"+str(sec_value))
        elif(operation == 2):
            self.value.setText(
                str(fir_value)+" - "+"\n"+str(sec_value))
        elif(operation == 3):
            self.value.setText(
                str(fir_value)+" / "+"\n"+str(sec_value))
        elif(operation == 4):
            self.value.setText(
                str(fir_value)+" * "+"\n"+str(sec_value))

    def switch_plus_minus(self):
        global fir_value, sec_value
        if(plus_minuse == 0):
            if(operation == 0):
                fir_value = -fir_value
                self.value.setText("\n"+str(fir_value))
            else:
                sec_value = -sec_value
                self.op_text()

    def result__(self):
        if(sec_value != 0):
            self.result_()
        else:
            self.error_message("error", "값을 입력해주세요")

    def result_(self):
        global fir_value, operation, fir_sec, sec_value, op_exp_value, fir_exp_value, sec_exp_value

        fir_exp_value = fir_value
        sec_exp_value = sec_value

        if(operation == 1):
            value = fir_value + sec_value
            fir_value = value
            op_exp_value = "+"

        elif(operation == 2):
            value = fir_value - sec_value
            fir_value = value
            op_exp_value = "-"

        elif(operation == 3):
            value = fir_value / sec_value
            fir_value = value
            op_exp_value = "/"

        elif(operation == 4):
            value = fir_value * sec_value
            fir_value = value
            op_exp_value = "*"

        value = 0
        fir_sec = 0
        operation = 0
        sec_value = 0
        self.value.setText(str(fir_exp_value)+op_exp_value +
                           str(sec_exp_value)+"\n"+str(fir_value))

    def Operator(self, message, operation_):
        global fir_sec, operation
        if(sec_value == 0):
            if(fir_value == 0):
                self.error_message("error", message+"를 입력해주세요. ")
            else:
                fir_sec = 1
                operation = operation_
                self.value.setText("\n"+str(fir_value))
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
        fir_sec = 0
        self.value.setText("\n"+str(sec_value))

    def error_message(self, title, message):
        msgbox.showerror(title, message)

    def number(self, number):
        global fir_value, sec_value, operation
        if(fir_sec == 1):
            if(sec_value == 0):
                if(number == 0):
                    self.error_message("error", "0으로 시작할 수 없습니다.")
                else:
                    sec_value = number
                    self.op_text()
            else:
                sec_value = sec_value * 10 + number
                self.op_text()

        else:
            if(fir_value == 0):
                if(number == 0):
                    self.error_message("error", "0으로 시작할 수 없습니다.")
                else:
                    fir_value = number
                    self.value.setText("\n"+str(fir_value))
            else:
                fir_value = fir_value * 10 + number
                self.value.setText("\n"+str(fir_value))

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
