from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('hello world')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())