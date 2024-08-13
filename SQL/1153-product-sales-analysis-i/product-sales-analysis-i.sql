# Write your MySQL query statement below
select P.product_name, S.year, S.price from Sales as S join Product as P on P.Product_id = S.Product_id;