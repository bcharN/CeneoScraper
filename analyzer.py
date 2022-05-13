import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")



product_num="91714422"
#product_num=(input("enter product number: ")

opinions = pd.read_json(f"./opinions/{product_num}.json")
print(opinions)


opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",".")))

opinions_count = len(opinions.index)
#opnions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum() 
avaerage_score = opinions.stars.mean().round(2)

recommendation = opinions.recommendation.value_counts(dropna = False).sort_index().reindex(["Nie Polecam","Polecam",None])
recommendation.plot.pie(
    label="",
    autopct="%1.1f%%",
    colors=["crimson","lightskyblue","forestgreen"],
    labels = ["Nie polecam","Polecem","Nie mam zdania"]
    )




plt.title("recomendacja")
plt.savefig(f"plots/{product_num}_recommendations.png")
plt.close()

stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar()
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.xticks(rotation=0)
plt.savefig(f"plots/{product_num}_stars.png")
plt.close()


#pandas tabela przestawna w pandas