from pyautocad import Autocad, aDouble
from collections import Counter
import plotly.express as pex
import plotly.io as pio
import pandas as pd
import os

pio.renderers.default='browser'
acad = Autocad()
doc = acad.ActiveDocument
ms = doc.ModelSpace
print(acad.doc.Name)
df = pd.DataFrame(columns=['name', 'count'])
a =[]
for obj in acad.iter_objects():
	a.append(obj.ObjectName)
b = Counter(a)
df = pd.DataFrame.from_dict(b, orient='index').reset_index()
df.columns = ['name', 'count']
df['file'] = acad.doc.Name
df.sort_values(by='count', ascending=False, inplace=True)
fig = pex.bar(data_frame=df, x = 'name',y='count' )
fig.show()
print(df)
# if file does not exist write header
if not os.path.isfile('Archive.csv'):
   df.to_csv('Archive.csv', header='column_names')
else: # else it exists so append without writing the header
   df.to_csv('Archive.csv', mode='a', header=False)