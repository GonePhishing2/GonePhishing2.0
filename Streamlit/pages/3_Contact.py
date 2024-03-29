import streamlit as st

# Set the title of the app
st.title('Thank You Koch and Snowflake!')
st.write('### Things We Have Learned During This Competition')

# List of items to display as bullet points
items = ["Tyler: Snowflake, Data Cleaning, Pycarot, Pytorch", "Randy: Pycarot Libary, Data Cleaning, Connecting to Remote Databases", 
         "Logan: Machine Learning ,Streamlit, SQL, Snowflake", "Annaka: Machine Learning, Data Cleaning, Snowflake, Streamlit, Classification Models"]

# Convert the list to a Markdown-formatted string
bullet_list = "\n".join(f"* {item}" for item in items)

# Display the bullet list in the app
st.markdown(bullet_list)


