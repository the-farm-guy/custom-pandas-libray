class DataFrame():
    def __init__(self, data, file_path = None):
        self.data = data
        self.file_path = file_path

    def __str__(self):
        """Return a string representation when print() is called on the object"""
        return self.as_table()
    
    def __repr__(self):
        """Return a string representation for debugging"""
        
        return f"CSVProcessor(file_path='{self.file_path}', rows={len(self.data)})"

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key):
        """Enable slicing, row access, and column selection with indexing"""

        if isinstance(key, slice):    
            return DataFrame(self.data[key])

        elif isinstance(key, str):
            if not self.data:
                return []
            if key not in self.columns():
                raise KeyError(f"Column '{key}' not found. Available columns: {', '.join(self.columns())}")
            
            return [row[key] for row in self.data] 

        elif isinstance(key, list):  
            if not all(isinstance(col, str) for col in key): 
                raise TypeError("All column names must be strings.")
            
            missing_columns = [col for col in key if col not in self.columns()]
            if missing_columns:
                raise KeyError(f"Columns {missing_columns} not found. Available columns: {', '.join(self.columns())}")

            return DataFrame([{col: row[col] for col in key} for row in self.data]) 
        
        elif isinstance(key, int):  
            return self.data[key]

        else:
            raise TypeError("Invalid Operation")

    def columns(self):
        return list(self.data[0].keys()) if self.data else []
    
    @classmethod
    def as_table(CLS, data = None, columns = None):
        """Format data as a string table."""

        if not data:
            return "Empty dataset"
            
        if columns is None:
            columns = data[0].keys()

        col_widths = {col: max(len(col), max(len(str(row.get(col, ''))) for row in data)) for col in columns}
        header = " | ".join(col.ljust(col_widths[col]) for col in columns)
        separator = "-+-".join('-' * col_widths[col] for col in columns)
        
        rows = []
        for row in data:
            row_str = " | ".join(str(row.get(col, '')).ljust(col_widths[col]) for col in columns)
            rows.append(row_str)

        table = f"{header}\n{separator}\n" + "\n".join(rows)
        return table

    def head(self, number = 5):
        return self.as_table(self.data[ : number])
    
    def tail(self, number = 5):
        return self.as_table(self.data[-number : ])
    
    def columns(self):
        return list(self.data[0].keys())
    
    def shape(self):
        return (len(self.data), len(list(self.data[0].keys())))
    
    def dropna(self, axis=0, how='any'):
        missing_indicators = ['', 'none', 'null', 'na', 'n/a', 'nan', '\'\'', '""', "''", "None"]
        
        if axis == 0:  
            filtered_rows = []
            
            for row in self.data:
                keep_row = True  
                
                if how == 'any':
                    for value in row.values():
                        if str(value).strip().lower() in missing_indicators:
                            keep_row = False  
                            break
                
                elif how == 'all':
                    all_missing = True
                    for value in row.values():
                        if str(value).strip().lower() not in missing_indicators:
                            all_missing = False  
                            break
                    if all_missing:
                        keep_row = False  

                if keep_row:
                    filtered_rows.append(row) 
            
            self.data = filtered_rows
        
        elif axis == 1:  
            columns_to_keep = []
            all_columns = self.columns()
            
            for col in all_columns:
                keep_column = True  
        
                if how == 'any':
                    for row in self.data:
                        if str(row[col]).strip().lower() in missing_indicators:
                            keep_column = False  
                            break
                
                elif how == 'all':
                    all_missing = True
                    for row in self.data:
                        if str(row[col]).strip().lower() not in missing_indicators:
                            all_missing = False 
                            break
                    if all_missing:
                        keep_column = False  
                
                if keep_column:
                    columns_to_keep.append(col)  
            
            new_data = []
            for row in self.data:
                new_row = {}
                for col in columns_to_keep:
                    new_row[col] = row[col]
                new_data.append(new_row)
            
            self.data = new_data

        return self.data
    
    def replace(self, old_value, new_value):
        for row in self.data:  
            for key in row: 
                if row[key] == old_value:  
                    row[key] = new_value  
        return self.data
    
    def fillna(self, value):
        missing_indicators = ['', 'none', 'null', 'na', 'n/a', 'nan', '\'\'', '""', "''", "None"]
        for rows in self.data:
            for key in rows:
                if rows[key].strip().lower() in missing_indicators:
                    rows[key] = value

        return self
    
    def isnull(self):
        missing_indicators = {'', 'none', 'null', 'na', 'n/a', 'nan', '""', "''"}  
        missing_values = [] 

        for row in self.data:  
            row_missing = {} 

            for key, value in row.items():  
                if value is None or str(value).strip().lower() in missing_indicators:
                    row_missing[key] = True 
                else:
                    row_missing[key] = False 

            missing_values.append(row_missing)  

        return missing_values 

    def fillna_fill(self, type = ''):
            missing_indicators = {'', 'none', 'null', 'na', 'n/a', 'nan', '""', "''"} 
            if type.lower() == 'bfill': 
                for i in range(len(self.data)):
                    for j, k in self.data[i].items():
                        if k in missing_indicators:
                            self.data[i][j] = self.data[i + 1][j]

            elif type.lower() == 'ffill':
                for i in range(len(self.data)):
                    for j, k in self.data[i].item():
                        if k in missing_indicators:
                            self.data[j][k] = self.data[i - 1][j]

            else:
                raise ValueError('unsupported Type')

            return self.data
    