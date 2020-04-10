
from options.constants.search_criteria import PROBABILITY_PROFIT, EXPECTED_PROFIT, CREDIT_PERCENT

class SpreadFilter(object):
    def __init__(self, filter_type, comparison_op, filter_value):
        self.filter_type = filter_type
        self.comparison_op = comparison_op
        self.filter_value = filter_value
    
    def filter(self, spread):
        actual_value = None

        if self.filter_type == PROBABILITY_PROFIT:
            actual_value = spread.prob_profit()
        if self.filter_type == EXPECTED_PROFIT:
            actual_value = spread.expected_profit()
        if self.filter_type == CREDIT_PERCENT:
            actual_value = spread.credit_percentage

        if actual_value is None:
            raise ValueError(f'Invalid filter type specified: {self.filter_type}')

        if self.comparison_op == 'GT':
            return actual_value > self.filter_value
        if self.comparison_op == 'GTEQ':
            return actual_value >= self.filter_value
        if self.comparison_op == 'EQ':
            return actual_value == self.filter_value
        if self.comparison_op == 'LT':
            return actual_value < self.filter_value
        if self.comparison_op == 'LTEQ':
            return actual_value <= self.filter_value
        if self.comparison_op == 'NEQ':
            return actual_value != self.filter_value

        raise ValueError(f'Invalid comparison op specified: `{self.comparison_op}`')
