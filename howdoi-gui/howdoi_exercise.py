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
                self.label = w()
                layout.addWidget(w(self.howdo("switch case in python")))
            elif w == QLineEdit:
                self.line_edit_widget = w()
                self.line_edit()
                layout.addWidget(self.line_edit_widget)

            else:
                layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def return_pressed(self):
        self.widget.setText("BOOM!")

    def selection_changed(self):
        print(self.widget.selectedText())

    # def text_changed(self, text):
    #     print(text)

    def text_edited(self, text):
        self.label.setText(self.howdo(text))

    def line_edit(self):
        self.line_edit_widget.setPlaceholderText("Enter your text")
        #self.widget.setReadOnly(True) # uncomment this to make readonly
        #self.line_edit_widget.returnPressed.connect(self.return_pressed)
        #self.line_edit_widget.selectionChanged.connect(self.selection_changed)
        #self.line_edit_widget.textChanged.connect(self.text_changed)
        self.line_edit_widget.textEdited.connect(self.text_edited)

    def howdo(self, text):
        if __name__ == "__main__":
            return howdoi.howdoi(text)
    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")
    # def mousePressEvent(self, e):
    #     self.label.setText("mousePressEvent")
    # def mouseReleaseEvent(self, e):
    #     self.label.setText("mouseReleaseEvent")
    # def mouseDoubleClickEvent(self, e):
    #     self.label.setText("mouseDoubleClickEvent")

    # def contextMenuEvent(self, e):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self, triggered=self.do_something))
    #     context.addAction(QAction("test 2", self, triggered=lambda: print("test 2")))
    #     context.addAction(QAction("test 3", self, triggered=lambda: print("test 3")))
    #     context.exec_(e.globalPos())
    # def do_something(self):
    #     print("test 1")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


# if __name__ == "__main__":
#     print(howdoi.howdoi("switch case in python"))