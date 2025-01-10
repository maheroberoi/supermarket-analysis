#ANALYSIS
from scipy.stats import ttest_ind 

 

def loyalty_analysis(df, store): 

    """ 

    Compare rankings for loyalty scheme users vs non-users for a specific store. 

    """ 

    loyalty_users = df[df[f"{store}_Loyalty_User"]][f"{store}_Rank"] 

    non_loyalty_users = df[~df[f"{store}_Loyalty_User"]][f"{store}_Rank"] 

     

    # Perform t-test 

    t_stat, p_value = ttest_ind(loyalty_users, non_loyalty_users, nan_policy='omit') 

    return {"store": store, "t_stat": t_stat, "p_value": p_value} 

 

if __name__ == "__main__": 

    from data_preprocessing import preprocess_data 

    file_path = "Maher - PWC/Supermarket Analysis/data/Supermarket_Study_Responses.xlsx" 

    df = preprocess_data(file_path) 

     

    result = loyalty_analysis(df, "Tesco") 

    print(f"Loyalty analysis for Tesco: {result}") 