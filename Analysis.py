
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv(r"C:\Users\saini\Downloads\archive (2)\zomato.csv")


#Basic cleaning and analysis of the data
dfdata = data.copy()
dfdata.drop(['url','address','phone','reviews_list','menu_item'], axis=1, inplace=True)
print(dfdata.head(5))
print(dfdata.info())
print(dfdata.describe())
print(dfdata.isnull().sum())
print(dfdata.dropna(inplace=True))

# Restaurant Distribution by Location (Top 10)
location_counts = dfdata['location'].value_counts().head(10)  # Get the top 10 locations with the most restaurants
plt.figure(figsize=(10, 6)) # Set the figure size for better visibility
sns.barplot(x=location_counts.values, y=location_counts.index, palette='viridis')  #viridis is a color palette in seaborn
plt.title('Top 10 Locations by Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('Location')
plt.show()


# Rating Distribution
plt.figure(figsize=(12 , 6))  # Set the figure size for better visibility
sns.histplot(dfdata['rate'], bins=20, kde=True, palette='viridis')  #viridis is another color palette in seaborn
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.xticks(fontsize=10 , rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()


# Cost vs Rating (Boxplot)
plt.figure(figsize=(14, 6))  # Set the figure size for better visibility
sns.boxplot(x='rate', y='approx_cost(for two people)', data=dfdata, palette='viridis' )  #viridis is a color palette in seaborn
plt.title('Cost for Two People vs Restaurant Rating')
plt.xlabel('Rating')
plt.ylabel('Approximate Cost for Two People')
plt.xticks(fontsize=10 , rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()


# Online Order vs Rating
plt.figure(figsize=(8,5))
sns.barplot(x='online_order',
            y='rate',
            data=dfdata,
            palette='viridis')  #viridis is a color palette in seaborn
plt.title("Average Rating by Online Order Availability")
plt.xlabel("Online Order Availability")
plt.ylabel("Average Rating")
plt.xticks(fontsize=10 , rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()


# Votes vs Rating (Most Important)
plt.figure(figsize=(10, 6))  # Set the figure size for better visibility
sns.scatterplot(x='votes', y='rate', data=dfdata, palette='viridis')  #viridis is a color palette in seaborn
plt.title('Votes vs Restaurant Rating') 
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.xticks(fontsize=10 , rotation=45)  # Rotate x-axis labels for
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()  


# Correlation Heatmap
plt.figure(figsize=(8,6))
numeric_cols = dfdata.select_dtypes(include=['float64','int64']) # Select only numeric columns for correlation analysis
correlation_matrix = numeric_cols.corr()
sns.heatmap(correlation_matrix,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=0.5)
plt.title("Correlation Heatmap of Zomato Dataset", fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()


# Top 10 Cuisines -  pie chart   
cuisine_counts = dfdata['cuisines'].value_counts().head(10)
plt.figure(figsize=(8, 8))
plt.pie(cuisine_counts.values, labels=cuisine_counts.index, autopct='%1.1f%%' , explode=[0.1]*10, colors=sns.color_palette('viridis', n_colors=10))  #viridis is a color palette in seaborn 
plt.title('Top 10 Cuisines')
plt.show()
