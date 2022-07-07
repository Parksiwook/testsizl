import pymysql.cursors

conn = pymysql.connect(host='3.34.122.118', port=3306, user='wook', db='testpsw', password='222',
                       charset='utf8', cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()


def create():
    sql = '''create table wook2 (id int(5) NOT NULL auto_increment primary key, name varchar(10),
            record int(5))'''
    cursor.execute(sql)


def update():
    sql = '''update '''

def result():
    result2 = cursor.fetchall()
    for res in result2:
        print(res)


def show_table():
    sql = "show tables"
    cursor.execute(sql)


show_table()
result()
conn.commit()
conn.close()