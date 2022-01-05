from datetime import datetime
from http import HTTPStatus

data = '2022-01-06 12:31:25'
data = '20220106 123125'
try:
    date = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    print (date)
except ValueError as ve: #올바르지 않은 형식일 경우 오류를 반환.
    print ({"error":"올바른 날짜 형식이 아닙니다."}, HTTPStatus.OK)