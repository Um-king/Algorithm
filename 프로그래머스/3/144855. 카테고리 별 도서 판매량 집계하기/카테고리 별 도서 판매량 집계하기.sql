-- 코드를 입력하세요
SELECT A.CATEGORY, SUM(SALES) AS TOTAL_SALES FROM BOOK A
INNER JOIN BOOK_SALES B ON A.BOOK_ID = B.BOOK_ID
WHERE MONTH(SALES_DATE) = 1
GROUP BY CATEGORY
ORDER BY CATEGORY