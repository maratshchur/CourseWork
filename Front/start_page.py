import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QEventLoop 
from admin_main import AdminPage
from email_verification import VerifyEmailPage
from login import LoginPage
from register import RegisterPage
from session import check_session
from urls import BASE_URL
from user_main import UserPage

class StartPage(QDialog):
    def __init__(self):
        super(StartPage, self).__init__()
        self.login()
        
    def login(self):
        
        while True:
            response = check_session(f"{BASE_URL}/check_session")
            if response.status_code == 200:
                if response.json().get('is_admin'):
                    self.admin_page = AdminPage()
                    self.admin_page.exec()
                    if self.admin_page.was_rejected and self.admin_page.log_out:
                        continue
                    elif self.admin_page.was_rejected:
                        self.break_loop(True)
                else:
                    self.user_page = UserPage(response)
                    self.user_page.exec()
                    if self.user_page.was_rejected and self.user_page.logout:
                        continue
                    elif self.user_page.was_rejected:
                        self.break_loop_main_page(True)
                    
            else:
                self.show_login_page()
                    
    def show_register_page(self):           
        self.register_page = RegisterPage()
        result = self.register_page.exec()
        if result == QDialog.Accepted:
            self.email_verification_page = VerifyEmailPage(self.register_page.email, self.register_page.username)
            result = self.email_verification_page.exec()
            if result == QDialog.Accepted:
                pass
            
    def show_login_page(self):
        self.login_page = LoginPage()
        # self.login_page.ui.register_button.clicked.connect(self.login_page.close)
        self.login_page.ui.register_button.clicked.connect(self.show_register_page)
        self.login_page.rejected.connect(lambda: self.break_loop(True))  # Break the loop if the user closes the login page
        self.login_page.exec()
            
    def break_loop(self, exit_loop):
        if exit_loop:
            raise SystemExit  # Exit the loop              

    def break_loop_main_page(self, exit_loop):
        self.user_page.save_game_data()
        if exit_loop:
            raise SystemExit  # E

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartPage()
    window.show()
    sys.exit(app.exec())