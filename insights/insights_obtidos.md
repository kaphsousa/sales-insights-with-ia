
# 📌 1. Prompts for Data Interpretation

## Prompt 1 — Sales Overview
---

| Metric | Category | Value |
|:---|:---|:---|
| **Total Sales** | Total Sales Value (BRL) | R$165,979.00 |
| | Total Sales Volume | 324 units |
| **Total Discounted Sales** | Total Discount Value (BRL) | R$28,365.13 |
| | Total Discounted Sales Value (BRL) | R$137,613.87 |
| **Average Ticket** | Average Ticket Value (BRL) | R$512.28 |
| **Total Number of Orders** | Total Number of Orders | 110 |
| **Products Sold by Site** | AliExpress | 5 unique products |
| | Etsy | 5 unique products |
| | Shopee | 5 unique products |

---

### 🛒 **Summary per Site**

| Marketplace    | Total Sales | Total Sales Volume | Orders | Average Ticket |
| -------------- | ------------- | ----------------- | ------- | ------------ |
| **Shopee**     | R$ 10,250.00  | 113               | 34      | R$ 301,47     |
| **Etsy**       | R$ 10,650.00  | 116               | 42      | R$ 253,57     |
| **AliExpress** | R$ 8,710.00   | 95                | 34      | R$ 256,17     |

---

### 🔍 **Initial Interpretation**

* **Shopee** boasts the highest average ticket per order (R$301.47), indicating a higher average purchase value per customer on that platform.
* **Etsy** has the largest number of orders, though with a slightly lower average ticket.
* **AliExpress** shows the lowest performance in terms of both revenue and average ticket.

---
<br>
<br>
<br>
<br>

## Prompt 2 – **Top 10 products by marketplace**:

### Top Products by Quantity and Revenue (by Marketplace)

| Marketplace | Product Name | Quantity Sold | Total Revenue (BRL) | Rank by Quantity | Rank by Revenue |
|:------------|:-------------|:--------------|:--------------------|:-----------------|:----------------|
| **AliExpress** | MEGANIUM RG353M | 27 units | R$16,049.00 | 1 | 1 |
| | NEW MEGANIUM RG35XX | 19 units | R$9,882.00 | 2 | 2 |
| | NEW MEGANIUM RG CubeXX | 18 units | R$8,112.00 | 3 | 3 |
| | NEW MEGANIUM RG28XX | 17 units | R$6,657.00 | 4 | 5 |
| | NEW MEGANIUM RG 40XXV | 14 units | R$8,040.00 | 5 | 4 |

| Marketplace | Product Name | Quantity Sold | Total Revenue (BRL) | Rank by Quantity | Rank by Revenue |
|:------------|:-------------|:--------------|:--------------------|:-----------------|:----------------|
| **Etsy** | NEW MEGANIUM RG 40XXV | 38 units | R$21,600.00 | 1 | 1 |
| | NEW MEGANIUM RG28XX | 25 units | R$10,101.00 | 2 | 4 |
| | NEW MEGANIUM RG35XX | 23 units | R$11,466.00 | 3 | 3 |
| | MEGANIUM RG353M | 21 units | R$12,276.00 | 4 | 2 |
| | NEW MEGANIUM RG CubeXX | 9 units | R$3,976.00 | 5 | 5 |

| Marketplace | Product Name | Quantity Sold | Total Revenue (BRL) | Rank by Quantity | Rank by Revenue |
|:------------|:-------------|:--------------|:--------------------|:-----------------|:----------------|
| **Shopee** | NEW MEGANIUM RG 40XXV | 32 units | R$18,200.00 | 1 | 1 |
| | NEW MEGANIUM RG35XX | 30 units | R$14,805.00 | 2 | 2 |
| | NEW MEGANIUM RG CubeXX | 18 units | R$8,000.00 | 3 | 4 |
| | NEW MEGANIUM RG28XX | 18 units | R$7,245.00 | 4 | 5 |
| | MEGANIUM RG353M | 15 units | R$9,570.00 | 5 | 3 |

---

### 📌 **Product Performance Analysis by Line**

Looking at the detailed product sales across our marketplaces, a clear pattern emerges regarding the MEGANIUM product line:

