import sqlite3
import pandas as pd
import numpy as np

df = (pd.read_excel(r"C:\Users\adria\Desktop\Music Chord Project\Music Chords.xlsx"))
#ways to append:
df.append({"Song Name":"I want you back", "Artist":"Jackson 5"}, ignore_index=True)





pd.DataFrame()
cutiearray = np.array([(1,2,3), (4,5,6)]) #2x3 array
cutiedf = pd.DataFrame(cutiearray, columns= ["a","b","c"])
cutie2 = {"a":7,"b":8,"c":9}
cutiedf.append(cutie2, ignore_index=True)


con = sqlite3.connect("test.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE t (name, verse1);") # use your column names here

#with open('data.csv','r') as fin: # `with` statement available in 2.5+
 #   # csv.DictReader uses first line in file for column headings by default
  #  dr = csv.DictReader(fin) # comma is default delimiter
  #  to_db = [(i['col1'], i['col2']) for i in dr]