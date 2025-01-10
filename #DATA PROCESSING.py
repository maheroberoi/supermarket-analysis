#DATA PROCESSING 
import pandas as pd 

 

def preprocess_data(file_path): 

    """ 

    Load and preprocess the dataset: 

    - Convert rankings to numerical values. 

    - Extract loyalty scheme usage. 

    """ 

    data = pd.ExcelFile('Maher - PWC/Supermarket Analysis/data/Supermarket_Study_Responses.xlsx') 

    df = data.parse('Form Responses 1') 

 

    # Map rankings to numerical values 

    ranking_map = { 

        "First choice": 1, 

        "Second choice": 2, 

        "Third choice": 3, 

        "Fourth choice": 4, 

        "Fifth choice": 5, 

        "Sixth choice": 6, 

    } 

    for store in ["Asda", "Sainsbury's", "Tesco", "Waitrose", "Aldi", "Lidl"]: 

        col_name = f"Rank these stores in order of choice for your regular food shop. [{store}]" 

        df[f"{store}_Rank"] = df[col_name].map(ranking_map) 

 

    # Extract loyalty scheme users 

    df['Loyalty Schemes'] = df['Which of these stores\' reward schemes do you use?'].str.split(', ') 

    for store in ["Asda", "Sainsbury's", "Tesco", "Waitrose", "Aldi", "Lidl"]: 

        df[f"{store}_Loyalty_User"] = df['Loyalty Schemes'].apply( 

            lambda x: store in x if isinstance(x, list) else False) 

 

    return df 

 

if __name__ == "__main__": 

    # Example usage 

    file_path = "Maher - PWC/Supermarket Analysis/data/Supermarket_Study_Responses.xlsx" 

    processed_data = preprocess_data(file_path) 

    print(processed_data.head()) 