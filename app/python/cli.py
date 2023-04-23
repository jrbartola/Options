import argparse
import sys
from pathlib import Path
import os
from pathlib import Path
from dotenv import load_dotenv


from options.api.auth import generate_access_token

from options.trades.iron_condor_finder import find_iron_condors
from options.trades.vertical_finder import find_verticals

from options.cli.settings import update_df_display_settings
from options.api.option_chain import get_option_chain
from options.constants.contracts import CONTRACT_TYPES
from options.constants.strategies import IRON_CONDOR, CREDIT_VERTICAL

# Load the .env file
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_arguments():
    parser = argparse.ArgumentParser(description="Find options trades.")
    parser.add_argument(
        "--symbol", help="The (optionable) underlying symbol", required=True
    )
    parser.add_argument(
        "--strategy", help="The strategy to search for (see docs)", required=True
    )
    parser.add_argument(
        "--contract",
        help="The type of contract to search for (CALL or PUT)",
        required=False,
    )

    return parser.parse_args()


def main():
    update_df_display_settings()
    # generate_access_token()
    os.environ[
        "TDAMERITRADE_REFRESH_TOKEN"
    ] = "2uLSrEdmFjDpiV5HclCiZJEyWPsnxPn/BKv3eTvd0jdrau9s6+KCqefbxTVwwF9fp2ftiTuoCkNIWq9kfjSC2HwOJMyCg5iQC39NAaSjZflJAcbwOXM/zEGiw8wcKZ85zyqxswblhhp21rTUJn67zxHdjfsL9pRIJ8WD8Foln1pdi04qjuWnVNnWWN9AaXfJXU4HAyVNiftHsZAyCixYxeQ3ePwTBDC+X64UqHJ45EUEzBraKETycvia8DFiPryJG4IjKRNeabPVRJj68fp++lgA2GQbrodmhQCrLParXKEaKubSMLq8vm/Fv05Plr0EgQ8wojCWZIQHL5Ue/lQOydUfSao1G/+M1ZUv0JkSAR+epss2XtxPt1XCUPIiFwB53cVaD8pW8HSYokpXlf/p8uRwuLgBlpySEFZWRHnR+74Ed0HWhAgbwjnzXD2100MQuG4LYrgoVi/JHHvlSoGURf85BE+7H0+Ut4EY6m7Pjn77c1kmMDJ9j7D3/2w7XpD9RuDZxZivdnXzpZdsGh1m/8MhAq0JuFEYrK1P1n1J91pMjrf1z5e8ZgTwAdu465BfZjnx4b9C7ZQz6GFLvHe6RS2BBzZIckogwf1ygPZ0dQPRm0Nm1hvVk/B/mUZqEPrGQ0XJsTitKW3RnS/0XruUJS0fr1amQE6AwH1VpLDIFlBGVYRUY1al4PZ1F5NuKPcgV9+CHSSQnt/n6hfSTPnKAHUSD7c0y6lEoE3U9RMywnOovu70K6JEBQ4sfcAv9AJDzuHtB12h54j2fAv9oZfMuPQHkGItokMlTdAS+xAN+WRK9zJUNqITikeQtW4sQoLv7Ui1YRzebzQYYv04SLuFPmohUnjwIdiVKh8brSdnJTGQoJM4YHZUB9BZnN/Sd/F0jwSBTUSAscA=212FD3x19z9sWBHDJACbC00B75E"
    # Needed so that the dataframes show all row/column values
    print(find_iron_condors("AAPL"))
    exit()


if __name__ == "__main__":
    main()
    # args = get_arguments()
    # symbol = args.symbol

    # if args.strategy == IRON_CONDOR:
    #     print(find_iron_condors(symbol))

    # elif args.strategy == CREDIT_VERTICAL:
    #     if not args.contract:
    #         raise AttributeError('Argument `--contract` must be supplied with the CREDIT_VERTICAL strategy')

    #     if args.contract not in CONTRACT_TYPES:
    #         raise ValueError(f'Argument `--contract` must be either `CALL` or `PUT`. Got `{args.contract}`')

    #     print(find_verticals(symbol, args.contract))

    # else:
    #     raise ValueError(f'Invalid strategy `{args.strategy}`. See docs for possible values')
