import streamlit as st

if "acounts" not in st.session_state:
    st.session_state.acounts = {}

st.set_page_config(page_title="SMIT bank")

st.title("SMIT Bank")
st.markdown("Wellcome to SMIT bank")


action = st.selectbox("Select your choice: ", ["Account Open", "Check Balance", "Deposite", "withdraw"])


def account_open():
    with st.form(key = "account_form"):
        name = st.text_input("Acount Tittle: ") 
        pin = st.text_input("create a accout pin: pin must be 4 digit: ")
        submit_CA = st.form_submit_button("Create Account")

        if submit_CA:
            if pin in st.session_state.acounts:
                st.error("pin is already exist")
            else:
                st.session_state.acounts[pin] = {"name":name, "balance": 0}
                st.success("account is successfully created")


def check_balance():
    with st.form(key="check_balance_form"):
        pin = st.text_input("Enter your Pin")
        submit_CB = st.form_submit_button("Check Balance")

        if submit_CB:
            if pin in st.session_state.acounts:
                name = st.session_state.acounts[pin]["name"]
                balance = st.session_state.acounts[pin]["balance"]
                st.success(f"Acount title is {name}\nAccount balance is {balance}")
            else:
                st.error("Invalid Pin")

def deposite ():
    with st.form(key="deposite_form"):
        pin = st.text_input("Enter your Pin")
        amount = st.number_input("Enter your amount: ")
        submit_DB = st.form_submit_button("deposite Balance")

        if submit_DB:
            if pin in st.session_state.acounts:
                st.session_state.acounts[pin]["balance"] += amount
                st.success(f"Amount deposite successfully {amount}: ")
            else:
                st.error("Invalid Pin")

def withdraw():
    with st.form(key="withdraw_form"):
        pin = st.text_input("Enter your Pin")
        amount = st.number_input("Enter your amount: ")
        submit_WA = st.form_submit_button("withdraw amount")
        if submit_WA:
            if pin in st.session_state.acounts:
                if amount  <= st.session_state.acounts[pin]["balance"]:
                    st.session_state.acounts[pin]["balance"] -= amount
                    st.success(f"Amount withdraw successfully {amount}: ")
                else:
                    st.error(f"Insufficient amount {amount}: ")
            else:
                st.error("Invalid Pin")



if action == "Account Open":
    account_open()
elif action == "Check Balance":
    check_balance()
elif action == "Deposite":
    deposite()
elif action == "withdraw":
    withdraw()