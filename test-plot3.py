from matplotlib import rcParams
rcParams['font.family'] = "Times New Roman"
import numpy as np
import matplotlib.pyplot as plt

N = 3

width = 0.85       # the width of the bars: can also be len(x) sequence
ind = np.arange(N)    # the x locations for the groups
p1 = plt.bar(ind, [0, 43, 0], width, color='#f2f2f2')
p2 = plt.bar(ind, [0, 17, 0], width, color='#999999', bottom=43)
p3 = plt.bar(ind, [0, 13, 0], width, color='#808080', bottom=60)
p4 = plt.bar(ind, [0, 7, 0], width, color='#595959', bottom=73)
p5 = plt.bar(ind, [0, 6, 0], width, color='#cccccc', bottom=80)
p6 = plt.bar(ind, [0, 3, 0], width, color='#737373', bottom=86)
p7 = plt.bar(ind, [0, 3, 0], width, color='#b3b3b3', bottom=89)
p8 = plt.bar(ind, [0, 2, 0], width, color='#d9d9d9', bottom=92)
p9 = plt.bar(ind, [0, 2, 0], width, color='#040404', bottom=94)
p0 = plt.bar(ind, [0, 4, 0], width, color='#8c8c8c', bottom=96)




plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('', 'G1', ''))
plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0],p6[0],p7[0],p8[0],p9[0],p0[0]), ('Collision 16','Collision 12','Collision 15','Ion Proton 16','Collision 11','Proton Helium 16','Lead 15','Proton Ion 16','Collision 10','Other'))

plt.show()

'''
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')

 


# library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
 
# Make data
data = pd.DataFrame({  'group_A':[1], 'group_B':[2], 'group_C':[2], }, index=range(1,6))
 

# We need to transform the data from raw data to percentage (fraction)
data_perc = data.divide(data.sum(axis=1), axis=0)
 
# Make the plot
plt.stackplot(range(1,6),  data_perc["group_A"],  data_perc["group_B"],  data_perc["group_C"], labels=['A','B','C'])
plt.legend(loc='upper left')
plt.margins(0,0)
plt.title('100 % stacked area chart')
plt.show()

r = [0]
raw_data = {'greenBars': [20], 'orangeBars': [5],'blueBars': [2]}
df = pd.DataFrame(raw_data)

# plot
barWidth = 0.55
names = ('A')

for d in data:
    plt.bar(r, d[0], edgecolor='white', width=barWidth, label=d[1])

#plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth, label="group B")
# Create blue Bars
#plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white', width=barWidth, label="group C")

# Custom x axis
plt.xticks(r, names)
plt.xlabel("group")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# Show graphic
plt.show()
'''
