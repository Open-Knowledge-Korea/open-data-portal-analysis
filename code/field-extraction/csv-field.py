# [ 다운받은 폴더에서 확장자가 CSV 인 파일들에 대해 파일명과 필드 추출후 새 CSV 파일 작성 ] - CSV 파일준비

# *** 코드를 다운로드 파일들이 있는 폴더안에서 실행***

import csv
import glob
import os
lst=[]
files=glob.glob('C:/*.csv') # 유형이 '.csv' 인 파일
with open('C:/','w',encoding='cp949',newline='') as testfile: #새로운 csv 파일 생성
    csv_writer=csv.writer(testfile)
    for file in files:
        try:
            with open(file,'r') as infile:
                file=file[file.rfind('\\')+1:]
                reader=csv.reader(infile)
                headers=next(reader) 
                headers=[str for str in headers if str]
                while len(headers) < 3 : # 받아온 행의 열이 3개 이하일 경우 필드명이 아니라고 가정. 다음 행 읽어오기
                    headers=next(reader) 
                    headers=[str for str in headers if str]
                lst=[file]+headers
                csv_writer.writerow(lst)
        except:
            with open(file,'r',encoding='utf8') as infile: # 인코딩이 utf8로 된 파일의 경우
                file=file[file.rfind('\\')+1:]
                reader=csv.reader(infile)
                headers=next(reader)
                headers=[str for str in headers if str]
                headers[0] = headers[0].strip('\ufeff')
                while len(headers) < 3 :
                    headers=next(reader) 
                    headers=[str for str in headers if str]
                lst=[file]+headers 
                csv_writer.writerow(lst)
