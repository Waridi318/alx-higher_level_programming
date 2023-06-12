-- Import in hbtn_0c_0 database the table dump
SELECT city, avg(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
