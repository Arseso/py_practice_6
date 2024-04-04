import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QCheckBox, QVBoxLayout, QDialog, QLabel


class CheckBoxDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Диалог с чекбоксом")

        self.checkbox = QCheckBox("Соглашаюсь")
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.on_ok_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def on_ok_clicked(self):
        if self.checkbox.isChecked():
            QMessageBox.information(self, "Состояние чекбокса", "Чекбокс выбран")
        else:
            QMessageBox.information(self, "Состояние чекбокса", "Чекбокс не выбран")


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
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())

