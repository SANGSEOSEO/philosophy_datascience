# fileparse.py
#
# Exercise 3.3
# Exercise 3.4
# Exercise 3.7
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    컬럼을 리스트 타입 인자로 받아 원하는 컬럼만 뽑아서 리턴
    :param filename:
    :param select: list
    :param type: list
    :param has_headers : 헤더 존재 여부
    :param delimiter : 구분자
    :return: dictionary를 내포한 리스트
    """
    import csv

    with open("Work/Data/"+filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        # read the file header
        headers = next(rows) if has_headers else []

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

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if not has_headers:  #헤더가 없으면 튜플로 변환
                records.append(tuple(row))
            else:
                record = dict(zip(headers, row))
                records.append(record)
    return records


