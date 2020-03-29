
prob_profit_gt = lambda prob: lambda spread: spread.prob_profit() > prob

expected_profit_gt = lambda profit: lambda spread: spread.expected_profit() > profit

credit_percentage_gt = lambda credit_pct: lambda spread: spread.credit_percentage and spread.credit_percentage > credit_pct

max_profit_gt = lambda amt: lambda spread: spread.max_profit > amt
