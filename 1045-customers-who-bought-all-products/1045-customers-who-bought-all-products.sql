# Write your MySQL query statement below
select customer_id from Customer
GROUP BY customer_id
having count(distinct product_key)=(
    select count(*) from Product
)