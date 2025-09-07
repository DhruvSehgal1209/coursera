import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from baseline_model import BaselineModel
import joblib

def train_and_save_model():
    data = pd.read_csv('data/sample_data.csv')
    X = data.drop('sales', axis=1)
    y = data['sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)

    preds = rf.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
    print(f"Random Forest RMSE: {rmse}")

    joblib.dump(rf, 'models/rf_model.joblib')

if __name__ == "__main__":
    train_and_save_model()
