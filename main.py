from analysis.vertical_analysis import analyze_verticals



if __name__ == '__main__':
    data = analyze_verticals('SPY', 'CALL', 'CREDIT', max_strike_width=10)
    thirty_days = data[30]

    spreads = sorted([thirty_days[strkey] for strkey in thirty_days.keys()], key=lambda x: x.expected_profit())

    for spread in spreads:
        print(spread, spread.expected_profit() * 100, spread.credit_percentage)