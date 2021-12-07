import sqlite3


def instantiate_db():
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")


def add_entry(day, date, time):
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")
    c_obj.execute("INSERT INTO timings VALUES(?,?,?)", (day, date, time))
    connection.commit()
    connection.close()


def update_entry(date, time):
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")
    c_obj.execute(
        "UPDATE timings SET time = (?) WHERE date = (?)", (time, date))
    connection.commit()
    connection.close()


def delete_entry(date):
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")
    c_obj.execute("DELETE FROM timings WHERE date = (?)", (date,))
    connection.commit()
    connection.close()


def view_entry(date):
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")
    items = c_obj.execute("SELECT time FROM timings WHERE date = (?)", [date])
    for item in items:
        print(item)
    # need to give input in docstrings???
    connection.close()


def view_all_entry():
    connection = sqlite3.connect("database.db")
    c_obj = connection.cursor()
    c_obj.execute("""CREATE TABLE IF NOT EXISTS timings
                        (day TEXT, date TEXT, time INTEGER)""")
    items = c_obj.execute('SELECT rowid, * FROM timings')
    print("ROWID" + "\t  " + "DAY" + "\t       " + " DATE" + "\t\t" + "TIME")
    print("---" + "\t  " + "------" + "\t" + "----------" + "\t" + "---")
    for item in items:
        print(str(item[0]) + "\t  " + item[1] +
              "\t" + str(item[2]) + "\t" + str(item[3]))

    connection.close()

#
# a = c_obj.execute("SELECT * FROM timings")
# for item in a:
#     print(item)
# print(a.lastrowid)
# connection.close()


# add_entry("Monday", "2021-12-01", "10")
