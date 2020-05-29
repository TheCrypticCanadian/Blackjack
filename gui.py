from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
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
        
        self.layout = QGridLayout()
        #self.layout.addWidget(self.hit_button)
        #self.layout.addWidget(self.stand_button)
        #self.layout.addWidget(self.ng_button)
        self.setLayout(self.layout)
        #icon

        self.pixmap = QPixmap("Cards/JC.png")
        self.pixmap2 = self.pixmap.scaledToWidth(125)
        
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap2)
        
        self.layout.addWidget(self.lbl,1,1)

        self.setWindowTitle("Blackjack")
        self.setGeometry(top, left, width, height)
        #self.setWindowIcon(QIcon(icon))
        
        self.show()

    def display_hands():
        pass

    def display_end():
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec()
