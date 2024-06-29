import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'p',
    database = 'data'
)

mycursor = mydb.cursor()

def insert_data(user_name,select_movie,Mail_id):
    sql = "insert into datas(name,title,email_id) values (%s,%s,%s)"
    val = (user_name,select_movie,Mail_id)

    try:
        mycursor.execute(sql,val)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        mydb.rollback()
        
def update_data():
    update = ("UPDATE datas SET name = %s WHERE id = %s")
    name = input("Enter your name to update: ")
    id = input("Enter id to update: ")
    val = (name,id)

    try:
        mycursor.execute(update,val)
        mydb.commit()
        print("Update successfully")
        mycursor.execute("select * from datas")
        res = mycursor.fetchall()
        for dat in res:
            print(dat)
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        mydb.rollback()
    

def delete_data():
    delete_query = "DELETE FROM datas WHERE id = %s"
    id = input("Enter the ID to delete: ")
    try:
        mycursor.execute(delete_query, (id,))
        mydb.commit()
        print("Data Deleted successfully")
        mycursor.execute("SELECT * FROM datas")
        res = mycursor.fetchall()
        for da in res:
            print(da)
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        mydb.rollback()

def show_data():
    mycursor.execute('select * from datas')
    res = mycursor.fetchall()
    for da in res:
        print(da)
