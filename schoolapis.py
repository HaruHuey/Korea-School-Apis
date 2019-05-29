# -*- coding: utf-8 -*-

"""
Korea School Apis
~~~~~~~~~~~~~~~

Python3 기반 NEIS 대국민서비스 · 학교 데이터 API 라이브러리

API Guide:

    >>> from schoolapis import SchoolApisCore
    >>> School = SchoolApisCore("서울", "고등학교", "B000000000")
    >>> MonthTODO = School.MonthCalender("5")
    >>> print(str(MonthTODO))
    [
        {'Schedule': '재량휴업일',
         'Today': '01',
         'WeekDay': '수',
         'Weeks': '1'
         },
        ···
        {'Schedule': '', 
        'Today': '31', 
        'WeekDay': '금', 
        'Weeks': '5'}
    ]

... or More Apis:

    >>> from schoolapis import SchoolApisCore
    >>> School = SchoolApisCore("서울", "고등학교", "B000000000")
    <schoolapis.SchoolApisCore object at 0x0000000000000000>

Copyright: (c) 2019 by HaruHuey(KiHyun Kim)

Source Code: https://github.com/HaruHuey/Korea-School-Apis

README: https://haruhuey.github.io/Korea-School-Apis/

License: Apache License 2.0

class SchoolApisCore
~~~~~~~~~~~~~~~~~~

초기 값 설정: 교육청 지역 · 교육기관 종류(정수) · 학교 코드

### def MonthCalender
Arguments: 월(정수)

### def SemesterCalender
Arguments: 학기(정수)
"""

import datetime
import urllib.request
import requests
from bs4 import BeautifulSoup

class SchoolApisCore(object):
    # 교육청 · 교육기관 종류 · 학교 코드
    def __init__(self, EduOffice, SchoolType, SchoolCode):
        # 지역 교육청
        EduOffice_List = {
            "서울": "sen.go.kr",
            "부산": "pen.go.kr",
            "대구": "dge.go.kr",
            "인천": "ice.go.kr",
            "광주": "gen.go.kr",
            "대전": "dje.go.kr",
            "울산": "use.go.kr",
            "세종": "sje.go.kr",
            "경기": "goe.go.kr",
            "강원": "kwe.go.kr",
            "충북": "cbe.go.kr",
            "충남": "cne.go.kr",
            "전북": "jbe.go.kr",
            "전남": "jne.go.kr",
            "경북": "gbe.go.kr",
            "경남": "gne.go.kr",
            "제주": "jje.go.kr",
        }

        # 교육기관 종류
        SchoolType_List = {
            "병설유치원": "1",
            "초등학교": "2",
            "중학교": "3",
            "고등학교": "4"
        }

        NeisPage_List = {
            "MonthCalender": "/sts_sci_sf01_001.do",
            "SemesterCalender": "/sts_sci_sf00_001.do"
        }

        # 사전 요일 생성 [7일:일 ~ 토]
        Day_List = ["일", "월", "화", "수", "목", "금", "토"]

        # 학교 코드
        self._SchoolCode = "?schulCode=" + SchoolCode
        # 기본 URL · ex) https://stu.[0:교육청]/
        self._BaseURL = "https://stu.{0}".format(EduOffice_List[EduOffice])
        # 교육청 교육기관 종류
        self._SchoolType = "&schulCrseScCode={0}&schulKndScCode={0}".format(SchoolType_List[SchoolType])
        # 년도
        self._Year = "&ay=" + datetime.datetime.now().strftime("%Y")
        # 요일 목록
        self._Day = Day_List
        # 사이트 주소
        self._NeisPage = NeisPage_List

    # 월 별 캘린더 조회 · 해당 월 입력 // Month 값이 없을 경우 현재 월 조회
    def MonthCalender(self, Month):
        if int(Month) in range(1, 9):
            Month = "&mm=" + "0" + Month

        else:
            pass

        setURL = self._BaseURL + self._NeisPage['MonthCalender'] + self._SchoolCode + self._SchoolType + self._Year + Month
        connectURL = urllib.request.urlopen(setURL, timeout=5)
        readURL = connectURL.read()

        soupData = BeautifulSoup(readURL, "html.parser")

        LV1_Data = soupData.find(id="contents")
        LV2_Data = LV1_Data.find_all("div")[2]
        LV3_Data = LV2_Data.find("table")
        LV4_Data = LV3_Data.find("tbody")
        Data = LV4_Data.find_all("tr")

        returnData = []
        WeeksCount = 1

        for line in Data:
            line_count = 0
            line = line.find_all("td")

            for day in line:
                day = day.find("div")
                if day.em.get_text().strip() != "":
                    emData = day.em.get_text().strip()
                    try:
                        aData = day.a.strong.get_text().strip()
                    except:
                        aData = ""

                    # Schedule · Today · WeekDay · Weeks
                    DayData = {}
                    DayData['Weeks'] = str(WeeksCount)
                    DayData['Today'] = emData
                    DayData['WeekDay'] = self._Day[line_count]
                    DayData['Schedule'] = aData

                    returnData.append(DayData)

                else:
                    pass

                line_count += 1
            WeeksCount += 1

        return returnData

    
    # 학기 별 캘린더 조회 · 해당 학기 입력 // Semester(학기) 값이 없을 경우 1학기 조회
    # *** 참고 ***
    # 1학기 : 3월 · 4월 · 5월 · 6월 · 7월 · 8월
    # 2학기 : 9월 · 10월 · 11월 · 12월 · 1월 · 2월
    def SemesterCalender(self, Semester):
        Semester = "&sem=" + Semester
        setURL = self._BaseURL + self._NeisPage['SemesterCalender'] + self._SchoolCode + self._SchoolType + self._Year + Semester
        connectURL = urllib.request.urlopen(setURL, timeout=5)
        readURL = connectURL.read()

        soupData = BeautifulSoup(readURL, "html.parser")

        LV1_Data = soupData.find(id="contents")
        LV2_Data = LV1_Data.find_all("div")[2]
        LV3_Data = LV2_Data.find("table")
        LV4_Data = LV3_Data.find("tbody")
        Data = LV4_Data.find_all("tr")

        returnData = [[], [], [], [], [], []]
        Weeks_count = [1, 1, 1, 1, 1, 1]
        noneDay = [False, False, False, False, False, False]

        for line in Data:
            Today = line.th.get_text().strip()
            exData = [{}, {}, {}, {}, {}, {}]
            line_td = line.find_all("td")
            Data_list = [line_td[i:i+2] for i in range(0, len(line_td), 2)]

            for index, (textC, textL) in enumerate(Data_list):
                if noneDay[index] == True:
                    continue

                refine_textC = textC.get_text().strip()

                if refine_textC == "":
                    noneDay[index] = True
                    continue

                refine_textL = ""
                if textL.a:
                    LV1_textL = textL.find_all("a")

                    for i, x in enumerate(LV1_textL):
                        LV1_textL[i] = x.span.get_text().strip()

                    refine_textL = ' · '.join(LV1_textL)

                if refine_textC == "월" and Today != "01":
                    Weeks_count[index] += 1

                exData[index]['Today'] = Today
                exData[index]['Schedule'] = refine_textL
                exData[index]['WeekDay'] = refine_textC
                exData[index]['Weeks'] = Weeks_count[index]

            for index, x in enumerate(exData):
                if x != {}:
                    returnData[index].append(x)

        return returnData