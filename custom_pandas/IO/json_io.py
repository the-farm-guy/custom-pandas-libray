import json
import os 

class JsonInputOutput:
    @classmethod
    def read_json(cls, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            raise FileNotFoundError('could not find the file')
    
    @classmethod
    def to_json(cls, data, file_path=None, orient='records', indent=4):
        if not data:
            raise ValueError('no data found')
        
        if orient == 'records':
            formatted_data = data
            
        elif orient == 'columns':
            columns = {}
            for record in data:
                for key, value in record.items():
                    if key not in columns:
                        columns[key] = []
                    columns[key].append(value)
            formatted_data = columns
            
        else:
            raise ValueError(f"Unsupported orientation: {orient}. Supported values are 'records' and 'columns'.")
        
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(formatted_data, file, indent=indent)
            print(f'data has been written to: {file_path}')
            return None
        else:
            return json.dumps(formatted_data, indent=indent)