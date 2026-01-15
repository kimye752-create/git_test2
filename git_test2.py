import streamlit as st 
import numpy as np   # 숫자 계산해주는 역할
import pandas as pd  # 데이터프레임 다루는 역할, 엑셀 자료를 가장 잘 다루는 자료
from datetime import datetime as dt # 날짜와 시간 다루는 역할
import datetime

st.title("이것이 타이틀이다.")
st.header("이것이 헤더이다.")
st.subheader("이것이 서브헤더이다.") 
st.text("이것이 일반 텍스트이다.")
st.title("스마일 : 😊")
st.caption("캡션입니다.") # 그림에 대한 설명이 캡션
                        # 마크다운은 지피티가 잘 구성함.
st.markdown("**ㅎㅎ** _이탤릭체_ ~~취소선~~") # **2개는 굵게 *1개는 기울인체 ~~3개는 취소선~~   

# 코드 표시
sample_code = '''
def hello_world():
    print("Hello, World!")
'''

st.code(sample_code, language='python') # 샘플코드를 가져오고 이름은 파이썬이야.   

# 마크다운 문법 지원       # 앞에 콜론을 넣었음.
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 :blue[파란색] 볼드체를 설정할 수 있다.")

st.markdown("[sqrt{x^2 + y^2}=1] 와 같은 수식도 지원한다.")
st.markdown("[:green[$\sqrt{x^2 + y^2}=1$]] 와 같은 수식도 지원한다.")
st.latex(r"\sqrt{x^2 + y^2}=1")   # 화면 중간에 줄 내용 출력.



# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 차트 그리기 / 차트를 그리려면 데이터가 필요함.
st.title("데이터프레임 출력하기")
# dataframe 생성
dataframe = pd.DataFrame( # 클래스. 첫글자들이 대문자. 메소드로 가져온 것.
    {"first_column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
    })            # 이 데이터로 차트를 만들겠다.

# 데이터프레임 출력
st.dataframe(dataframe)   # 프레임은 sort도 알아서 됨. 오른쪽 왼쪽 정렬도 있음. 칸 조절도 마우스 드래그로 가능함.   

# 테이블 출력
st.table(dataframe)       # 프레임 수정이 안됨. 고정됨.


# 메트릭   # 유동적인 데이터 표시 함수
st.metric(label="온도", value="25 °C", delta="1.2 °C")   # delta는 변화량 표시.
st.metric(label="삼성전자", value="140,000 원", delta="+3,800 원")


# 칼럼을 나눠서 쓰려면 :  한개 줄에 3개의 데이터 표를 표시하려면
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="달러USD", value="1,471", delta="+30")
with col2:
    st.metric(label="유로EUR", value="1,602", delta="-12")  
with col3:
    st.metric(label="엔JPY", value="1,054", delta="+5")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 버튼을 만들기
button = st.button("핵 발사")  # 버튼을 누르면 True, 안누르면 False
if button:
    st.warning(":red[🚨 핵 발사! ! ! 🚨]")   # 경고창

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
agree = st.checkbox("체크박스를 눌러주세요")  # 체크박스
if agree:
    st.success("체크박스가 선택되었습니다.")   # 성공 메시지    

mbti = st.radio("당신의 MBTI는?", ("INTJ", "INFP", "ENTP", "ESFJ"), index=0)  # 라디오 버튼   # 인덱스 버튼 번호 줘서 기본 선택항 설정 가능.
st.write("당신의 MBTI는 ", mbti, "입니다.")

# 라디오 버튼

if mbti == "INTJ":
    st.info("INTJ는 전략가 유형입니다.")
elif mbti == "INFP":
    st.info("INFP는 중재자 유형입니다.")
elif mbti == "ENTP":
    st.info("ENTP는 발명가 유형입니다.")
else:
    st.info("ESFJ는 집정관 유형입니다.")


agree = st.radio("라디오 버튼을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))  # 라디오 버튼

# 셀렉트박스
favorite_color = st.selectbox("좋아하는 색상을 선택하세요",
                              ("빨강", "파랑", "초록", "노랑"))    

st.write("당신이 선택한 색상은 :red[{ favorite_color}]입니다")

# 멀티셀렉트박스
hobbies = st.multiselect("취미를 선택하세요", 
                            ("독서", "운동", "여행", "게임", "요리"))
st.write("당신의 취미는 :blue[{ hobbies}]입니다.")

#슬라이더    :   0부터 ~까지의 선 
age = st.slider("당신의 나이는?", 0, 120, 25)  # 최소값, 최대값, 기본값
st.write("당신의 나이는 :green[{age}]입니다.")

# 날짜 선택 위젯
start_time = st.slider(
    "언제 약속 잡을까요?",
    min_value=dt(2026, 1, 15, 12, 0),  # 기본값 설정, 연 월 일 시 분
    max_value=dt(2026, 12, 31, 23, 59),
    value=dt(2026, 1, 15, 0, 0),  # 기본값 설정
    step =datetime.timedelta(hours=1), # 시간 단위도 넣고 싶으면 hours=1, minutes=10 등으로 설정 가능
    format="YYYY-MM-DD HH:mm")  # 날짜 형식 지정


 # 텍스트 입력
title = st.text_input(
    label="가고 싶은 여행지가 있어요?",
    placeholder="예: 파리, 뉴욕, 런던, 하와이")  # 기본값 설정   # 정보 입력하는 란 안에 어떻게 입력하라고 예시 얕게 넣어주는 것
st.write(f"당신이 가고 싶은 여행지는 :green[{title}]입니다.")


# 숫자 선택 버튼 란
number = st.number_input(
    label="몇 명이서 여행가시나요?",
    min_value=1,
    max_value=100,
    value=2,  # 기본값 설정
    step=1)   # 증가 단위 설정
st.write(f"여행가는 인원은 :blue[{number}]명 입니다.")


# 파일 다운로드 버튼 :  먼저 데이터가 있어야 함.   # CSV 파일은 파일 크기를 줄여놓은 것. 공공포탈에서는 CSV 파일을 많이 씀.
st.download_button(
    label="CSV 파일 다운로드",                 #유니코드. 
    data=dataframe.to_csv(index=False).encode('utf-8'),  # 데이터프레임을 csv로 변환
    file_name='sample_data.csv',
    mime='text/csv'
)