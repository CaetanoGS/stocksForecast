import stocker

class Stocker:
    def __init__(self, ticker):
        result = stocker.predict.tomorrow(ticker)
        self.value = result[0]
        self.error = result[1]
        self.date = result[2]
        super().__init__()
    
    def getTomorrowPrice(self, ticket):

        return 'Oi'
