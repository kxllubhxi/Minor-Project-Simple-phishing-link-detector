import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle

print("Loading data...")
data = pd.read_csv("DataFiles/phishing.csv")
data = data.drop(['Index'], axis=1)

y = data['class']
X = data.drop('class', axis=1)

print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Gradient Boosting Classifier...")
gbc = GradientBoostingClassifier(max_depth=4, learning_rate=0.7)
gbc.fit(X_train, y_train)

print("Saving model to newmodel.pkl...")
with open('newmodel.pkl', 'wb') as f:
    pickle.dump(gbc, f)

print("Done!")
