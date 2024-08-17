import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Importing the dataset
data = pd.read_csv('train.csv')

#Preprocessing
data = data.dropna()

# Features and target
X = data.drop('price_range', axis=1)
y = data['price_range']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Testing model
preds = model.predict(X_test)
correct_preds = sum(a == b for a, b in zip(y_test, preds))
print(f"Accuracy of model : {correct_preds*100/len(preds)}%")

# Save the model
joblib.dump(model, 'mobile_price_model.pkl')