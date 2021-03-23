import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse  CSV file into a list of records with conversion
    """
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected make indices for filtering and set output columns
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []

        for rowno, row in enumerate(rows, 1):
            if not row:  # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [row[index] for index in indices]

            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Coudln't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
            
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        
        return records