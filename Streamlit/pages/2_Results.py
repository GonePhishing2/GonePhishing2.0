import streamlit as st

# Set the title of the app
st.title('Results of Exploration')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#criteria-for-choosing-a-model" style="text-decoration: none; color: black;">Criteria for Choosing a Model</a>', unsafe_allow_html=True)


st.markdown("<a name='criteria-for-choosing-a-model'></a>", unsafe_allow_html=True)
st.header('Criteria for Choosing a Model')
st.write('Insert your content here...')


st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/binary_models.png', caption='binary_model')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_feature.png', caption='class_feature')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_fold.png', caption='class_fold')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_model.png', caption='class_model')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_recall_curve.png', caption='class_recall')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_roc.png', caption='class_roc')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/hackusu_scatterplot.png', caption='scatter')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/hackusu_scatterplot_code.png', caption='scatter_code')