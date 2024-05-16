import pandas as pd
import plotly.express as px

# Import bacteria and fungi taxonomy csv datasets
bacteria = pd.read_csv('taxonomy/bac_tax_div.csv')
fungi = pd.read_csv('taxonomy/fun_tax_div.csv')

# Group the bacteria phyla
bacteria['Normalize_totalK'] = bacteria.groupby('Phylum')['totalK'].transform(lambda x: x / x.sum())
# Tree map of all bacteria phyla
fig = px.treemap(bacteria, path=['Phylum', 'Class', 'Order'], values='Normalize_totalK')

# Tree map of the top 5 bacteria phyla by diversity
top5_Phyla = 5
top_Phyla = bacteria.sort_values('totalK', ascending=False).head(top5_Phyla)
fig = px.treemap(top_Phyla, path=['Phylum'], values='totalK',title=f'Top 5 Bacteria Phyla by Diversity')

# Group the fungal phyla
fungi['Normalize_totalK'] = fungi.groupby('Phylum')['totalK'].transform(lambda x: x / x.sum())
# Tree map of the fungal phyla 
fig = px.treemap(fungi, path=['Phylum', 'Class', 'Order'], values='Normalize_totalK')

# Tree map of the top 2 fungal phyla by diversity
top5_Phyla = 2
top_Phyla = fungi.sort_values('totalK', ascending=False).head(top5_Phyla)
fig = px.treemap(top_Phyla, path=['Phylum'], values='totalK',title=f'Top 2 Fungi Phyla by Diversity')
