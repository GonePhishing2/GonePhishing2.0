import streamlit as st

# Set the title of the app
st.title('Results of Exploration')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#criteria-for-choosing-a-model" style="text-decoration: none; color: black;">Criteria for Choosing a Model</a>', unsafe_allow_html=True)


st.markdown("<a name='criteria-for-choosing-a-model'></a>", unsafe_allow_html=True)
st.header('Criteria for Choosing a Model')
st.write('The model needed to be accurate and be capable of predicting the number of days late or early a delivery would be.')

st.subheader("Features")
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/hackusu_scatterplot.png', caption='scatter')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/hackusu_scatterplot_code.png', caption='scatter_code')

st.subheader("Binary Model")
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/binary_models.png', caption='binary_model')

st.subheader("Basic Regression")
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/reg_model.png', caption='reg_model')


st.subheader("Classification Model")
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_model.png', caption='class_model')
st.write("Better than the Basic Regression models and worse than Classification model. Bining every 10 days from -100 to 100.")

st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_fold.png', caption='class_fold')
st.write("Went with Random Forest model")

st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_feature.png', caption='class_feature')

st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_roc.png', caption='class_roc')
st.write("""
ROC Curve: The ROC curve plots the True Positive Rate (TPR, also known as recall or sensitivity) against the False Positive Rate (FPR) at various threshold settings. The True Positive Rate is the ratio of correctly predicted positive observations to all actual positives, while the False Positive Rate is the ratio of incorrectly predicted positive observations to all actual negatives.
AUC-ROC: The AUC of the ROC curve (AUC-ROC) measures the entire two-dimensional area underneath the entire ROC curve from (0,0) to (1,1). It provides an aggregate measure of the model across all possible classification thresholds. An AUC-ROC value of 1 indicates a perfect model, while a value of 0.5 suggests no discriminative power, equivalent to random guessing.
""")

st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/classification_recall_curve.png', caption='class_recall')
st.markdown('''
The Precision-Recall curve is a plot that showcases the trade-off between 
precision (positive predictive value) and recall (sensitivity) for every 
possible threshold of a classification model. It's particularly useful for 
evaluating models on imbalanced datasets where the positive class 
(the class of interest) is much rarer compared to the negative class.

The curve starts at the top-left corner, indicating high precision for low recall values, 
and it typically decreases as recall increases. This is because initially, when the threshold 
for classifying a positive is high, the model is very precise but not very sensitive 
(it doesn't capture many positives). As the threshold is lowered, the model captures more 
true positives, but also more false positives, which decreases precision.

In conclusion, the RandomForestClassifier model shown in the plot has a high average 
precision of 0.88, suggesting it performs well in distinguishing between the positive 
and negative classes for the task at hand. However, the precision decreases as the 
recall increases, which is a typical behavior for most classifiers.
''')


st.subheader("NN Regression")
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/NeuralNetTraining.png', caption='NN_training')
st.image('https://raw.githubusercontent.com/peircerandy/GonePhishing2.0/main/Streamlit/images/NeuralNetTrainingCode.png', caption='NN_code')