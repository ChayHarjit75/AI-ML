import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Student Mark Prediction")

df = pd.read_csv("student_habits_performance.csv")
df.head()

df = pd.get_dummies(df,columns=['gender','diet_quality','parental_education_level','internet_quality','extracurricular_participation','part_time_job']).dropna()
df

print(df.dtypes)

x =df.drop(columns='exam_score')
print(x)

y = df['exam_score']
print(y)

model = LinearRegression()
x = x.drop(columns='student_id')
model.fit(x,y)

age = st.number_input("Enter your age:")
hours = st.number_input("Enter your hours of study:")
sleep = st. number_input("Enter your sleep hours:")
score = st.number_input("Enter your previous Score:")
gender = st.selectbox("Choose your Gender:", ('Male','Female'))
diet = st.selectbox("Choose your Diet Quality:",('Average','Good','Poor'))
educate = st.selectbox("Choose your Education:",('Associate degree','Bachelor\'s degree','High School Diploma','Master\'s degree'))
study = st.selectbox("Choose where you are studing:",('School','College'))
quality = st.selectbox("Choose your Quality:",('average','good','poor'))
course = st.selectbox("extracurricular participation",('yes','no'))
part = st.selectbox("Did you are going to Part time job",('yes','no'))
atten = st.number_input("Enter your Attendance:")
execrise = st.number_input("Enter your Frequency:")
menhel = st.number_input("Enter your Mental Health:")

if gender == 'Male':
    genderx = 0
    gendery = 1
elif gender =='Female':
    genderx = 1
    gendery = 0

if diet == 'Average':
    aver = 1
    good = 0
    poor = 0
elif  diet == 'Good':
    aver = 0
    good = 1
    poor = 0
elif diet == 'Poor':
    aver = 0
    good = 0
    poor = 1

if educate == 'Associate degree':
    asso = 1
    bache = 0
    hisc = 0
    mast = 0
elif educate == 'Bachelor\'s degree':
    asso = 0
    bache = 1
    hisc = 0
    mast = 0
elif educate == 'High School Diploma':
    asso = 0
    bache = 0
    hisc = 1
    mast = 0
elif educate == 'Master\'s degree':
    asso = 0
    bache = 0
    hisc = 0
    mast = 1

if study == 'College':
    college = 1
    school = 0
elif study == 'School':
    college = 0
    school = 1

if quality == 'average':
    goo = 0
    average = 1
    poo = 0
elif quality == 'good':
    goo = 1
    average = 0
    poo = 0
elif quality == 'poor':
    goo = 0
    average = 0
    poo = 1

if course == 'no':
    a = 1
    b = 0
elif course == 'yes':
    a = 0
    b = 1

if part == 'yes':
    c = 0
    d = 1
elif part == 'no':
    d = 1
    c = 0

new_data_row = {
    'age': age,
    'hours_studied': hours,
    'sleep_hours': sleep,
    'previous_scores': score,
    'gender_Female': genderx,
    'gender_Male': gendery,
    'diet_quality_Average': aver,
    'diet_quality_Good': good,
    'diet_quality_Poor': poor,
    'parental_education_level_Associate degree': asso,
    'parental_education_level_Bachelor\'s degree': bache,
    'parental_education_level_High School Diploma': hisc,
    'parental_education_level_Master\'s degree': mast,
    'parental_education_level_Some College': college,
    'parental_education_level_Some High School': school,
    'internet_quality_Average': average,
    'internet_quality_Good': goo,
    'internet_quality_Poor': poo,
    'extracurricular_participation_No': a,
    'extracurricular_participation_Yes': b,
    'part_time_job_No': d,
    'part_time_job_Yes': c,
    'attendance_percentage': atten,
    'exercise_frequency': execrise,
    'mental_health_rating': menhel
}

input_data = pd.DataFrame([new_data_row])

input_data = input_data.reindex(columns=x.columns, fill_value=0)

predicted_score = model.predict(input_data)
if st.button("Submit"):
    st.write(f"Predicted exam score: {predicted_score[0]:.2f}")
