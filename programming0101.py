#1
answer = input("What is your name?")

print ("Nice to meet you! " + answer)

#3 a friend helped me with this and explained that the code used reverse function
string=input(("Enter a word:"))  
if(string==string[::-1]):  
      print("This word is a palindrome!!")  
else:  
      print("This word is not a palindrome...")

#2
def isMultiple(num1,num2):
      if num1 % num2 == 0:
            print(str(num1) + " is a multiple of " + str(num2))
      else:
            print(str(num1) + " is not a multiple of " + str(num2))
      
def main():
      isMultiple(3,13)

if __name__ == "__main__":
      main()

