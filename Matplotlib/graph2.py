import matplotlib.pyplot as plt
Fruit = ["Apple","Bananas","Cherries","Dates"]
sold = [40,70,20,50]
plt.figure(figsize = (6,4))
plt.bar(Fruit,sold,color = ["red","yellow","black","brown"])
plt.xlabel("Fruits")
plt.ylabel("Quantity sold")
