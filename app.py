import streamlit as st

st.title("퀴즈")

st.subheader("광운대가 위치한 지역의 이름은 무엇일까요?")
options = ["노원", "창동", "신촌", "잠실"]
answer1 = st.radio("선택하세요:", options, key="q1")

st.subheader("Q2. 광운대의 설립자는 누구인가요?")
answer2 = st.text_input("정답을 입력하세요:", key="q2")

# 정답 확인 버튼
if st.button("정답 확인"):
    score = 0

    # Q1 정답 체크
    if answer1 == "노원":
        score += 1
        st.success("Q1 정답 ✅")
    else:
        st.error(f"Q1 오답 ❌ (정답: 노원)")

    # Q2 정답 체크
    if answer2.strip() == "조광운":
        score += 1
        st.success("Q2 정답 ✅")
    else:
        st.error(f"Q2 오답 ❌ (정답: 조광운운)")

    st.markdown(f"### 📊 총 점수: {score} / 2점")

