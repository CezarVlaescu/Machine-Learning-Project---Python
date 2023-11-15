from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class AvailabilityPredictor:
    def __int__(self, historical_data):
        self.model = self.train_model(historical_data)

    def train_model(self, data):
        X_train, X_test, y_train, y_test = train_test_split(data['features'], data['labels'], test_size=0.2, random_state=42)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model Accuracy: {accuracy}")

        return model

    def predict_availability(self, features):
        prediction = self.model.predict(features)
        return prediction
