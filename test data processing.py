#test data processing
import pandas as pd
from src.data_preprocessing import preprocess_data
def test_preprocess_data():
 # Load test data
 file_path = "../data/Supermarket_Study_Responses.xlsx"
 df = preprocess_data(file_path)
 # Check that rankings columns exist
 assert "Tesco_Rank" in df.columns
 assert "Asda_Rank" in df.columns
 # Check that there are no missing values
 assert not df.isnull().values.any()
