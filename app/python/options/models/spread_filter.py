
class SpreadFilter(object):
    def __init__(self, *args):
        self.criteria = list(args)

    def add_criteria(self, filter_fn):
        self.criteria.append(filter_fn)
        return self
    
    def get_filtered(self, spreads):
        passes_criteria = lambda spread: all(filter_fn(spread) for filter_fn in self.criteria)
        return [spread for spread in spreads if passes_criteria(spread)]
