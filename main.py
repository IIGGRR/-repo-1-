import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor, QBrush
from random import randint

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('pup')
        self.setGeometry(100, 100, 400, 400)
        self.flag = False
        self.button = QPushButton("press!", self)
        self.button.clicked.connect(self.toggle_circle)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def toggle_circle(self):
        self.flag = not self.flag
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setBrush(QBrush(QColor(255, 255, 0)))
            r = randint(10, 1000)
            painter.drawEllipse(100, 100,  r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())
