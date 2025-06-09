# Python program to calculate days between 2 dates.

from datetime import datetime

# Input format: YYYY-MM-DD
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert strings to date objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Calculate the difference in days
delta = abs((date2 - date1).days)

print(f"Number of days between {date_str1} and {date_str2}: {delta}")

