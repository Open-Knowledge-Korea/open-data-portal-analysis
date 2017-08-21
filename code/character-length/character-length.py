# [ 글자 길이 세기 ]
# 행은 늘어나지 않으나 특정한 경우 열로 늘어남 ( 빈도 적음 ).

input_fileName = "./character-length.csv" #원본파일
output_fileName = "./standard-character-length.csv" #출력파일

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
