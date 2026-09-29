import matplotlib.pyplot as plt

# Rainfall Data Analyzer

# Store rainfall data
rainfall = {}

# Number of entries
n = int(input("Enter number of cities/months: "))

# Input data
for i in range(n):
    name = input("Enter city or month name: ")
    value = float(input("Enter rainfall in mm: "))
    rainfall[name] = value

# Display data
print("\n--- Rainfall Data ---")
for name, value in rainfall.items():
    print(name, ":", value, "mm")

# Calculations
values = list(rainfall.values())

total = sum(values)
average = total / len(values)
maximum = max(values)
minimum = min(values)

# Summary Report
print("\n--- Summary Report ---")
print("Total Rainfall   :", total, "mm")
print("Average Rainfall :", average, "mm")
print("Maximum Rainfall :", maximum, "mm")
print("Minimum Rainfall :", minimum, "mm")

# Find city/month with maximum and minimum rainfall
max_name = max(rainfall, key=rainfall.get)
min_name = min(rainfall, key=rainfall.get)

print("Highest Rainfall :", max_name, "-", rainfall[max_name], "mm")
print("Lowest Rainfall  :", min_name, "-", rainfall[min_name], "mm")

# Graphical Visualization
plt.bar(rainfall.keys(), rainfall.values())

plt.title("Rainfall Data Analyzer")
plt.xlabel("City / Month")
plt.ylabel("Rainfall (mm)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
