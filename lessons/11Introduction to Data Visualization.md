
# **Lesson 11 — Introduction to Data Visualization**

## **Lesson Overview**
**Learning objective:** Students will learn to create and customize basic and advanced data visualizations using Python libraries such as Matplotlib and Seaborn. These skills will enable effective data storytelling through visual representation.

### **Topics:**
1. Introduction to Matplotlib: Creating basic plots (line, bar, histogram).
2. Customizing Plots: Labels, titles, legends, and colors.
3. Introduction to Seaborn: Creating advanced visualizations (heatmaps, pair plots).

---

## **11.1 Introduction to Matplotlib**

### **Overview**
Matplotlib is a foundational Python library for creating static, animated, and interactive visualizations. It is versatile and widely used for creating basic plots.

### **Key Plot Types:**
1. **Line Plot:** Shows trends over time or continuous data.
2. **Bar Plot:** Compares categorical data.
3. **Histogram:** Displays the distribution of numerical data.

### **Example Code: Creating Basic Plots**
```python
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]
plt.plot(months, revenue, marker='o', linestyle='-', color='blue')
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.show()

# Bar Plot
categories = ["Region A", "Region B"]
sales = [500, 700]
plt.bar(categories, sales, color=['green', 'orange'])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.show()

# Histogram
random_data = np.random.randn(1000)
plt.hist(random_data, bins=30, color='purple', alpha=0.7)
plt.title("Random Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

---

## **11.2 Customizing Plots**

### **Overview**
Customizations enhance the readability and aesthetic of plots. This includes:
- Changing colors, line styles, or bar widths.
- Adding grids for better value estimation.
- Using legends, titles, and labels for context.

### **Example Code: Customizing Plots**
```python
# Customized Line Plot
plt.plot(months, revenue, marker='o', linestyle='--', color='red', linewidth=2)
plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(["Revenue"], loc="upper left")
plt.show()

# Customized Bar Plot
plt.bar(categories, sales, color=['skyblue', 'salmon'], width=0.5, edgecolor='black')
plt.title("Sales by Region", fontsize=14, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.show()
```

---

## **11.3 Introduction to Seaborn**

### **Overview**
Seaborn is a Python library for creating advanced statistical plots with beautiful default styles. It integrates seamlessly with Pandas DataFrames.

### **Key Plot Types:**
1. **Heatmap:** Displays correlations or relationships in tabular data.
2. **Pair Plot:** Shows pairwise relationships in a dataset.

### **Example Code: Creating Advanced Visualizations**
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# Heatmap of correlations
plt.figure(figsize=(10, 6))
correlation_matrix = titanic.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(titanic, vars=["age", "fare", "survived"], hue="survived", palette="Set2")
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()
```

### **Saving Plots:**
To save visualizations as image files:
```python
plt.savefig("heatmap.png")
```

---

## **Summary**

In this lesson, you learned:
1. How to create basic visualizations (line plots, bar plots, histograms) using Matplotlib.
2. Techniques for customizing plots to improve readability and presentation.
3. How to use Seaborn to create advanced visualizations like heatmaps and pair plots.

For more details, explore the [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) and [Seaborn Documentation](https://seaborn.pydata.org/).
