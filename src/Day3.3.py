# using the python libraries to manipulate dates and times

#
# Example file working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    # print("Today's date is" , date.today())

    # print("Date components: ", date.today().day, date.today().month, date.today().year)

    # print("Today's day is:", date.today().weekday())

    # days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
    # print("Which is a", days[date.today().weekday()])

    current_date_time =  datetime.now()

    print("The current date and time is ", current_date_time)

    t = datetime.time(datetime.now())

    print(t)
if __name__ == "__main__":
    main()