import streamlit as st

# Set the title of the app
st.title('Koch Industries Report')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Project Outline', 'Problem Statement', 'Data Preparation/Cleaning', 'Feature Engineering', 'Modeling Techniques', 'Criteria for Choosing a Model'])

# Page content
if page == 'Project Outline':
    st.header('Collaboratively Outline the Project')
    st.text('Insert your content here...')

    st.subheader('Chosen Quickstart')
    st.text('We looked at all.')

elif page == 'Problem Statement':
    st.header('Problem Statement')
    st.text('Insert your content here...')

elif page == 'Data Preparation/Cleaning':
    st.header('Data Preparation/Cleaning')
    st.text('Insert your content here...')

elif page == 'Feature Engineering':
    st.header('Feature Engineering')
    st.text('Insert your content here...')

elif page == 'Modeling Techniques':
    st.header('Modeling Techniques')
    st.text('Insert your content here...')

elif page == 'Criteria for Choosing a Model':
    st.header('Criteria for Choosing a Model')
    st.text('Insert your content here...')
