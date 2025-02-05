import pandas as pd 
import matplotlib.pyplot as plt
import mplcursors

data = pd.read_csv("penglings.csv")

colors = {'Adelie': '#FF4500', 'Gentoo': '#FF0000', 'Chinstrap':'#7FFF00'}

plot = plt.scatter(data['flipper_length_mm'], data['body_mass_g'], s=data['bill_length_mm'], c=data['species'].map(colors), alpha=0.8)

# hover label 
mplcursors.cursor(plot, hover=True).connect("add", lambda sel: sel.annotation.set_text(
    f"Species: {data.iloc[sel.target.index]['species']}\n"
    f"Flipper Length (mm): {data.iloc[sel.target.index]['flipper_length_mm']}\n"
    f"Body Mass (g): {data.iloc[sel.target.index]['body_mass_g']}\n"
    f"Bill Length (mm): {data.iloc[sel.target.index]['bill_length_mm']}"
))


# color mapping legend
for species, color in colors.items():
    plt.scatter([], [], c=color, label=species)  

plt.legend()
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()