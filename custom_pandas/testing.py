from IO.csv_io import CsvInputOutput
from Dataframe.pandas_dataframe import DataFrame 

data = CsvInputOutput.read_csv('business.csv')
# print(AsTable.as_table(data))

df = DataFrame(data)

# print(df.head())
# print(df.tail())
# print(df.columns())
print(df[['Year', 'Units']].as_table())