import pandas as pd

# Load the dataset
df = pd.read_csv("../data/Meganium_Sales_Data_-_CONSOLIDATED.csv")

# Define exchange rates to BRL
exchange_rates = {
    'USD': 5.20,
    'EUR': 5.60,
    'GBP': 6.10,
    'BRL': 1.00
}

# Check required columns
required_columns = {
    'total_price', 'currency', 'quantity', 'date'
}
missing = required_columns - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Convert prices to BRL
df['total_price_brl'] = df['total_price'] * df['currency'].map(exchange_rates).fillna(1.0)

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'])

# Group by week (weekly report)
df['week'] = df['date'].dt.to_period('W')

# Group by month (monthly report)
df['month'] = df['date'].dt.to_period('M')

# Weekly sales aggregation
weekly_sales = df.groupby('week').agg(
    total_sales_value_brl=('total_price_brl', 'sum'),
    total_sales_volume=('quantity', 'sum')
).reset_index()

# Monthly sales aggregation
monthly_sales = df.groupby('month').agg(
    total_sales_value_brl=('total_price_brl', 'sum'),
    total_sales_volume=('quantity', 'sum')
).reset_index()

# Sort data by week and month for better visualization
weekly_sales = weekly_sales.sort_values(by='week')
monthly_sales = monthly_sales.sort_values(by='month')

# Generate output
output_lines = []

# Weekly report section
output_lines.append("## Weekly Sales Analysis (Converted to BRL)")

for idx, row in weekly_sales.iterrows():
    output_lines.append(f"* **{row['week']}** - *Sales Volume*: {int(row['total_sales_volume'])} units, *Total Sales Value*: R${row['total_sales_value_brl']:,.2f}")

# Monthly report section
output_lines.append("\n## Monthly Sales Analysis (Converted to BRL)")

for idx, row in monthly_sales.iterrows():
    output_lines.append(f"* **{row['month']}** - *Sales Volume*: {int(row['total_sales_volume'])} units, *Total Sales Value*: R${row['total_sales_value_brl']:,.2f}")

# Save the report to a markdown file
with open("../insights/prompt_3.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("✅ Weekly and Monthly sales analysis saved to 'insights/prompt_3.md'")
