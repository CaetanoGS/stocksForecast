# Necessary imports

import stocker

# Running stocker to create a model and predict the tomorrow stock price

class Stocker:
    def __init__(self, ticker):
        result = stocker.predict.tomorrow(ticker)
        self.value = result[0]
        self.error = result[1]
        self.date = result[2]
        super().__init__()
    
