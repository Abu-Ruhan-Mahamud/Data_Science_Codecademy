import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for i in columns:
  sns.countplot(x=df[i], order=df[i].value_counts().index, palette='ch:s=.25,rot=-.25')
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(i, fontsize=12)
  plt.title('{} Value Counts'.format(i))
  plt.show()
  plt.clf()

for i in columns:
    if i in ['Veil Type', 'Veil Color']:
        print ('No informative data available for {}'.format(i))
    elif len(df[i].unique()) < 3:
        sns.set_palette("Paired")
        plt.pie(df[i].value_counts(), labels=df[i].value_counts().index)
        plt.axis("equal")
        plt.title('{} VALUE COUNTS'.format(i.upper()), color='blue', fontsize=14)
        plt.show()
        plt.clf()
    else:
        sns.countplot(x=df[i], order=df[i].value_counts().index, palette= 'Spectral')
        plt.xticks(rotation=30, fontsize=10)
        plt.xlabel(i, fontsize=12)
        plt.title('{} VALUE COUNTS'.format(i.upper()), color='blue', fontsize=14)
        plt.show()
        plt.clf()


df['Veil Type'].unique()
