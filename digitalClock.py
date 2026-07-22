# Python PyQt5 Digital Click

import sys
from pathlib import Path

from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

FONT_PATH = str(Path(__file__).parent / "DS-DIGIT.TTF")


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(0, 0, 1512, 982)

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label.setStyleSheet("font-size: 300px;color: #1efc29")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont(FONT_PATH)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            my_font = QFont(font_families[0], 300)
            self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString(
            "hh:mm:ss"
        )  # do (hh:mm:ss AP) for non-military time
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
