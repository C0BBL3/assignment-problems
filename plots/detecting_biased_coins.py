import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from coin_flipping import probability

def make_graph_for_biased_coins(coin):
    result = [0, 0, 0, 0]
    for flips in coin:
        if flips.count('H') == 0:
            result[0] += 1 / len(coin)
            
        if flips.count('H') == 1:
            result[1] += 1 / len(coin)

        elif flips.count('H') == 2:
            result[2] += 1 / len(coin)
        
        elif flips.count('H') == 3:
            result[3] += 1 / len(coin)
    
    return result

plt.style.use('bmh')
coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH', 'TTH', 'TTH', 'TTH', 'THT', 'TTH', 'HTH', 'HTH', 'TTT', 'HTH', 'HTH', 'TTH', 'HTH', 'TTT', 'TTT', 'TTT', 'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH', 'THH', 'HHH', 'HHH', 'HTT', 'TTH', 'TTH', 'HHT', 'TTH', 'HTH', 'HHT', 'THT', 'THH', 'THT', 'TTH', 'TTT', 'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH', 'HHT', 'HHT', 'HHH', 'TTT', 'THH', 'HHH', 'HHH', 'TTH', 'THH', 'THH', 'TTH', 'HTT', 'TTH', 'HTT', 'HHT', 'TTH', 'HTH', 'THT', 'THT', 'HTH']
plt.plot([i for i in range(0, 4)], [probability(i, 3) for i in range(0, 4)], linewidth=2.5)
plt.plot([i for i in range(0, 4)], make_graph_for_biased_coins(coin_1), linewidth=1)
plt.plot([i for i in range(0, 4)], make_graph_for_biased_coins(coin_2), linewidth=1)
plt.plot([i for i in range(0, 4)], make_graph_for_biased_coins(coin_3), linewidth=1)
plt.legend(['True Distribution', 'P_1(x)', 'P_2(x)', 'P_3(x)'])
plt.ylabel('Probability')
plt.xlabel('Number of heads')
plt.title('True Distribution vs Coin sets')
plt.savefig('plot.png')
plt.show()

#coin set 1 is more tails biased
#coin set 2 is even
#coin set 3 is more head biased