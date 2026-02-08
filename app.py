import streamlit as st
import re

st.set_page_config(page_title="AI Resume Builder")

st.title("AI Resume Builder with ATS Score")

# Inputs
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email")
role = st.text_input("Target Job Role")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience")
projects = st.text_area("Projects")

jd = st.text_area("Job Description")

# ---------- ATS Functions ----------

def get_keywords(text):
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    return set(words)


def calculate_ats(resume, jd, skills, role):

    score = 0
    explanation = []

    # 1. Skill Match (40 Marks)
    skill_list = [s.strip().lower() for s in skills.split(",")]
    matched_skills = [s for s in skill_list if s in jd.lower()]

    skill_score = min(len(matched_skills) * 10, 40)
    score += skill_score

    explanation.append(f"Skill Match: {skill_score}/40")

    # 2. Keyword Match (30 Marks)
    resume_words = get_keywords(resume)
    jd_words = get_keywords(jd)

    matched_words = resume_words.intersection(jd_words)

    keyword_score = min(len(matched_words), 30)
    score += keyword_score

    explanation.append(f"Keyword Match: {keyword_score}/30")

    # 3. Role Match (20 Marks)
    if role.lower() in jd.lower():
        score += 20
        explanation.append("Role Match: 20/20")
    else:
        explanation.append("Role Match: 0/20")

    # 4. Format Check (10 Marks)
    if len(resume) > 300:
        score += 10
        explanation.append("Format: 10/10")
    else:
        explanation.append("Format: 5/10")
        score += 5

    return score, explanation


# ---------- Button ----------

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

    # ATS Score
    if jd:

        ats_score, exp = calculate_ats(
            resume_text, jd, skills, role
        )

        st.subheader("ATS Score")

        st.success(f"Your ATS Score: {ats_score}/100")

        st.write("Explanation:")

        for e in exp:
            st.write("•", e)

    else:
        st.warning("Enter Job Description to get ATS score")
