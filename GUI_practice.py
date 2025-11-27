import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GuidelinesPage(QWidget):
    def __init__(self, go_next):
        pass

class Get_Username(QWidget):
    def __init__(self, go_next):
        super().__init__()
        self.name_of_user = QLineEdit()
        self.Submit = QPushButton('Submit')
        self.go_next = go_next

    def initUIDesign_User(self):
        vbox = QVBoxLayout
        hbox = QHBoxLayout

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
        self.Submit.clicked.connect(self.Submit_on_click)\
        

    def Submit_on_click(self):
        user = self.name_of_user.text()
        self.Greeting.setText(f'Welcome {user}!')
        self.Submit.setDisabled(True)

class Questionnaire(QWidget):
    def __init__(self):
        super().__init__()
        self.Greeting = QLabel('Welcome!')
        self.ButtonY = QPushButton('Yes')
        self.ButtonN = QPushButton('No')
        self.text1 = QLabel('What''s your favorite fruit?')

    def initUIDesign_Questions(self):
        vbox = QVBoxLayout()
        hbox_buttons = QHBoxLayout()
        self.ButtonY.setStyleSheet('color: white;'
                                   'background-color: green;'
                                   'font-weight: bold;'
                                   )
        self.ButtonY.clicked.connect(self.on_click_Yes)
        hbox_buttons.addWidget(self.ButtonY)
        self.ButtonN.setStyleSheet('color: white;'
                                   'background-color: red;'
                                   'font-weight: bold;'
                                   )
        self.ButtonN.clicked.connect(self.on_click_No)
        hbox_buttons.addWidget(self.ButtonN)
        vbox.addLayout(hbox_buttons)
        
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
                            #'font-style: itallic;'
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