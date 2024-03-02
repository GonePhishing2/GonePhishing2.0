import streamlit as st

# Set the title of the app
st.title('Data Cleaning and Preporation')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#data-preparationcleaning" style="text-decoration: none; color: black;">Data Preparation/Cleaning</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#feature-engineering" style="text-decoration: none; color: black;">Feature Engineering</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#modeling-techniques" style="text-decoration: none; color: black;">Modeling Techniques</a>', unsafe_allow_html=True)

st.markdown("<a name='data-preparationcleaning'></a>", unsafe_allow_html=True)
st.header('Data Cleaning and Preporation')
st.write('Insert your content here...')

st.markdown("<a name='feature-engineering'></a>", unsafe_allow_html=True)
st.header('Feature Engineering')
st.write('Insert your content here...')

st.markdown("<a name='modeling-techniques'></a>", unsafe_allow_html=True)
st.header('Modeling Techniques')
st.write('Insert your content here...')