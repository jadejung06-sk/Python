##### Manage DB
## Connection, Control, get keyword, Insert data
import pymysql as my

class DBHelper:
    conn = None
    def __init__(self):
        self.db_init()
        
    def db_init(self):
        self.conn = my.connect(
                            host='localhost',
                            user='root',
                            password='1234',
                            database='pythondb',
                            cursorclass=my.cursors.DictCursor
        )
    def db_free(self):
        if self.conn:
            self.conn.close()
    def db_selectKeyword(self):
        # Open Cursor
        # with == I/O & Automatically close
        rows = None
        with self.conn.cursor() as cursor:
        # Read a single record
            sql = "select * from tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows
        
    def db_insertCrawlingData(self, title, price, area, contents, keyword):
        with self.conn.cursor() as cursor:
            sql = '''insert into `tbl_crawlingdata` (title, price, area, contents, keyword) 
            values (%s,%s,%s,%s,%s);'''
            cursor.execute(sql, (title, price, area, contents, keyword)) # Parameters
        self.conn.commit()

## Only for Testing Code     
if __name__=="__main__":
    db = DBHelper()
    print(db.db_selectKeyword())
    db.db_insertCrawlingData('1','2','3','4','5')
    db.db_free()