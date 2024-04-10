# Load the Ames dataset
import pandas as pd
Ames = pd.read_csv('Ames.csv')

# Calculating the percentage of missing values for each column
missing_data = Ames.isnull().sum()
missing_percentage = (missing_data / len(Ames)) * 100
data_type = Ames.dtypes

# Combining the counts and percentages into a DataFrame for better visualization
missing_info = pd.DataFrame({'Missing Values': missing_data,
                             'Percentage': missing_percentage,
                             'Data Type': data_type})

# Sorting the DataFrame by the percentage of missing values in descending order
missing_info = missing_info.sort_values(by='Percentage', ascending=False)

# Display columns with missing values of 'object' data type
print(missing_info[(missing_info['Missing Values'] > 0) &
                   (missing_info['Data Type'] == 'object')])

mode_value = Ames['Electrical'].mode()[0]
Ames['Electrical'].fillna(mode_value, inplace=True)
print(mode_value)
print(Ames['Electrical'].isnull().sum())

missing_categorical = missing_info[(missing_info['Missing Values'] > 0)
                           & (missing_info['Data Type'] == 'object')]

for item in missing_categorical.index.tolist():
    Ames[item].fillna("None", inplace=True)

print(Ames[missing_categorical.index].isnull().sum())
