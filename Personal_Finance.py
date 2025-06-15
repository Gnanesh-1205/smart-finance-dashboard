print("👋 Welcome to Your Smart Finance Dashboard 💸")

# Step 1: Input income and expenses
income = float(input("Enter your monthly income (in ₹): "))

# Create a dictionary to store expenses
expenses = {}

# List of common categories
categories = ["Rent", "Food", "Transport", "Subscriptions", "Shopping", "Others"]

# Take expense inputs
for category in categories:
    amount = float(input(f"Enter your monthly {category} expense (in ₹): "))
    expenses[category] = amount

# Step 2: Calculate total expenses and savings
total_expenses = sum(expenses.values())
savings = income - total_expenses

print("\n📊 Summary:")
print(f"Total Income: ₹{income}")
print(f"Total Expenses: ₹{total_expenses}")
print(f"Savings: ₹{savings}")

# Step 3: Analyze spending
print("\n📈 Expense Breakdown by Category:")

for category, amount in expenses.items():
    percent = (amount / income) * 100
    print(f"{category}: ₹{amount} ({percent:.2f}%)")
    
    # Smart suggestions
    if percent > 40 and category == "Rent":
        print("⚠️ Your rent is above 40% of income. Try to reduce housing costs.")
    elif percent > 30 and category == "Food":
        print("⚠️ You're spending a lot on food. Try cooking more at home.")
    elif percent > 20 and category == "Shopping":
        print("⚠️ Too much shopping! Control those impulse buys 😅")
import matplotlib.pyplot as plt

# Step 4: Create a Pie Chart of Expenses
labels = list(expenses.keys())
values = list(expenses.values())

plt.figure(figsize=(7, 7))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution")
plt.axis('equal')  # Makes the pie chart a circle
plt.show()
# Step 5: Calculate Financial Health Score
score = 0

# 1. Savings >= 20% of income
if savings >= 0.2 * income:
    score += 30

# 2. Rent <= 40%
if expenses["Rent"] <= 0.4 * income:
    score += 25
else:
    score -= 10

# 3. Food <= 30%
if expenses["Food"] <= 0.3 * income:
    score += 25
else:
    score -= 10

# 4. Shopping <= 15%
if expenses["Shopping"] <= 0.15 * income:
    score += 20
else:
    score -= 10

print("\n🧮 Your Financial Health Score: ", score, "/ 100")

# Add interpretation
if score >= 85:
    print("💚 Excellent! You're financially healthy!")
elif score >= 70:
    print("💙 Good job! Some improvements can be made.")
elif score >= 50:
    print("🟡 Be careful! You're spending too much in some areas.")
else:
    print("🔴 Warning! Your financial habits need serious attention.")
