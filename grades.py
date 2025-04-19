#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.


name=input("Enter Your Name: ")
maths=int(input("Enter your Maths marks: "))
english=int(input("Enter your English marks: "))        
science=int(input("Enter your Science marks: "))
total=maths+english+science 
percentage=total/3
print("Total Marks: ",total)
print("Percentage: ",percentage)           
if percentage>=90:
    print(name,"Your Grade is A+")
elif percentage>=80:
    print(name,"Your Grade is A")           
elif percentage>=70:
    print(name,"Your Grade is B")
elif percentage>=60:
    print(name,"Your Grade is C")  
elif percentage>=50:
    print(name,"Your Grade is D")
elif percentage>=40:
    print(name,"Pass ")
else:   
    print(name,"Fail")