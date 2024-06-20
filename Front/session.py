from PySide6.QtCore import QTimer, QSettings
import requests

def get_session_id():
    settings = QSettings('MyCompany', 'MyApp')
    session_id = settings.value('session_id')
    return session_id

def check_session(url):
        session_id = get_session_id()
        headers = {'Cookie': f'sessionid={session_id}'}
        response = requests.get(url, headers=headers)
        return response