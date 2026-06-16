# 🎓 Grade Calculator (Streamlit App)

A simple web-based Grade Calculator built using Streamlit.  
This app allows students to calculate their overall percentage and grade easily.



## 🚀 Features

- Add multiple subjects dynamically  
- Input marks and total marks  
- Automatic percentage calculation  
- Clean and interactive UI  
- Runs locally in your browser  



## 🛠️ Tech Stack

- Python 3  
- Streamlit  



## 📦 Installation

### 1. Clone Repository
git clone (https://github.com/muskan-thakre-ai/gradecalculator) 
cd grade-calculator-streamlit  

### 2. Install Dependencies
pip install streamlit  


## ▶️ Run the App

streamlit run app.py  

Open in browser:  
http://localhost:8501  

---

## 📊 How It Works

1. Enter student details
2. Input marks obtained for each subject  
3. Input total marks  
4. Click **Calculate**  
5. View total, percentage,  grade , leadboeard 

---

## 🧮 Example

| Subject   | Marks | Total |
|----------|------|------|
| Math     | 85   | 100  |
| Science  | 90   | 100  |
| English  | 80   | 100  |

**Percentage = 85%**
## screnshot
<img width="1577" height="782" alt="Screenshot 2026-06-16 113154" src="https://github.com/user-attachments/assets/f9b1f971-0c20-451c-9299-772abd9b7e1a" />
<img width="1390" height="576" alt="Screenshot 2026-06-16 113006" src="https://github.com/user-attachments/assets/7ceb8177-710a-4276-acc2-e2ed83dd2fb3" />
<img width="1372" height="812" alt="Screenshot 2026-06-16 113042" src="https://github.com/user-attachments/assets/1a02386d-86c6-40c5-a991-63ba10804788" />




## 📂 Project Structure

grade-calculator-streamlit/  
│── app.py  
│── README.md  
│── requirements.txt  



## 💻 Sample Code (app.py)

```python
import streamlit as st

st.title("🎓 Grade Calculator")

num_subjects = st.number_input("Enter number of subjects", min_value=1, step=1)

marks = []
total_marks = []

for i in range(int(num_subjects)):
    st.subheader(f"Subject {i+1}")
    m = st.number_input(f"Marks obtained {i+1}", min_value=0.0)
    t = st.number_input(f"Total marks {i+1}", min_value=1.0)
    marks.append(m)
    total_marks.append(t)

if st.button("Calculate"):
    total_obtained = sum(marks)
    total_possible = sum(total_marks)
    percentage = (total_obtained / total_possible) * 100

    st.success(f"Total Marks: {total_obtained}/{total_possible}")
    st.info(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        st.write("Grade: A+")
    elif percentage >= 75:
        st.write("Grade: A")
    elif percentage >= 60:
        st.write("Grade: B")
    else:
        st.write("Grade: C")


