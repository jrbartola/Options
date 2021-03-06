import argparse

from trades.iron_condor_finder import find_iron_condors
from trades.vertical_finder import find_verticals

from settings import update_df_display_settings
from constants.contracts import CONTRACT_TYPES
from constants.strategies import IRON_CONDOR, CREDIT_VERTICAL

def get_arguments():
    parser = argparse.ArgumentParser(description='Find options trades.')
    parser.add_argument('--symbol', help='The (optionable) underlying symbol', required=True)
    parser.add_argument('--strategy', help='The strategy to search for (see docs)', required=True)
    parser.add_argument('--contract', help='The type of contract to search for (CALL or PUT)', required=False)

    return parser.parse_args()

if __name__ == '__main__':
    # Needed so that the dataframes show all row/column values
    update_df_display_settings()

    args = get_arguments()
    symbol = args.symbol
    
    if args.strategy == IRON_CONDOR:
        print(find_iron_condors(symbol))
    
    elif args.strategy == CREDIT_VERTICAL:
        if not args.contract:
            raise AttributeError('Argument `--contract` must be supplied with the CREDIT_VERTICAL strategy')

        if args.contract not in CONTRACT_TYPES:
            raise ValueError(f'Argument `--contract` must be either `CALL` or `PUT`. Got `{args.contract}`')

        print(find_verticals(symbol, args.contract))

    else:
        raise ValueError(f'Invalid strategy `{args.strategy}`. See docs for possible values')