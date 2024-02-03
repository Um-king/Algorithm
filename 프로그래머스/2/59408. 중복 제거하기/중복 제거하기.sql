-- 코드를 입력하세요
SELECT COUNT(*) count FROM
(
    SELECT NAME FROM ANIMAL_INS 
    Where NAME is not null
    GROUP BY NAME
) Q