import streamlit as st
st.header("Students Records Management")
st.title("Welcome to the student Application system")
st.subheader("Manage student records efficiently and effectively")
st.markdown("------------------------------")
st.text("This application allows you to perform crud operations on student records")
st.write("Hello Streamlit")
st.write(123)
st.write([1,2,3])
st.write({"name":"sree","age":20})
st.markdown("*SREE*")
st.markdown("**tekworks**")
st.markdown("- Item 1\n- Item 2")
st.markdown("### Features of Application")
st.markdown("<h3 style='color:red'>HELLO</h3>",unsafe_allow_html=True)
st.caption("This is a Application from students")
st.divider()
st.code("""
        def add(a,b):
        return a+b
          """,language="python")
st.divider()
st.latex(r'''
         a^2 + b^2 = c^2
         ''')
st.divider()
if st.button("Click me"):
    st.write("Button clicked !")
    st.success("Operation Successfull!!!")
    st.balloons()
else:
    st.write("Button not clicked yet")
    st.error("Connection error!")
st.divider()
name=st.text_input("Enter your name:")
st.write(f"Hello {name}!")
if name=="":
    st.warning("Name cannot me Empty !")
elif not name.isalpha():
    st.error("Invalid input please enter only alphabets")
else:
    st.success(f"Welcome!!!{name}")
st.divider()
feedback=st.text_area("enter your feedback")
st.write(feedback)
st.divider()
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thankyou for agreeing")
st.divider()
gender=st.radio("Select your gender:",("Male","Female","Other"))
st.write(f"You selected : {gender}")
st.divider()
country=st.selectbox("Select your country:",["India","Dubai","America"])
st.write(f"you selected :{country}")
st.divider()
skills=st.multiselect("slectskills",["python","sql","java"])
st.write("skills:",skills)
st.divider()
age=st.slider("select your age :",0,100,25)
st.write(f"You are  {age}  years old")
st.divider()
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
    st.success("File uploaded Successfully!")
    st.write(f"Filename: {uploaded_file.name}")
st.divider()
with st.form("my_form"):
    name=st.text_input("Name")
    age=st.number_input("Age",0,100)
    submit=st.form_submit_button("Submit")
if submit:
    st.write(name,age)
st.divider()
with st.form("login"):
    user=st.text_input("username")
    pwd=st.text_input("password",type="password")
    login=st.form_submit_button("login")
if login:
    st.success("Login Successfull !")
st.divider()
col1,col2,col3 = st.columns(3)
with col1:
    st.header("column 1")
    st.write("this is column 1")
with col2:
    st.header("column 2")
    st.write("this is column 2")
with col3:
    st.header("column 3")
    st.write("this is column 3")
st.divider()
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Choose page",
["Home", "About", "Contact"])
st.sidebar.write(f"You selected: {option}")
st.divider()
container=st.container()
container.button("Click")
data = {'Name': ['Anurag', 'Sumit', 'Rohit'],'Age': [21, 22, 20],'Course': ['B.Tech', 'M.Tech', 'BBA']}
st.table(data)
st.divider()
@st.cache_data
def load_data():
    return [1,2,3,4,5]
data=load_data()
st.write(data)
