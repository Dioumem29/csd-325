#Moustapha Dioume
#Assignment 1-2
#creating the function for the bottles couunt
def count_bottles(n):
    while n>= 1:
       
        if n==1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
        else:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        n-=1
        if n == 0:
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        elif n == 1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"Take one down and pass it around, {n} bottles of beer on the wall.")
#get the user input and display the output
bottles =int(input("enter the number of bottles:"))
count_bottles(bottles)
print("Time to buy more beer")