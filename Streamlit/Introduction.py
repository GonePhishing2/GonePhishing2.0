import streamlit as st

# Set the title of the app
st.title('Project Outline/Background')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#project-outline" style="text-decoration: none; color: black;">Project Outline</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#problem-statement" style="text-decoration: none; color: black;">Problem Statement</a>', unsafe_allow_html=True)



# Sections of the app
st.markdown("<a name='project-outline'></a>", unsafe_allow_html=True)
st.header('Collaboratively Outline the Project')
st.write("This project represents a concerted effort by our team to tackle Koch Industries pressing issue of parts delivery delays. \
        We're methodically working through stages from data cleaning to model selection, aiming to significantly improve our prediction accuracy. \
        By transforming disjointed data into a reliable forecasting tool, we intend to provide Koch with the ability to anticipate delays and plan accordingly, thus maintaining uninterrupted production and safeguarding the bottom line.")

st.markdown("<a name='problem-statement'></a>", unsafe_allow_html=True)
st.header('Problem Statement')
st.write('Insert your content here...')




