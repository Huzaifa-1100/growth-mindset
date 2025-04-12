import streamlit as st
import pandas as pd
import datetime

# --- APP TITLE ---
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")
st.title("🌱 Growth Mindset Challenge 🌱")
st.markdown("""
Welcome to the Growth Mindset Challenge! This app is designed to help you embrace challenges, learn from mistakes, 
and persist through difficulties. Let’s grow together!
""")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to:", ["Home", "Assessment Quiz", "Goal Tracker", "Reflection Journal", "Resources"])

# --- HOME PAGE ---
if menu == "Home":
    st.header("What is a Growth Mindset?")
    st.markdown("""
    A **growth mindset** is the belief that your abilities and intelligence can be developed through hard work, 
    perseverance, and learning from your mistakes. It helps you:
    - Embrace challenges
    - Learn from mistakes
    - Persist through difficulties
    - Celebrate effort
    - Keep an open mind
    """)
    st.subheader("Why Adopt a Growth Mindset?")
    st.markdown("""
    People with a growth mindset see obstacles as opportunities to grow, embrace feedback, and stay determined even 
    when things get tough. This mindset empowers you to continuously improve and achieve your goals.
    """)

# --- ASSESSMENT QUIZ ---
elif menu == "Assessment Quiz":
    st.header("Assessment Quiz: What’s Your Mindset?")
    st.markdown("Answer the following questions to assess whether you have a fixed or growth mindset.")

    # Questions
    q1 = st.radio("1. When faced with a challenge, I feel:", 
                  ["Excited to learn something new", "Anxious and unsure"])
    q2 = st.radio("2. When I make a mistake, I:", 
                  ["Reflect on it and try again", "Feel discouraged and give up"])
    q3 = st.radio("3. I believe my intelligence and skills:", 
                  ["Can be developed with effort", "Are fixed and cannot change"])
    
    # Score Calculation
    score = 0
    if q1 == "Excited to learn something new": score += 1
    if q2 == "Reflect on it and try again": score += 1
    if q3 == "Can be developed with effort": score += 1

    # Submit Button
    if st.button("Submit"):
        if score >= 2:
            st.success("You have a **growth mindset**! Keep embracing challenges and learning.")
        else:
            st.warning("You might lean toward a **fixed mindset**. Practice embracing challenges and learning from mistakes!")

# --- GOAL TRACKER ---
elif menu == "Goal Tracker":
    st.header("🎯 Goal Tracker")
    st.markdown("Set your learning goals and track your progress here.")

    # Input Fields
    goal = st.text_input("Enter your goal:")
    deadline = st.date_input("Set a deadline:", min_value=datetime.date.today())

    # Save Goals
    if 'goals' not in st.session_state:
        st.session_state.goals = []

    if st.button("Add Goal"):
        if goal.strip() != "":
            st.session_state.goals.append({"Goal": goal, "Deadline": deadline})
            st.success(f"Goal added: {goal} (by {deadline})")
        else:
            st.error("Please enter a valid goal.")

    # Display Goals
    if st.session_state.goals:
        st.subheader("Your Goals:")
        goals_df = pd.DataFrame(st.session_state.goals)
        st.table(goals_df)

# --- REFLECTION JOURNAL ---
elif menu == "Reflection Journal":
    st.header("📝 Reflection Journal")
    st.markdown("Take a moment to reflect on your learning experiences. Write down what you’ve learned today.")

    # Text Area for Reflection
    reflection = st.text_area("What did you learn today?", height=150)

    # Save Reflections
    if 'reflections' not in st.session_state:
        st.session_state.reflections = []

    if st.button("Save Reflection"):
        if reflection.strip() != "":
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.reflections.append({"Timestamp": timestamp, "Reflection": reflection})
            st.success("Reflection saved!")
        else:
            st.error("Please write something before saving.")

    # Display Reflections
    if st.session_state.reflections:
        st.subheader("Your Reflections:")
        reflections_df = pd.DataFrame(st.session_state.reflections)
        st.table(reflections_df)

# --- RESOURCES ---
elif menu == "Resources":
    st.header("📚 Resources")
    st.markdown("""
    Here are some resources to help you develop a growth mindset:
    - **Books**: 
      - *Mindset: The New Psychology of Success* by Carol S. Dweck
      - *Grit: The Power of Passion and Perseverance* by Angela Duckworth
    - **Videos**: 
      - [Carol Dweck: The Power of Believing That You Can Improve](https://www.youtube.com/watch?v=_X0mgOOSpLU)
    - **Articles**: 
      - [The Growth Mindset](https://www.mindsetworks.com/science/)
    - **Tools**: 
      - Use this app daily to track your progress and reflect on your learning.
    """)

# --- FOOTER ---
st.sidebar.markdown("🌱 Built with ❤️ using Streamlit")