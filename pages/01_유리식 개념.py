import streamlit as st
import sympy as sp

# -----------------------------
# 📘 페이지 설정
# -----------------------------
st.set_page_config(page_title="유리식의 개념 학습", page_icon="📘")

# ✅ 배경색 적용 (#d4f4ff)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #d4f4ff;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("📘 유리식의 개념과 계산법")
st.write("이 페이지에서는 **유리식의 뜻**, **성질**, **사칙연산 방법**을 배우고 직접 계산해볼 수 있습니다.")

# -----------------------------
# 🧠 1. 유리식의 뜻
# -----------------------------
st.header("1️⃣ 유리식이란?")
st.markdown("""
**유리식**이란, **다항식이 나눗셈(분수)** 형태로 되어 있는 식을 말합니다.  
즉, 분모와 분자가 모두 다항식으로 이루어진 식입니다.  

예를 들어,

- \\( \\frac{1}{x} \\)
- \\( \\frac{x+1}{x-2} \\)
- \\( \\frac{2x^2 - 3}{x^2 + 1} \\)

모두 유리식입니다.

> **유리식 = 다항식 ÷ 다항식**
""")

st.info("📍 분모가 0이 되면 식의 값이 정의되지 않아요!")

# -----------------------------
# ⚖️ 2. 유리식의 성질
# -----------------------------
st.header("2️⃣ 유리식의 성질")
st.markdown("""
- **분모 ≠ 0** 이어야 합니다.  
- **분자와 분모에 같은 인수가 있을 경우 약분할 수 있습니다.**  
- 유리식은 **대입 가능한 값의 범위(정의역)** 에서만 계산이 가능합니다.  
- 사칙연산(＋, −, ×, ÷) 시에는 **공통 분모**나 **약분**을 잘 해야 합니다.
""")

# -----------------------------
# ➕ 3. 유리식의 사칙연산 학습
# -----------------------------
st.header("3️⃣ 유리식의 사칙연산 연습")

st.markdown("""
아래 입력창에 두 유리식을 입력하고, 사칙연산 결과를 확인해보세요.  
예시:  
- 유리식1: `(x + 1)/(x - 2)`  
- 유리식2: `(x - 3)/(x + 2)`
""")

expr1 = st.text_input("유리식 1", "(x + 1)/(x - 2)")
expr2 = st.text_input("유리식 2", "(x - 3)/(x + 2)")

x = sp.Symbol("x")

try:
    f1 = sp.sympify(expr1)
    f2 = sp.sympify(expr2)

    st.subheader("🧮 계산 결과")
    add = sp.simplify(f1 + f2)
    sub = sp.simplify(f1 - f2)
    mul = sp.simplify(f1 * f2)
    div = sp.simplify(f1 / f2)

    st.latex(rf"({sp.latex(f1)}) + ({sp.latex(f2)}) = {sp.latex(add)}")
    st.latex(rf"({sp.latex(f1)}) - ({sp.latex(f2)}) = {sp.latex(sub)}")
    st.latex(rf"({sp.latex(f1)}) \times ({sp.latex(f2)}) = {sp.latex(mul)}")
    st.latex(rf"({sp.latex(f1)}) \div ({sp.latex(f2)}) = {sp.latex(div)}")

    st.success("✅ 계산 완료! 유리식의 사칙연산 결과를 위에서 확인하세요.")

except Exception:
    st.error("❌ 식을 해석할 수 없습니다. 올바른 형태로 입력해주세요 (예: (x+1)/(x-2)).")

# -----------------------------
# ✨ 정리
# -----------------------------
st.header("4️⃣ 정리")
st.markdown("""
| 연산 | 방법 | 예시 |
|:--|:--|:--|
| 덧셈/뺄셈 | 공통 분모로 통분 후 계산 | \\( \\frac{1}{x} + \\frac{1}{x+1} = \\frac{2x+1}{x(x+1)} \\) |
| 곱셈 | 분자끼리, 분모끼리 곱하기 | \\( \\frac{1}{x} \\times \\frac{x+2}{x} = \\frac{x+2}{x^2} \\) |
| 나눗셈 | 두 번째 분수를 뒤집어 곱하기 | \\( \\frac{1}{x} ÷ \\frac{x+1}{x} = \\frac{1}{x+1} \\) |
""")
