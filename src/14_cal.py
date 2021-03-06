"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

data = sys.argv[1:]
curr = datetime.now()
error = "Welcome to the calendar printer, please provide a valid month number followed by a specific year of your choice"

if int(data[0]) not in range(1, 13):
    print(error)
    sys.exit()
else:
    if len(data) == 0:
        data = [curr.month, curr.year]
    elif(len(data) == 1):
        data.append(curr.year)

    my_cal = calendar.prmonth(int(data[1]), int(data[0]))

    print(my_cal)

    sys.exit()

# improvements to include defaults and if there is a missinf arg, use default.

# Victor's example

#  argv = sys.argv[1:]
#  month = int(datetime.now().month)
#  year = int(datetime.now().year)
#  if len(argv) > 2:
#      print("Usage format: 14_cal.py [-h] [-m M] [-y Y]")
#      exit()
#  elif len(argv) == 2:
#      month = int(argv[0])
#      year = int(argv[1])
#  elif len(argv) == 1:
#      month = int(argv[0])
#  print(calendar.month(int(year), int(month)))
