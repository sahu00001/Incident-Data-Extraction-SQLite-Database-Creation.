import urllib.request
import tempfile
import re
import sqlite3 
from PyPDF4 import PdfFileReader

def fetchincidents(url):
    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def extractIncidents(incident_data):
    try:
        store = tempfile.TemporaryFile()
        store.write(incident_data)
        store.seek(0)
        pdfReader = PdfFileReader(store)
        pagecount = pdfReader.getNumPages()
        incidents = []
        for p in range(pagecount):
            page = pdfReader.getPage(p).extractText()
            pagecontent = page.replace(" \n", " ")
            pagecontent = re.split(r'\s+(?=\d?\d?\/\d?\d?\/\d{4} \d?\d?:\d?\d?)', pagecontent)
            for i in range(len(pagecontent)):
                pagecontent[i] = pagecontent[i].split("\n")
                if (len(pagecontent[i]) == 5):
                    incidents.append(pagecontent[i])
        return incidents
    except:
        print("Error in extracting incidents from PDF file.")

def create_populateDatabase(incidents):
    conn = sqlite3.connect('incident.db')
    c = conn.cursor()
   #creating a table name incidents
    drop_table='''drop TABLE IF EXISTS incidents'''
    c.execute(drop_table)
    table = '''CREATE TABLE incidents(date_time text, incident_number, location text, nature text , ori text );'''
    c.execute(table)
    # inserting data in the table
    #for i in range(len(incidents)):
    c.executemany('''INSERT INTO incidents VALUES (?,?,?,?,?)''',incidents)
    #executing the sql query
    # data= c.execute('''SELECT * FROM incidents''')
    data = c.execute(
        '''SELECT nature,count(nature) FROM incidents GROUP BY nature ORDER BY count(nature) DESC, nature ASC''')
    solution = c.fetchall()
    for x in solution:
        #printing the required data
        print(x[0], "|", x[1])
    # for row in data:
    # print(row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4])
    # commit changes and close connection
    # conn.commit()
    return(print(x[0], "|", x[1]))
    conn.close()

