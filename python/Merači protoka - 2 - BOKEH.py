#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bokeh.plotting import figure
from bokeh.io import output_file, output_notebook, show
from bokeh.models import DatetimeTickFormatter, BoxSelectTool
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown
import pandas

# GET-WinSystemLocale


# In[2]:


# data

dtypes = {'vreme': 'str', 'I-1-LJB':'float', 'I-2-DIV':'float', 'I-3-MOK':'float','I-4-KR1':'float','I-4-KR2':'float','I-5-STU':'float','I-6-MLJ':'float','I-7-M10':'float','I-7-M11':'float','I-7-M2':'float'}
parse_dates = ['vreme']
df = pandas.read_csv("SCADA_2020.csv", sep=',', header=0, dtype=dtypes, parse_dates=parse_dates, infer_datetime_format=True)
df.set_index("vreme", inplace=True)

vreme = df.index
LJB = df['I-1-LJB']
DIV = df['I-2-DIV']
MOK = df['I-3-MOK']
KR1 = df['I-4-KR1']
KR2 = df['I-4-KR2']
STU = df['I-5-STU']
MLJ = df['I-6-MLJ']
M10 = df['I-7-M10']
M11 = df['I-7-M11']
M20 = df['I-7-M2']

# print(df.columns) 
# print(df.index[0])
# print(df['I-1-LJB'][0], type(df['I-1-LJB'][0]))

# x, y
# output_file("izvorišta_csv.html")

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
f = figure(plot_width=1500, plot_height=500, x_axis_type='datetime', tools=TOOLS)

f.title.text="Мерачи Протока НИВОС"
# f.xaxis.formatter=DatetimeTickFormatter(hours=["%d %B %Y"],days=["%d %B %Y"],months=["%d %B %Y"],years=["%d %B %Y"])
f.xaxis.formatter=DatetimeTickFormatter(hours=["%H:%M"],days=["%d %B"],months=["%B %Y"],years=["%Y"])

f.line(vreme, LJB, color="brown")
f.line(vreme, DIV, color="red")
f.line(vreme, MOK, color="purple")
f.line(vreme, KR1, color="orange")
f.line(vreme, KR2, color="yellow")
f.line(vreme, STU, color="cyan")
f.line(vreme, MLJ, color="green")
f.line(vreme, M10, color="blue")
f.line(vreme, M11, color="skyblue")
f.line(vreme, M20, color="powderblue")

show(f)


# In[5]:


# data

# 'M-100-120-9', 'M-10-100-11', 'M-10-20-1', 'M-10-20-12', 'M-10-40-3', 'M-10-40-4', 'M-10-50-5',
# 'M-10-60-6', 'M-10-80-7', 'M-10-80-8', 'M-10-90-10', 'M-10-90-32', 'M-120-150-28', 'M-20-100-15',
# 'M-20-30-14', 'M-20-30-22', 'M-20-40-18', 'M-20-40-21', 'M-20-50-23', 'M-40-50-16', 'M-50-60-19',
# 'M-80-140-29', 'M-90-91-20'
        
dtypes = {'vreme': 'str',
          'I-1-LJB':'float',
          'I-BBV-2':'float',
          'BBV_II-8':'float',
          'I-2-DIV':'float',
          'I-3-MOK':'float',
          'I-4-KR1':'float',
          'I-4-KR2':'float',
          'I-V-6':'float',
          'M-20-992-13':'float',
          'M-20-992-27':'float',
          'M-170-992-34':'float',
          'M-190-21-35':'float',
          'MRB':'float', 
          'III-8':'float',
          'M-70-81-17':'float',
          'I-5-STU':'float',
          'I-6-MLJ':'float',
          'I-7-M10':'float',
          'I-7-M11':'float',
          'I-7-M2':'float'
         }
parse_dates = ['vreme']
df = pandas.read_csv("SCADA_2020.csv", sep=',', header=0, dtype=dtypes, parse_dates=parse_dates, infer_datetime_format=True)
df.set_index("vreme", inplace=True)

vreme = df.index
LJB = df['I-1-LJB']
BNI = df['I-BBV-2']
BAB = df['BBV_II-8']
DIV = df['I-2-DIV']
MOK = df['I-3-MOK']
KR1 = df['I-4-KR1']
KR2 = df['I-4-KR2']
VIN = df['I-V-6'] 
VN1 = df['M-20-992-13'] 
VN2 = df['M-20-992-27'] 
VN3 = df['M-170-992-34'] 
VN4 = df['M-190-21-35'] 
MRB = df['MRB'] 
MET = df['III-8'] 
BUB = df['M-70-81-17'] 
STU = df['I-5-STU']
MLJ = df['I-6-MLJ']
M10 = df['I-7-M10']
M11 = df['I-7-M11']
M20 = df['I-7-M2']


TOOLS = "xpan, xwheel_zoom, box_zoom, reset, save"
f = figure(
           plot_width=1500,
           plot_height=500,
           x_axis_type='datetime',
           y_range=(0, 800),
           tools=TOOLS,
           active_scroll='xwheel_zoom',
           background_fill_color="#f9f9f9"
          )
f.add_tools(BoxSelectTool(dimensions="width"))

f.title.text="Мерачи Протока НИВОС"
f.title.text_color="blue"
f.title.text_font="arial"
f.title.text_font_style="bold"
f.title.text_font_size="14pt" # "1.5em" 
f.title.text_alpha=1 #floating point between 0 (transparent) and 1 (opaque)

f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Време"
f.yaxis.axis_label="Проток (лит/сек)" 

f.xaxis.formatter=DatetimeTickFormatter(hours=["%H:%M"],days=["%d %B"],months=["%B %Y"],years=["%Y"])

f.toolbar.autohide = True

# f.line(vreme, LJB, color="brown")
# f.line(vreme, BNI, color="red")
# f.line(vreme, BAB, color="purple")
# f.line(vreme, DIV, color="red")
# f.line(vreme, MOK, color="purple")
# f.line(vreme, KR1, color="orange")
# f.line(vreme, KR2, color="yellow")
# f.line(vreme, VIN, color="blue")
# f.line(vreme, VN1, color="green")
# f.line(vreme, VN2, color="lightseagreen")
# f.line(vreme, VN3, color="cyan")
# f.line(vreme, VN4, color="lightsteelblue")
# f.line(vreme, STU, color="cyan")
# f.line(vreme, MLJ, color="green")
f.line(vreme, M10, color="blue")
f.line(vreme, M11, color="skyblue")
f.line(vreme, M20, color="powderblue")

menu = [("Option 1", "item_1"), ("Option 2", "item_2")]
dropdown = Dropdown(label="Dropdown Menu", button_type="warning", menu=menu)
show(f)


# In[ ]:



menu = [("Option 1", "item_1"), ("Option 2", "item_2")]

#Create the Dropdown

dropdown = Dropdown(label="Dropdown Menu", button_type="warning", menu=menu)

#Output the dropdown menu

output_file("dropdown.html")

show(widgetbox(dropdown))

