import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QEventLoop 
from login import LoginPage
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
                    pass
                    # self.admin_page = AdminPage()
                    # self.admin_page.show()
                else:
                    self.user_page = UserPage(response)
                    self.user_page.rejected.connect(lambda: break_loop(True))  # Break the loop if the user closes the login page
                    self.user_page.exec()
                    
            else:
                self.login_page = LoginPage()
                self.login_page.rejected.connect(lambda: break_loop(True))  # Break the loop if the user closes the login page
                self.login_page.exec()
                

def break_loop(exit_loop):
    if exit_loop:
        raise SystemExit  # Exit the loop              
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartPage()
    window.show()
    sys.exit(app.exec())