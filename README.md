1. Importing Necessary Libraries
-The program starts by importing essential libraries for handling data, performing visualizations, and building a machine-learning model.
-Libraries like pandas and NumPy are used for data manipulation, while Seaborn and Matplotlib help in visualizing patterns in the dataset.
-Scikit-learn is used to preprocess data, split it into training and testing sets, and build a Logistic Regression model.

2. Loading the Dataset
-The program reads a dataset containing credit card transactions.
-This dataset includes details like transaction amount, merchant ID, transaction type, location, and whether it was fraudulent or not.

3. Visualizing the Data
-The program creates graphs to better understand the dataset.
-One graph compares transaction amounts across different transaction types.
-Another graph shows the number of fraudulent transactions in various locations.
-This helps identify patterns and trends in fraudulent transactions.

4. Converting Categorical Data into Numeric Form
-Some data, like Transaction Type and Location, are stored as words or labels.
-Machine learning models work better with numbers, so these labels are converted into numeric values using a process called label encoding.
-For example, if "Online" = 0, "In-store" = 1, and "ATM" = 2, this numeric format allows the model to understand and process the data.

5. Selecting Features and Target Variable
-The program chooses specific columns (features) that will help in predicting fraud.
-These features might include:
Transaction Amount
Merchant ID
Transaction Type
Location
-The target variable is the fraud status (whether the transaction is fraudulent or not).

6. Splitting the Data into Training and Testing Sets
-The dataset is divided into two parts:
-Training set (67%) → Used to teach the model.
-Testing set (33%) → Used to evaluate the model’s performance.
-This step ensures that the model learns from past transactions and can accurately predict fraud for new transactions.

7. Training the Logistic Regression Model
-The program creates and trains a Logistic Regression model.
-Logistic Regression is a statistical method that helps in classifying data into two categories (fraudulent or non-fraudulent).
-The model learns patterns from past transactions to make predictions on future transactions.

8. Taking User Input for a New Transaction
-The program asks the user to enter transaction details:
Transaction Amount
Merchant ID
Transaction Type
Location
-These inputs simulate a real-world transaction that needs to be checked for fraud.

10. Preparing the User Input for Prediction
-The entered values are converted into a format that the model can understand.
-The input is reshaped to match the expected format.

11. Predicting Whether the Transaction is Fraudulent
-The trained Logistic Regression model analyzes the transaction details.
-It outputs a prediction:
-If the model predicts 1, the transaction is flagged as fraudulent.
-If the model predicts 0, the transaction is not fraudulent.

12. Displaying the Prediction Result
The program displays a message based on the model’s prediction:
If fraud is detected, it warns: "The transaction is fraud".
Otherwise, it confirms: "The transaction is not fraud".
