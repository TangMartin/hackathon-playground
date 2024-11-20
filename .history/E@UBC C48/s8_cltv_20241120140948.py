tier_prices = {
    "Essential": 100,  # Monthly price
    "Professional": 500,  # Monthly price
    "Enterprise": 1500  # Monthly price (base for simplicity)
}

# Average customer retention period (in months)
customer_retention = {
    "Essential": 24,  # 2 years average
    "Professional": 36,  # 3 years average
    "Enterprise": 48  # 4 years average
}

# Gross margin for simplicity (assumed uniform across tiers)
gross_margin = 0.7  # 70%

# Sales and marketing costs and new customers (assumed for simulation)
sales_marketing_costs = 50000  # total monthly sales/marketing spend
new_customers_acquired = {
    "Essential": 100,  # New customers acquired for Essential
    "Professional": 50,  # New customers acquired for Professional
    "Enterprise": 20  # New customers acquired for Enterprise
}