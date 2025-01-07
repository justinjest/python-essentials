
# **Lesson 12 — Advanced Data Visualization Techniques**

## **Lesson Overview**
**Learning objective:** In this lesson, students will learn how to create advanced and interactive visualizations using Python libraries like Pandas, Plotly, and Dash. By the end of this lesson, students will understand how to visualize data directly from DataFrames, create interactive plots, and build simple dashboards for real-time data exploration.

### **Topics:**
1. Plotting with Pandas: Visualizing data directly from DataFrames.
2. Interactive Visualizations: Using Plotly for interactive plotting.
3. Dashboards: Creating dynamic dashboards with Plotly and Dash.
4. Advanced Customization: Advanced interactivity, subplots, and real-time updates.

---

## **12.1 Plotting with Pandas**

### **Overview**
Pandas simplifies data visualization by providing built-in plotting methods for DataFrames and Series. These plots are ideal for quick data exploration and basic visualizations.

### **Key Plot Types:**
- **Line Plot:** Displays trends over time or continuous data.
- **Bar Plot:** Used for comparing categorical data.
- **Histogram:** Shows the distribution of numerical data.

### **When to Use These Plots:**
- **Line Plots** are typically used for showing data trends over time, such as sales or stock prices over months.
- **Bar Plots** are ideal when you need to compare quantities between different categories, such as the sales of different products or regions.
- **Histograms** are useful for analyzing the distribution of numerical data, identifying patterns, skewness, or the range of values.

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
Plotly is a powerful library for creating interactive, highly customizable plots. It allows for hover tooltips, zooming, and dynamic interactions that improve user experience.

### **Steps to Create Interactive Visualizations:**
1. Install Plotly:
   ```bash
   pip install plotly
   ```
2. Use Plotly to create interactive plots like scatter plots, bar charts, and more.

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

### **Key Features of Plotly:**
- **Interactivity:** Hover tooltips, zooming, and panning.
- **Customization:** Wide range of customization options for visual aesthetics and user interaction.

---

## **12.3 Building Dashboards with Dash**

### **Overview**
Dash is a framework for creating interactive web applications in Python. It leverages Plotly for visualizations and allows you to create dashboards that update in real-time based on user input.

### **Steps to Build a Dashboard:**
1. Install Dash:
   ```bash
   pip install dash
   ```
2. Build a Dash app with components like dropdowns and interactive graphs.

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
- **Static Visualizations:** Easier to create and quicker to render but lack user interaction.
- **Interactive Visualizations:** Allow users to explore data, zoom, filter, and interact, providing a deeper and more engaging analysis experience.

### **Advantages of Dashboards:**
- Real-time data exploration and updates.
- User interaction with data (e.g., dropdowns, sliders) enables custom insights.
- Efficient presentation of key metrics in a professional setting.

---

## **12.5 Extension Task (Optional)**

### **Advanced Dashboard Features:**
1. **Add a Date Range Selector:**
   Use Dash’s `dcc.DatePickerRange` to allow users to filter data by date.
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

For more details, explore the [Plotly Documentation](https://plotly.com/python/) and [Dash Documentation](https://dash.plotly.com/).

---

### Additional Resources:
1. **Matplotlib Tutorials:** For more detailed Matplotlib tutorials, check out [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html).
2. **Seaborn Gallery:** Explore different plot examples at the [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html).
3. **Data Visualization in Python:** To explore more about data visualization strategies and best practices, visit [Data Visualization in Python](https://realpython.com/python-data-visualization-using-matplotlib/).

