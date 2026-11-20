import streamlit as st

st.set_page_config(
    page_title="C Calculator",
    page_icon="🧮",
)

st.title("🧮 Calculator")
st.write("Enter two numbers and choose an operation.")

if "history" not in st.session_state:
    st.session_state.history = []

with st.form("calculator"):
    col1, col2 = st.columns(2)

    with col1:
        first = st.number_input("First number", value=0.0, format="%.10g")

    with col2:
        second = st.number_input("Second number", value=0.0, format="%.10g")

    operation = st.selectbox(
        "Operation",
        ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
    )

    calculate = st.form_submit_button("Calculate")

if calculate:
    symbol = operation[-2]

    try:
        if symbol == "+":
            result = first + second
        elif symbol == "-":
            result = first - second
        elif symbol == "*":
            result = first * second
        elif symbol == "/":
            if second == 0:
                raise ZeroDivisionError
            result = first / second
    except ZeroDivisionError:
        st.error("Division by zero is not allowed.")
    else:
        formatted_result = f"{result:.10g}"

        st.success(f"{first:.10g} {symbol} {second:.10g} = **{formatted_result}**")

        st.session_state.history.insert(
            0,
            f"{first:.10g} {symbol} {second:.10g} = {formatted_result}",
        )

if st.session_state.history:
    st.divider()
    st.subheader("History")

    for entry in st.session_state.history[:10]:
        st.write(entry)

    if st.button("Clear history"):
        st.session_state.history.clear()
        st.rerun()