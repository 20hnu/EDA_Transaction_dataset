# EDA of Transaction Dataset

This repository contains an exploratory data analysis (EDA) of a real-world transaction dataset, with a focus on fraud detection. The dataset includes transaction details, customer information, and a target feature indicating whether each transaction is fraudulent. Visualizations, plots, and analysis outcomes can be found throughout this repository.

In analysis tried to find answer of following questions:
 - What are the most common merchants and merchant categories by transaction count and amount?
- What is the distribution of transactionAmount? Are there any outliers?
- What time of day and day of the week do most transactions (or frauds) occur?
- Is there a difference in spending behavior between fraudulent and non-fraudulent transactions?
- How does the availableMoney relate to the transactionAmount in fraudulent vs. normal transactions?
- Which posEntryMode and posConditionCode combinations are more prone to fraud?
- Are there specific merchant categories (merchantCategoryCode) that have higher fraud rates?
- Does length of Entered cardCVV number impact fraud rate?

It also answers many other questions along with suitable visuals and plots. The project includes some level of feature Engineering, Hypothesis testing and appropriate handling of Datetime fields. 

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/20hnu/EDA_Transaction_dataset.git
   cd EDA_Transaction_dataset
   ```
2. Create Virtual Environment
   ##### For Linux/macOS
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    
##### For Windows

    python -m venv venv
    .\venv\Scripts\activate
    
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Navigate to Jupyter Notebooks and find analysis
  
## visuals
![](https://github.com/20hnu/EDA_Transaction_dataset/blob/main/visuals/plots/Correlation_Matrix(creditLimit_availableMoney_currentBalance).png?raw=true)

![](https://github.com/20hnu/EDA_Transaction_dataset/blob/main/visuals/plots/Fraud_Rate_vs_Total_Transactions_per_Customer.png?raw=true)

![](https://github.com/20hnu/EDA_Transaction_dataset/blob/main/visuals/plots/Day_of_week_Average_Transaction_and_Fraud_Amounts.png?raw=true)

![](https://github.com/20hnu/EDA_Transaction_dataset/blob/main/visuals/plots/Balance_Difference_Distribution_Fraud_Cases_negative(currentBalance%20-%20availableMoney).png?raw=true)


The outcome of each analysis is noted in respective notebooks.