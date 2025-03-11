from IO.csv_io import CsvInputOutput
from Dataframe.pandas_dataframe import DataFrame

data = CsvInputOutput.read_csv('data_files/email.csv', delimiter = ';')
df = DataFrame(data) 

