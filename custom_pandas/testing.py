from IO.csv_io import CsvInputOutput
from Dataframe.pandas_dataframe import DataFrame

data = CsvInputOutput.read_csv('business.csv')
# print(AsTable.as_table(data))

df = DataFrame(data).isnull()
print(df)

# formatted_df = DataFrame.as_table(df)

# with open('isnull_testing.txt', 'w') as file:
    # file.write(formatted_df)
# print(df)

# print(DataFrame.as_table(df))
# print(df.head())
# print(df.tail())
# print(df.columns())
# print(df[['Year', 'Units']].as_table())
# print(df.dropna(axis = 0, how = 'any'))
# formatted_df = df.dropna(axis = 0, how = 'any')

# with open('dropna_testing.txt', 'w') as file:
#     file.write(DataFrame.as_table(formatted_df)) 

# isnull_df = df.isnull()
# print(isnull_df)