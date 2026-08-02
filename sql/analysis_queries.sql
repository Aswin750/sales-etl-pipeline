use retale_sales;

select count(*) as total_orders
from sales;

select * from sales
limit 10;

select 
count(Order_Id) as total,
count(distinct Order_Id) as unique_id
from sales;

select *
from sales
where Customer_Name is null;

select * 
from sales 
where Discount>100;

# finding insights

select sum(Sales) as revenue
from sales;

select count(*)as total_orders
from sales;

select avg(sales) as average_sales
from sales;

select max(sales) as max_sales
from sales;

select min(sales) as max_sales
from sales;

select City,sum(sales)as total_revenue
from sales 
group by City;


SELECT
    Product,
    SUM(Sales) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 1;

select City,sum(sales)as total_revenue
from sales 
group by City
order by total_revenue desc
limit 5;

select City,sum(sales) as revenue
from sales
where Order_Status="Delivered"
group by City
order by revenue desc;

select Category,avg(sales) as avg_revenue
from sales 
group by Category
having avg_revenue>5000
order by avg_revenue;

select City,Category,sum(sales) as revenue
from sales 
group by City,Category
order by sum(sales) desc;

