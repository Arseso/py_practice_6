from datetime import datetime
import sys

from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QDialog, QLineEdit, \
    QDateTimeEdit, QLabel


class AddNoteDialog(QDialog):
    def __init__(self, mode: str = "add", text: str = None):
        super().__init__()
        self.__mode = mode
        if self.__mode == "add":
            self.setWindowTitle("Добавить заметку")
        else:
            self.setWindowTitle("Изменить заметку")

        self.text_edit = QLineEdit()
        self.date_edit = QDateTimeEdit()
        if self.__mode == "edit":
            txt, date = text.split(" - ")
            self.text_edit.setText(txt)
            datetime_object = datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
            self.date_edit.setDateTime(datetime_object)

        self.date_edit.setDateTime(QDateTime.currentDateTime())

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Текст заметки:"))
        layout.addWidget(self.text_edit)
        layout.addWidget(QLabel("Дата и время:"))
        layout.addWidget(self.date_edit)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_note_data(self):
        return self.text_edit.text(), self.date_edit.dateTime().toString()




class NoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение для заметок")

        self.note_list = QListWidget()
        self.add_button = QPushButton("Добавить заметку")
        self.add_button.clicked.connect(self.add_note_dialog)
        self.note_list.itemDoubleClicked.connect(self.edit_note_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.note_list)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_note_dialog(self):
        dialog = AddNoteDialog()
        if dialog.exec():
            text, date = dialog.get_note_data()
            self.note_list.addItem(f"{text} - {date}")

    def edit_note_dialog(self, item):
        dialog = AddNoteDialog(mode="edit", text=item.text())
        if dialog.exec():
            text, date = dialog.get_note_data()
            item.setText(f"{text} - {date}")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    note_app = NoteApp()
    note_app.show()
    sys.exit(app.exec())

