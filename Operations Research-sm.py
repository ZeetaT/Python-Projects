import pulp
import matplotlib.pyplot as plt
import numpy as np

#Initialize the Maximization Problem
prob = pulp.LpProblem("Reddy_Mikks_Paint_Production", pulp.LpMaximize)

#Define Non-Negative Decision Variables
x1 = pulp.LpVariable('x1_Exterior', lowBound = 0)
x2 = pulp.LpVariable('x2_Exterior', lowBound = 0)

# Define Objective Function (Profit in $1,000s) 
prob += 5 * x1 + 4 * x2, "Total_Profit_Thousands" 

# Add Constraints 
prob += 6 * x1 + 4 * x2 <= 24, "Raw_Material_M1" 
prob += 1 * x1 + 2 * x2 <= 6, "Raw_Material_M2" 
prob += -1 * x1 + 1 * x2 <= 1, "Market_Limit" 
prob += x2 <= 2, "Demand_Limit" 

# Solve using the default Simplex Solver (CBC) 
status = prob.solve() 

# Display Optimal Results 
print(f"Status: {pulp.LpStatus[status]}") 
print(f"Exterior Paint (x1): {pulp.value(x1)} tons/day") 
print(f"Interior Paint (x2): {pulp.value(x2)} tons/day") 
print(f"Maximum Profit (z): ${pulp.value(prob.objective)*1000:,.2f}")