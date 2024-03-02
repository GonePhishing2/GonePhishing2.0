import streamlit as st

# Set the title of the app
st.title('Koch Industries Report')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#project-outline" style="text-decoration: none; color: black;">Project Outline</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#problem-statement" style="text-decoration: none; color: black;">Problem Statement</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#data-preparationcleaning" style="text-decoration: none; color: black;">Data Preparation/Cleaning</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#feature-engineering" style="text-decoration: none; color: black;">Feature Engineering</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#modeling-techniques" style="text-decoration: none; color: black;">Modeling Techniques</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#criteria-for-choosing-a-model" style="text-decoration: none; color: black;">Criteria for Choosing a Model</a>', unsafe_allow_html=True)

# Sections of the app
st.markdown("<a name='project-outline'></a>", unsafe_allow_html=True)
st.header('Collaboratively Outline the Project')
st.text('Insert your content here...')

st.markdown("<a name='problem-statement'></a>", unsafe_allow_html=True)
st.header('Problem Statement')
st.text('Insert your content here...')

st.markdown("<a name='data-preparationcleaning'></a>", unsafe_allow_html=True)
st.header('Data Preparation/Cleaning')
st.text('Insert your content here...')

st.markdown("<a name='feature-engineering'></a>", unsafe_allow_html=True)
st.header('Feature Engineering')
st.text('Insert your content here...')

st.markdown("<a name='modeling-techniques'></a>", unsafe_allow_html=True)
st.header('Modeling Techniques')
st.text('Insert your content here...')

st.markdown("<a name='criteria-for-choosing-a-model'></a>", unsafe_allow_html=True)
st.header('Criteria for Choosing a Model')
st.text('Insert your content here...')
