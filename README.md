# Korea School APIs 
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

## 라이브러리 사용 가이드
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
[EduOffice · 지역 교육청](#지역-교육청) 예) '서울'  
[SchoolType · 교육기관 종류](#교육기관-종류) 예) '4'  
[SchoolCode · 학교 코드](#학교-코드) 예) 'B000000000'  

```python
def MonthCalender(self, Month)
```
*__MonthCalender__(self, Month)*  
Month 예) '1'  
1월 ~ 12월 사이의 값 입력

```python
def SemesterCalender(self, Semester)
```
*__SemesterCalender__(self, Semester)*  
Semester 예) '1'  
1학기 / 2학기 중 하나 입력

## Restful API 가이드
https://apis.haruhuey.kr/open/schoolapis?reqdata=[요청데이터]&code=[학교코드]&returntype=[JSON/XML/HTML]  
준비중

## 세부 정보

#### 지역 교육청
| 이름 | 데이터 값 |
|------|:---------:|
| 서울 | sen.go.kr |
| 부산 | pen.go.kr |
| 대구 | dge.go.kr |
| 인천 | ice.go.kr |
| 광주 | gen.go.kr |
| 대전 | dje.go.kr |
| 울산 | use.go.kr |
| 세종 | sje.go.kr |
| 경기 | goe.go.kr |
| 강원 | kwe.go.kr |
| 충북 | cbe.go.kr |
| 충남 | cne.go.kr |
| 전북 | jbe.go.kr |
| 전남 | jne.go.kr |
| 경북 | gbe.go.kr |
| 경남 | gne.go.kr |
| 제주 | jje.go.kr |

#### 교육기관 종류
| 이름 | 데이터 값 |
|------------|:-:|
| 병설유치원 | 1 |
| 초등학교   | 2 |
| 중학교     | 3 |
| 고등학교   | 4 |

#### 접속 주소
| 이름 | 데이터 값 |
|----------------|:--------------------:|
| MonthCalender | /sts_sci_sf01_001.do |
| SemesterCalender | /sts_sci_sf00_001.do |

*자동으로 URL이 완성되며 접속 주소는 참고 용입니다.*

#### 학교 코드
학교 코드는 'B000000000' 형식에 10자리로 이루어진 코드입니다.

## 변경 사항
1.0 - NeisApisCore와 Month/Semester 일정 조회 추가

## 라이브러리 프로젝트 참가하기
API에 오류 혹은 기능 추가를 요청해주세요.  
오류는 이슈 등록 또는 수정 후 PR을 진행부탁드리며, 
기능 추가에 관해서는 kkh555999@naver.com 으로 내용을 보내주세요!

## 라이센스
이 라이브러리는 [Apache License 2.0](https://github.com/HaruHuey/Korea-Neis-Apis/blob/master/LICENSE)를 따라 자유롭게 이용하실 수 있습니다.