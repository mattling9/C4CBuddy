import sys, datetime, pickle

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.GlobalList = []
        
        self.NameLabel = QLabel("Enter Users Name:")
        self.NameInput = QLineEdit()
        self.NameInput.setPlaceholderText("Matt Ling")

        
        self.PostLabel = QLabel("Paste the Post/Comment Here:")
        self.postInput = QTextEdit()
        self.postInput.setFixedHeight(180)
        self.Generate = QPushButton("Add To Table..")
        self.Generate.clicked.connect(self.GenerateClicked)

        self.clickerLabel = QLabel("Who Clicked:")
        self.clickerInput = QComboBox()
        self.clickerInput.currentIndexChanged.connect(self.ManualAd)
        self.clickerInput.addItem("Them")
        self.clickerInput.addItem("You")
        self.clickerlayout = QHBoxLayout()
        self.clickerlayout.addWidget(self.clickerLabel)
        self.clickerlayout.addWidget(self.clickerInput)
        self.clickerWidget = QWidget()
        self.clickerWidget.setLayout(self.clickerlayout)

        self.manualAdLabel = QLabel("What Ad Did you Click:")
        self.manualAdInput = QLineEdit()
        self.manualAdLayout = QHBoxLayout()
        self.manualAdLayout.addWidget(self.manualAdLabel)
        self.manualAdLayout.addWidget(self.manualAdInput)
        self.manualAdWidget = QWidget()
        self.manualAdWidget.setLayout(self.manualAdLayout)
        self.manualAdWidget.setVisible(False)





        self.searchLabel = QLabel("Search Clickers:")
        self.searchInput = QLineEdit()
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchInput)
        



        self.TodayLabel = QLabel("Todays Clickers:")
        self.TodayTable = QTableWidget(0,6)
        self.TodayTable.setFixedWidth(600)
        self.TodayHeaders = ["Name","Country","Time","Ad","Who Clicked","Returned"]
        self.TodayTable.setHorizontalHeaderLabels(self.TodayHeaders)
        self.TodayTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.TodayTable.setAlternatingRowColors(True)
        self.TodayTable.horizontalHeader().setStretchLastSection(True)



        #PREMIUM COUNTRIES

        self.PremLabel = QLabel("""Premium Countries:\n\n• USA\n• UK\n• Canada\n• Ireland\n• Australia\n• New Zealand\n• Germany\n\n""") 
        self.SubLabel = QLabel("""Sub-Premium Countries:\n\n• The Netherlands\n• Singapore\n• France\n• Spain\n• Japan\n• Italy\n• Belgium\n• Switzerland\n""")
        self.NonLabel = QLabel("""** If your Country is not listed above then you must assume that you are in a NON PREMIUM Country, so please follow people's NON PREMIUM rules. **""")

        self.CountriesTabLayout = QVBoxLayout()
        self.CountriesTabLayout.addWidget(self.PremLabel)
        self.CountriesTabLayout.addWidget(self.SubLabel)
        self.CountriesTabLayout.addWidget(self.NonLabel)
        self.CountriesTab = QWidget()
        self.CountriesTab.setLayout(self.CountriesTabLayout)

        #High Ads

        self.AdDescription = QLabel("""The Following List is compiled from the High Paying Ads we know of.

If you happen to find a high paying Ad that is not listed here, You can contact any one of the members listed in the credits.""")
        self.AdDescription.setFixedHeight(60)
        self.AdList = QLabel("• Plus500\n• Egnyte\n• Deacon\n• Manage Engine\n• Fresh Desk\n• Fresh Service\n• Mulesoft\n• Softlayer\n• Solarwinds\n• Ehealth\n• Full Sail\n• Experian\n• Fisher Investments\n• Google Ads(including Gmail, ChromeCast, Adwords, Adsense)\n• GoDaddy\n•123-reg""")
        self.AdLayout = QVBoxLayout()
        self.AdWidget = QWidget()
        self.AdLayout.addWidget(self.AdDescription)
        self.AdLayout.addWidget(self.AdList)
        self.AdWidget.setLayout(self.AdLayout)
                        



        #SearchBar
        self.SearchLabel = QLabel("Search:")
        self.SearchInput = QLineEdit()
        self.SearchInput.setPlaceholderText("Looking For Someone?...")
        self.searchLayout = QHBoxLayout()
        self.searchLayout.addWidget(self.SearchLabel)
        self.searchLayout.addWidget(self.SearchInput)
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(self.searchLayout)
        

        #LAYOUT

        self.TabWidget = QTabWidget()


        
        self.TodayLayout = QHBoxLayout()
        self.LeftLayout = QVBoxLayout()
        self.RightLayout = QVBoxLayout()

        self.LeftLayout.addWidget(self.NameLabel)
        self.LeftLayout.addWidget(self.NameInput)
        self.LeftLayout.addWidget(self.PostLabel)
        self.LeftLayout.addWidget(self.postInput)
        self.LeftLayout.addWidget(self.clickerWidget)
        self.LeftLayout.addWidget(self.manualAdWidget)
        self.LeftLayout.addWidget(self.Generate)

        self.RightLayout.addWidget(self.searchWidget)
        self.RightLayout.addWidget(self.TodayLabel)
        self.RightLayout.addWidget(self.TodayTable)

        self.LeftWidget = QWidget()
        self.RightWidget = QWidget()

        self.LeftWidget.setLayout(self.LeftLayout)
        self.RightWidget.setLayout(self.RightLayout)

        self.TodayLayout.addWidget(self.LeftWidget)
        self.TodayLayout.addWidget(self.RightWidget)

        self.TodayWidget = QWidget()
        self.TodayWidget.setLayout(self.TodayLayout)

        self.TabWidget.addTab(self.TodayWidget, "Today")
        self.TabWidget.addTab(self.CountriesTab, "Premium Countires")
        self.TabWidget.addTab(self.AdWidget, "High Paying Ads")
        self.TabWidget.setWindowTitle("C4C Buddy")
        self.TabWidget.resize(900,460)

        self.LoadFromFile()
        
        self.TabWidget.show()
        self.TabWidget.raise_()

        
        
        

    def GenerateClicked(self):

        rowNo = int(self.TodayTable.rowCount())
        
        #while self.NameInput.text() == "":
            #print("Please Enter a Name!")

        #while self.postInput.toPlainText() == "":
            #print("Please Enter a Post/Comment!")

        
        self.TodayTable.insertRow(int(self.TodayTable.rowCount()))

        Name = self.NameInput.text()
        FinalName = QTableWidgetItem(Name)
        FinalName.setTextAlignment(Qt.AlignCenter)

        post = self.postInput.toPlainText()
        

        Country = self.GetCountry(post)
        if Country != None:
            FinalCountry = QTableWidgetItem(Country)
            FinalCountry.setTextAlignment(Qt.AlignCenter)
            self.TodayTable.setItem(rowNo, 1, FinalCountry)
        elif Country == None:
            ("Country not Recognised")

        if self.clickerInput.currentText() == 'Them':
            Ad = self.GetAd(post)
            if Ad != None:
                FinalAd = QTableWidgetItem(Ad.lower().title())
                FinalAd.setTextAlignment(Qt.AlignCenter)
                self.TodayTable.setItem(rowNo, 3, FinalAd)
            elif Ad == None:
                print("Ad Not Recognised")
                #self.nonRecgonisedAd()
        elif self.clickerInput.currentText() == 'You':
            Ad = self.GetAd(self.manualAdInput.text().upper())
            if Ad != None:
                FinalAd = QTableWidgetItem(Ad.lower().title())
                FinalAd.setTextAlignment(Qt.AlignCenter)
                self.TodayTable.setItem(rowNo, 3, FinalAd)
            elif Ad == None:
                print("Ad Not Recognised")
                #self.nonRecgonisedAd()

        time = datetime.datetime.now().time()
        Time = time.strftime("%H:%M")
        FinalTime = QTableWidgetItem(Time)
        FinalTime.setTextAlignment(Qt.AlignCenter)


        checkBoxWidget = QWidget()
        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(QCheckBox())
        checkBoxLayout.setAlignment(Qt.AlignCenter)
        checkBoxLayout.setContentsMargins(0,0,0,0)
        checkBoxWidget.setLayout(checkBoxLayout)

        FinalClicker = QTableWidgetItem(self.clickerInput.currentText())
        FinalClicker.setTextAlignment(Qt.AlignCenter)
        
        self.TodayTable.setItem(rowNo, 0, FinalName)
        self.TodayTable.setItem(rowNo, 2, FinalTime)
        self.TodayTable.setItem(rowNo, 4, FinalClicker)
        self.TodayTable.setCellWidget(rowNo, 5, checkBoxWidget)

        self.insertClickList()

    def GetCountry(self,post):
        Recognised = False
        with open("CountryList.txt", mode ="r", encoding="UTF-8")as CountryFile:
            for Country in CountryFile:
                if not Recognised:
                    if Country.rstrip("\n") in post.upper():
                        Recognised = True
                        Match = Country.rstrip("\n")
                        
        if Recognised:
            return Match
        else:
            return None
        

    def GetAd(self,post):
        Recognised = False
        with open("AdList.txt", mode ="r", encoding="UTF-8")as AdFile:
            for Advert in AdFile:
                if not Recognised:
                    if Advert.rstrip("\n") in post.upper():
                        Recognised = True
                        Match = Advert.rstrip("\n")
        if Recognised:
            return Match
        else:
            return None

    def ManualAd(self):
        if self.clickerInput.currentText() == "You":
            self.manualAdWidget.setVisible(True)
        elif self.clickerInput.currentText() == "Them":
                self.manualAdWidget.setVisible(False)

    def insertClickList(self):
        Click = []
        with open("ClickList.txt", mode="wb")as listFile:
            rowNo = int(self.TodayTable.rowCount()-1)
            for column in range(0,5):
                Click.append(self.TodayTable.item(rowNo, column).text())
            Click.append('N')
            self.GlobalList.append(Click)
            pickle.dump(self.GlobalList, listFile)

    def LoadFromFile(self):
        with open("ClickList.txt", mode="rb")as loadList:

            lineCounter = 0
            try:
                List = pickle.load(loadList)
                self.GlobalList = List
                
                for item in List:
                    self.TodayTable.insertRow(int(self.TodayTable.rowCount()))
                    
                    Name = QTableWidgetItem(item[0])
                    Name.setTextAlignment(Qt.AlignCenter)

                    Country = QTableWidgetItem(item[1])
                    Country.setTextAlignment(Qt.AlignCenter)

                    Time = QTableWidgetItem(item[2])
                    Time.setTextAlignment(Qt.AlignCenter)

                    Ad = QTableWidgetItem(item[3])
                    Ad.setTextAlignment(Qt.AlignCenter)

                    WhoClicked = QTableWidgetItem(item[4])
                    WhoClicked.setTextAlignment(Qt.AlignCenter)
                    

                    self.TodayTable.setItem(lineCounter, 0, Name)
                    self.TodayTable.setItem(lineCounter, 1, Country)
                    self.TodayTable.setItem(lineCounter, 2, Time)
                    self.TodayTable.setItem(lineCounter, 3, Ad)
                    self.TodayTable.setItem(lineCounter, 4, WhoClicked)
                    lineCounter += 1
            except:
                pass
                
            

    
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
