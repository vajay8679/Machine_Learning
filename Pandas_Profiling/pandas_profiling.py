import seaborn as sns

df = sns.load_dataset('tips')
# print(df.head())

from pandas_profiling import ProfileReport
profile = ProfileReport(df,explorative=True)
profile.to_file('output.html')