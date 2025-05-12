import streamlit as st

st.title("객관식 퀴즈")

# 문제
st.subheader("Q. 대한민국의 수도는 어디일까요?")

# 선택지
options = ["부산", "서울", "대전", "광주"]

# 선택지 라디오 버튼
answer = st.radio("선택하세요:", options)

# 정답 체크 버튼
if st.button("정답 확인"):
    if answer == "서울":
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸습니다 😢 다시 도전해보세요!")

