from analysis.vertical_analysis import analyze_verticals



if __name__ == '__main__':
    data = analyze_verticals('SPY', 'CALL', 'CREDIT', max_strike_width=10)
    thirty_days = data[33]

    spreads = sorted([thirty_days[strkey] for strkey in thirty_days.keys()], key=lambda x: x.expected_profit())
    filtered_spreads = [spread for spread in spreads if spread.credit_percentage and spread.credit_percentage > 0.3]

    for spread in filtered_spreads:
        high_leg = spread.high_leg
        low_leg = spread.low_leg
        print(high_leg.prob_itm(), low_leg.prob_otm())
        print(spread, spread.expected_profit() * 100, spread.credit_percentage)