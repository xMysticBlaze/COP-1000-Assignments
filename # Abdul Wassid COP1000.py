# Abdul Wassid COP1000


#prompt user for three test scores 
#add the three test scores together
#divide the total score by 3 to get the average score
#print the average score to the first two decimal places

test_1 = int(input("enter the first test score "))
test_2 = int(input("enter the second test score "))
test_3 = int(input("enter the third test score "))

totalscore = test_1 + test_2 + test_3

averagescore = totalscore/3

print(f"the average score is {averagescore:.2f}% ")

