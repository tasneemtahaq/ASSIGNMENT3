# Save as app.py and run with: streamlit run app.py

import streamlit as st

# Class info (Tuple - Immutable)
class_info = ("Python Programming", "Monday", "10:00 AM")
st.title("📚 Student Attendance Tracker")
st.write(f"**Class:** {class_info[0]} | **Day:** {class_info[1]} | **Time:** {class_info[2]}")

# Student list
students = ["Alice", "Bob", "Charlie", "David", "Emma"]  # list

# Attendance dictionary
attendance = {}  # dictionary

st.subheader("✅ Mark Attendance")

# Loop through students
for student in students:
    present = st.radio(f"Is {student} present?", ("Yes", "No"), key=student)
    attendance[student] = True if present == "Yes" else False  # control flow

# Button to finalize attendance
if st.button("📋 Submit Attendance"):
    absentees = set()  # set
    for name, is_present in attendance.items():  # loop
        if not is_present:
            absentees.add(name)
    
    frozen_absentees = frozenset(absentees)  # frozenset

    # Show summary
    st.success("✅ Attendance Submitted!")
    st.subheader("📊 Attendance Summary:")
    for name, status in attendance.items():
        st.write(f"{name}: {'Present' if status else 'Absent'}")
    
    st.subheader("❌ Absentees (Frozen Set):")
    st.write(frozen_absentees)
