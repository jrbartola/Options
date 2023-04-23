from math import log, sqrt
from scipy.stats import norm


def black_scholes(S, X, D, volatility):
    T = D / 365
    z = (log(S / X) - (0.5 * volatility**2) * T) / (volatility * sqrt(T))
    probability = norm.cdf(z)
    print(
        f"Probability the stock will be higher than {X} price in {D} days:", probability
    )


S = 165  # current stock price
X = 172.47  # target price
D = 40  # number of days until target date
annual_volatility = 0.21

for i in range(150, 180):
    black_scholes(S, i, D, annual_volatility)
