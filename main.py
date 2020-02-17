from trades.iron_condor_finder import find_profitable_iron_condors
from trades.vertical_finder import find_profitable_verticals

if __name__ == '__main__':
    find_profitable_verticals('MSFT', 'CALL')
    find_profitable_verticals('MSFT', 'PUT')