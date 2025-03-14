import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
lower_percentile = df['value'].quantile(0.025)
upper_percentile = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_percentile) & (df['value'] <= upper_percentile)]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df_line.index, df_line['value'], color='tab:blue')

    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='value')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_monthly = df_bar.groupby(['year', 'month']) ['value'].mean().unstack()

    
    fig, ax = plt.subplots(figsize=(12,6))
    df_monthly.plot(kind='bar', ax=ax, width=0.8, colormap='tab20')

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Daily Page Views')
    ax.set_title('Average Daily Page Views per Month')

    ax.legend(title='Months', labels= ['Jan', 'Feb', 'Mar', 'Apr','May',
                                        'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1,2, figsize=(15,6))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0], palette='coolwarm')
    ax[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='value')


    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], palette='coolwarm')
    ax[1].set(title='Month-wise Box Plot (Seansonality)', xlabel='Month', ylabel='value')

    ax[1].tick_params(axis='x', rotation=45)
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
