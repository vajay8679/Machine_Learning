import pandas as pd
import dtale
import seaborn as sns


df = sns.load_dataset('titanic')


# print(df.head())

dtale.show(df)