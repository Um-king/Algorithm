-- 코드를 입력하세요
SELECT A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES,
ADDRESS, round(AVG(REVIEW_SCORE), 2) REVIEW_SCORE 
From REST_INFO A
    Inner Join REST_REVIEW B On A.REST_ID = B.REST_ID
Where A.ADDRESS like '서울%'
Group By A.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS
Order By AVG(REVIEW_SCORE) desc, FAVORITES desc