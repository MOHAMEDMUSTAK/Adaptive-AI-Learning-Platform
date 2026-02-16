import streamlit as st
import random
import time
import matplotlib.pyplot as plt
from backend.database import init_db, save_performance, get_user_data
from backend.mastery_engine import compute_mastery
from backend.adaptive_engine import adjust_difficulty
from models.question_loader import questions

init_db()

st.title("AI Adaptive Learning Platform (Scalable Version)")

username = st.text_input("Enter Username")

if username:

    user_data = get_user_data(username)
    difficulty = adjust_difficulty(user_data)

    available = [q for q in questions if q["difficulty"] == difficulty]

    if available:
        q = random.choice(available)

        st.subheader(f"Difficulty Level: {difficulty}")
        st.write(q["question"])

        start_time = time.time()
        selected = st.radio("Select Answer:", q["options"])

        if st.button("Submit"):

            response_time = time.time() - start_time
            correct = int(selected == q["answer"])

            save_performance(username, q["concept"], correct, response_time)

            if correct:
                st.success("Correct")
            else:
                st.error("Incorrect")

            updated_data = get_user_data(username)
            overall, concept_mastery = compute_mastery(updated_data)

            st.subheader("Performance Analytics")
            st.write("Overall Mastery:", overall)

            fig, ax = plt.subplots()
            ax.bar(concept_mastery.keys(), concept_mastery.values())
            ax.set_title("Concept Mastery")
            st.pyplot(fig)
