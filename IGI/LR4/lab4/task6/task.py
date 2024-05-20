import pandas as pd

class Task6:
    def __init__(self):
        data = pd.read_csv("task6/Coffee_Qlty.csv")
        print("Robusta mean sweetness: ")
        print(data[data["Species"] == "Robusta"]["Sweetness"].mean())
        print("Arabica mean sweetness: ")
        print(data[data["Species"] == "Arabica"]["Sweetness"].mean())

        print("The sweetest coffee in 2014 from: ")
        print(data[data["Harvest.Year"] == 2014].sort_values(["Sweetness"], ascending=False).iloc[0]["Country.of.Origin"])

        print("Country with most defected coffee")
        print(data[data["Category.One.Defects"] > 5]["Country.of.Origin"].mode().iloc[0])
