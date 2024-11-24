import streamlit as st

# إعداد الصفحة
st.set_page_config(
    layout="wide",
    page_title="Introduction to Eliza and PhantomMeet",
    page_icon="🤖"
)

# عنوان الصفحة
st.title("🤖 Introduction to Eliza and PhantomMeet")

# تقسيم الصفحة إلى أقسام باستخدام أعمدة
st.header("Introduction to Eliza")
st.subheader("1. Who is Eliza?")
st.write("""
One of the first **_Neuro-Linguistic Programming (NLP)_** programs was developed in 1964 by **_Joseph Weizenbaum_**, 
a computer scientist at **_Massachusetts Institute of Technology (MIT)_**.  
The program is designed to conduct conversations with humans in a way that makes you feel as if you are talking to a human being and not a machine, and it simulates the style of a psychiatrist.
""")

# ماذا تفعل إليزا؟
st.subheader("2. What does she do?")
st.write("""
1. **Simulates a Conversation**: ELIZA creates the illusion of a conversation with a human. Though it doesn't truly understand the meaning behind the words.  
2. **Imitates a Psychotherapist**: The most famous script for ELIZA is called the **_"DOCTOR" script_**, where ELIZA simulates the role of a psychotherapist.  
3. **Pattern Matching and Substitution**: ELIZA doesn't understand the meaning of words or concepts but instead relies on pattern matching.
""")

# رابط المصدر
st.caption("📖 **Source:** [ACM Digital Library](https://dl.acm.org/doi/pdf/10.1145/365153.365168)")

# مقدمة عن برنامج PhantomMeet
st.markdown("---")
st.header("🎙️ Welcome to PhantomMeet")
st.subheader("1. What is PhantomMeet?")
st.write("""
PhantomMeet is a combination of two words:  
1. **_Phantom_**: You are not talking with a human, but it feels like you are.  
2. **_Meet_**: Refers to an interview or a meeting.
""")

st.subheader("2. What does PhantomMeet do?")
st.write("""
Designed for job interviews, PhantomMeet is an intelligent bot that assesses the person it interacts with, 
discovering their skills and experiences through structured questions.
""")

# زر تفاعلي
#if st.button("🤖 Start Exploring PhantomMeet"):
   # st.success("You are now ready to explore the world of PhantomMeet! 🚀")

# شريط جانبي
#st.sidebar.header("Options")
#page = st.sidebar.radio("Choose a section:", ["Introduction to Eliza and PhantomMeet", "Chat Page ", "Team Members"])
#if page == "Introduction to Eliza and PhantomMeet":
 #   st.sidebar.write("You are currently exploring Introduction to Eliza and PhantomMeet")
#elif page == "Chat Page":
 #   st.sidebar.write("")
#else:
#    st.sidebar.write("Learn more about this project!")

# نهاية الصفحة
st.markdown("---")
st.write("✨ **Thank you for exploring Our PhantomMeet!**")


