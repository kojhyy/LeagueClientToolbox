import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *
import Graphic.Graphic as Graphic





if __name__ == "__main__":
    app = QApplication([])

    widget = Graphic.Main_Widget()
    widget.resize(800, 600)
    widget.show()

    _style = open("style.qss", "r").read()
    app.setStyleSheet(_style)

    sys.exit(app.exec())
