import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QRadioButton, QCheckBox, QMessageBox, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GuidelinesPage(QWidget):
    def __init__(self, go_name):
        super().__init__()
        self.greet = QLabel('Please agree to our terms and conditions!')
        self.guideline1 = QCheckBox('blah blah blah')
        self.guideline2 = QCheckBox('Boo boo')
        self.agree = QRadioButton('Agree.')
        self.disagree = QRadioButton('Disagree.')
        self.confirm = QPushButton('Confirm')
        self.initUIDesign_Guideline()
        self.go_name = go_name

    def initUIDesign_Guideline(self):
        vbox = QVBoxLayout()
        hbox_button = QHBoxLayout()
        self.greet.setStyleSheet('font-size: 25px;'
                                 'font-weight: bold;')
        self.greet.setAlignment(Qt.AlignCenter)
        self.guideline1.setStyleSheet('font-size: 20px;')
        self.guideline2.setStyleSheet('font-size: 20px;')
        self.agree.setStyleSheet('font-size: 15px;'
                                 'font-style: italic;'
                                 'color: green;')
        self.disagree.setStyleSheet('font-size: 15px;'
                                    'font-style: italic;'
                                    'color: red;')
        self.confirm.setStyleSheet('font-size: 15px;'
                                   'color: white;'
                                   'background-color: black;')
        self.agree.setDisabled(True)
        self.disagree.setDisabled(True)
        self.confirm.setDisabled(True)
        self.guideline1.stateChanged.connect(self.agree_or_disagree)
        self.guideline2.stateChanged.connect(self.agree_or_disagree)
        self.confirm.clicked.connect(self.on_click_confirm)
        vbox.addWidget(self.greet)
        vbox.addWidget(self.guideline1)
        vbox.addWidget(self.guideline2)
        hbox_button.addWidget(self.agree)
        hbox_button.addWidget(self.disagree)
        hbox_button.addWidget(self.confirm)
        vbox.addLayout(hbox_button)
        self.setLayout(vbox)

    def on_click_confirm(self):
        if self.disagree.isChecked():
            QApplication.quit()
        elif self.agree.isChecked():
            self.go_name()
        print('User Confirmed')

    def agree_or_disagree(self):
        all_Checked = self.guideline1.isChecked() and self.guideline2.isChecked()
        if all_Checked:
            self.agree.setDisabled(False)
            self.disagree.setDisabled(False)
        else:
            self.agree.setDisabled(True)
            self.disagree.setDisabled(True)
        
        if all_Checked:
            self.confirm.setDisabled(False)
        else:
            self.confirm.setDisabled(True)

class Get_Username(QWidget):
    def __init__(self, go_next):
        super().__init__()
        self.name_of_user = QLineEdit()
        self.Submit = QPushButton('Submit')
        self.Greeting = QLabel('Welcome!')
        self.initUIDesign_User()
        self.go_next = go_next

    def initUIDesign_User(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.Greeting.setStyleSheet('color: green;' 
                                    'font-size: 25px;')
        self.Greeting.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.Greeting)
        self.name_of_user.setStyleSheet('font-size: 20px;')
        self.name_of_user.setPlaceholderText('What''s your name?')
        self.Submit.setStyleSheet('font-weight: bold;'
                                  'color: blue')
        hbox.addWidget(self.name_of_user, stretch=4)
        hbox.addWidget(self.Submit, stretch=1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.Submit.clicked.connect(self.Submit_on_click)
        

    def Submit_on_click(self):
        user = self.name_of_user.text()
        self.Greeting.setText(f'Welcome {user}!')
        reply = QMessageBox.question(
            self, "Confirm", "Do you want to go to the questionnaire?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.go_next()
        print("User pressed submit!")


class Questionnaire(QWidget):
    def __init__(self):
        super().__init__()
        self.ButtonY = QPushButton('Yes')
        self.ButtonN = QPushButton('No')
        self.Q1 = QLabel('Do you like fruits?')
        self.initUIDesign_Questions()

    def initUIDesign_Questions(self):
        vbox = QVBoxLayout()
        hbox_buttons = QHBoxLayout()
        self.Q1.setStyleSheet('font-size: 50px;')
        self.Q1.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.Q1)
        self.ButtonY.setStyleSheet('color: white;'
                                   'background-color: green;'
                                   'font-weight: bold;')
        self.ButtonY.clicked.connect(self.on_click_Yes)
        hbox_buttons.addWidget(self.ButtonY)
        self.ButtonN.setStyleSheet('color: white;'
                                   'background-color: red;'
                                   'font-weight: bold;')
        self.ButtonN.clicked.connect(self.on_click_No)
        hbox_buttons.addWidget(self.ButtonN)
        vbox.addLayout(hbox_buttons)
        self.setLayout(vbox)
        
    def on_click_Yes(self):
        print('Yes was clicked!')

    def on_click_No(self):
        print('No was clicked!')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("weewoopoopoo")
        self.setGeometry(0, 0, 500, 500)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        

        self.guideline = GuidelinesPage(self.go_name)
        self.namepage = Get_Username(self.go_questionnaire)
        self.questions = Questionnaire()
    
        self.stack.addWidget(self.guideline)
        self.stack.addWidget(self.namepage)
        self.stack.addWidget(self.questions)

    def go_name(self):
        self.stack.setCurrentIndex(1)

    def go_questionnaire(self):
        self.stack.setCurrentIndex(2)


        

        ## this is for alignment and adding label ##
        #label = QLabel("Hello", self)
        #label.setFont(QFont("Arial", 40))
        #label.setGeometry(0, 0, 500, 500)
        #label.setStyleSheet("color: blue;"
                            #'background-color: green;'
                            #"font-weight: bold;"
                            #'font-style: italic;'
                            #'text-decoration: underline;')
        
        #label.setAlignment(Qt.AlignTop) #Vertically top
        #label.setAlignment(Qt.AlignBottom) #Vertically bot
        #label.setAlignment(Qt.AlignVCenter) #Vertically center
        #label.setAlignment(Qt.AlignLeft) #Horizontally Left
        #label.setAlignment(Qt.AlignRight) #Horizontally right
        #label.setAlignment(Qt.AlignHCenter) #Horizontally center
        #label.setAlignment(Qt.AlignCenter)
    
    ## this is the initialization of designs/layouts ##

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()