* The **MEGANIUM** line of products still overwhelmingly dominates sales in terms of both volume and revenue across all three marketplaces (*AliExpress, Etsy, and Shopee*).
* The **NEW MEGANIUM RG 40XXV** product stands out as both the most sold and the most profitable across *Etsy* and *Shopee*, making it a clear flagship product for our brand. On *AliExpress*, while it's in the top five, **MEGANIUM RG353M** leads in both quantity and revenue. This suggests **MEGANIUM RG353M** is the flagship for that particular platform.
* Products like **NEW MEGANIUM RG CubeXX** consistently appear with lower sales volume and revenue compared to other **MEGANIUM** variants in the top rankings, suggesting either lower demand for this specific model or a secondary focus in our sales strategy for it.

---

<br>
<br>
<br>
<br>

## Prompt 3 - **Weekly and Monthly sales analysis**:

### 📆 **Weekly Sales Analysis**

| Week Range | Sales Volume | Total Sales Value (BRL) |
|:-----------|:-------------|:------------------------|
| 2024-05-13/2024-05-19 | 8 units | R$4,280.00 |
| 2024-05-20/2024-05-26 | 15 units | R$6,940.00 |
| 2024-05-27/2024-06-02 | 3 units | R$1,248.00 |
| 2024-06-03/2024-06-09 | 14 units | R$7,736.00 |
| 2024-06-10/2024-06-16 | 5 units | R$2,340.00 |
| 2024-06-17/2024-06-23 | 9 units | R$4,139.00 |
| 2024-06-24/2024-06-30 | 10 units | R$4,656.00 |
| 2024-07-01/2024-07-07 | 23 units | R$12,284.00 |
| 2024-07-08/2024-07-14 | 6 units | R$2,960.00 |
| 2024-07-15/2024-07-21 | 13 units | R$6,409.00 |
| 2024-07-22/2024-07-28 | 17 units | R$8,577.00 |
| 2024-07-29/2024-08-04 | 10 units | R$4,968.00 |
| 2024-08-05/2024-08-11 | 21 units | R$11,683.00 |
| 2024-08-12/2024-08-18 | 13 units | R$5,892.00 |
| 2024-08-19/2024-08-25 | 25 units | R$13,252.00 |
| 2024-08-26/2024-09-01 | 12 units | R$6,747.00 |
| 2024-09-02/2024-09-08 | 10 units | R$5,646.00 |
| 2024-09-09/2024-09-15 | 12 units | R$6,455.00 |
| 2024-09-16/2024-09-22 | 18 units | R$9,423.00 |
| 2024-09-23/2024-09-29 | 12 units | R$6,618.00 |
| 2024-09-30/2024-10-06 | 11 units | R$5,856.00 |
| 2024-10-07/2024-10-13 | 14 units | R$6,631.00 |
| 2024-10-14/2024-10-20 | 14 units | R$6,916.00 |
| 2024-10-21/2024-10-27 | 15 units | R$7,044.00 |
| 2024-10-28/2024-11-03 | 8 units | R$3,808.00 |
| 2024-11-04/2024-11-10 | 6 units | R$3,471.00 |

---

### Monthly Sales Analysis

| Month | Sales Volume | Total Sales Value (BRL) |
|:------|:-------------|:------------------------|
| 2024-05 | 26 units | R$12,468.00 |
| 2024-06 | 38 units | R$18,871.00 |
| 2024-07 | 59 units | R$30,230.00 |
| 2024-08 | 81 units | R$42,542.00 |
| 2024-09 | 52 units | R$28,142.00 |
| 2024-10 | 61 units | R$29,695.00 |
| 2024-11 | 7 units | R$4,031.00 |

---

### 📈 Observed Trends

* We saw consistent growth from May through August, with sales peaking in August 2024 at R$42,542.00.
* Following this peak, there was a significant drop in September (R$28,142.00).
* October showed a partial recovery, bringing in R$29,695.00 in revenue.

### 💡 Key Takeaways

* August might represent a strategic period for us (e.g., back-to-school campaigns, winter season in Brazil, etc.).
* The decline after the August peak could suggest a lack of ongoing campaigns or unfavorable seasonality.
* Despite November typically being associated with Black Friday, its weak performance might indicate a missed opportunity or the absence of specific, compelling promotions during that time.

---