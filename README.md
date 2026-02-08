# 🚀 AI Resume Builder (ATS-Friendly)

An AI-powered web application that helps students generate professional, ATS-optimized resumes with real-time scoring and feedback.

---

## 📦 Project Overview

This project is designed to assist students in creating resumes that are compatible with Applicant Tracking Systems (ATS).  
It collects user information, generates structured resumes, evaluates them against job descriptions, and provides an ATS score with explanation.

### Key Highlights

🔹 Purpose  
To improve students' chances of getting shortlisted by creating optimized resumes.

🔹 Features  
- User-friendly resume input form  
- ATS-friendly resume generation  
- Automatic keyword extraction  
- Resume and Job Description matching  
- ATS score (0–100) with explanation  
- Clean and simple interface  

🔹 Technology Stack  
- Python  
- Streamlit  
- Regex-based text processing  
- Git & GitHub  

🔹 Working Mechanism  
1. User enters personal and professional details  
2. System analyzes skills and job description  
3. Keywords are extracted automatically  
4. ATS score is calculated  
5. Resume is generated in standard format  

🔹 ATS Scoring Criteria  

| Parameter     | Weight |
|---------------|---------|
| Skill Match   | 40%     |
| Keyword Match | 30%     |
| Role Match    | 20%     |
| Format Check  | 10%     |

🔹 Installation & Execution  

```bash
git clone https://github.com/mittalshriya/AI-Resume-Builder.git
cd AI-Resume-Builder
pip install streamlit openai python-docx reportlab
streamlit run app.py
🔹 Learning Outcomes

Python application development
Resume optimization logic
ATS analysis techniques
GitHub project management
System design fundamentals
