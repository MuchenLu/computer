from PyQt6 import QtWidgets, QtCore, QtGui
import sys

COLORS = {"red": "#C0392B", "green": "#388E3C"}

class Basic(QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()
        self._width = 324
        self._height = 720
        self.resize(self._width, self._height)
        self.setFixedSize(self._width, self._height)
        self.setWindowTitle("計算機")
        self.setWindowIcon(QtGui.QIcon("./icon.ico"))

        self.compute_area = Compute_Area(self)
        self.button_frame = Button_Frame(self)
        
        self.compute_area.show()
    
    def resizeEvent(self, event):
        width = event.size().width()
        height = event.size().height()
        
        aspect_ratio = 9 / 20
        
        if width / height > aspect_ratio :
            self._width = int(height * aspect_ratio)
            self._height = height
            self.resize(self._width, self._height)
        else :
            self._height = int(width / aspect_ratio)
            self._width = width
            self.resize(self._width, self._height)
        
        self.compute_area.resize()

class Compute_Area(QtWidgets.QTextEdit) :
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.parent = parent
        self._width = self.parent.width()
        self._height = int(self.parent.height() * 0.4)
        self._x = 0
        self._y = 0
        self.setGeometry(self._x, self._y, self._width, self._height)
        self.font_size = 20
        self.setStyleSheet(f'''font-size: {self.font_size}px''')

    def resize(self) :
        self._width = self.parent.width()
        self._height = int(self.parent.height() * 0.4)
        self._x = 0
        self._y = 0
        self.setGeometry(self._x, self._y, self._width, self._height)

class Button_Frame(QtWidgets.QFrame) :
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.parent = parent
        self._width = self.parent.width()
        self._height = int(self.parent.height() * 0.6)
        self._x = 0
        self._y = int(self.parent.height() * 0.4)
        self.setGeometry(self._x, self._y, self._width, self._height)
        self.font_size = 20
        # self.setStyleSheet("border: 2px solid red")
        self.layout = QtWidgets.QGridLayout(self)

        # region: 第一行
        self.clear = QtWidgets.QPushButton(text = "C")
        self.clear.setStyleSheet(f'''color: {COLORS['red']};
                                 font-size: {self.font_size}px''')
        self.clear.clicked.connect(self.func_clear)
        self.layout.addWidget(self.clear, 0, 0)

        self.bracket = QtWidgets.QPushButton(text = "()")
        self.bracket.setStyleSheet(f'''color: {COLORS['green']};
                                   font-size: {self.font_size}px''')
        self.bracket.clicked.connect(self.func_bracket)
        self.layout.addWidget(self.bracket, 0, 1)
        
        self.percent = QtWidgets.QPushButton(text = "%")
        self.percent.setStyleSheet(f'''color: {COLORS['green']};
                                   font-size: {self.font_size}px''')
        self.percent.clicked.connect(self.func_percent)
        self.layout.addWidget(self.percent, 0, 2)

        self.divide = QtWidgets.QPushButton(text = "÷")
        self.divide.setStyleSheet(f'''color: {COLORS['green']};
                                  font-size: {self.font_size}px''')
        self.divide.clicked.connect(self.func_divide)
        self.layout.addWidget(self.divide, 0, 3)
        #endregion
        # region: 第二行
        self.seven = QtWidgets.QPushButton(text = "7")
        self.seven.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.seven.clicked.connect(self.func_seven)
        self.layout.addWidget(self.seven, 1, 0)

        self.eight = QtWidgets.QPushButton(text = "8")
        self.eight.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.eight.clicked.connect(self.func_eight)
        self.layout.addWidget(self.eight, 1, 1)

        self.nine = QtWidgets.QPushButton(text = "9")
        self.nine.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.nine.clicked.connect(self.func_nine)
        self.layout.addWidget(self.nine, 1, 2)

        self.times = QtWidgets.QPushButton(text = "×")
        self.times.setStyleSheet(f'''color: {COLORS["green"]};
                                 font-size: {self.font_size}px''')
        self.times.clicked.connect(self.func_times)
        self.layout.addWidget(self.times, 1, 3)
        # endregion
        # region: 第三行
        self.four = QtWidgets.QPushButton(text = "4")
        self.four.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.four.clicked.connect(self.func_four)
        self.layout.addWidget(self.four, 2, 0)

        self.five = QtWidgets.QPushButton(text = "5")
        self.five.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.five.clicked.connect(self.func_five)
        self.layout.addWidget(self.five, 2, 1)

        self.six = QtWidgets.QPushButton(text = "6")
        self.six.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.six.clicked.connect(self.func_six)
        self.layout.addWidget(self.six, 2, 2)

        self.minus = QtWidgets.QPushButton(text = "-")
        self.minus.setStyleSheet(f'''color: {COLORS["green"]};
                                 font-size: {self.font_size}px''')
        self.minus.clicked.connect(self.func_minus)
        self.layout.addWidget(self.minus, 2, 3)
        # endregion
        # region: 第四行
        self.one = QtWidgets.QPushButton(text = "1")
        self.one.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.one.clicked.connect(self.func_one)
        self.layout.addWidget(self.one, 3, 0)
        
        self.two = QtWidgets.QPushButton(text = "2")
        self.two.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.two.clicked.connect(self.func_two)
        self.layout.addWidget(self.two, 3, 1)

        self.three = QtWidgets.QPushButton(text = "3")
        self.three.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.three.clicked.connect(self.func_three)
        self.layout.addWidget(self.three, 3, 2)

        self.plus = QtWidgets.QPushButton(text = "+")
        self.plus.setStyleSheet(f'''color: {COLORS["green"]};
                                font-size: {self.font_size}px''')
        self.plus.clicked.connect(self.func_plus)
        self.layout.addWidget(self.plus, 3, 3)
        # endregion
        # region: 第五行
        self.sign = QtWidgets.QPushButton(text = "+/-")
        self.sign.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.sign.clicked.connect(self.func_PNsign)
        self.layout.addWidget(self.sign, 4, 0)

        self.zero = QtWidgets.QPushButton(text = "0")
        self.zero.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.zero.clicked.connect(self.func_zero)
        self.layout.addWidget(self.zero, 4, 1)

        self.point = QtWidgets.QPushButton(text = ".")
        self.point.setStyleSheet(f'''font-size: {self.font_size}px''')
        self.point.clicked.connect(self.func_point)
        self.layout.addWidget(self.point, 4, 2)

        self.equal = QtWidgets.QPushButton(text = "=")
        self.equal.setStyleSheet(f'''background: {COLORS["green"]};
                                 font-size: {self.font_size}px''')
        self.equal.clicked.connect(self.func_equal)
        self.layout.addWidget(self.equal, 4, 3)
        # endregion

    def resize(self) :
        self._width = self.parent.width()
        self._height = int(self.parent.height() * 0.6)
        self._x = 0
        self._y = int(self.parent.height() * 0.4)
        self.setGeometry(self._x, self._y, self._width, self._height)

    # region: 數字按鈕函式區
    def func_zero(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "0"
        self.parent.compute_area.setText(text)

    def func_one(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "1"
        self.parent.compute_area.setText(text)
    
    def func_two(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "2"
        self.parent.compute_area.setText(text)
    
    def func_three(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "3"
        self.parent.compute_area.setText(text)
    
    def func_four(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "4"
        self.parent.compute_area.setText(text)
    
    def func_five(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "5"
        self.parent.compute_area.setText(text)
    
    def func_six(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "6"
        self.parent.compute_area.setText(text)
    
    def func_seven(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "7"
        self.parent.compute_area.setText(text)

    def func_eight(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "8"
        self.parent.compute_area.setText(text)
    
    def func_nine(self) -> None :
        text = self.parent.compute_area.toPlainText()
        text += "9"
        self.parent.compute_area.setText(text)
    # endregion
    # region: 計算符號按鈕函式區
    def func_plus(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text = text[:-1]
        except IndexError :
            pass
        text += "+"
        self.parent.compute_area.setText(text)

    def func_minus(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text = text[:-1]
        except IndexError :
            pass
        text += "-"
        self.parent.compute_area.setText(text)

    def func_times(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text = text[:-1]
        except IndexError :
            pass
        text += "×"
        self.parent.compute_area.setText(text)

    def func_divide(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text = text[:-1]
        except IndexError :
            pass
        text += "÷"
        self.parent.compute_area.setText(text)

    def func_equal(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text = text[:-1]
        except IndexError :
            pass
        if "×" in text :
            text = text.replace("×", "*")
        if "÷" in text :
            text = text.replace("÷", "/")
        if "%" in text :
            text = text.replace("%", "*0.01")
        while True :
            try :
                text = str(eval(text))
                break
            except SyntaxError :
                self.func_bracket()
                text = self.parent.compute_area.toPlainText()
        
        self.parent.compute_area.setText(text)
    # endregion
    # region: 其他功能按鈕函式區
    def func_clear(self) :
        self.parent.compute_area.setText("")
    
    def func_point(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] in ("+", "-", "×", "÷") :
                text += "0."
            elif text[-1] == "." :
                pass
            else :
                text += "."
        except IndexError :
            pass
        self.parent.compute_area.setText(text)
    
    def func_bracket(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            for index in range(len(text)-1, -1, -1) :
                if text[index] in ("+", "-", "×", "÷") :
                    text += "("
                    break
                right_bracket = list(text).count("(")
                left_bracket = list(text).count(")")
                if left_bracket < right_bracket :
                    text += ")"
                    break
                else :
                    text += "("
                    break
            if "(" not in text :
                text += "("
        except IndexError as e :
            print(e)
        self.parent.compute_area.setText(text)
    
    def func_percent(self) :
        text = self.parent.compute_area.toPlainText()
        try :
            if text[-1] == "%" :
                return
            else :
                text += "%"
        except IndexError :
            pass
        self.parent.compute_area.setText(text)
    
    def func_PNsign(self) :
        text = self.parent.compute_area.toPlainText()
        for t in range(len(text)-1, -1, -1) :
            if text[t-1] + text[t] == "(-" :
                text = text[:t-1] + text[t+1:]
                self.parent.compute_area.setText(text)
                return
            elif text[t] in ("+", "-", "×", "÷") :
                if t == len(text)-1 :
                    return
                text = text[:t+1] + "(-" + text[t+1:]
                self.parent.compute_area.setText(text)
                return
            elif t == 0 :
                text = "(-" + text
                self.parent.compute_area.setText(text)
                return
    # endregion

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    basic = Basic()
    basic.show()
    sys.exit(app.exec())