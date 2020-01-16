class Spread(object):

    @property
    def max_profit(self):
        raise NotImplementedError
    
    @property
    def max_loss(self):
        raise NotImplementedError

    def expected_profit(self):
        raise NotImplementedError

    def prob_profit(self):
        raise NotImplementedError