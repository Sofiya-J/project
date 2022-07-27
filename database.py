import sqlite3
# connect to db
conn=sqlite3.connect('movies.db')
# create a cursor instance
c=conn.cursor()

#queries
c.execute("SELECT * FROM Movies") 
print("All movies present in table")
output=c.fetchall()
for i in output:
    print()

c.execute("SELECT movie_name FROM Movies WHERE actor='Sivakarthikeyan'")
print("movies name based on actor")
output=c.fetchall()
for i in output:
    print(i)

# commit our command
conn.commit() 
# close our connection
conn.close()