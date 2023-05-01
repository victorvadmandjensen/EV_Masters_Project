import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# import seaborn as sns

df = pd.read_excel("energy_per_round.xlsx")
print(df)

# REMEBEMBER that you need more than one round to see the stacked chart!
plt.stackplot(df["Round"], df["Red"],df["Blue"],df["Yellow"],df["Green"], labels=["Red", "Blue", "Yellow", "Green"], colors=["#DE7162", "#A7E8F1", "#F0E963", "#2F8E4B"])
plt.xlabel("Round")
plt.ylabel("Energy sent to the community battery by players")
plt.title("Energy sent to the community battery in every round")
plt.xlim( (1, 12) )
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([-3,0,3,6,9,12,15,18,21,24,27,30])
#plt.locator_params(axis="y", integer=True, tight=True)
#tick_spacing = 1
plt.ylim(-3, )
plt.legend(loc="upper left")

plt.show()