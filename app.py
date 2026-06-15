
import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Baby Pink Background */
.stApp {
    background-color: #F8C8DC;
}

/* Main Cards */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Section Titles */
.section-title {
    color: #D63384;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Button Styling */
.stButton > button {
    background-color: #FF69B4;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #DB7093;
    color: white;
}

/* Metrics */
div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1 style='text-align:center;
           color:#C71585;'>
🎀 Student Grade Calculator 🎀
</h1>

<h4 style='text-align:center;
           color:#8B008B;'>
Academic Performance Dashboard
</h4>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.header("🏫 School Information")

    school_name = st.text_input(
        "School Name",
        "ABC Public School"
    )

    attendance = st.slider(
        "Attendance %",
        0,
        100,
        85
    )

    photo = st.file_uploader(
        "Upload Student Photo",
        type=["png", "jpg", "jpeg"]
    )

# -----------------------------
# PERSONAL INFORMATION
# -----------------------------
st.markdown(
    "<h3 style='color:#C71585;'>👤 Student Personal Information</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")

with col2:
    student_class = st.text_input("Class")
    age = st.number_input("Age", 1, 30)

email = st.text_input("Email Address")

st.divider()

# -----------------------------
# MARKS DETAILS
# -----------------------------
st.markdown(
    "<h3 style='color:#C71585;'>📚 Academic Marks Details</h3>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    maths = st.number_input("Mathematics", 0, 100)
    science = st.number_input("Science", 0, 100)
    english = st.number_input("English", 0, 100)

with c2:
    computer = st.number_input("Computer", 0, 100)
    social = st.number_input("Social Studies", 0, 100)
    physics = st.number_input("Physics", 0, 100)

st.divider()

# -----------------------------
# GENERATE BUTTON
# -----------------------------
generate = st.button(
    "🚀 Generate Result"
)

# -----------------------------
# RESULT SECTION
# -----------------------------
if generate:

    marks_list = [
        maths,
        science,
        english,
        computer,
        social,
        physics
    ]

    total = sum(marks_list)
    percentage = total / 6

    # Grade Calculation
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
        grade_color = "green"

    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
        grade_color = "blue"

    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
        grade_color = "orange"

    elif percentage >= 60:
        grade = "C"
        remark = "Good"
        grade_color = "purple"

    elif percentage >= 50:
        grade = "D"
        remark = "Average"
        grade_color = "brown"

    else:
        grade = "F"
        remark = "Needs Improvement"
        grade_color = "red"

    # Pass / Fail
    if all(mark >= 35 for mark in marks_list):
        result = "PASS ✅"
    else:
        result = "FAIL ❌"

    st.success("Result Generated Successfully!")

    # -----------------------------
    # PHOTO DISPLAY
    # -----------------------------
    if photo:
        st.image(photo, width=180)

    # -----------------------------
    # REPORT CARD
    # -----------------------------
    st.subheader("📋 Student Report Card")

    st.write(f"**Name:** {name}")
    st.write(f"**Roll Number:** {roll_no}")
    st.write(f"**Class:** {student_class}")
    st.write(f"**Age:** {age}")
    st.write(f"**Email:** {email}")

    st.divider()

    # -----------------------------
    # METRICS
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📊 Total Marks", f"{total}/600")

    with col2:
        st.metric("📈 Percentage", f"{percentage:.2f}%")

    with col3:
        st.metric("🏆 Grade", grade)

    with col4:
        st.metric("📝 Attendance", f"{attendance}%")

    st.markdown(
        f"<h2 style='color:{grade_color};'>Grade : {grade}</h2>",
        unsafe_allow_html=True
    )

    st.write(f"### Result : {result}")
    st.write(f"### Remark : {remark}")

    # -----------------------------
    # PROGRESS BAR
    # -----------------------------
    st.subheader("Overall Performance")

    st.progress(int(percentage))

    # -----------------------------
    # SUBJECT TABLE
    # -----------------------------
    df = pd.DataFrame({
        "Subject": [
            "Mathematics",
            "Science",
            "English",
            "Computer",
            "Social Studies",
            "Physics"
        ],
        "Marks": [
            maths,
            science,
            english,
            computer,
            social,
            physics
        ]
    })

    st.subheader("📚 Subject-wise Marks")
    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # CHART
    # -----------------------------
    st.subheader("📈 Performance Analysis")

    st.bar_chart(
        df.set_index("Subject")
    )

    # -----------------------------
    # STATUS
    # -----------------------------
    st.subheader("🏅 Academic Status")

    if percentage >= 90:
        st.success("🌟 Eligible for School Topper List")

    elif percentage >= 75:
        st.info("🎉 Excellent Academic Performance")

    elif percentage >= 60:
        st.warning("📖 Good Performance - Can Improve Further")

    else:
        st.error("📚 Needs Additional Academic Support")

    # -----------------------------
    # DOWNLOAD REPORT
    # -----------------------------
    report = f"""
SCHOOL REPORT CARD

School Name: {school_name}

Student Name: {name}
Roll Number: {roll_no}
Class: {student_class}
Age: {age}
Email: {email}

Attendance: {attendance}%

Mathematics: {maths}
Science: {science}
English: {english}
Computer: {computer}
Social Studies: {social}
Physics: {physics}

Total Marks: {total}/600
Percentage: {percentage:.2f}%
Grade: {grade}
Result: {result}
Remark: {remark}
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name=f"{name}_report.txt",
        mime="text/plain"
    )
