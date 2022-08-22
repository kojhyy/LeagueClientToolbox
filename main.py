import sys
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # création de la liste d'onglets sur le côté
        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        # création de 2 éléments
        text_widget = QLabel("test")
        button = QPushButton("bouton")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)

        self.setLayout(layout)

        

    #     self.button = QtWidgets.QPushButton("Click me!")
    #     self.text = QtWidgets.QLabel("Hello World",
    #                                  alignment=QtCore.Qt.AlignCenter)

    #     self.layout = QtWidgets.QVBoxLayout(self)
    #     self.layout.addWidget(self.text)
    #     self.layout.addWidget(self.button)

    #     self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        
        text_widget = QLabel("test")
        button = QPushButton("bouton")


if __name__ == "__main__":
    app = QApplication([])

    widget = Widget()
    widget.resize(800, 600)
    widget.show()
    
    _style = open("style.qss", "r").read()
    app.setStyleSheet(_style)

    sys.exit(app.exec())
