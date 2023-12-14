import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# DB 파일이 존재하는지 확인하고, 있다면 연결하고, 없다면 새로운 데이터베이스를 생성한다.
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    # Products 테이블이 없으면 새로 생성한다.
    cur.execute("create table Products (id integer primary key autoincrement, Name text, Price integer);")

# 디자인 파일을 로딩
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기값 설정 
        self.id = 0 
        self.name = ""
        self.price = 0 

        # QTableWidget의 컬럼폭 설정 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 설정
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        # QTableWidget의 컬럼 정렬 설정 
        #self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        #self.tableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        # 탭키로 네비게이션 금지 
        self.tableWidget.setTabKeyNavigation(False)
        # 엔터키를 클릭하면 다음 컨트롤로 이동하는 경우 
        # self.prodID.tabOrder = 0 
        # self.prodName.tabOrder = 1 
        # self.prodPrice.tabOrder = 2 
        # QLineEdit으로 수정함(엔터키를 누르면 이동)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        # 입력 파라미터 처리 
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        # 데이터베이스에 제품 추가
        cur.execute("insert into Products (Name, Price) values (?, ?);", (self.name, self.price))
        # 리프레시
        self.getProduct() 
        # 입력, 수정, 삭제 작업 후에는 커밋을 한다. 
        con.commit() 

    def updateProduct(self):
        # 업데이트 작업시 파라미터 처리 
        self.id  = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        # 데이터베이스에서 제품 정보 업데이트
        cur.execute("update Products set name=?, price=? where id=?;", (self.name, self.price, self.id))
        # 리프레시
        self.getProduct() 
        # 입력, 수정, 삭제 작업 후에는 커밋을 한다. 
        con.commit()  

    def removeProduct(self):
        # 삭제 파라미터 처리 
        self.id  = self.prodID.text() 
        strSQL = f"delete from Products where id={self.id}"
        # 데이터베이스에서 제품 삭제
        cur.execute(strSQL)
        # 리프레시
        self.getProduct() 
        # 입력, 수정, 삭제 작업 후에는 커밋을 한다. 
        con.commit()  

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()

        # 모든 제품 정보를 가져옴
        cur.execute("select * from Products;") 
        # 행 숫자 카운트 
        row = 0 
        for item in cur: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            
            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            
            # 제품명은 그대로 출력
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1
            print("row: ", row)  

    def doubleClick(self):
        # 더블클릭 시 해당 제품 정보를 편집 창에 표시
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 인스턴스 생성
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
