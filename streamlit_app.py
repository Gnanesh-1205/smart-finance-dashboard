import streamlit as st

st.set_page_config(page_title="Smart Finance Dashboard ", layout="centered")

st.title("👋 Welcome to Your Smart Finance Dashboard ")

# Input Section
income = st.number_input("Enter your monthly income (in ₹):", min_value=0)
rent = st.number_input("Enter your monthly Rent expense (in ₹):", min_value=0)
food = st.number_input("Enter your monthly Food expense (in ₹):", min_value=0)
transport = st.number_input("Enter your monthly Transport expense (in ₹):", min_value=0)
subscriptions = st.number_input("Enter your monthly Subscriptions expense (in ₹):", min_value=0)
shopping = st.number_input("Enter your monthly Shopping expense (in ₹):", min_value=0)
others = st.number_input("Enter your monthly Others expense (in ₹):", min_value=0)

if st.button("Analyze"):
    total_expenses = rent + food + transport + subscriptions + shopping + others
    savings = income - total_expenses

    st.subheader("Summary:")
    st.write(f"**Total Income:** ₹{income}")
    st.write(f"**Total Expenses:** ₹{total_expenses}")
    st.write(f"**Savings:** ₹{savings}")

    st.subheader("Expense Breakdown by Category:")

    categories = {
        "Rent": rent,
        "Food": food,
        "Transport": transport,
        "Subscriptions": subscriptions,
        "Shopping": shopping,
        "Others": others
    }

    for category, amount in categories.items():
        percent = (amount / income * 100) if income > 0 else 0
        st.write(f"{category}: ₹{amount} ({percent:.2f}%)")
        if category == "Rent" and percent > 40:
            st.warning("⚠️ Your rent is above 40% of income. Try to reduce housing costs.")
        if category == "Food" and percent > 30:
            st.warning("⚠️ You're spending a lot on food. Try cooking more at home.")

    st.subheader("🧮 Your Financial Health Score:")
    if savings >= income * 0.2:
        st.success("🟢 Great! You're saving well.")
        score = 100
    elif savings >= 0:
        st.info("🟡 Okay, but could save more.")
        score = 60
    else:
        st.error("🔴 Warning! Your financial habits need serious attention.")
        score = 0
    st.write(f"Your Score: **{score} / 100**")
