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
        
    def as_table(self, data=None, columns=None):
        """Format data as a string table."""

        data = data or self.data
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