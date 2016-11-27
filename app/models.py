import sqlite3 as sql

# def get_users():
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row # Convert rows into a dictionary format
#         cur = con.cursor()
#         result = cur.execute("select * from users").fetchall()
#         return result

def add_user_profile(name, email, code, bio):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user_profile (name, email, pwd_code, bio) VALUES (?,?,?,?)", (name, email, code, bio))
        con.commit()

def get_idea(idea_id): # For an idea, return their ideas
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        # for user, select trips
        # sql_query = "select * from idea where id = " + idea_id
        # print(sql_query)
        # result = cur.execute(sql_query).fetchall()
        # for i in result:
        result = cur.execute("select * from idea where idea_id = (?)", ([idea_id])).fetchall()
        # print(result)
    # return result[0]
    return result

# def remove_trip(trip_name):
#     with sql.connect("app.db") as con:
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         sql_query = "DELETE from trips where trip_name = '" + trip_name + "'"
#         cur.execute(sql_query)
#         con.commit()
    
