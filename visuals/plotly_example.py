#Bar Graph
import plotly.graph_objects as go  # import plotly
fig = go.Figure(data=go.Bar(y=[3, 5, 1, 2, 4])) # create a figure
fig.write_html('figure.html') # export to HTML file

#Scatter Plot Graph
import plotly.express as pe
fig1 = pe.scatter(x=[0,1,2,3], y=[4,5,6,7])
fig1.write_html("scatter.html")


df = pe.data.iris()
print(df.head())
fig2 = pe.scatter(df, x="sepal_width", y="sepal_length", color="species", size="petal_length", hover_data=["petal_width"])
fig2.write_html("iris_scatter.html")

