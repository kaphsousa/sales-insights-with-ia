import pandas as pd

# Load the data from CSV
df = pd.read_csv("../data/Meganium_Sales_Data_-_CONSOLIDATED.csv")

# Define exchange rates to BRL
exchange_rates = {
    'USD': 5.20,
    'EUR': 5.60,
    'GBP': 6.10,
    'BRL': 1.00
}

# Apply conversion to a new column
df['total_price_brl'] = df['total_price'] * df['currency'].map(exchange_rates).fillna(1.0)
# Calculate total price with discount in BRL
df['total_price_w_discount_brl'] = df['total_price_w_discount'] * df['currency'].map(exchange_rates).fillna(1.0)

# Calculate metrics in BRL
total_sales_value_brl = df['total_price_brl'].sum()
total_sales_w_discount_value_brl = df['total_price_w_discount_brl'].sum()
discount_value = total_sales_value_brl - total_sales_w_discount_value_brl

# Calculate additional metrics
total_sales_volume = df['quantity'].sum()
average_ticket_value_brl = total_sales_value_brl / total_sales_volume
total_number_of_orders = len(df)
products_sold_by_site = df.groupby('site')['product_sold'].nunique()

# Prepare output
output_lines = []
output_lines.append("## Statistical Summary (Converted to BRL)\n")

output_lines.append("### Total Sales")
output_lines.append(f"* **Total Sales Value (BRL)**: R${total_sales_value_brl:,.2f}")
output_lines.append(f"* **Total Sales Volume**: {total_sales_volume} units\n")

output_lines.append("### Total Discounted Sales")
output_lines.append(f"* **Total Discount Value (BRL)**: R${discount_value:,.2f}")
output_lines.append(f"* **Total Discounted Sales Value (BRL)**: R${total_sales_w_discount_value_brl:,.2f}\n")

output_lines.append("### Average Ticket")
output_lines.append(f"* **Average Ticket Value (BRL)**: R${average_ticket_value_brl:,.2f}\n")

output_lines.append("### Total Number of Orders")
output_lines.append(f"* **Total Number of Orders**: {total_number_of_orders}\n")

output_lines.append("### Products Sold by Site")
for site, count in products_sold_by_site.items():
    output_lines.append(f"* **{site}**: {count} unique products")

# Save to file
with open("../insights/prompt_1.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("✅ Summary saved to 'insights/prompt_1.md'")
