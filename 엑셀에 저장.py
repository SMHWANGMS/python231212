import openpyxl
from random import randint

# 데이터 생성
data = []
for i in range(1, 101):
    product_id = i
    product_name = f"제품{i}"
    quantity = randint(1, 10)
    price = randint(1000, 10000)
    data.append((product_id, product_name, quantity, price))

# Excel 파일 생성 및 데이터 저장
wb = openpyxl.Workbook()
ws = wb.active

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 데이터 추가
for row in data:
    ws.append(row)

# Excel 파일 저장
file_path = r"c:\work2\products.xlsx"
wb.save(file_path)

print(f"데이터가 {file_path}에 저장되었습니다.")
