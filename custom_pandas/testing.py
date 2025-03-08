from IO.csv_io import CsvInputOutput
from Dataframe.pandas_dataframe import DataFrame

data = CsvInputOutput.read_csv('business.csv')
df = DataFrame(data)
formatted_df = df.isnull()

with open('isnull_testing.txt', 'w') as file:
    file.write(DataFrame.as_table(formatted_df)) 