# fileparse.py
#
# Exercise 3.3
# Exercise 3.4
def parse_csv(filename, select=None):
    """
    컬럼을 리스트 타입 인자로 받아 원하는 컬럼만 뽑아서 리턴
    :param filename:
    :param select: list
    :return: dictionary를 내포한 리스트
    """
    import csv

    with open("Work/Data/"+filename, 'rt') as f:
        rows = csv.reader(f)
        # read the file header
        headers = next(rows)

        if select:
            col_idx = [headers.index(name) for name in select]
            headers = select
        else:
            col_idx = []

        records = []

        for row in rows:
            if not row:
                continue
            if col_idx:
                row = [row[idx] for idx in col_idx]
            record = dict(zip(headers, row))
            records.append((record))
    return records


