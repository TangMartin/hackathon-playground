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

# Calculate CAC for each tier
cac = {tier: sales_marketing_costs / count for tier, count in new_customers_acquired.items()}

# Calculate CLV for each tier
clv = {tier: (price * retention * gross_margin) for tier, (price, retention) in zip(tier_prices.keys(), zip(tier_prices.values(), customer_retention.values()))}

# Combine CAC and CLV for results
cac_clv_ratios = {tier: clv[tier] / cac[tier] for tier in tier_prices.keys()}

import pandas as pd

# Create a DataFrame for clear presentation
df = pd.DataFrame({
    "Tier": tier_prices.keys(),
    "Monthly Price (USD)": tier_prices.values(),
    "Customer Retention (Months)": customer_retention.values(),
    "CAC (USD)": [cac[tier] for tier in tier_prices.keys()],
    "CLV (USD)": [clv[tier] for tier in tier_prices.keys()],
    "CAC-to-CLV Ratio": [cac_clv_ratios[tier] for tier in tier_prices.keys()]
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Customer Acquisition Cost and Lifetime Value Analysis", dataframe=df)