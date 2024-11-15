# Write your MySQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) FROM Teacher WHERE teacher_id > 0;