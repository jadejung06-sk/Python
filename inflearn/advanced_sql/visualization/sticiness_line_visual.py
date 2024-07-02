
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#  일주일 간 stickiness, 평균 stickiness
query = r'''select *, round(100.0 * dau/mau, 2) as stickiness
	,round(avg(100.0 * dau/mau) over(), 2) as avg_stickiness
from ga.daily_acquisitions
where curr_date between to_date('2016-10-25', 'yyyy-mm-dd') and to_date('2016-10-31', 'yyyy-mm-dd')'''

df = pd.read_sql_query(sql = query, con = postgres_engine)


fig = make_subplots(specs = [[{"secondary_y": True}]])


fig.update_layout(barmode = 'group', xaxis_tickangle = 45)

fig.update_xaxes(type='')
fig.show()