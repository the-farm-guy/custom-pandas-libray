from Dataframe.pandas_dataframe import DataFrame
data = [
    {'Login email': 'laura@example.com', 'Identifier': '2070', 'First name': 'Laura', 'Last name': 'Grey'},
    {'Login email': 'craig@example.com', 'Identifier': '4081', 'First name': 'Craig', 'Last name': 'Johnson'},
    {'Login email': 'mary@example.com', 'Identifier': '9346', 'First name': 'Mary', 'Last name': 'Jenkins'},
    {'Login email': 'jamie@example.com', 'Identifier': '5079', 'First name': 'Jamie', 'Last name': 'Smith'}
]

df = DataFrame(data)
print(df.head(2))