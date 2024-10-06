import pandas as pd
from sklearn.linear_model import LinearRegression

# Loading the data
df = pd.read_csv('/Users/ayumikatsuya/Desktop/merged.csv')

# Removing 'mph' from Left_Speed and Right_Speed and check for missing values
df['Left_Speed_Clean'] = df['Left_Speed'].str.replace(' mph', '', regex=False)
df['Right_Speed_Clean'] = df['Right_Speed'].str.replace(' mph', '', regex=False)

# Converting to numeric
df['Left_Speed_Clean'] = pd.to_numeric(df['Left_Speed_Clean'], errors='coerce')
df['Right_Speed_Clean'] = pd.to_numeric(df['Right_Speed_Clean'], errors='coerce')
print(df)

# Selecting features for regression
df['Day_of_Week_Numeric'] = df['Day_of_Week'].astype('category').cat.codes
df['Stratum_Numeric'] = df['Stratum'].astype('category').cat.codes

# Separating rows with missing Left_Speed
train_data_left = df[df['Left_Speed_Clean'].notna()]
missing_data_left = df[df['Left_Speed_Clean'].isna()]

# Defining features and target for the regression model
features_left = ['Day_of_Week_Numeric', 'Stratum_Numeric']
X_train_left = train_data_left[features_left]
y_train_left = train_data_left['Left_Speed_Clean']

# Training a linear regression model
model_left = LinearRegression()
model_left.fit(X_train_left, y_train_left)

# Predicting missing Left_Speed values
X_missing_left = missing_data_left[features_left]
predictions_left = model_left.predict(X_missing_left)

# Filling missing Left_Speed values with predictions
df.loc[df['Left_Speed_Clean'].isna(), 'Left_Speed_Clean'] = predictions_left

# Separating rows with missing Right_Speed
train_data_right = df[df['Right_Speed_Clean'].notna()]
missing_data_right = df[df['Right_Speed_Clean'].isna()]

# Defining features and target for the regression model
features_right = ['Day_of_Week_Numeric', 'Stratum_Numeric']
X_train_right = train_data_right[features_right]
y_train_right = train_data_right['Right_Speed_Clean']

# Training a linear regression model
model_right = LinearRegression()
model_right.fit(X_train_right, y_train_right)

# Predicting missing Right_Speed values
X_missing_right = missing_data_right[features_right]
predictions_right = model_right.predict(X_missing_right)

# Filling missing Right_Speed values with predictions
df.loc[df['Right_Speed_Clean'].isna(), 'Right_Speed_Clean'] = predictions_right

# Checking for missing values
print(df.isnull().sum())

# Filling missing date values with the previous row's value
df.ffill(inplace=True)

# Converting date format from 'DD.MM.YYYY' to a standard date format
df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y', errors='coerce')

# Checking for NaT values
print(df['Date'].isnull().sum())

# Saving the cleaned DataFrame to a new CSV file
df.to_csv('/Users/ayumikatsuya/Desktop/cleaned_traffic_data.csv', index=False)
print("Saved to 'cleaned_traffic_data.csv'.")