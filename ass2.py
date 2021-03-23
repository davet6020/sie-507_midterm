import os
import pathlib

# Build path string to data files using current OS path separator
cabin_data = os.path.join(os.getcwd(), 'cabin.csv')
booking_data = os.path.join(os.getcwd(), 'booking.txt')

# Book a cabin will verify the cabin is available. If it is
# Update cabin.csv and insert record into booking.txt
def book():
  print('Booking that cabin')
  # 1. Ask what deck, row and col
  # 2. Search booking.txt for availability
  # 3. If avail, get lastname and firstname and book it
  # 4. If not avail, ask if they have alternate choice and
  #      either book that or quit

  booking = book_get_cabin_req()

  book_search_availability(booking)
  booking = book_get_name_req(booking)
  print(booking)
  return

  update_book(booking)
  update_cabin()

def book_get_cabin_req():
  booking = {'Deck': [], 'Row': [], 'Column': [], 'LastName': [], 'FirstName': []}
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
      col = int(input('What Column? (1 or 2):'))
    except ValueError:
      print('Choose Column 1 or 2')

  booking['Column'].append(col)

  return booking

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

# Called from book(). Test to see if requested
# cabin is available
def book_search_availability(booking):
  print('Search for {}'.format(booking))

# Clear the screen for neatness
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

# Display the current cabin chart from cabins.csv
# If cabins.csv ! exist no cabins have been booked yet.
def display():
  cdata = pathlib.Path(cabin_data)
  c = open(cdata, 'r')
  print(' Current cabin chart for all decks')
  print(c.read())
  c.close()

def exit_program(msg=''):
  print(msg)
  exit()

# When the program is first run, check to see if the data files exist
# If either booking.txt or cabin.csv do not exist, create them.
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

  if(len(msg) > 1):
    print('Created data file(s): {}'.format(msg.rstrip(', ')))

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


def menu():
  # List of menu choices makes it easier to add more later
  menu_display = ['D to display current cabin chart',
                  'P to purchase an available cabin',
                  'Q to quit']

  print('Select choice from menu')
  for m in menu_display:
    print(m)


def update_book(booking):
    # Count # lines in booking file.  If not empty,
    #   prepend a new line to each new row appended
    count = len(open(booking_data).readlines())

    bdata = pathlib.Path(booking_data)
    b = open(bdata, 'a')

    if count > 0:
      b.write('\n' + booking)
    else:
      b.write(booking)

    b.close()

def update_cabin():
    print()

# Run the menu choice selected
main()
