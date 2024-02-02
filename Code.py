import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data back from CSV
df_read = pd.read_csv('genotype_data.csv', index_col=0)

# Plot heatmap with dendrogram
clustermap = sns.clustermap(df_read, method='average', cmap='viridis', figsize=(12, 12),
                            cbar_kws={'label': 'Score'})

# Show all row and column labels
clustermap.ax_heatmap.set_xticks(range(len(df_read.columns)))
clustermap.ax_heatmap.set_xticklabels(df_read.columns, rotation=90, ha='right')
clustermap.ax_heatmap.set_yticks(range(len(df_read.index)))
clustermap.ax_heatmap.set_yticklabels(df_read.index)

# Display the plot
plt.title('')
plt.show()
