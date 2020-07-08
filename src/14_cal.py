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
"""
  --Assumptions:
  - Must run program via the command line
  - Input is optional
  - Without input, a Calendar will print out the month and year.
      Should use datetime to produce result

  - With Month input, a Calendar will print out chosen month of current year.
      Might extrapolate current year from datetime
  - With 2 inputs (month, year) a calendar will print based on both inputs

  --Plan:
"""
# Pseudocode
# import modules to run the program
import sys
import calendar
from datetime import datetime

# Acquire calendar (month, year) variables
# use datetime to acquire current date arguments (year or month)
today = datetime.today()
month = int(today.month)
year = int(today.year)

is_running = True
while is_running:
# check if there are no cmd line args for year and month (Will have one for file)
  if len(sys.argv) < 2:
    automatic_cal = calendar.monthcalendar(year, month)
    print('Current Month:', calendar.month_name[month])
    print('Current Year:', year)
    print(automatic_cal)
    print('Program expects Month and Year input')
    is_running = False

  # check if there are both cmd line args for month and year
  elif len(sys.argv) > 2:
    chosen_month = int(sys.argv[1]) 
    chosen_year = int(sys.argv[2])
    my_cal = calendar.monthcalendar(chosen_year, chosen_month)
    print('Chosen Month:', calendar.month_name[chosen_month])
    print('Chosen Year:', chosen_year)
    print('My Chosen Calendar:', my_cal)
    is_running = False
    # check if the cmd line arg for year is missing and produce calendar with chosen month and current year
    if not sys.argv[2]:
      my_month_cal = calendar.monthcalendar(year, chosen_month)
      print('Current Year:', year)
      print('Chosen Month:', calendar.month_name[chosen_month])
      print('Selected Month Calendar:', my_month_cal)
      print('Program expects Month and Year input')
    is_running = False

   
