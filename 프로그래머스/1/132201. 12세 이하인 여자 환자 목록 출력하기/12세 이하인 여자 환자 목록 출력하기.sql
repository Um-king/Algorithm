-- 코드를 입력하세요
Select PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') as TLNO
From PATIENT 
Where AGE <= 12 and GEND_CD = 'W'
Order By AGE DESC, PT_NAME













