#test analysis
from src.analysis import loyalty_analysis
from src.data_preprocessing import preprocess_data
def test_loyalty_analysis():
 # Load data and preprocess
 file_path = "../data/Supermarket_Study_Responses.xlsx"
 df = preprocess_data(file_path)
 # Run analysis
 result = loyalty_analysis(df, "Tesco")
# Validate results
 assert result["t_stat"] is not None
 assert result["p_value"] < 1.0 # P-value should be a valid number