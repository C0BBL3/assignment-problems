import matplotlib.pyplot as plt
plt.style.use('bmh')
coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH', 'TTH', 'TTH', 'TTH', 'THT', 'TTH', 'HTH', 'HTH', 'TTT', 'HTH', 'HTH', 'TTH', 'HTH', 'TTT', 'TTT', 'TTT', 'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH', 'THH', 'HHH', 'HHH', 'HTT', 'TTH', 'TTH', 'HHT', 'TTH', 'HTH', 'HHT', 'THT', 'THH', 'THT', 'TTH', 'TTT', 'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH', 'HHT', 'HHT', 'HHH', 'TTT', 'THH', 'HHH', 'HHH', 'TTH', 'THH', 'THH', 'TTH', 'HTT', 'TTH', 'HTT', 'HHT', 'TTH', 'HTH', 'THT', 'THT', 'HTH']
plt.plot([i for i in range(0, 25)], [coin_1[i].count('H') for i in range(0, 25)], linewidth=1)
plt.plot([i for i in range(0, 25)], [coin_2[i].count('H') for i in range(0, 25)], linewidth=1)
plt.plot([i for i in range(0, 25)], [coin_3[i].count('H') for i in range(0, 25)], linewidth=1)
plt.legend(['P_1(x)', 'P_2(x)', 'P_3(x)'])
plt.ylabel('Number of Heads per Sample')
plt.xlabel('Sample Number')
plt.title('Detecting Biased Coins')
plt.savefig('plot.png')
plt.show()
