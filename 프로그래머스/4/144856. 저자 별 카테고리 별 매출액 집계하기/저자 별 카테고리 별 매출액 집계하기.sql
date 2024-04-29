SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(TOTAL_SALES) TOTAL_SALES
FROM
(
    SELECT A.BOOK_ID, A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(C.SALES * A.PRICE) TOTAL_SALES
    FROM BOOK A
    INNER JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
    INNER JOIN BOOK_SALES C ON A.BOOK_ID = C.BOOK_ID
    WHERE MONTH(C.SALES_DATE) = 1
    GROUP BY A.BOOK_ID, A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY
) Q
GROUP BY AUTHOR_ID, AUTHOR_NAME, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC