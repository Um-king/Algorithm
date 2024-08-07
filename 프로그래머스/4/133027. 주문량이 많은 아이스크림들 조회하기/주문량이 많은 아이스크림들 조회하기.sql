WITH ORDER_TABLE AS (
SELECT A.FLAVOR, (A.TOTAL_ORDER + B.TOTAL_ORDER) TOTAL_ORDER
FROM FIRST_HALF A
LEFT JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) TOTAL_ORDER FROM JULY
    GROUP BY FLAVOR
) B ON A.FLAVOR = B.FLAVOR
ORDER BY TOTAL_ORDER desc
)

SELECT FLAVOR FROM ORDER_TABLE
LIMIT 3