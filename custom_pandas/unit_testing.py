import os 
import unittest
from IO.csv_io import CsvInputOutput
from IO.excel_io import ExcelInputOutput
from IO.json_io import JsonInputOutput

class CsvExcelJsonInputTest(unittest.TestCase):
    def setUp(self):
        with open('email.csv', 'w') as f:
            f.write("Login email;Identifier;First name;Last name\n")
            f.write("laura@example.com;2070;Laura;Grey\n")
            f.write("craig@example.com;4081;Craig;Johnson\n")
            f.write("mary@example.com;9346;Mary;Jenkins\n")
            f.write("jamie@example.com;5079;Jamie;Smith\n")
        
        import json
        json_data = [
            {"Login email": "laura@example.com", "Identifier": "2070", "First name": "Laura", "Last name": "Grey"},
            {"Login email": "craig@example.com", "Identifier": "4081", "First name": "Craig", "Last name": "Johnson"},
            {"Login email": "mary@example.com", "Identifier": "9346", "First name": "Mary", "Last name": "Jenkins"},
            {"Login email": "jamie@example.com", "Identifier": "5079", "First name": "Jamie", "Last name": "Smith"}
        ]
        with open('email.json', 'w') as f:
            json.dump(json_data, f)
            
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.append(["Login email", "Identifier", "First name", "Last name"])
        ws.append(["laura@example.com", "2070", "Laura", "Grey"])
        ws.append(["craig@example.com", "4081", "Craig", "Johnson"])
        ws.append(["mary@example.com", "9346", "Mary", "Jenkins"])
        ws.append(["jamie@example.com", "5079", "Jamie", "Smith"])
        wb.save('email.xlsx')
    
    def tearDown(self):
        for file in ['email.csv', 'email.xlsx', 'email.json', 'to_email.csv', 'to_email.xlsx', 'to_email.json']:
            if os.path.exists(file):
                os.remove(file)
    
    def test_read_csv(self):
        expected = [
            {'Login email;Identifier;First name;Last name': 'laura@example.com;2070;Laura;Grey'},
            {'Login email;Identifier;First name;Last name': 'craig@example.com;4081;Craig;Johnson'},
            {'Login email;Identifier;First name;Last name': 'mary@example.com;9346;Mary;Jenkins'},
            {'Login email;Identifier;First name;Last name': 'jamie@example.com;5079;Jamie;Smith'}
        ]
        result = CsvInputOutput.read_csv('email.csv')
        self.assertEqual(expected, result)

    def test_read_csv_delimiter(self):
        expected = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]
        result = CsvInputOutput.read_csv('email.csv', delimiter=';')
        self.assertEqual(expected, result)

    def test_read_csv_skiprows(self):
        expected = [
            {'laura@example.com': 'craig@example.com', '2070': '4081', 'Laura': 'Craig', 'Grey': 'Johnson'},
            {'laura@example.com': 'mary@example.com', '2070': '9346', 'Laura': 'Mary', 'Grey': 'Jenkins'},
            {'laura@example.com': 'jamie@example.com', '2070': '5079', 'Laura': 'Jamie', 'Grey': 'Smith'}
        ]
        result = CsvInputOutput.read_csv('email.csv', delimiter=';', skiprows=1)
        self.assertEqual(expected, result)

    def test_read_excel(self):
        expected = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]
        result = ExcelInputOutput.read_excel('email.xlsx')
        self.assertEqual(expected, result)

    def test_read_json(self):
        expected = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]
        result = JsonInputOutput.read_json('email.json')
        self.assertEqual(expected, result)

class CsvExcelJsonOutputTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]
    
    def tearDown(self):
        for file in ['to_email.csv', 'to_email.xlsx', 'to_email.json']:
            if os.path.exists(file):
                os.remove(file)
    
    def test_to_csv(self):
        CsvInputOutput.to_csv(file_path='to_email.csv', data=self.data)
        self.assertTrue(os.path.exists('to_email.csv'))
        
        csv_data = CsvInputOutput.read_csv('to_email.csv')
        self.assertEqual(self.data, csv_data)

    def test_to_json(self):
        JsonInputOutput.to_json(file_path='to_email.json', data=self.data)
        self.assertTrue(os.path.exists('to_email.json'))
        
        json_data = JsonInputOutput.read_json('to_email.json')
        self.assertEqual(self.data, json_data)

    def test_to_excel(self):
        ExcelInputOutput.to_excel(file_path='to_email.xlsx', data=self.data)
        self.assertTrue(os.path.exists('to_email.xlsx'))
        
        excel_data = ExcelInputOutput.read_excel('to_email.xlsx')
        self.assertEqual(self.data, excel_data)

class DataFrameTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]

    def test_head(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)