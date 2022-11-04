import pandas as pd
import pulp as p

bidDetails = pd.read_csv('./output/bids_details.csv')
print(bidDetails)

bids = bidDetails.query('ItemId == 1899332 and Quoted_Price > 0')
bids = bids.reset_index()
print(bids)

'''
 Item selected in UI
 Qty is bid quantity
 Price entered in UI
 Call prediction for a item/price to get supplier characteristics
'''
quality = 3
timeliness = 4
problem = p.LpProblem(name='Supplier_Optimization', sense=p.LpMinimize)
print(problem)

suppliers = p.LpVariable.dicts("", bids['SupplierId'], cat='Binary')
print(suppliers)

# Optimization function
problem += p.lpSum(suppliers[bids['SupplierId'][i]] * bids['Quoted_Price'][i] for i in range(bids['SupplierId'].count()))
print(problem)

# Constraints
# Required Quantity
problem += p.lpSum(suppliers[bids['SupplierId'][i]] for i in range(bids['SupplierId'].count())) == bids['Quantity'].unique()
print(problem)

# Max price
problem += p.lpSum(suppliers[bids['SupplierId'][i]] * bids['Quoted_Price'][i] for i in range(bids['SupplierId'].count())) <= 54.5
print(problem)