# 
# Python Conditionals
#

def main():
    x, y = 100, 1000

    # if x < y:
    #     st = ("X is less than Y")
    
    # elif (x == y):
    #     st = ("X is equal to Y")
    
    # else:
    #     st = ("X is greater than Y")
         
    # print(st)

    # conditional statement shorthand in Python

    st = "x is less than y" if x<y else "x is greater than or equal to y"
    print(st)

if __name__ == "__main__":
    main()