SELECT C.ID, Q.FISH_NAME, Q.LENGTH FROM (
    SELECT A.FISH_TYPE, B.FISH_NAME, MAX(LENGTH) AS LENGTH 
    FROM FISH_INFO A
    INNER JOIN FISH_NAME_INFO B ON A.FISH_TYPE = B.FISH_TYPE
    WHERE LENGTH IS NOT NULL
    GROUP BY A.FISH_TYPE, B.FISH_NAME
) Q
INNER JOIN FISH_INFO C ON Q.FISH_TYPE = C.FISH_TYPE and Q.LENGTH = C.LENGTH 
ORDER BY ID ASC

