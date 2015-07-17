import sys, datetime

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C4C Buddy")
        
        self.NameLabel = QLabel("Enter Users Name:")
        self.NameInput = QLineEdit()
        self.NameInput.setPlaceholderText("Matt Ling")

        
        self.PostLabel = QLabel("Paste the Post/Comment Here:")
        self.postInput = QTextEdit()
        self.postInput.setFixedHeight(120)
        self.Generate = QPushButton("Generate Post..")
        self.Generate.clicked.connect(self.GenerateClicked)



        self.TodayLabel = QLabel("Todays Clickers:")
        self.TodayTable = QTableWidget(0,4)
        self.TodayTable.setFixedWidth(400)
        self.TodayHeaders = ["Name","Country","Time","Returned"]
        self.TodayTable.setHorizontalHeaderLabels(self.TodayHeaders)
        self.TodayTable.setAlternatingRowColors(True)
        self.TodayTable.horizontalHeader().setStretchLastSection(True)




        self.searchLabel = QLabel("Search Clickers:")
        self.searchInput = QLineEdit()
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchInput)
        



        self.YesterdayLabel = QLabel("Yesterdays Clickers:")
        self.YesterdayTable = QTableWidget(0,4)
        self.YesterdayTable.setFixedWidth(400)
        self.YesterdayHeaders = ["Name","Country","Time","Returned"]
        self.YesterdayTable.setHorizontalHeaderLabels(self.YesterdayHeaders)
        self.YesterdayTable.setAlternatingRowColors(True)
        self.YesterdayTable.horizontalHeader().setStretchLastSection(True)


        self.mainLayout = QHBoxLayout()
        self.LeftLayout = QVBoxLayout()
        self.RightLayout = QVBoxLayout()

        self.LeftLayout.addWidget(self.NameLabel)
        self.LeftLayout.addWidget(self.NameInput)
        self.LeftLayout.addWidget(self.PostLabel)
        self.LeftLayout.addWidget(self.postInput)
        self.LeftLayout.addWidget(self.Generate)

        self.LeftLayout.addWidget(self.TodayLabel)
        self.LeftLayout.addWidget(self.TodayTable)

        self.RightLayout.addWidget(self.YesterdayLabel)
        self.RightLayout.addWidget(self.YesterdayTable)

        self.LeftWidget = QWidget()
        self.RightWidget = QWidget()

        self.LeftWidget.setLayout(self.LeftLayout)
        self.RightWidget.setLayout(self.RightLayout)

        self.mainLayout.addWidget(self.LeftWidget)
        self.mainLayout.addWidget(self.RightWidget)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)

    def GenerateClicked(self):
        self.TodayTable.insertRow(int(self.TodayTable.rowCount()))
        
        Name = self.NameInput.text()
        
        post = self.postInput.toPlainText()
        Country = self.GetCountry(post)

        time = datetime.datetime.now().time()
        Time = time.strftime("%H:%M")

        print("Name: {0} \nCountry: {1} \nTime: {2}".format(Name, Country[0], Time))

        FinalName = QTableWidgetItem(Name)
        FinalName.setTextAlignment(Qt.AlignCenter)

        FinalCountry = QTableWidgetItem(Country[0])
        FinalCountry.setTextAlignment(Qt.AlignCenter)

        FinalTime = QTableWidgetItem(Time)
        FinalTime.setTextAlignment(Qt.AlignCenter)

        rowNo = int(self.TodayTable.rowCount() - 1)
        print(rowNo)

        checkBoxWidget = QWidget()
        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(QCheckBox())
        checkBoxLayout.setAlignment(Qt.AlignCenter)
        checkBoxLayout.setContentsMargins(0,0,0,0)
        checkBoxWidget.setLayout(checkBoxLayout)
        
        self.TodayTable.setItem(rowNo, 0, FinalName)
        self.TodayTable.setItem(rowNo, 1, FinalCountry)
        self.TodayTable.setItem(rowNo, 2, FinalTime)
        self.TodayTable.setCellWidget(rowNo, 3, checkBoxWidget)

    def GetCountry(self,post):
        Premium = False
        PremiumList = ["UK","US","USA","AUS","NZ","GER","CAN"]
        for item in PremiumList:
            if item in post:
                Premium = True
                Country = [item, Premium]
        return Country
            

    
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
