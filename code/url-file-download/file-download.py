#  2017-08-17-강원대학교 글로벌비즈니스학과 김도훈

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
