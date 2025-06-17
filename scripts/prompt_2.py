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

# Convert prices to BRL
df['total_price_brl'] = df['total_price'] * df['currency'].map(exchange_rates).fillna(1.0)

# Group by product and site
product_site_summary = df.groupby(['product_sold', 'site']).agg(
    total_quantity=('quantity', 'sum'),
    total_revenue_brl=('total_price_brl', 'sum')
).reset_index()

# Sort by quantity and revenue within each site
top_10_by_quantity = product_site_summary.sort_values(by=['site', 'total_quantity'], ascending=[True, False])
top_10_by_revenue = product_site_summary.sort_values(by=['site', 'total_revenue_brl'], ascending=[True, False])

# Function to get top 10 per site
def get_top_10_by_site(df, metric_col, metric_name):
    output = []
    for site, site_df in df.groupby('site'):
        output.append(f"\n### {site} Marketplace")
        top_10 = site_df.nlargest(10, metric_col)
        for idx, row in top_10.iterrows():
            output.append(f"* **{row['product_sold']}** - {int(row['total_quantity'])} units, R${row['total_revenue_brl']:,.2f}")
    return output

# Generate output
output_lines = []
output_lines.append("## Top 10 Products by Quantity Sold (by Marketplace)")

# Top 10 by quantity for each site
output_lines.extend(get_top_10_by_site(top_10_by_quantity, 'total_quantity', 'Quantity'))

output_lines.append("\n## Top 10 Products by Total Revenue (BRL) (by Marketplace)")

# Top 10 by revenue for each site
output_lines.extend(get_top_10_by_site(top_10_by_revenue, 'total_revenue_brl', 'Revenue'))

# Save report
with open("../insights/prompt_2.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("✅ Top 10 products by marketplace saved to 'insights/prompt_2.md'")
