


def validator(num:int) -> bool:
    """ This funct returns a bool if the number is perfect or not """
    # List that will take numbers returned by divisions below
    divisors = []
    
    
    #Runner of the validator
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
            
        #Here we skip if the num counted is equal to itself.
        elif num == i:
            continue
        
    #Sum all int in list
    if sum(divisors) == num:
        #returns if the sum is equal to num
        return True
    # Returns if false if it's not
    else:
        return False


#entry point
def run():
    #User gives a number
    num = int(input("Type a number: "))
    
    # 2 validator
    if validator(num):
        print(f"The {num} is a perfect number.")
    else:
        print(f"The {num} is not a perfect number")
        
        
if __name__ == "__main__":
    run()
