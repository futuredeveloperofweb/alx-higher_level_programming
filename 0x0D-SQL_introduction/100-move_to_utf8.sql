-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate
-- utf8mb4_unicode_ci)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
