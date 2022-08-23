import sys
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # création de la liste d'onglets sur le côté
        self.menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            self.menu_widget.addItem(item)
        
        self.menu_widget.itemClicked.connect(self.change_page)

        # création de 2 éléments
        text_widget = QLabel("test")
        button = QPushButton("bouton")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(content_layout)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.menu_widget, 1)
        self.layout.addWidget(self.main_widget, 4)

        self.setLayout(self.layout)


    @Slot()
    def change_page(self):
        match (self.menu_widget.currentRow()):
            case 0:
                print(0)
            case 1:
                print(1)
            case _:
                print("erreur")


if __name__ == "__main__":
    app = QApplication([])

    widget = Widget()
    widget.resize(800, 600)
    widget.show()
    
    _style = open("style.qss", "r").read()
    app.setStyleSheet(_style)

    sys.exit(app.exec())
