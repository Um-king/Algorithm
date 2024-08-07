SELECT 
    CONCAT('/home/grep/src/', A.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) AS FILE_PATH 
FROM 
(
    SELECT BOARD_ID, MAX(VIEWS) AS VIEWS
    FROM USED_GOODS_BOARD
    GROUP BY BOARD_ID
    ORDER BY VIEWS DESC
    LIMIT 1
) A 
INNER JOIN USED_GOODS_FILE B ON A.BOARD_ID = B.BOARD_ID
ORDER BY B.FILE_ID desc