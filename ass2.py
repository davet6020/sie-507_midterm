
import os
import pathlib

# Build path string to data files using current OS path separator
cabin_data = os.path.join(os.getcwd(), 'cabin.csv')
booking_data = os.path.join(os.getcwd(), 'booking.txt')

"""Book a cabin will verify the cabin is available. If it is
Update cabin.csv and insert record into booking.txt"""
def book():
  """1. Ask what deck, row and col
  2. Search booking.txt for availability
  3. If avail, get lastname and firstname and book it
  4. If not avail, ask if they have alternate choice and
       either book that or quit"""

  booking = book_get_cabin_req()

  if booking_available(booking):
    booking = book_get_name_req(booking)
    # Update the booking and cabin files to show occupied
    update_book(booking)
  else:
    # Cabin not available, try for a different one?
    retry = input('That cabin is not available.  Try another one? (Yy/Nn)')
    if retry.lower() == 'y':
      clear()
      book()
    else:
      msg = 'Exiting.'
      exit_program(msg)

  return

'''Prompts a user for the Deck, Row and Cabin they want'''
def book_get_cabin_req():
  booking = {'Deck': [], 'Row': [], 'Cabin': [], 'LastName': [], 'FirstName': []}
  print('Please specify where you would like your cabin to be located')
  deck = row = col = 0

  # Must select a valid Deck
  while deck < 1 or deck > 3:
    try:
      deck = int(input('What Deck? (1-3):'))
    except ValueError:
      print('Choose Deck 1, 2, or 3')

  booking['Deck'].append(deck)

  # Must select a valid Row
  while row < 1 or row > 24:
    try:
      row = int(input('What Row? (1-24):'))
    except ValueError:
      print('Choose Row 1 - 24')

  booking['Row'].append(row)

  # Must select a valid Col
  while col < 1 or col > 2:
    try:
      col = int(input('What Cabin? (1 or 2):'))
    except ValueError:
      print('Choose Cabin 1 or 2')

  booking['Cabin'].append(col)

  return booking

'''If an available cabin was selected, prompt for customers name'''
def book_get_name_req(booking):
  ln = fn = ''

  # Enter Last Name
  while len(ln) == 0:
    try:
      ln = input('What is your last name?:')
    except ValueError:
      print('Enter your last name')

  booking['LastName'].append(ln)

  # Enter First Name
  while len(fn) == 0:
    try:
      fn = input('What is your first name?:')
    except ValueError:
      print('Enter your first name')

  booking['FirstName'].append(fn)

  return booking

# Clear the screen for neatness
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

'''Called from book(). Test to see if requested
    cabin is available'''
def booking_available(booking):
  # Get the three values from the list we want
  tmp1 = booking['Deck'] + booking['Row'] + booking['Cabin']
  # Convert those array values into a string.
  tmp2 = list(map(str, tmp1))
  comma = ','
  # Convert the array values into a string
  needle = comma.join(tmp2)

  with open('booking.txt') as haystack:
    if needle in haystack.read():
      # Cabin is booked, not available
      return False
    else:
      # Cabin is available
      return True

'''Display the current cabin chart from cabins.csv
If cabins.csv ! exist no cabins have been booked yet.'''
def display():
  cdata = pathlib.Path(cabin_data)
  c = open(cdata, 'r')
  print(' Current cabin chart for all decks')
  print(c.read())
  c.close()

def exit_program(msg=''):
  print(msg)
  exit()

'''When the program is first run, check to see if the data files exist
If either booking.txt or cabin.csv do not exist, create them.'''
def initialize_data_files():
  bdata = pathlib.Path(booking_data)
  cdata = pathlib.Path(cabin_data)
  msg = ''

  if not bdata.exists():
    b = open(bdata, 'w')
    b.close()
    msg += 'booking.txt, '

  if not cdata.exists():
    title = ' Deck1    Deck2    Deck3\n'
    row = ' .  .  |  .  .  |  .  .  |\n'

    c = open(cdata, 'w')
    # Write the title one time
    c.writelines(title)

    # Write 24 empty rows
    for r in range(24):
      c.writelines(row)

    c.close()
    msg += 'cabin.csv'

  if len(msg) > 1:
    print('Created data file(s): {}'.format(msg.rstrip(', ')))

'''This is the main function. It gets things started.'''
def main():
  # Check for data files and create if needed
  initialize_data_files()

  while True:
    clear()
    menu()

    # Receive user input of menu choice
    choice = input().lower().strip()

    if choice == 'd':
      clear()
      display()
      input('Press enter key to continue')
    elif choice == 'p':
      clear()
      book()
      input('Press enter key to continue')
    elif choice == 'q':
      msg = 'Exiting.'
      exit_program(msg)
    else:
      msg = 'You have selected an invalid menu choice.  Exiting.'
      exit_program(msg)

'''Build and display the menu'''
def menu():
  # List of menu choices makes it easier to add more later
  menu_display = ['D to display current cabin chart',
                  'P to purchase an available cabin',
                  'Q to quit']

  print('Welcome to the Pacific Princess Booking System\n')
  print('Select a choice from menu')
  for m in menu_display:
    print(m)

# Updates bdata (the pointer to Booking.txt) to contain name and location of cabin
def update_book(booking):
  # Get the five values from the list we want
  tmp1 = booking['LastName'] + booking['FirstName'] + booking['Deck'] + booking['Row'] + booking['Cabin']
  # Convert those array values into a string.
  tmp2 = list(map(str, tmp1))
  # update_cabin needs this info
  cu = list(map(int, booking['Deck'] + booking['Row'] + booking['Cabin']))
  comma = ','
  # Convert the array values into a string
  booking = comma.join(tmp2)

  # Count # lines in booking file.  If not empty,
  #   prepend a new line to each new row appended
  count = len(open(booking_data).readlines())

  bdata = pathlib.Path(booking_data)
  b = open(bdata, 'a')
  b.write(booking + '\n')
  b.close()

  # Call the function to update cabin.csv
  update_cabin(tmp2, cu)

# Update cdata (the pointer to cabin.csv) with location of new booking
def update_cabin(customer, cu):
  lname = customer[0]
  fname = customer[1]
  deck = cu[0]
  row = cu[1]
  col = cu[2]

  cdata = pathlib.Path(cabin_data)
  c = open(cdata, 'r')
  all_rows = c.readlines()
  c.close()

  new_row = all_rows[row]

  # This handles placement of the X on the cabin chart
  if deck == 1:
    if col == 1:
      new_row = new_row[:1] + 'X' + new_row[2:]
    else:
      new_row = new_row[:4] + 'X' + new_row[5:]

  if deck == 2:
    if col == 1:
      new_row = new_row[:10] + 'X' + new_row[11:]
    else:
      new_row = new_row[:13] + 'X' + new_row[14:]

  if deck == 3:
    if col == 1:
      new_row = new_row[:19] + 'X' + new_row[20:]
    else:
      new_row = new_row[:22] + 'X' + new_row[23:]

  # Update all_rows list with new value
  all_rows[row] = new_row
  c = open(cdata, 'wt')

  # Loop through all_rows and re-write cabin.csv
  for row in all_rows:
    c.write(row)

  c.close()

  # Confirm the booking
  clear()
  print('Congratulations {} {}! You have been booked on the Pacific Princess!'.format(fname, lname))
  print("Your stateroom location is as follows:")
  print('Deck {}: Row {}: Cabin {}'.format(cu[0], cu[1], cu[2]))
  print()

# Run the menu choice selected
main()
