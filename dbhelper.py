from sqlite3 import connect, Row

database = 'skills.db'

def getallprocess(sql:str)-> list:
    db:object = connect(database)
    db.row_factory = Row
    cursor: object = db.cursor()
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    return data

def postprocess(sql:str)-> bool:
    db = connect(database)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    return True if cursor.rowcount>0 else False

def add_record(table: str, **kwargs) -> bool:
    keys = list(kwargs.keys())
    values = [f"'{v}'" for v in kwargs.values()]  # Wrap values in quotes for SQL
    
    fld = "`,`".join(keys)
    dta = ",".join(values)
    sql = f"INSERT INTO `{table}` (`{fld}`) VALUES ({dta})"
    
    return postprocess(sql)
    
def getall_records(table:str)-> list:
    sql:str = f"SELECT * FROM `{table}`"
    return getallprocess(sql)
    
def  getall_books()-> list:
    sql:str = f"SELECT isbn, title, author, copyright, edition, price, qty, [price] * [qty] as total FROM `books`"
    return getallprocess(sql)