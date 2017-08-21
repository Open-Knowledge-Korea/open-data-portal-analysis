# [ 다운로드 완료된 CSV 파일에 대한 필드 수 기록 - 저장된 폴더에서 읽어오기 ]

import glob
import csv

files=glob.glob('C:/data12/*.csv') #원본파일
with open('C:/dk.csv','w',encoding='cp949',newline='') as testfile: #작성파일
    csv_writer=csv.writer(testfile)
    for file in files:
        try:
            with open(file,'r') as infile:
                file=file[file.rfind('\\')+1:]
                reader=csv.reader(infile)
                headers=next(reader) 
                headers=[str for str in headers if str] 
                while len(headers) < 3 :
                    headers=next(reader) 
                    headers=[str for str in headers if str]
                lst=[file]+[len(headers)]
                csv_writer.writerow(lst)
        except:
            with open(file,'r',encoding='utf8') as infile:
                file=file[file.rfind('\\')+1:]
                reader=csv.reader(infile)
                headers=next(reader)
                headers=[str for str in headers if str]
                headers[0] = headers[0].strip('\ufeff')
                while len(headers) < 3 :
                    headers=next(reader) 
                    headers=[str for str in headers if str]
                lst=[file]+[len(headers)]
                csv_writer.writerow(lst)
