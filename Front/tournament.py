class TournamentDialog(QDialog):
    def __init__(self, parent):
        super(TournamentDialog, self).__init__(parent)
        self.ui = Ui_TournamentDialog()
        self.ui.setupUi(self)
        self.ui.create_button.clicked.connect(self.create_tournament)

    def create_tournament(self):
        # Get the tournament name and other details from the dialog
        tournament_name = self.ui.name_edit.text()
        tournament_description = self.ui.description_edit.text()
        # Create the tournament using the API
        response = requests.post(f"{BASE_URL}/create_tournament", json={
            'name': tournament_name,
            'description': tournament_description
        })
        if response.status_code == 201:
            QMessageBox.information(self, "Success", "Tournament created successfully!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Failed to create tournament")