import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("weewoopoopoo")
        self.setGeometry(500, 500, 500, 500)
        self.ButtonY = QPushButton('Yes', self)
        self.ButtonN = QPushButton('No', self)
        self.initUIDesign()

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
    def initUIDesign(self):
        central_widget = (QWidget())
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()
        self.ButtonY.setStyleSheet('color: white;'
                                   'background-color: green;'
                                   'font-weight: bold;')
        self.ButtonY.clicked.connect(self.on_click_Yes)
        vbox.addWidget(self.ButtonY)
        self.ButtonN.setStyleSheet('color: white;'
                                   'background-color: red;'
                                   'font-weight: bold;')
        self.ButtonN.clicked.connect(self.on_click_No)
        vbox.addWidget(self.ButtonN)
        
        ## This is for label layout ##
        #label1 = QLabel("YES")
        #label1.setStyleSheet('background-color: green;')
        #vbox.addWidget(label1)
        #label2 = QLabel("No")
        #label2.setStyleSheet('background-color: red;')
        #vbox.addWidget(label2)
        central_widget.setLayout(vbox)
    
    def on_click_Yes(self):
        print('Yes was clicked!')
        self.ButtonY.setDisabled(True)

    def on_click_No(self):
        print('No was clicked!')
        self.ButtonN.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()