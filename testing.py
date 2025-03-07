import recreate_pandas as rp

data = rp.read_csv('business.csv', dtype={'Identifier': float}, delimiter=',', skiprows=0, header=True)
print(data.format_as_table())