# LIST COMPREHENSION= A CONCISE WAY TO CREATE LISTS IN PYTHON
#                     COMPACT AND EASIER  TO READ THAN TRADITIONAL LOOPS
#                      [EXPRESSION FOR VALUE IN  ITERABLES IF CONDITION]

#doubles=[x*2 for x in range(1,11) ]
#print(doubles)

#fruits=['apple','banana','coconut','dragonfruit']
#fruits=[fruit.upper() for fruit in fruits]
#print(fruits)

numbers=[1,-2,3,-4,5,-6]
positive_num=[number for number in numbers if number >=0 ]
negative_num=[number for number in numbers if number <=0 ]
print(positive_num)
print(negative_num)