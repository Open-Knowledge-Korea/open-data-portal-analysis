#  2017-08-17-강원대학교 글로벌비즈니스학과 김도훈

# ----------------------------------{ 파일 준비 단계 }----------------------------------------------

# [ Module 불러오기 ]

import glob
import cgi
import requests
import csv
import re
import itertools

# [ URL이 기록된 csv를 읽어들여 다운로드 진행 ]


SAVE_DIR = 'C:/' # 저장 위치

def downloadURLResource(url): # URL 에서 파일 다운받는 함수 정의
    r = requests.get(url.rstrip(), stream=True)
    if r.status_code == 200:
        content_disposition = r.headers.get('content-disposition')
        if content_disposition is not None:
            targetFileName = requests.utils.unquote(cgi.parse_header(content_disposition)[1]['filename'])
            with open("{}/{}".format(SAVE_DIR, targetFileName), 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            return targetFileName
        else: # 에러가 났을 경우 기록
            print('url {} had no content-disposition header'.format(url)) # content dispostion이 없는 경우
    elif r.status_code == 404:
        print('{} returned a 404, no file was downloaded'.format(url)) # r-status 코드가 404 인 경우
    else:
        print('something else went wrong with {}'.format(url)) # 기타 에러가 난 경우
        
with open('C:/') as f: # URL만 기록된 CSV 파일
    failItems = filter(lambda i:i[1] == False, {url.rstrip():downloadURLResource(url.rstrip()) for url in f.readlines()}.items())
    list(map(print, failItems))

 
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

# 필드명 일렬 나열시키는 excel 매크로 ( 필드 분석 시 필드 나열 파일 작성용,*** excel 에서 사용 *** )

#Sub TableToColumn()
    #Dim Rng As Range, LR As Long, i As Long
    #LR = Range("B" & Rows.Count).End(xlUp).Row # B = 시작 열
    #For i = 2 To LR
        #Set Rng = Range("B" & i, "E" & i)  # B / E 대신 <- 시작/종료열 
        #Range("A" & Rows.Count).End(xlUp)(2).Resize(Rng.Count) = Application.WorksheetFunction.Transpose(Rng) # A <- 작성열
    #Next i
#End Sub

# [ Open API 데이터 정리 ] - 행마다 API 명이 반복되고 항목명만 다른 행들을 API 명 당 하나의 행으로 (API명+항목명) 정리  

with open('C:/','w',encoding='cp949',newline='') as testfile:
    csv_writer=csv.writer(testfile)
    with open('C:/', 'r') as f:
        reader = csv.reader(f)
        for key, group in itertools.groupby(reader, lambda i:i[0]):
            lst=([key]+list(map(lambda i:i[1], group)))
            csv_writer.writerow(lst)

# ----------------------------------{ 파일/필드 빈도 분석 단계 }----------------------------------------------

# [ 다운로드 완료된 CSV 파일에 대한 필드 수 기록 - 저장된 폴더에서 읽어오기 ]

files=glob.glob('C:/') #원본파일
with open('C:/','w',encoding='cp949',newline='') as testfile: #작성파일
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

# [ 파일명과 필드 추출된 새 CSV 파일에서 필드 수 기록 ]

file1 = ('C:/') # 읽을 파일
file2 = ('C:/') # 작성 파일
with open(file1, 'r') as f1, open(file2, 'w', encoding='cp949', newline='') as f2:
    csv_reader = csv.reader(f1)
    csv_writer = csv.writer(f2)
    for row in csv_reader:
        x=[x for x in row if x]
        csv_writer.writerow([len(x)-1]) #파일명은 빼고 필드수만 기록하기 위해 -1

# 사용 권장하지 않음
# [ 글자 길이 (Space 제외 글자만 카운팅 가능) ]
# * 파일 내의 하나의 셀에서 엔터로 줄이 구분되었을 경우, 새 파일에서 두개의 행으로 읽음 * / 표준 데이터에만 사용 가능

def count_letters(word): # 글자 수를 세는 함수.
    BAD_LETTERS=[""," ","\n","   ","    ","    ","     " ] # 제외할 글자를 명시
    return len([letter for letter in word if letter not in BAD_LETTERS])

file = "C:/" #원본파일
with open("C:/",'w',encoding='cp949',newline='') as testfile: #작성파일
    csv_writer=csv.writer(testfile)
    with open(file,'r') as fi:
            for each in fi:
                file=each
                linecount=count_letters(file)
                lst=[file]+[linecount]
                csv_writer.writerow(lst)

# 사용 권장하지 않음
# [ 띄어쓰기 길이 ]
# * 파일 내의 하나의 셀에서 엔터로 줄이 구분되었을 경우, 새 파일에서 두개의 행으로 읽음 * / 표준 데이터에만 사용 가능

file = "C:/" #원본파일
with open("C:/",'w',encoding='cp949',newline='') as testfile: #작성파일
    csv_writer=csv.writer(testfile)
    with open(file,'r') as fi:
            for line in fi:
                file=line
                linecount=line.count(' ')
                lst=[file]+[linecount]
                csv_writer.writerow(lst)

# 사용 권장하지 않음
# [ 필드명/파일명 내 특수문자 기록 ( 특수문자 Yes/No , 개수, Yes 시 특수문자 나열 ) ]
# * 파일 내의 하나의 셀에서 엔터로 줄이 구분되었을 경우, 새 파일에서 두개의 행으로 읽음 * / 표준 데이터에만 사용 가능

regex = "[^가-힣a-zA-Z0-9\n ]" # " " 를 제외한 모든 문자를 특수문자로 취급함.
list1=[]
file="C:/"
with open("C:/",'w',encoding='cp949',newline='') as testfile: #작성파일
    csv_writer=csv.writer(testfile)
    with open(file,'r') as fi:
            for line in fi:
                search_target = line
                result=re.findall(regex,search_target)
                if result != []:
                    list1=[line]+['Yes']+[len(result)]+result
                else :
                    list1=[line]+['No']+[len(result)]
                csv_writer.writerow(list1)

# [ 글자 길이 세기 ]
# 행은 늘어나지 않으나 특정한 경우 열로 늘어남 ( 빈도 적음 ).

input_fileName = "C:/" #원본파일
output_fileName = "C:/" #출력파일

f = open(input_fileName, 'r')
out_list = []
buf = ''
flg = 0
for line in f:
    if line.count('"')%2 == 1:
        if flg == 0: flg = 1
        else: flg = 0
    if flg == 1: buf += line.strip(' \n')
    elif flg == 0 and len(buf) > 0:
        buf += line.strip(' \n')
        buf = buf.strip(' "')
        out_list.append([buf,len(buf)])
        buf = ''
    else:
        line = line.strip(' \n')
        out_list.append([line,len(line)])
f.close()

of = open(output_fileName, 'w')
for each in out_list:
    print(each[0]+','+str(each[1]), file=of)
of.close()

# [ 띄어쓰기 길이 ]
# 행은 늘어나지 않으나 특정한 경우 열로 늘어남 ( 빈도 적음 ).

input_fileName = "C:/" #원본파일
output_fileName = "C:/" #출력파일

f = open(input_fileName, 'r')
out_list = []
buf = ' '
flg = 0
for line in f:
    if line.count('"')%2 == 1:
        if flg == 0: flg = 1
        else: flg = 0
    if flg == 1: buf += line.strip(' \n')
    elif flg == 0 and len(buf) > 0:
        buf += line.strip(' \n')
        buf = buf.strip(' "')
        result=buf.count(' ')
        out_list.append([buf,result])
        buf = ''
    else:
        line = line.strip(' \n')
        result=line.count(' ')
        out_list.append([line,result])
f.close()

of = open(output_fileName, 'w')
for each in out_list:
    print(each[0]+','+str(each[1]), file=of)
of.close()


# [ 특수문자 여부 ]
# 행은 늘어나지 않으나 특정한 경우 열로 늘어남 ( 빈도 적음 ).

input_fileName = "C:/" #원본파일
output_fileName = "C:/" #출력파일

regex = "[^가-힣a-zA-Z0-9\n ]"

f = open(input_fileName, 'r')
out_list = []
buf = ' '
flg = 0
for line in f:
    if line.count('"')%2 == 1:
        if flg == 0: flg = 1
        else: flg = 0
    if flg == 1: buf += line.strip(' \n')
    elif flg == 0 and len(buf) > 0:
        buf += line.strip(' \n')
        buf = buf.strip(' "')
        search_target=buf
        result=re.findall(regex,search_target)
        if result !=[]:
            result='Yes'
        else:
            result='No'
        out_list.append([buf,result])
        buf = ''
    else:
        line = line.strip(' \n')
        search_target=line
        result=re.findall(regex,search_target)
        if result !=[]:
            result='Yes'
        else:
            result='No'
        out_list.append([line,result])
f.close()

of = open(output_fileName, 'w')
for each in out_list:
    print(each[0]+','+str(each[1]), file=of)
of.close()

# elif 부분 아래 코드로 대체시 특수문자 개수 세기

elif flg == 0 and len(buf) > 0:
        buf += line.strip(' \n')
        buf = buf.strip(' "')
        search_target=buf
        result=re.findall(regex,search_target)
        result=len(result)
        out_list.append([buf,result])
        buf = ''
    else:
        line = line.strip(' \n')
        search_target=line
        result=re.findall(regex,search_target)
        result=len(result)
        out_list.append([line,result])
