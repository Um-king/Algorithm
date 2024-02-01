-- 코드를 입력하세요
SELECT * From FOOD_PRODUCT 
Where PRICE in (Select MAX(PRICE) From FOOD_PRODUCT)