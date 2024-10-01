import time
import streamlit as st

# Title and description
st.title("Workout Timer Application")
st.write("This app will guide you through your workout session based on your chosen parameters.")

# Collecting user inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=20, max_value=100, step=1)
workout_cat = st.selectbox("Select your workout category:",
                           ["STRENGTH WORKOUT", "CARDIO WORKOUT", "FLEXIBILITY WORKOUT", "MOBILITY WORKOUT",
                            "BODYWEIGHT WORKOUT", "YOGA", "POWER LIFTING",
                            "HIGH INTENSITY INTERVAL TRAINING", "CORE WORKOUT", "LOW IMPACT WORKOUT"])
fitness_level = st.radio("Select your fitness level:", ("Beginner", "Intermediate", "Advanced"))

# Defining parameters for each workout category and fitness level
workout_params = {
    "STRENGTH WORKOUT": {"Beginner": (3, 2, 10, 30, 60), "Intermediate": (4, 3, 12, 40, 90), "Advanced": (5, 4, 15, 50, 120)},
    "CARDIO WORKOUT": {"Beginner": (3, 2, 20, 30, 45), "Intermediate": (4, 3, 25, 45, 60), "Advanced": (5, 4, 30, 60, 90)},
    "FLEXIBILITY WORKOUT": {"Beginner": (3, 2, 5, 20, 30), "Intermediate": (4, 3, 8, 30, 45), "Advanced": (5, 4, 10, 40, 60)},
    "MOBILITY WORKOUT": {"Beginner": (3, 2, 10, 30, 60), "Intermediate": (4, 3, 12, 40, 90), "Advanced": (5, 4, 15, 50, 120)},
    "BODYWEIGHT WORKOUT": {"Beginner": (3, 2, 12, 30, 60), "Intermediate": (4, 3, 15, 40, 90), "Advanced": (5, 4, 18, 50, 120)},
    "YOGA": {"Beginner": (3, 2, 5, 60, 60), "Intermediate": (4, 3, 5, 75, 90), "Advanced": (5, 4, 5, 90, 120)},
    "POWER LIFTING": {"Beginner": (3, 2, 5, 45, 120), "Intermediate": (4, 3, 5, 60, 150), "Advanced": (5, 4, 3, 75, 180)},
    "HIGH INTENSITY INTERVAL TRAINING": {"Beginner": (3, 2, 10, 30, 60), "Intermediate": (4, 3, 15, 45, 90), "Advanced": (5, 4, 20, 60, 120)},
    "CORE WORKOUT": {"Beginner": (3, 2, 15, 30, 60), "Intermediate": (4, 3, 20, 40, 90), "Advanced": (5, 4, 25, 50, 120)},
    "LOW IMPACT WORKOUT": {"Beginner": (3, 2, 10, 30, 60), "Intermediate": (4, 3, 12, 35, 90), "Advanced": (5, 4, 15, 40, 120)}
}

# Extract workout parameters based on the category and fitness level
selected_params = workout_params[workout_cat][fitness_level]
total_exercises = selected_params[0]
sets = selected_params[1]
reps = selected_params[2]
exercise_duration = selected_params[3]
rest_period = selected_params[4]

# Display workout parameters
if st.button("Show Workout Details"):
    st.subheader("Your Workout Parameters")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Workout Category:** {workout_cat}")
    st.write(f"**Fitness Level:** {fitness_level}")
    st.write(f"**Total Exercises:** {total_exercises}")
    st.write(f"**Sets per Exercise:** {sets}")
    st.write(f"**Reps per Set:** {reps}")
    st.write(f"**Exercise Duration:** {exercise_duration} seconds")
    st.write(f"**Rest Period:** {rest_period} seconds")

# Workout Timer Function
def workout_timer(total_exercises, sets, reps, exercise_duration, rest_period):
    st.write("\nStarting your workout...")

    for exercise in range(1, total_exercises + 1):
        st.write(f"\nExercise {exercise}/{total_exercises}")
        for current_set in range(1, sets + 1):
            st.write(f" Set {current_set}/{sets}: Perform {reps} reps for {exercise_duration} seconds")
            with st.spinner(f"Exercising for {exercise_duration} seconds..."):
                time.sleep(exercise_duration)  # exercise time

            if current_set < sets:
                st.write(f" Rest for {rest_period} seconds between sets")
                with st.spinner(f"Resting for {rest_period} seconds..."):
                    time.sleep(rest_period)  # Rest between sets

        if exercise < total_exercises:
            st.write(f" Rest for {rest_period} seconds before the next exercise")
            with st.spinner(f"Resting for {rest_period} seconds..."):
                time.sleep(rest_period)  # Rest between exercises

    st.success("Workout complete! Great job!")

# Start the workout timer
if st.button("Start Workout Timer"):
    workout_timer(total_exercises, sets, reps, exercise_duration, rest_period)

