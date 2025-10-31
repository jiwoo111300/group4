import streamlit as st

# ====== 스타일 (배경색 + 글자색) ======
st.markdown(
    """
    <style>
    .stApp {
        background-color: #d4f4ff;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====== 제목 ======
st.title("📘 유리함수 중단원 마무리")
st.write("유리함수의 개념을 정리하고 문제를 풀며 마무리해 봅시다!")

# ====== 문제 데이터 ======
problems = [
    {"num": 1, "question": "함수 y = 1/x 의 정의역은?", "answer": "x ≠ 0", "level": "하"},
    {"num": 2, "question": "함수 y = 2/x 에서 x=1일 때 y의 값은?", "answer": "2", "level": "하"},
    {"num": 3, "question": "함수 y = 1/(x-1)의 정의역은?", "answer": "x ≠ 1", "level": "하"},
    {"num": 4, "question": "함수 y = -3/x 의 그래프는 어느 사분면에 대칭인가?", "answer": "원점", "level": "하"},
    {"num": 5, "question": "함수 y = 2/(x+1)의 점근선은?", "answer": "x = -1, y = 0", "level": "중"},
    {"num": 6, "question": "y = 1/x 그래프를 y축 방향으로 2배 확대한 식은?", "answer": "y = 2/x", "level": "중"},
    {"num": 7, "question": "y = 1/x 그래프를 오른쪽으로 2만큼 평행이동한 식은?", "answer": "y = 1/(x-2)", "level": "중"},
    {"num": 8, "question": "y = 1/x 그래프를 위로 3만큼 평행이동한 식은?", "answer": "y = 1/x + 3", "level": "중"},
    {"num": 9, "question": "y = -1/x 의 그래프는 y = 1/x 그래프를 어떤 축 대칭한 것인가?", "answer": "x축", "level": "중"},
    {"num": 10, "question": "y = 3/(x-2) + 1 의 점근선을 구하시오.", "answer": "x = 2, y = 1", "level": "중"},
    {"num": 11, "question": "y = a/x 그래프가 (2,1)을 지난다면 a의 값은?", "answer": "2", "level": "중"},
    {"num": 12, "question": "y = 1/(x-1) + 2 그래프의 교점의 개수를 구하시오.", "answer": "1", "level": "중"},
    {"num": 13, "question": "y = 2/(x-3) - 1 그래프의 점근선의 교점을 구하시오.", "answer": "(3, -1)", "level": "상"},
    {"num": 14, "question": "y = k/x 그래프가 제2, 제4사분면에만 존재하려면 k의 부호는?", "answer": "음수", "level": "상"},
    {"num": 15, "question": "y = (x+2)/(x-1) 의 점근선을 구하시오.", "answer": "x = 1, y = 1", "level": "상"}
]

# ====== 문제 출력 ======
st.subheader("🧩 문제를 풀어보세요!")

for p in problems:
    st.markdown(f"**({p['level']}) 문제 {p['num']}. {p['question']}**")
    user_answer = st.text_input(f"문제 {p['num']}의 답을 입력하세요:", key=f"q{p['num']}")

    if user_answer:
        # 🔹 띄어쓰기 제거 후 비교
        clean_user = user_answer.replace(" ", "")
        clean_answer = p["answer"].replace(" ", "")
        
        if clean_user == clean_answer:
            st.success("🎉 너 쫌치네?")
        else:
            st.error("💪 중요한건 꺾이지 않는 마음. 다시 한번 해보자!")

st.write("---")
st.info("답 입력 시 띄어쓰기는 무시하고 채점됩니다.")
