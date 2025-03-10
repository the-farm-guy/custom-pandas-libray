from IO.csv_io import CsvInputOutput
from IO.excel_io import ExcelInputOutput

data = CsvInputOutput.read_csv('email.csv', skiprows = 1, delimiter = ';')
print(data)

excel_data = ExcelInputOutput.to_excel(file_path = 'email.xlsx', data = data)