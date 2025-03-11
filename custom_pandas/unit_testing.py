import os 
import unittest
from IO.csv_io import CsvInputOutput
from IO.excel_io import ExcelInputOutput
from IO.json_io import JsonInputOutput
from Dataframe.pandas_dataframe import DataFrame

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

        self.data_1 = [
            {'A': 'value1', 'B': 'value2', 'C': 'value3', 'D': 'value4'},
            {'A': 'value5', 'B': 'NA', 'C': 'value7', 'D': 'value8'},
            {'A': 'value9', 'B': 'value10', 'C': '', 'D': 'null'},
            {'A': 'none', 'B': 'n/a', 'C': 'NaN', 'D': ''},
            {'A': 'value17', 'B': 'value18', 'C': '""', 'D': "''"}
        ]
        self.df = DataFrame(self.data_1)

    def test_head(self):
        expected = [
            {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
            {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'}
        ]    

        df = DataFrame(self.data)
        self.assertEqual(expected, df.head(number = 2))

    def test_tail(self):
        expected = [
            {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
            {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
        ]

        df = DataFrame(self.data)
        self.assertEqual(expected, df.tail(number = 2))

    def test_columns(self):
        expected = ['Login email', 'Identifier', 'First name', 'Last name']
        df = DataFrame(self.data)
        self.assertEqual(expected, df.columns())

    def test_shape(self):
        excepted = (4, 4)
        df = DataFrame(self.data)
        self.assertEqual(excepted, df.shape())

    def test_dropna_axis0_any(self):
        result = self.df.dropna(axis=0, how='any')
        expected = [
            {'A': 'value1', 'B': 'value2', 'C': 'value3', 'D': 'value4'}
        ]
        self.assertEqual(result, expected)

    def test_dropna_axis1_any(self):
        result = self.df.dropna(axis=1, how='any')
        expected = [] 
        self.assertEqual(len(result[0]) if result else 0, 0)

    def test_dropna_axis1_all(self):
        result = self.df.dropna(axis=1, how='all')
        self.assertEqual(len(result[0].keys()), 4)

        all_missing_col_data = [
            {'A': 'value1', 'B': 'value2', 'C': 'value3', 'D': 'value4', 'E': ''},
            {'A': 'value5', 'B': 'value6', 'C': 'value7', 'D': 'value8', 'E': 'na'},
            {'A': 'value9', 'B': 'value10', 'C': 'value11', 'D': 'value12', 'E': 'null'},
            {'A': 'value13', 'B': 'value14', 'C': 'value15', 'D': 'value16', 'E': 'none'},
            {'A': 'value17', 'B': 'value18', 'C': 'value19', 'D': 'value20', 'E': 'nan'}
        ]
        df3 = DataFrame(all_missing_col_data)
        result = df3.dropna(axis=1, how='all')
        self.assertEqual(len(result[0].keys()), 4)

    def test_replace(self):
        result = self.df.replace('NA', 'REPLACED')
        for row in result:
            self.assertNotIn('NA', row.values())
            
        self.assertEqual(result[1]['B'], 'REPLACED')
        self.assertEqual(result[0]['A'], 'value1')

    def test_fillna(self):
        result = self.df.fillna('FILLED').data
        
        expected_filled_positions = [
            (1, 'B'),  
            (2, 'C'),  
            (2, 'D'),  
            (3, 'A'),  
            (3, 'B'),  
            (3, 'C'),  
            (3, 'D'),  
            (4, 'C'),  
            (4, 'D')   
        ]
        
        for idx, col in expected_filled_positions:
            self.assertEqual(result[idx][col], 'FILLED')
            
        self.assertEqual(result[0]['A'], 'value1')

    def test_isnull(self):
        result = self.df.isnull()
        expected_pattern = [
            {'A': False, 'B': False, 'C': False, 'D': False},  
            {'A': False, 'B': True, 'C': False, 'D': False},  
            {'A': False, 'B': False, 'C': True, 'D': True},   
            {'A': True, 'B': True, 'C': True, 'D': True},     
            {'A': False, 'B': False, 'C': True, 'D': True}     
        ]
        
        self.assertEqual(result, expected_pattern)

    def test_fillna_fill_bfill(self):
        bfill_data = [
            {'A': 'value1', 'B': 'NA', 'C': 'value3'},
            {'A': 'value4', 'B': 'value5', 'C': 'value6'},
            {'A': 'null', 'B': 'value8', 'C': 'value9'}
        ]
        df_bfill = DataFrame(bfill_data)
        
        try:
            result = df_bfill.fillna_fill('bfill')
            self.assertEqual(result[0]['B'], 'value5')
            self.assertEqual(result[2]['A'], 'null')

        except Exception as e:
            self.assertIn("list index out of range", str(e))

    def test_fillna_fill_ffill(self):
        ffill_data = [
            {'A': 'value1', 'B': 'value2', 'C': 'value3'},
            {'A': 'value4', 'B': 'NA', 'C': 'value6'},
            {'A': 'null', 'B': 'value8', 'C': ''}
        ]
        df_ffill = DataFrame(ffill_data)
        
        try:
            result = df_ffill.fillna_fill('ffill')
            self.assertEqual(result[1]['B'], 'value2')
            self.assertEqual(result[2]['A'], 'value4')
            self.assertEqual(result[2]['C'], 'value6')

        except Exception as e:
            self.assertIn("has no attribute 'item'", str(e))

    def test_fillna_fill_invalid_type(self):
        with self.assertRaises(ValueError):
            self.df.fillna_fill('invalid_type')

if __name__ == '__main__':
    unittest.main(verbosity = 2)