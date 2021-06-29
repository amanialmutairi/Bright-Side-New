import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
  buffer = BytesIO()
  plt.savefig(buffer, format="png")
  buffer.seek(0)
  img = buffer.getvalue()
  g = base64.b64encode(img)
  g = g.decode("utf-8")
  buffer.close()
  return g

# create a plot function for different matplotlib plots
def line_plot(x, y):
  plt.figure(figsize=(6,5)) # you can set size
  plt.xticks(rotation=25)
  plt.plot(x,y)
  return get_graph()

def pie_plot(props, labels):
  
  plt.figure(figsize=(5.5,4))
  plt.pie(props, labels=labels, autopct='%1.1f%%')
  
  return get_graph()

def bar_plot(x, h):
  plt.figure(figsize=(4,4))
  plt.bar(x,h)
  return get_graph()