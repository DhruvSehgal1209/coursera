class BaselineModel:
    def fit(self, X, y):
        self.mean = sum(y) / len(y)

    def predict(self, X):
        return [self.mean for _ in X]
