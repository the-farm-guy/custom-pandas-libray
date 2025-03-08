import csv
import os 

class CsvInputOutput():

    @classmethod
    def read_csv(cls, file_path = None, dtype = None, delimiter = ',', skiprows = 0, header = True):
        file_path = file_path
        dtype = dtype
        delimiter = delimiter
        skiprows = skiprows
        header = header

        if not file_path:
              raise ValueError('no file path provided')
        
        if os.path.exists(file_path):
              with open(file_path, 'r') as file:
                    reader = csv.reader(file, delimiter = delimiter)
                    rows = list(reader)

        else:
              raise FileNotFoundError('could not find file')
        
        if skiprows > 0:
            rows = rows[skiprows:]

        if header:
            if len(rows) > 0:
                columns = rows[0]
                rows = rows[1 : ]
            else:
                return []
        else:
            if len(rows) > 0:
                columns = [f'columns_{i}' for i in range(len(rows[0]))]
            else:
                return []
            
        data = []
        for row in rows:
            raw_dict = {}
            for i, col in enumerate(columns):
                value = row[i]
                if dtype and col in dtype:
                    try:
                        value = dtype[col](value)
                    except:
                        raise ValueError(f"Failed to convert column '{col}' to {dtype[col].__name__} for value '{value}'")
                raw_dict[col] = value
            data.append(raw_dict)       

        data = data
        return data
    
    @classmethod
    def to_csv(cls, file_path, data, delimiter = ','):
        if not data:
            raise ValueError('no data found')
        
        columns = data[0].keys()
        with open(file_path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames = columns, delimiter = delimiter) 
            writer.writeheader()
            writer.writerows(data)
            print(f'data has written to the {file_path}') 

if __name__ == '__main__':
    pass
