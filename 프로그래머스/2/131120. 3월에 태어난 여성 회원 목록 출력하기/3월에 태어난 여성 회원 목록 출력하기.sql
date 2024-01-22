-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') DATE_OF_BIRTH
From MEMBER_PROFILE 
Where extract(month from DATE_OF_BIRTH) = 3
    and GENDER = 'W'
    and TLNO is not null
Order By MEMBER_ID