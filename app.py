import streamlit as st

name = st.text_input("Please enter the candidate's name")
role = st.text_input("Please enter the candidate's role")
date = st.text_input("Please enter date which you want the candidate to start his/her candidature")


st.write("""Dear """ + name + """,

Thank you for attending the 43nd NUSSU Student Life Project Director Recruitment. I appreciate you taking the time to consider us amongst the various student leadership opportunities in and out of NUS. On behalf of NUSSU Student Life cell, I am pleased to offer you a role in NUSSU Student Life 21/22!

**1) Appointment Offer**

After consulting with my fellow deputies, I am pleased to offer you the position of """+ role
+ """

**2) Acceptance of Appointment**

Please respond to this email with your acceptance, by """ + date+ """, with the following information to accept your appointment:

1. Please confirm that you have no pending disciplinary proceedings with the NUS Board of Discipline.

Thank you and I look forward to hearing from you!""")