from IO.csv_io import CsvInputOutput

data = CsvInputOutput.read_csv('business.csv')
# print(AsTable.as_table(data))

# df = DataFrame(data)

# print(DataFrame.as_table(df))
# print(df.head())
# print(df.tail())
# print(df.columns())
# print(df[['Year', 'Units']].as_table())
# print(df.dropna(axis = 0, how = 'any'))
# formatted_df = df.dropna(axis = 0, how = 'any')

# with open('dropna_testing.txt', 'w') as file:
#     file.write(DataFrame.as_table(formatted_df)) 