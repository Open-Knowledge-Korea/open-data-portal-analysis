# [ 특수문자 개수 ]
# 행은 늘어나지 않으나 특정한 경우 열로 늘어남 ( 빈도 적음 ).
import csv
import re

input_fileName = "C:/광복절/표준데이터/표준데이터/원본/파일명나열.csv" #원본파일
output_fileName = "C:/추가작업/코드작업/특수문자/표준파일_특수문자_개수.csv" #출력파일

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
        result=len(result)
        out_list.append([buf,result])
        buf = ''
    else:
        line = line.strip(' \n')
        search_target=line
        result=re.findall(regex,search_target)
        result=len(result)
        out_list.append([line,result])
f.close()

of = open(output_fileName, 'w')
for each in out_list:
    print(each[0]+','+str(each[1]), file=of)
of.close()
