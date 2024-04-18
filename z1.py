import sys

from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QCheckBox, QVBoxLayout, QDialog, QLabel


class CheckBoxDialog(QDialog):
    data_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Диалог с чекбоксом")

        self.checkbox = QCheckBox("Соглашаюсь")
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.send_data)

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def send_data(self):
        btn = self.checkbox.isChecked()
        self.data_signal.emit(btn)
        self.accept()


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")

        self.button = QPushButton("Открыть диалог")
        self.button.clicked.connect(self.open_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_dialog(self):
        dialog = CheckBoxDialog()
        dialog.data_signal.connect(self.on_ok_clicked)
        dialog.exec()

    @Slot(bool)
    def on_ok_clicked(self, btn):
        self.button.setText(":)" if btn else ":(")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
