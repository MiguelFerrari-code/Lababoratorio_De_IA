import pandas as pd

dfs = pd.read_html('/home/alunos/Lababoratorio_De_IA/PMC3/PMC3.md')
print(len(dfs))
for i, df in enumerate(dfs):
    print(f"Table {i} shape: {df.shape}")

