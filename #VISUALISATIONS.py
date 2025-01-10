#VISUALISATIONS
import matplotlib.pyplot as plt 

import seaborn as sns 

 

def plot_loyalty_vs_ranking(df, store): 

    """ 

    Plot the rankings of loyalty scheme users vs non-users for a given store. 

    """ 

    loyalty_users = df[df[f"{store}_Loyalty_User"]][f"{store}_Rank"] 

    non_loyalty_users = df[~df[f"{store}_Loyalty_User"]][f"{store}_Rank"] 



    plt.figure(figsize=(8, 5)) 

    sns.boxplot(data=[loyalty_users, non_loyalty_users], palette="pastel") 

    plt.xticks([0, 1], ['Loyalty Users', 'Non-Loyalty Users']) 

    plt.title(f"{store} Rankings: Loyalty Users vs Non-Loyalty Users") 

    plt.ylabel("Rank (Lower is Better)") 

    plt.show() 

 

if __name__ == "__main__": 

    from data_preprocessing import preprocess_data 

    file_path = "Maher - PWC/Supermarket Analysis/data/Supermarket_Study_Responses.xlsx" 

    df = preprocess_data(file_path) 

    plot_loyalty_vs_ranking(df, "Tesco") 