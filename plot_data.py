import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


col_names = ['datetime','ignore','humidity','temperature','hic']
df = pd.read_csv('data/temp_humid_data.csv', header=None, names=col_names)
df['datetime'] = pd.to_datetime(df['datetime']) 

def plot_data(metric):
    sns.scatterplot(data=df, x='datetime', y=metric)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'plots/{metric}_plot.png')
    plt.close()

plot_data('temperature')
plot_data('humidity')

