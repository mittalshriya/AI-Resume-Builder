import streamlit as st

st.set_page_config(page_title="AI Resume Builder")

st.title("AI-Based Resume Builder")

# Input fields
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email")
role = st.text_input("Target Job Role")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience")
projects = st.text_area("Projects")

jd = st.text_area("Job Description (Optional)")

# Button
if st.button("Generate Resume"):

    resume_text = f"""
{name}
{phone} | {email}

ROLE: {role}

SKILLS:
{skills}

EDUCATION:
{education}

EXPERIENCE:
{experience}

PROJECTS:
{projects}
"""

    st.subheader("Generated Resume")
    st.text(resume_text)

    st.success("Resume Generated Successfully!")
