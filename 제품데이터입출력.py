import sqlite3

class ProductManager:
    def __init__(self, db_name='products.db'):
        # SQLite 데이터베이스 연결 및 커서 생성
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # 테이블 생성 또는 이미 존재하면 무시
        self.create_table()

    def create_table(self):
        # products 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        # 제품 추가
        self.cursor.execute('''
            INSERT INTO products (product_name, price) VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, price):
        # 제품 업데이트
        self.cursor.execute('''
            UPDATE products SET product_name=?, price=? WHERE product_id=?
        ''', (product_name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        # 제품 삭제
        self.cursor.execute('''
            DELETE FROM products WHERE product_id=?
        ''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        # 제품 조회
        self.cursor.execute('''
            SELECT * FROM products WHERE product_id=?
        ''', (product_id,))
        return self.cursor.fetchone()

    def display_all_products(self):
        # 모든 제품 데이터 조회
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def __del__(self):
        # 데이터베이스 연결 종료
        self.conn.close()


class ElectronicsManager:
    def __init__(self, db_name='electronics.db'):
        # SQLite 데이터베이스 연결 및 커서 생성
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # 테이블 생성 또는 이미 존재하면 무시
        self.create_table()

    def create_table(self):
        # electronics 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        ''')
        self.conn.commit()

    def insert_electronic(self, product_name, price):
        # 전자제품 추가
        self.cursor.execute('''
            INSERT INTO electronics (product_name, price) VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()

    def update_electronic(self, product_id, product_name, price):
        # 전자제품 업데이트
        self.cursor.execute('''
            UPDATE electronics SET product_name=?, price=? WHERE product_id=?
        ''', (product_name, price, product_id))
        self.conn.commit()

    def delete_electronic(self, product_id):
        # 전자제품 삭제
        self.cursor.execute('''
            DELETE FROM electronics WHERE product_id=?
        ''', (product_id,))
        self.conn.commit()

    def select_electronic(self, product_id):
        # 전자제품 조회
        self.cursor.execute('''
            SELECT * FROM electronics WHERE product_id=?
        ''', (product_id,))
        return self.cursor.fetchone()

    def display_all_electronics(self):
        # 모든 전자제품 데이터 조회
        self.cursor.execute('SELECT * FROM electronics')
        return self.cursor.fetchall()

    def __del__(self):
        # 데이터베이스 연결 종료
        self.conn.close()


# 샘플 데이터 추가
if __name__ == "__main__":
    product_manager = ProductManager()
    electronics_manager = ElectronicsManager()

    # 제품 샘플 데이터 10개 추가
    product_sample_data = [
        ('Laptop', 1200.0),
        ('Mouse', 20.0),
        ('Keyboard', 50.0),
        ('Monitor', 300.0),
        ('Headphones', 80.0),
        ('Tablet', 500.0),
        ('Printer', 150.0),
        ('Camera', 700.0),
        ('Smartphone', 1000.0),
        ('External Hard Drive', 120.0)
    ]

    for data in product_sample_data:
        product_manager.insert_product(data[0], data[1])

    # 전자제품 샘플 데이터 10개 추가
    electronic_sample_data = [
        ('Laptop', 1200.0),
        ('Smartphone', 800.0),
        ('Tablet', 500.0),
        ('Camera', 700.0),
        ('Smart TV', 1200.0),
        ('Headphones', 80.0),
        ('Gaming Console', 400.0),
        ('Printer', 150.0),
        ('Smart Watch', 300.0),
        ('VR Headset', 200.0)
    ]

    for data in electronic_sample_data:
        electronics_manager.insert_electronic(data[0], data[1])

    # 모든 제품 데이터 출력
    all_products = product_manager.display_all_products()
    print("All Products:")
    for product in all_products:
        print(product)

    # 모든 전자제품 데이터 출력
    all_electronics = electronics_manager.display_all_electronics()
    print("\nAll Electronics:")
    for electronic in all_electronics:
        print(electronic)
