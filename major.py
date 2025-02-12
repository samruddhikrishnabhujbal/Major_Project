import streamlit as st
import time
import pyttsx3
from datetime import datetime

def speak_reminder(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

reminders = {
    "07:30": "It's time for breakfast.",
    "12:30": "It's time for lunch.",
    "18:30": "It's time for dinner.",
    "09:00": "Drink water.",
    "15:27": "Time to take your medicine."
}

st.title("Digital Assistance System for Elderly")

# Task Management
st.header("Daily Task Management")
task_list = st.session_state.get("tasks", [])
new_task = st.text_input("Enter a new task")
if st.button("Add Task") and new_task:
    task_list.append(new_task)
    st.session_state["tasks"] = task_list
for task in task_list:
    st.write(f"✅ {task}")

# Grocery List
st.header("Grocery List")
grocery_list = st.session_state.get("groceries", [])
new_grocery = st.text_input("Enter a grocery item")
if st.button("Add Grocery") and new_grocery:
    grocery_list.append(new_grocery)
    st.session_state["groceries"] = grocery_list
for grocery in grocery_list:
    st.write(f"🛒 {grocery}")

# Emergency Button
st.header("Emergency Assistance")
if st.button("Send Emergency Alert"):
    st.warning("Emergency Alert Sent to Caregiver and Hospital!")

# Real-time Reminder Check
st.header("Automated Reminders")
if st.button("Start Reminder Service"):
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in reminders:
            speak_reminder(reminders[now])
            st.success(f"Reminder: {reminders[now]}")
        time.sleep(60)
