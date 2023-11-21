-- Write your PostgreSQL query statement below
delete from person where id not in (
  select distinct on (email) id from person order by email asc, id asc
)