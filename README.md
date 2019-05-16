# KOREA NEIS APIs   
나이스 대국민서비스 API # 대한민국 초 · 중 · 고 관련 데이터 API  
나이스 대국민서비스(학생 / 학부모)에서 제공하는 데이터와 학교와 학생에게 필요한 데이터를 간단하게 Restful API와 라이브러리 형태로 제공합니다.

## 환경 셋업
Python 3.6 이상
###### Windows CMD / Powershell
```shell
pip install beautifulsoup4 requests urllib3 urllib5
```

###### Linux Shell
```shell
pip install beautifulsoup4, requests, urllib3, urllib5
```

###### 개별 설치
```shell
pip install beautifulsoup4
pip install requests
pip install urllib3
pip install urllib5
```

## 라이브러리 사용 예시
###### 일정 API @ 1개월
```python
from neisapis import NeisApisCore
from pprint import pprint # pprint

Neis = NeisApisCore("서울", "고등학교", "B000000000")
MonthTODO = Neis.MonthCalender("5") # 개월

pprint(MonthTODO)
```

###### 일정 API @ 1학기
```python
from neisapis import NeisApisCore
from pprint import pprint # pprint

Neis = NeisApisCore("서울", "고등학교", "B000000000")
SemesterTODO = Neis.SemesterCalender("1") # 학기

pprint(SemesterTODO)
```
#### 기능 상세
```python
class NeisApisCore(object)
```
*__ __init__ __(self, EduOffice, SchoolType, SchoolCode)*  

[EduOffice · 지역 교육청]() 예) '서울'
[SchoolType · 교육기관 종류]() 예) '4'
[SchoolCode · 학교 코드]() 예) 'B000000000'
