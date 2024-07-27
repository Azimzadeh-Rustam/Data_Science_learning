from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

try:
    import common
    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / 'data'

AIRLINE_STATS_CSV = DATA / 'airline_stats.csv'

airline_stats = pd.read_csv(AIRLINE_STATS_CSV)
ax = airline_stats.boxplot(by='airline', column='pct_carrier_delay',
                           figsize=(5, 5))
ax.set_xlabel('')
ax.set_ylabel('Daily % of Delayed Flights')
plt.suptitle('')

plt.tight_layout()
plt.show()
