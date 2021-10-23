# fileparse.py
#
# Exercise 3.3
# Exercise 3.4
# Exercise 3.7
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
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

    """
    has_headers가 없는데 뽑고자 하는 컬럼을 파라미터로 주면 에러가 나므로 
    해당 에러에 대한 Exception처리 
    Exercise 3-8
    
    Exercise 3-9
    타입변환시 에러가 나는 경우 예외처리 하기 
    """
    if select and not has_headers:
        raise RuntimeError("select requires column headers")

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

        # enumerate객체는 튜플로 리턴하는데
        # 앞에 원소가 인덱스
        for idx, row in enumerate(rows):
            if not row:
                continue
            if col_idx:
                row = [row[idx] for idx in col_idx]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {idx} : Couldn't convert {row}")
                        print(f"Row {idx} : {e}")

            if not has_headers:  #헤더가 없으면 튜플로 변환
                records.append(tuple(row))
            else:
                record = dict(zip(headers, row))
                records.append(record)
    return records