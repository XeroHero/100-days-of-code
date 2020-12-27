def main():
    x = 0
# # while loop
#     while x<5:
#         print(x)
#         x+=1

# # for loop
#     for x in range(5, 10):
#         print(x)

# # for loop in collection

#     days = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     for d in days:
#         print(d)

# Break and continue statements
# for x in range(5, 10):
#     # if x == 7: break

#     if (x % 2 == 0): continue
    
#     print(x)

    days = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i,d in enumerate(days):
        print(str(i) + " " + d)
if __name__ == "__main__":
    main()