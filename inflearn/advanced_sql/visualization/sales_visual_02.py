import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs = [[{"secondary_y": True}]])


fig.update_layout(barmode = 'group', xaxis_tickangle = 45)

fig.update_xaxes(type='')
fig.show()