import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox, \
    QWizard, QWidget, QWizardPage
from PySide6.QtCore import Qt

class RegistrationWizard(QWizard):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация пользователя")

        self.addPage(LoginPage())
        self.addPage(NamePage())
        self.addPage(SubscribePage())

    def accept(self):
        login = self.field("login")
        password = self.field("password")
        fullname = self.field("fullname")
        interests = self.field("interests")
        subscribe = "да" if self.field("subscribe") else "нет"

        info_text = f"Логин: {login}\nПароль: {password}\nФИО: {fullname}\nИнтересы: {interests}\nПодписка: {subscribe}"
        main_window.info_label.setText(info_text)

        super().accept()

class LoginPage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.registerField("login*", self.login_edit)
        self.registerField("password*", self.password_edit)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Логин:"))
        layout.addWidget(self.login_edit)
        layout.addWidget(QLabel("Пароль:"))
        layout.addWidget(self.password_edit)

        self.setLayout(layout)

class NamePage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.fullname_edit = QLineEdit()

        self.registerField("fullname*", self.fullname_edit)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("ФИО:"))
        layout.addWidget(self.fullname_edit)

        self.setLayout(layout)


class SubscribePage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.interests_edit = QLineEdit()
        self.subscribe_checkbox = QCheckBox("Согласен на рассылку")

        self.registerField("interests*", self.interests_edit)
        self.registerField("subscribe", self.subscribe_checkbox)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Темы, интересные вам:"))
        layout.addWidget(self.interests_edit)
        layout.addWidget(self.subscribe_checkbox)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Основное окно программы")

        self.start_wizard_button = QPushButton("Запустить Wizard")
        self.start_wizard_button.clicked.connect(self.start_wizard)

        self.info_label = QLabel("Информация о пользователе:")
        self.info_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.start_wizard_button)
        layout.addWidget(self.info_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_wizard(self):
        wizard = RegistrationWizard()
        wizard.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
