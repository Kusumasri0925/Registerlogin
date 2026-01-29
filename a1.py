import pandas as pd
import pymysql
import streamlit as st
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Sree0925",
        database="Student_db"
    )
conn = get_connection()
cur = conn.cursor()
def register_user(username, password):
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password) )
        conn.commit()
        st.success("Registration successful")
    except:
        st.error("Username already exists")
st.title("Login & Registration System")


menu = st.selectbox("Select Option", ["Login", "Register"])
if menu == "Register":
    st.subheader("Register")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        if new_user and new_pass:
            register_user(new_user, new_pass)
        else:
            st.warning("Please fill all fields")