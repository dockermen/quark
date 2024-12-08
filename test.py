import pandas as pd
df = pd.read_excel("./info.xlsx")
df.columns = ["name","url","time"]
print(df["url"][0])



# import sqlite3

# conn = sqlite3.connect('test.db')
# print ("Opened database successfully")
# c = conn.cursor()
# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print ("Table created successfully")
# conn.commit()
# conn.close()
