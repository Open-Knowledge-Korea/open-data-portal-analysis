# [ 파일명과 필드 추출된 새 CSV 파일에서 필드 수 기록 ]

file1 = ('C:/') # 읽을 파일
file2 = ('C:/') # 작성 파일
with open(file1, 'r') as f1, open(file2, 'w', encoding='cp949', newline='') as f2:
    csv_reader = csv.reader(f1)
    csv_writer = csv.writer(f2)
    for row in csv_reader:
        x=[x for x in row if x]
        csv_writer.writerow([len(x)-1]) #파일명은 빼고 필드수만 기록하기 위해 -1
