"""
To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:

(Must have a .sqlite suffix)

Hint: The top organizational count is 536.
You do not need to export or convert the database - simply upload the .sqlite file that your program creates. See the example code for the use of the connect() statement.

Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
"""

import sqlite3

conn = sqlite3.connect('Python4EBdb.sqlite')
cur = conn.cursor()

# cur.execute('''
# DROP TABLE IF EXISTS Counts''')

# Verifica si existe la tabla Counts, si no existe, créala
cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

fname = 'mails2.txt'
if len(fname) < 1:
    fname = 'mails2.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
# Aca se podría splitear por '@' para luego no tener necesidad de hacer un query especial por el @ (consigna pide suma de correos institucionales independientemente del remitente)
    pieces = line.split()
    org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

# Realiza la consulta para obtener el dominio con más correos enviados
cur.execute('''
SELECT SUBSTR(org, INSTR(org, '@') + 1) AS dominio, SUM(count) AS total_correos_enviados
FROM Counts
GROUP BY dominio
ORDER BY total_correos_enviados DESC
LIMIT 1''')

# Imprime los resultados
for row in cur:
    print("Dominio con más correos enviados:", row[0])
    print("Total de correos enviados:", row[1])

# Realiza otra consulta para obtener la lista completa de correos y su cantidad
cur.execute('''SELECT org, count FROM Counts ORDER BY count''')
for row in cur:
    print(str(row[0]), row[1])

cur.close()


"""
Enter file name: mbox.txt
Counts:
iupui.edu 536
umich.edu 491
indiana.edu 178
caret.cam.ac.uk 157
vt.edu 110
uct.ac.za 96
media.berkeley.edu 56
ufp.pt 28
gmail.com 25
et.gatech.edu 17
"""





























