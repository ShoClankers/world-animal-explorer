import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species:", df['species'].unique())
print("Island:", df['island'].unique())

sns.histplot(data = df, x = 'Body_mass(g)', bins = 20, color = 'steelblue')
plt.title("Flipper legth shape by Species KDE")
plt.xlabel("FLipper length (mm)")
plt.show()

sns.kdeplot(data = df, x = 'flipper_length_mm', hue = 'species', fill = True)
plt.title("Flipper lenghth - histogram with KDE Curve")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Count")
plt.show()

sns.scatterplot(data = df, x = 'FLipper_lenghth_mm', y = 'body_mass_g', hue = 'species')
plt.title("Flipper length vs Body mass by Species")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap -  PEnguin Measurements")
plt.show()