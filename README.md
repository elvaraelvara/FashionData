# 📊 **Fashion Sales Dataset**  

📌 **Source Dataset:** [GitHub - all_data.csv](https://github.com/rfajri27/a555-dashboard/blob/main/all_data.csv)  

---

## 🛍️ **Overview**  

This dataset represents **fashion product sales transactions**, where each row corresponds to a single transaction or purchase.  
It includes various attributes such as **product details, customer information, transaction data, and delivery status**.  

✅ **Use Cases:**  
- 📈 **Sales Analysis** – Identify trends and best-selling products.  
- 🛒 **Customer Insights** – Analyze purchasing behavior based on age, gender, and location.  
- 🚚 **Delivery Performance** – Evaluate delivery times and optimize logistics.  

---

## 📂 **Dataset Information**  

This dataset contains the following columns:  

| 🏷 **Column Name** | 📝 **Description** |
|-------------------|------------------|
| 🔢 `sales_id` | Unique sales transaction ID |
| 🛍️ `order_id` | Order number |
| 🏷️ `product_id` | Unique product ID |
| 💰 `price_per_unit` | Price per unit of product |
| 🔢 `quantity_x` | Quantity purchased |
| 💵 `total_price` | Total purchase price (`quantity_x * price_per_unit`) |
| 👕 `product_type` | Type of product |
| 🏷️ `product_name` | Name of the product |
| 📏 `size` | Product size (e.g., S, M, L, XS) |
| 🎨 `colour` | Product color |
| 💲 `price` | Product price |
| 📦 `quantity_y` | Available stock at the time of purchase |
| 📝 `description` | Product description |
| 👤 `customer_id` | Unique customer ID |
| 💳 `payment` | Payment method used |
| 📆 `order_date` | Date of purchase |
| 🚚 `delivery_date` | Delivery date |
| ⏳ `delivery_time` | Delivery time |
| 🏷️ `customer_name` | Customer's name |
| 🚻 `gender` | Customer's gender |
| 🔢 `age` | Customer's age |
| 🏡 `home_address` | Customer's home address |
| 📍 `zip_code` | Customer's zip code |
| 🏙️ `city` | Customer's city |
| 🌍 `state` | Customer's state/province |
| 🌎 `country` | Customer's country |
| 🔄 `status` | Purchase or account status (e.g., Active) |
| 👥 `age_group` | Customer's age group (e.g., Seniors, Adults) |

---

## ⚙️ **Environment Setup**  

Follow these steps to set up the environment for analyzing and visualizing this dataset:  

### 🏗 **1. Create Virtual Environment**  
```bash
python -m venv venv
