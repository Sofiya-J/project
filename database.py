import sqlite3

# connect to db
conn=sqlite3.connect('movies.db')

# create a cursor instance
c=conn.cursor()

# create table
c.execute("""CREATE TABLE Movies(
    movie_name text NOT NULL,
    actor text NOT NULL,
    actress text NOT NULL,
    director text NOT NULL,
    year_of_release integer NOT NULL )""")

 # Insert into table   
movies=[('Don','Sivakarthikeyan','Priyanka','Chakaravarthi',2022),
        ('Doctor','Sivakarthikeyan','Priyanka','Nelson',2021),
        ('Bigil','Vijay','Nayanthara','Atlee',2019)
    ]
c.executemany("INSERT INTO Movies VALUES(?,?,?,?,?)",movies)  
   
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