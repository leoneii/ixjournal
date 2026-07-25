import sqlite3


dbp = sqlite3.connect("jourbd.sqlite")
cur = dbp.cursor()
#pqcount = cur.execute(quec)
pquery = cur.execute("SELECT namezak FROM jtab;")
print (pquery.fetchall())