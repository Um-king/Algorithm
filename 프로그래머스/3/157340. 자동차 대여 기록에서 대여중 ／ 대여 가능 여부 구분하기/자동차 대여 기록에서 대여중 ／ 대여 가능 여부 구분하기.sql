Select CAR_ID, MAX(CASE 
           WHEN '2022-10-16' BETWEEN START_DATE and END_DATE THEN '대여중' 
           ELSE '대여 가능' 
       END) AS AVAILABILITY
From CAR_RENTAL_COMPANY_RENTAL_HISTORY 
Group By CAR_ID
Order By CAR_ID desc