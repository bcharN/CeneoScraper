import os
import pandas as pd
import matplotlib as mpl

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")



product_num="91714422"
#product_num=(input("enter product number: ")

opinions = pd.read_json(f"./opinions/{product_num}.json")
print(opinions)

