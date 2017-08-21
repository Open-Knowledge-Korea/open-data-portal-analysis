# [ Open API 데이터 정리 ] - 행마다 API 명이 반복되고 항목명만 다른 행들을 API 명 당 하나의 행으로 (API명+항목명) 정리  

with open('C:/','w',encoding='cp949',newline='') as testfile:
    csv_writer=csv.writer(testfile)
    with open('C:/', 'r') as f:
        reader = csv.reader(f)
        for key, group in itertools.groupby(reader, lambda i:i[0]):
            lst=([key]+list(map(lambda i:i[1], group)))
            csv_writer.writerow(lst)
