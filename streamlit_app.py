import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Simple Streamlit App")
st.markdown("This app demonstrates basic Streamlit features like widgets and charts.")

# Sidebar user input
st.sidebar.header("User Input")
name = st.sidebar.text_input("What's your name?", "John Doe")
age = st.sidebar.slider("How old are you?", 0, 100, 25)

# Display user input
st.write(f"Hello, **{name}**! You are **{age}** years old.")

# Generate random data
st.header("Random Data Table")
data = pd.DataFrame(np.random.randn(10, 3), columns=["Column A", "Column B", "Column C"])
st.dataframe(data)

# Line chart of the data
st.header("Line Chart")
st.line_chart(data)

# Show Matplotlib plot
st.header("Matplotlib Plot")
fig, ax = plt.subplots()
ax.plot(data["Column A"], label="Column A")
ax.plot(data["Column B"], label="Column B")
ax.legend()
st.pyplot(fig)

# User input to generate numbers
st.header("Dynamic List of Numbers")
num = st.number_input("Enter a number:", min_value=1, max_value=10, value=5)
st.write(f"Here's a list of numbers from 1 to {num}:")
st.write(list(range(1, num + 1)))

# Button interaction
if st.button("Say Hello"):
    st.success(f"Hello, {name}!")

# Displaying checkbox result
if st.checkbox("Show a secret message"):
    st.write("🎉 You're awesome!")

