
# **Lesson 12 — Advanced Data Visualization Techniques**

## **Lesson Overview**
**Learning objective:** Students will learn to create advanced and interactive visualizations using Pandas, Plotly, and Dash. By the end of this lesson, students will understand how to visualize data directly from DataFrames, create interactive plots, and build simple dashboards for real-time data exploration.

### **Topics:**
1. Plotting with Pandas: Visualizing data directly from DataFrames.
2. Interactive Visualizations: Using Plotly for interactive plotting.
3. Dashboards: Creating dynamic dashboards with Plotly and Dash.

---

## **12.1 Plotting with Pandas**

### **Overview**
Pandas simplifies data visualization by providing built-in plotting methods for DataFrames and Series. These plots are suitable for quick data exploration and analysis.

### **Steps:**
1. Load data into a Pandas DataFrame.
2. Use `plot()` for line, bar, and other plots.

### **Example Code: Plotting with Pandas**
```python
import pandas as pd

# Load a dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300]
}
df = pd.DataFrame(data)

# Line Plot
df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")

# Bar Plot
df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
```

---

## **12.2 Interactive Visualizations with Plotly**

### **Overview**
Plotly is a library for creating interactive and visually appealing plots. It supports interactivity like hover tooltips, zooming, and panning.

### **Steps:**
1. Install Plotly:  
   ```bash
   pip install plotly
   ```
2. Use Plotly to create interactive scatter plots, bar charts, and more.

### **Example Code: Interactive Scatter Plot**
```python
import plotly.express as px

# Sample dataset
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 20, 15, 30],
    "Color": ["Group 1", "Group 2", "Group 1", "Group 2"]
})

# Create an interactive scatter plot
fig = px.scatter(df, x="Category", y="Value", color="Color",
                 title="Interactive Scatter Plot",
                 hover_data=["Value"])
fig.write_html("scatter_plot.html")  # Save as HTML file
fig.show()
```

---

## **12.3 Building Dashboards with Dash**

### **Overview**
Dash is a Python framework for building web-based interactive dashboards. It uses Plotly for visualizations and supports dynamic updates.

### **Steps:**
1. Install Dash:
   ```bash
   pip install dash
   ```
2. Create a Dash app with components like dropdowns and graphs.

### **Example Code: Simple Dashboard**
```python
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Sample dataset
df = pd.DataFrame({
    "Metric": ["Metric 1", "Metric 2", "Metric 3"],
    "Value": [100, 200, 150]
})

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="metric-dropdown",
        options=[{"label": metric, "value": metric} for metric in df["Metric"]],
        value="Metric 1"
    ),
    dcc.Graph(id="metric-graph")
])

# Callback for dynamic updates
@app.callback(
    Output("metric-graph", "figure"),
    [Input("metric-dropdown", "value")]
)
def update_graph(selected_metric):
    filtered_df = df[df["Metric"] == selected_metric]
    fig = px.bar(filtered_df, x="Metric", y="Value", title=f"{selected_metric} Value")
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
```

---

## **12.4 Reflection**

### **Differences Between Static and Interactive Visualizations:**
- **Static Visualizations:** Quick and easy to create, but lack interactivity.
- **Interactive Visualizations:** Allow users to explore data dynamically, enhancing understanding and engagement.

### **Advantages of Dashboards:**
- Facilitate real-time data exploration.
- Enable users to interact with data through filters, selectors, and updates.
- Useful for presenting key insights in professional settings.

---

## **12.5 Extension Task (Optional)**

### **Advanced Dashboard Features:**
1. **Add a Date Range Selector:**
   Use Dash’s `dcc.DatePickerRange` to filter data by date.
2. **Display Multiple Charts:**
   Arrange multiple visualizations side by side using Dash’s `html.Div`.

### **Code Example: Extended Dashboard Layout**
```python
# Add a date picker and multiple charts to the layout
app.layout = html.Div([
    dcc.DatePickerRange(id="date-picker"),
    html.Div([
        dcc.Graph(id="line-chart"),
        dcc.Graph(id="bar-chart")
    ], style={"display": "flex"})
])
```

---

## **Summary**

In this lesson, you learned:
1. How to visualize data directly from Pandas DataFrames.
2. How to create interactive visualizations with Plotly.
3. How to build dynamic dashboards using Dash.
4. The differences between static and interactive visualizations and their real-world applications.

Explore the [Plotly Documentation](https://plotly.com/python/) and [Dash Documentation](https://dash.plotly.com/) for further learning and inspiration.
