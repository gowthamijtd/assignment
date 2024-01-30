list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]
index=range(len(list1))
b=[index['meal'] for index in list1]
count_vegetarian=b.count('vegetarian')
count_standard=b.count('standard')
count_vegan=b.count('vegan')
food_count=dict([("vegetarian",count_vegetarian),("standard",count_standard),("vegan",count_vegan)])
print(food_count)


    
    

    
    
    





