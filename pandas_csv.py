import csv
import os 

def format_as_table(data, columns = None):
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

def head(data, n = 2):
    return format_as_table(data[ : n])

def tail(data, n = 2):
    return format_as_table(data[-n : ])

def read_csv(file_path, dtype, delimiter = ';', skiprows = 0, header = True):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter = delimiter)
            rows = list(reader)
    else:
        raise FileNotFoundError("couldn't find the file")

    if skiprows > 0:
        rows = rows[skiprows : ]

    if header:
        if skiprows > 0 and len(rows) > 0:
            columns = rows[0]
            rows = rows[1 : ]
        else:
            columns = rows[0]
            rows = rows[1 : ]
    else:
        columns = [f"column_{i}" for i in range(len(rows[0]))]

    data = []
    for row in rows:
        if len(row)!= len(columns):
            raise ValueError(f'row has {len(row)} columns but expected {len(columns)}')
        else:
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
    # print(data)
    return data

data = read_csv('email.csv', dtype = {'Identifier' : float}, delimiter = ';', skiprows = 0, header = True)
# print(data)

df = format_as_table(data)
print(df)

print('\n')
print(head(data))

print('\n')
print(tail(data))