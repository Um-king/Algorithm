
Select A.ITEM_ID, A.ITEM_NAME, A.RARITY From ITEM_INFO A
    Inner Join 
    (
        Select ITEM_ID From ITEM_TREE 
        Where PARENT_ITEM_ID in (
            Select ITEM_ID From ITEM_INFO Where RARITY = 'RARE'
        )
    ) B On A.ITEM_ID = B.ITEM_ID
Order By A.ITEM_ID desc