import streamlit as st

# Set the title of the app
st.title('Data Cleaning and Preporation')

# Sidebar for navigation with HTML and inline CSS to mimic normal text appearance
st.sidebar.title('Navigation')
st.sidebar.markdown('<a href="#data-preparationcleaning" style="text-decoration: none; color: black;">Data Preparation/Cleaning</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#feature-engineering" style="text-decoration: none; color: black;">Feature Engineering</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#modeling-techniques" style="text-decoration: none; color: black;">Modeling Techniques</a>', unsafe_allow_html=True)

st.markdown("<a name='data-preparationcleaning'></a>", unsafe_allow_html=True)
st.header('Data Cleaning and Preparation)
st.subheader('Dealing with Data Types')
st.write('We started by examining the data and its types. It was evident that the dates were formatted as numbers, which we corrected by converting them to date format.')

st.subheader('Dealing with Nulls')
st.write('To handle missing data, we conducted the following steps:')
st.write("- Filled in missing 'FIRST_GR_POSTING_DATE_ML' data using 'PLANNED_DELIVERY_DAYS' and 'RELEASE_DATE_ML'.")
st.write("- Filled in missing 'PLANNED_DELIVERY_DAYS' data using 'RELEASE_DATE_ML' and 'FIRST_GR_POSTING_DATE_ML'.")
st.write("- We removed rows with null values from specific columns to ensure data integrity.")
st.write("- Dropped nulls from the following columns:")
st.write("  - COMPANY_CODE_ID")
st.write("  - PURCHASE_DOCUMENT_ITEM_ID")
st.write("  - INBOUND_DELIVERY_ITEM_ID")
st.write("  - PLANNED_DELIVERY_DAYS")

st.subheader('Dealing with Creating New Columns')
st.write('We created a new column named "LATE" to determine if a delivery was late or not. We used an IF statement to assign a boolean value based on the comparison between "DELIVERY_DATE_ML" and "FIRST_GR_POSTING_DATE_ML".')
st.write('We created new columns that were the date instead of numeric for the date columns.')

          
st.subheader('Model Feature')
# Describe the feature engineering and selection methodology
st.markdown('''
    The analytical model aims to predict the delivery performance of purchase orders by 
    examining the lag between planned and actual delivery dates. To achieve this, the model 
    connects to the `PURCHASE_ORDER_HISTORY` table to extract necessary data.

    A key engineered feature, `target_feature`, was created to calculate the difference in days 
    between the planned delivery date (`DELIVERY_DATE_ML`) and the actual goods receipt 
    posting date (`FIRST_GR_POSTING_DATE_ML`). This feature represents the timeliness of 
    delivery, a crucial aspect of supply chain management.

    For modeling, the following pertinent columns were selected to encapsulate the details 
    of the purchase orders:
    
    - `PURCHASE_DOCUMENT_ITEM_ID`: Unique identifier for each item in the purchase order.
    - `CREATE_DATE_ML`: The creation date of the purchase order.
    - `COMPANY_CODE_ID`: The company within INVISTA making the purchase.
    - `VENDOR_ID`: The vendor from whom the purchase is made.
    - `POSTAL_CD`: Postal code associated with the company code.
    - `MATERIAL_ID`: Identifier for the material being purchased.
    - `SUB_COMMODITY_DESC`: Description of the sub-commodity.
    - `MRP_TYPE_ID`: Indicates if the material is reordered manually or automatically.
    - `PLANT_ID`: The plant that is making the purchase.
    - `REQUESTED_DELIVERY_DATE_ML`: The delivery date as requested in the requisition.
    - `INBOUND_DELIVERY_ID` & `INBOUND_DELIVERY_ITEM_ID`: Identifiers for the delivery and the items within.
    - `PLANNED_DELIVERY_DAYS`: The expected delivery duration.

    Rows lacking a recorded actual delivery date were excluded to ensure the model trained on complete records. 
    The processed data was transformed into a Pandas DataFrame, with NULL values filled with zeros. This 
    preprocessed dataset was used to configure the machine learning environment in PyCaret, optimizing for 
    computational efficiency and reproducibility by utilizing GPU acceleration and a unique session ID.
''')

st.markdown("<a name='modeling-techniques'></a>", unsafe_allow_html=True)
st.header('Modeling Techniques')
st.subheader('Binary Classification')
st.write("""
Starting with a basic model, we aimed to set the stage for future, more complex analyses. Our initial approach was straightforward: classify deliveries as either early (0) or late (1). We utilized PyCaret to explore various models and identify the most effective one for our data.
""")

st.subheader('Regression with Pycaret')
st.write('Following a similar approach to our initial model, we kept the target column unchanged to assess model performance on continuous data. It was a foundational step, providing insights for subsequent modeling techniques.')

st.subheader('Classification with Pycaret')
st.write('''
Building upon our previous models, we refined our approach to seek a more detailed understanding of delivery times. We moved beyond binary classification to categorize deliveries into discrete time intervals, excluding extreme delays to focus on a more typical range of -100 to 100 days, segmented into 10-day bins.
''')

st.subheader('Tuning with Pycaret')
st.write(''' 
Encouraged by the reasonable accuracy from our classification model, we attempted to fine-tune the best-performing model. Memory limitations led us to pivot back to the binary classification model for tuning, aiming to optimize its performance without overwhelming our resources.
''')

st.subheader('Regression NN')
st.write('''
Regression models provide more continuous predictions, which can be useful for understanding the nuances of delivery times. We explored the capabilities of a Neural Network for regression to leverage the complex patterns in our data and enhance our predictive capabilities by providing the exact lead time to expect. This effort took much data cleaning to convert categorical data into numerical data using techniques such as one-hot encoding and hashing. We were able to successfully implement the model, but due to time constraints, we were unable to fully optimize the model to actually learn. At the time being it's predictions are just as good as a random guess, but we are confident that with more time and resources, we can make this model a valuable asset to our predictive capabilities.
''')

st.subheader('Neural Network Classification')
st.write('''
Inspired by the effectiveness of our initial classification models, we decided to explore the capabilities of a Neural Network for classification. This is an ongoing effort to enhance our predictive accuracy and leverage the nuanced patterns in our data.
''')
