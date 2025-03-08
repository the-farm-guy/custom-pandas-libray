class AsTable():
    @classmethod
    def as_table(cls, data):
        """Format data as a string table."""

        if not data:
            return "Empty dataset"
        
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