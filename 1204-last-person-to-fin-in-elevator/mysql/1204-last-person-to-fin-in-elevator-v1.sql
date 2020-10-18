# Write your MySQL query statement below
select person_name from(
select person_name, turn, sum(weight) over(order by turn asc) as weight_sum from queue) x
where weight_sum <= 1000
order by turn desc
limit 1