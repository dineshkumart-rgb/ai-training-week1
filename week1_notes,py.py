
import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

products = ["A", "B", "C", "D"]
revenue = [250, 300, 180, 220]

days = [1, 2, 3, 4, 5]
temperature = [25, 27, 26, 30, 32]

categories = ["Python", "Java", "AI", "Data Science"]
students = [30, 20, 35, 15]

# Create one figure with four charts
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1: Line chart
axes[0, 0].plot(months, sales, marker="o", color="blue")
axes[0, 0].set_title("Monthly Sales")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")

# Chart 2: Bar chart
axes[0, 1].bar(products, revenue, color="green")
axes[0, 1].set_title("Product Revenue")
axes[0, 1].set_xlabel("Products")
axes[0, 1].set_ylabel("Revenue")

# Chart 3: Scatter plot
axes[1, 0].scatter(days, temperature, color="red")
axes[1, 0].set_title("Temperature Analysis")
axes[1, 0].set_xlabel("Day")
axes[1, 0].set_ylabel("Temperature")

# Chart 4: Pie chart
axes[1, 1].pie(
    students,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 1].set_title("Student Distribution")

plt.tight_layout()
plt.savefig("charts.png")
plt.show()
