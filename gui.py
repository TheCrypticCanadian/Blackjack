from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout 
from PyQt5.QtGui import QIcon, QImage
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600
        
        self.hit_button = QPushButton("Hit")
        self.stand_button = QPushButton("Stand")
        self.ng_button = QPushButton("New Game")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hit_button)
        self.layout.addWidget(self.stand_button)
        self.layout.addWidget(self.ng_button)
        self.setLayout(self.layout)
        #icon

        self.setWindowTitle("Blackjack")
        self.setGeometry(top, left, width, height)
        #self.setWindowIcon(QIcon(icon))
        
    def display_hands():
        pass

    def display_end():
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
