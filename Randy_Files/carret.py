# Import ML libraries
import pycaret
import xgboost

# Snowpark for Python
from snowflake.snowpark.session import Session
import snowflake.snowpark.types as T
import snowflake.snowpark.functions as F

# Import Misc
import json
import pandas as pd

# Create Snowflake Session object
connection_parameters = json.load(open("connection.json"))
session = Session.builder.configs(connection_parameters).create()
