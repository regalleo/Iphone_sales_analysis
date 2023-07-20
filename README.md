Sales Analysis Project - iPhone Sales in India

*Overview

This is a data science project that analyzes the sales of iPhones in India on the Flipkart platform. The project utilizes Python and various data science libraries such as pandas, numpy, and plotly to perform data analysis and visualization.

*Prerequisites

To run the code in this project, you need to have the following installed:

- Python (3.6 or higher)
- pandas
- numpy
- plotly

*Dataset

The dataset used in this project contains information about various iPhone models available on Flipkart. It includes the following columns:

- Product Name
- Product URL
- Brand
- Sale Price
- Mrp (Maximum Retail Price)
- Discount Percentage
- Number Of Ratings
- Number Of Reviews
- Upc
- Star Rating
- Ram

The dataset is provided as a CSV file, and it should be saved in the same directory as the Python script.

*Code Explanation

The Python script contains the following main sections:

1. Importing Libraries: The necessary libraries (pandas, numpy, plotly) are imported.

2. Loading the Dataset: The dataset is loaded into a pandas DataFrame for further analysis.

3. Data Analysis:
   - The highest-rated iPhones are sorted based on the 'Star Rating' column, and the top 10 are selected.
   - Basic information about the dataset is printed using `print(rajssdata.head())`, `print(rajssdata.isnull().sum())`, and `print(rajssdata.describe())`.

4. Data Visualization:
   - A scatter plot is created to visualize the relationship between 'Number Of Ratings' and 'Discount Percentage' using plotly express.

*How to Run the Code

1. Install the required libraries (pandas, numpy, plotly) if you haven't already.

2. Save the provided dataset in a CSV file named "apple_products.csv" in the same directory as the Python script.

3. Open your terminal or command prompt and navigate to the directory where the Python script is located.

4. The code will load the dataset, perform analysis, and display the scatter plot.

