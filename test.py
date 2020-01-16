import matplotlib.pyplot as plt
import numpy as np

class Trade(object):
    def __init__(self, prob_profit, max_profit, max_loss):
        self.prob_profit = prob_profit
        self.max_profit = max_profit
        self.max_loss = max_loss
    
    def expected_profit(self):
        return self.prob_profit * self.max_profit - (1 - self.prob_profit) * self.max_loss

def simulate_portfolio(balance, trade, num_trades=10000):
    from random import uniform

    balances = [balance]
    curr_balance = balance
    
    for _ in range(num_trades):
        if uniform(0, 1) < trade.prob_profit:
            curr_balance += trade.max_profit
        else:
            curr_balance -= trade.max_loss
        
        if curr_balance < 0:
            # print("Hit zero. Exiting...")
            return curr_balance, balances
        
        balances.append(curr_balance)
    return curr_balance, balances

def tally_defaults(trials=1000):
    sixty_pop = Trade(0.6, 220, 280)

    initial_balances = [1000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12500, 15000, 17500, 20000]
    prob_default = np.array([])

    for balance in initial_balances:
        num_negative = 0
        for _ in range(trials):

            end_balance, _ = simulate_portfolio(balance, sixty_pop)
            if end_balance < 0:
                num_negative += 1
        
        prob_default = np.append(prob_default, num_negative / trials)
    
    y_pos = np.arange(len(initial_balances))

    plt.bar(y_pos, prob_default)
    plt.xlabel('Initial Balance')
    plt.ylabel('Probability of default')
    plt.xticks(y_pos, initial_balances)
    plt.show()



if __name__ == '__main__':
    tally_defaults()    

    # starting_balance = 10000
    # sixty_pop = Trade(0.6, 250, 300)

    # final_balance, balances = simulate_portfolio(starting_balance, sixty_pop)

    # plt.plot(balances)
    # plt.show()
