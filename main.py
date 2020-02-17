from trades.iron_condor_finder import find_profitable_iron_condors
from trades.vertical_finder import find_profitable_verticals

from settings import update_df_display_settings

if __name__ == '__main__':
    update_df_display_settings()
    # find_profitable_verticals('MSFT', 'CALL')
    # find_profitable_verticals('MSFT', 'PUT')
    find_profitable_iron_condors('SPY')