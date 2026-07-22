# Python PyQt5 Stopwatch

import sys
from pathlib import Path

from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase, QFontMetrics
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

FONT_PATH = str(Path(__file__).parent / "DS-DIGIT.TTF")


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch - GT Colors Edition")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
            }
            QPushButton{
                font-size: 50px;
                font-family: "Times New Roman";
            }
            QLabel{
                font-size: 120px;
                color: #B3A369;
                background-color: #051E39; 
                border-radius: 20px;
            }
        """)

        font_id = QFontDatabase.addApplicationFont(FONT_PATH)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            clock_font = QFont(font_families[0], 120)
            self.time_label.setFont(clock_font)
            # Lock width so changing digits don't resize/recenter the label each tick
            metrics = QFontMetrics(clock_font)
            self.time_label.setFixedWidth(metrics.horizontalAdvance("88:88:88.88") + 40)
            self.time_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
