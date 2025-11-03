# User inputs 
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved   = float(input("Enter the portion of salary to be saved (decimal): "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

# Fixed values specified by the assignment
portion_down_payment = 0.25    # 25% down payment
r = 0.05                      # annual return rate (5%)

# Derived / working variables (initialized after required inputs)
monthly_salary = yearly_salary / 12.0
down_payment = cost_of_dream_home * portion_down_payment

amount_saved = 0.0
months = 0

# Safety check: if user will never save anything, avoid infinite loop
monthly_saved_from_salary = monthly_salary * portion_saved
if monthly_saved_from_salary <= 0 and amount_saved < down_payment:
    print("With the given salary and portion_saved, no progress toward the down payment will be made.")
else:
    # Loop until we have enough for the down payment
    while amount_saved < down_payment:
        # Each month:
        # 1) receive monthly return on current savings
        monthly_return = amount_saved * (r / 12.0)

        # 2) add the portion of monthly salary saved
        amount_saved += monthly_return + monthly_saved_from_salary

        # 3) increment month counter
        months += 1

    print("Number of months:", months)







# Part B: Saving with a raise


# Step 1: User Inputs (cast as floats in given order)
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the portion of salary to be saved (decimal): "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise (decimal): "))

# Step 2: Constants
portion_down_payment = 0.25   # 25% down payment
r = 0.05                      # Annual rate of return (5%)

# Step 3: Derived and initialized variables
monthly_salary = yearly_salary / 12.0
down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0.0
months = 0

# Step 4: Loop until the goal (down payment) is reached
while amount_saved < down_payment:
    # (a) Monthly return on investment
    monthly_return = amount_saved * (r / 12.0)
    
    # (b) Monthly savings from salary
    amount_saved += monthly_return + (monthly_salary * portion_saved)
    
    # (c) Count the month
    months += 1
    
    # (d) Apply raise every 6 months
    if months % 6 == 0:
        yearly_salary = yearly_salary * (1 + semi_annual_raise)
        monthly_salary = yearly_salary / 12.0

# Step 5: Output
print("Number of months:", months)





# ---------------------------------------------------
# Part C: Choosing an Interest Rate using Bisection Search
# ---------------------------------------------------

# Step 1: User input (cast as float at beginning)
initial_deposit = float(input("Enter the initial amount in your savings account: "))

# Step 2: Constants
cost_of_house = 800000.0                   # fixed house cost
portion_down_payment = 0.25                # 25% down payment
down_payment = cost_of_house * portion_down_payment  # $200,000
months = 36                                # 3 years = 36 months

# Step 3: Bisection search setup
low = 0.0               # lower bound for r
high = 1.0              # upper bound for r (100%)
epsilon = 100           # acceptable error margin for savings
steps = 0               # count how many bisection steps we perform
found = False           # flag to indicate success

# Step 4: Compute the savings difference function
# amount_saved = initial_deposit * (1 + r/12) ** months

while True:
    steps += 1
    r = (low + high) / 2.0  # midpoint rate for current guess
    amount_saved = initial_deposit * ((1 + (r / 12)) ** months)

    # Check the difference between saved amount and required down payment
    difference = amount_saved - down_payment

    # If within $100, we found the suitable rate
    if abs(difference) <= epsilon:
        found = True
        break
    # If savings too low, need higher rate → move lower bound up
    elif amount_saved < down_payment:
        low = r
    # If savings too high, rate is too high → move upper bound down
    else:
        high = r

    # Stop if range gets too small (to avoid infinite loops)
    if abs(high - low) < 1e-10:
        break

# Step 5: Output
if found:
    print("Best savings rate (r):", round(r, 6))
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to save enough for the down payment in 3 years.")
