# pandas support data io with CSV Excel HTML and SQL with following libs
# sqlalchemy, lxml, html5lib, BeautifulSoup4

import pandas as pd
# pandas support lots of read_xxx and to_ method for various sources IO
print("the input csv file:\n{}".format(pd.read_csv('example.csv')))
# output to external data source should be through dataframe
df = pd.read_csv('example.csv')
# use argument index=False to avoid output index as part of the data
df.to_csv('my_csv.csv',index=False)
print("input same file from excel output:\n{}"
      .format(pd.read_csv('my_csv.csv')))

# for excel file IO, conda install xlrd if necessary
print("the input excel file:\n{}"
      .format(pd.read_excel('example.xlsx',sheetname='Sheet1')))
df.to_excel('my_excel.xlsx',sheet_name='NewSheet')
print("readin again the exported excel file:\n{}"
      .format(pd.read_excel('my_excel.xlsx',sheetname='NewSheet')))

data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print("the head of a sample input html:\n{}".format(data[0].head()))
dfx = pd.DataFrame(data[0])
dfx.to_html('my_html.html',index=False)
print("read html back from saved version:\n{}"
      .format(pd.read_html('my_html.html')[0].head()))

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
dfx.to_sql('my_table',engine,index=False)
print("read sample data from sql:\n{}"
      .format(pd.read_sql('my_table',con=engine)))