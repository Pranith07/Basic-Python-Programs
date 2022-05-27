#Give two names as input. This code will find the love percentage based on the names. It will search for the characters which match "TRUE LOVE" and calculate the score.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Convert to lower case
n1_lower = name1.lower()
n2_lower = name2.lower()
# print(n1_lower)

#Join it into a single variable to find the count
n1_n2_joined = n1_lower + n2_lower
# print(n1_n2_joined)

#Count the characters which match "TRUE LOVE"
T_count = n1_n2_joined.count('t')
R_count = n1_n2_joined.count('r')
U_count = n1_n2_joined.count('u')
E_1_count = n1_n2_joined.count('e')

true_count = T_count + R_count + U_count + E_1_count

L_count = n1_n2_joined.count('l')
O_count = n1_n2_joined.count('o')
V_count = n1_n2_joined.count('v')
E_2_count = n1_n2_joined.count('e')

love_count = L_count + O_count + V_count + E_2_count

#Append the values to get the score
total_count = str(true_count) + str(love_count)
# print(total_count)

#Based on the score, check the compatibality
total_count1 = int(total_count)
if total_count1 < 10 or total_count1 > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count1 > 40 and total_count1 < 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}")
