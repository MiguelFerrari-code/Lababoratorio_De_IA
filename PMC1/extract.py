import pandas as pd

dfs = pd.read_html('/home/alunos/Lababoratorio_De_IA/PMC1/PMC1.md')

print("Test Set:")
print(dfs[0].head())

print("Training Set:")
print(dfs[1].head())

