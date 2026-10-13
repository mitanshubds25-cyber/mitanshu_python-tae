
import matplotlib.pyplot as plt

# Store rainfall data
rainfall_data = {}

# Enter rainfall data
n = int(input("Enter number of cities: "))

for i in range(n):
    city = input("\nEnter city name: ")
    rainfall = float(input("Enter rainfall in mm: "))
    rainfall_data[city] = rainfall

# Calculate rainfall statistics
values = list(rainfall_data.values())

total = sum(values)
average = total / len(values)
maximum = max(values)
minimum = min(values)

# Display summary report
print("\n===== RAINFALL SUMMARY REPORT =====")

for city, rainfall in rainfall_data.items():
    print(city, ":", rainfall, "mm")

print("\nTotal Rainfall:", total, "mm")
print("Average Rainfall:", round(average, 2), "mm")
print("Maximum Rainfall:", maximum, "mm")
print("Minimum Rainfall:", minimum, "mm")

# Find city with maximum and minimum rainfall
for city, rainfall in rainfall_data.items():
    if rainfall == maximum:
        print("Highest Rainfall City:", city)

    if rainfall == minimum:
        print("Lowest Rainfall City:", city)

# Display bar graph
plt.bar(rainfall_data.keys(), rainfall_data.values())
plt.title("Rainfall Data Analyzer")
plt.xlabel("Cities")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
