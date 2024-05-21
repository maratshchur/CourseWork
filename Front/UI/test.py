import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_register_dialog import Ui_Dialog

class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(self.register_user)

    def register_user(self):
        # Add your registration logic here
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Validate input data and perform registration
        if password == confirm_password:
            print(f"Registering user: {username} with email {email} and password {password}")
            # Add your registration logic here, e.g., database insert, API call, etc.
        else:
            print("Passwords do not match")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = RegisterDialog()
    dialog.show()
    sys.exit(app.exec())