import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '851Y5H2DI9T3F1AK'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='GME', interval = '1min', outputsize = 'full')

close_data = data['4. close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.005:
    print("GME Alert!:" + str(last_change))
    variables['alert_string'] = "GME Alert!:" + str(last_change)
