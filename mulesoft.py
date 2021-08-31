import sqlite3
connection = sqlite3.connect("Films.db")
cursor = connection.cursor()
sql_command=""" CREATE TABLE Movies(Name VARCHAR(25),
Actor VARCHAR(50),
Actress VARCHAR(50),
Director VARCHAR(50),
Year_of_release INTEGER);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Name,Actor,Actress,Director,Year_of_release)VALUES("Muthu","Rajinikanth","Meena","KSR",1995);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Name,Actor,Actress,Director,Year_of_release)VALUES("Yejamaan","Rajinikanth","Meena","RVU",1193);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Name,Actor,Actress,Director,Year_of_release)VALUES("Premam","Nivinpauly","MadonnaSebastien","Alphonse Puthren",2015);"""
cursor.execute(sql_command)
connection.commit()
cursor.execute("SELECT * FROM Movies")
print("fetchall:")
result=cursor.fetchall()
for r in result:
    print(r)
