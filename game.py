import streamlit as st
import random

# Set up the game parameters
LOWER_BOUND = 1
UPPER_BOUND = 100
MAX_ATTEMPTS = 10

# Initialize session state for the game
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(LOWER_BOUND, UPPER_BOUND)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Title of the game
st.title("Number Guessing Game")
st.write(f"Guess the number between {LOWER_BOUND} and {UPPER_BOUND}!")

# Input from the user
if not st.session_state.game_over:
    user_guess = st.number_input("Enter your guess:", min_value=LOWER_BOUND, max_value=UPPER_BOUND, step=1)

    # When the user submits a guess
    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        # Check if the guess is correct, too high, or too low
        if user_guess < st.session_state.number_to_guess:
            st.write("Too low! Try again.")
        elif user_guess > st.session_state.number_to_guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You've guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

        # Check if the user has reached the maximum number of attempts
        if st.session_state.attempts >= MAX_ATTEMPTS and not st.session_state.game_over:
            st.write(f"Game over! The correct number was {st.session_state.number_to_guess}.")
            st.session_state.game_over = True

# Option to restart the game
if st.session_state.game_over:
    if st.button("Play Again"):
        # Reset session state to start a new game
        st.session_state.number_to_guess = random.randint(LOWER_BOUND, UPPER_BOUND)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.write("Game has been reset. Try to guess again!")