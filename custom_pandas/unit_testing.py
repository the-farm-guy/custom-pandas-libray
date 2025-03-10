import os 
import unittest
from IO.csv_io import CsvInputOutput
from IO.excel_io import ExcelInputOutput
from IO.json_io import JsonInputOutput

class CsvExcelJsonInpuTest(unittest.TestCase):
    def test_read_csv(self):
        expected = [{'Login email;Identifier;First name;Last name': 'laura@example.com;2070;Laura;Grey'}, {'Login email;Identifier;First name;Last name': 'craig@example.com;4081;Craig;Johnson'}, {'Login email;Identifier;First name;Last name': 'mary@example.com;9346;Mary;Jenkins'}, {'Login email;Identifier;First name;Last name': 'jamie@example.com;5079;Jamie;Smith'}]
        result = CsvInputOutput.read_csv('email.csv')
        self.assertEqual(expected, result)

    def test_read_csv_delimeter(self):
        expected = [{'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'}, {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'}, {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'}, {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}]
        result = CsvInputOutput.read_csv('email.csv', delimiter = ';')
        self.assertEqual(expected, result)

    def test_read_csv_skiprows(self):
        expected = [{'laura@example.com': 'craig@example.com', '2070': '4081', 'Laura': 'Craig', 'Grey': 'Johnson'}, {'laura@example.com': 'mary@example.com', '2070': '9346', 'Laura': 'Mary', 'Grey': 'Jenkins'}, {'laura@example.com': 'jamie@example.com', '2070': '5079', 'Laura': 'Jamie', 'Grey': 'Smith'}]
        result = CsvInputOutput.read_csv('email.csv', delimiter = ';', skiprows = 1)
        self.assertEqual(expected, result)

    def test_read_excel(self):
        expected = [{'laura@example.com': 'craig@example.com', '2070': '4081', 'Laura': 'Craig', 'Grey': 'Johnson'}, {'laura@example.com': 'mary@example.com', '2070': '9346', 'Laura': 'Mary', 'Grey': 'Jenkins'}, {'laura@example.com': 'jamie@example.com', '2070': '5079', 'Laura': 'Jamie', 'Grey': 'Smith'}]
        result = ExcelInputOutput.read_excel('email.xlsx')
        self.assertEqual(expected, result)

    def test_read_josn(self):
        excepted = [
            {"laura@example.com": "craig@example.com", "2070": "4081", "Laura": "Craig", "Grey": "Johnson"},
            {"laura@example.com": "mary@example.com", "2070": "9346", "Laura": "Mary", "Grey": "Jenkins"},
            {"laura@example.com": "jamie@example.com", "2070": "5079", "Laura": "Jamie", "Grey": "Smith"}
        ]

        result = JsonInputOutput.read_json('email.json')
        self.assertEqual(excepted, result)

class CsvExcelJsonOutputTest(unittest.TestCase):
    def test_to_csv(self):
        data = [
            {"laura@example.com": "craig@example.com", "2070": "4081", "Laura": "Craig", "Grey": "Johnson"},
            {"laura@example.com": "mary@example.com", "2070": "9346", "Laura": "Mary", "Grey": "Jenkins"},
            {"laura@example.com": "jamie@example.com", "2070": "5079", "Laura": "Jamie", "Grey": "Smith"}
        ]

        CsvInputOutput.to_csv(file_path = 'to_email.csv', data = data)
        self.assertTrue(os.path.exists('to_email.csv'))

        csv_data = CsvInputOutput.read_csv('to_email.csv')
        self.assertEqual(data, csv_data)

    def test_to_json(self):
        data = [
            {"laura@example.com": "craig@example.com", "2070": "4081", "Laura": "Craig", "Grey": "Johnson"},
            {"laura@example.com": "mary@example.com", "2070": "9346", "Laura": "Mary", "Grey": "Jenkins"},
            {"laura@example.com": "jamie@example.com", "2070": "5079", "Laura": "Jamie", "Grey": "Smith"}
        ]

        JsonInputOutput.to_json(file_path = 'to_email.json', data = data)
        self.assertTrue(os.path.exists('to_email.json'))
        
        csv_data = JsonInputOutput.read_json('to_email.json')
        self.assertEqual(data, csv_data)

    def test_to_excel(self):
        data = [
            {"laura@example.com": "craig@example.com", "2070": "4081", "Laura": "Craig", "Grey": "Johnson"},
            {"laura@example.com": "mary@example.com", "2070": "9346", "Laura": "Mary", "Grey": "Jenkins"},
            {"laura@example.com": "jamie@example.com", "2070": "5079", "Laura": "Jamie", "Grey": "Smith"}
        ]

        ExcelInputOutput.to_excel(file_path = 'to_email.xlsx', data = data)
        self.assertTrue(os.path.exists('to_email.xlsx'))

class DataFrameTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)