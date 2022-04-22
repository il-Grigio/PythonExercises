import sys

from howdoi import howdoi

from PySide2.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QSpinBox ,QSlider,
    QDoubleSpinBox, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QTimeEdit, QVBoxLayout, QWidget, QMenu, QAction, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setWindowTitle("Widgets App")
        layout = QVBoxLayout()
        widgets = [
            QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
            QSpinBox, QDoubleSpinBox, QLabel, QLineEdit,
            QProgressBar, QPushButton, QRadioButton, QSlider, QTimeEdit,
        ]
        for w in widgets:
            if w == QLabel:
                self.label = w(howdoi.howdoi("zoom in vscode"))
                layout.addWidget(self.label)
            elif w == QLineEdit:
                self.line_edit_widget = w()
                self.line_edit()
                layout.addWidget(self.line_edit_widget)
            else:
                layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def return_pressed(self):
        self.label.setText(howdoi.howdoi(self.line_edit_widget.text()))

    def selection_changed(self):
        print(self.widget.selectedText())

    # def text_edited(self, text):
    #     self.label.setText(self.howdo(text))

    def line_edit(self):
        self.line_edit_widget.setPlaceholderText("Enter your text")
        #self.line_edit_widget.textEdited.connect(self.text_edited)
        self.line_edit_widget.returnPressed.connect(self.return_pressed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()