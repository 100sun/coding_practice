// 상위 n 개
ORDER BY ~
LIMIT 1

SELECT MAX(~), MIN(~), COUNT(*), HOUR(DATETIME)
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog"

// 보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
SELECT ANIMAL_ID, NAME,
CASE WHEN SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%"
THEN "O"
ELSE "X"
END AS "중성화"
FROM ANIMAL_INS


ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)

SELECT DATE_FORMATE(DATETIME , "%Y-%m-%d") AS 날짜

SELECT IFNULL(NAME, "No name") AS NAME