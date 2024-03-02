import streamlit as st

# Set the title of the app
st.title('Results of Exploration')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#criteria-for-choosing-a-model" style="text-decoration: none; color: black;">Criteria for Choosing a Model</a>', unsafe_allow_html=True)


st.markdown("<a name='criteria-for-choosing-a-model'></a>", unsafe_allow_html=True)
st.header('Criteria for Choosing a Model')
st.write('Insert your content here...')