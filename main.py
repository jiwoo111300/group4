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
st.write("함수의 기본 개념을 확장해 탄생한 **유리함수**의 이야기를 알아보고, 문제를 풀며 마무리해 봅시다!")

# ====== 📖 유리함수의 유래와 발전 ======
st.header("📖 유리함수의 등장 배경")

st.markdown("""
**유리함수**(Rational Function)는 분수 형태의 함수를 말합니다.  
즉,  
\[
f(x) = \frac{P(x)}{Q(x)} \quad (단,\; Q(x) ≠ 0)
\]  
처럼 **두 다항식의 비**로 이루어진 함수를 유리함수라고 부릅니다.

---

### 🏛️ 등장 시기
유리함수의 개념은 **17세기 후반~18세기 초**에 본격적으로 정리되었습니다.  
이 시기에는 수학자들이 **함수(function)**라는 개념 자체를 처음으로 명확하게 정의하기 시작했죠.  
특히, **르네 데카르트(René Descartes)**가 도입한 **좌표평면**과  
**아이작 뉴턴(Isaac Newton)**, **고트프리트 라이프니츠(G. W. Leibniz)**의  
**미적분 발달**이 유리함수 연구의 토대가 되었습니다.

---

### 🔍 등장 배경
초기에는 단순히 “두 수의 비”로 표현되는 관계를 다루다가,  
이후 “두 **다항식(polynomial)**의 비율”로 개념이 확장되었습니다.  
이유는 다음과 같습니다:

1. 다항식으로는 표현할 수 없는 복잡한 관계(예: 속도, 전류, 압력 등)를 다루기 위해  
2. 미적분과 그래프를 통해 함수의 극한값과 연속성을 이해하기 위해  
3. 실생활의 물리 현상 중 ‘나눗셈 형태’로 표현되는 관계(예: 반비례 관계)를 수학적으로 다루기 위해  

이러한 필요성 속에서 “나누는 형태의 함수”가 자연스럽게 등장했고,  
그것이 바로 유리함수입니다.

---

### 📈 발전 과정
이후 18세기~19세기에 들어서면서 유리함수는 **그래프 분석과 극한 개념**을 통해 급속히 발전했습니다.  
- **점근선(asymptote)** 개념이 등장하면서,  
  분모가 0이 되는 지점에서 함수가 어떻게 발산하는지를 설명할 수 있게 되었고  
- **좌표평면 상의 대칭과 이동**을 통해 다양한 형태의 그래프를 이해하게 되었습니다.  

지금 배우는 \( y = \frac{1}{x} \)나 \( y = \frac{a}{x - b} + c \) 같은 식들이  
이 시기에 체계적으로 정리된 대표적인 유리함수입니다.
""")

st.divider()

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
st.header("🧩 중단원 마무리 문제")

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
