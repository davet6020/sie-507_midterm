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

  book_get_cabin_req()
  book_search_availability()
  book_get_name_req()
  exit()
  deck = 1
  row = 24
  col = 1
  ln = 'Twiggs'
  fn = 'Rick'
  booking = ln + ',' + fn + ',' + str(deck) + ',' + str(row) + ',' + str(col)
  print('booking: ', booking)
  update_book(booking)
  update_cabin()

def book_get_cabin_req():
  print('book_get_cabin_req')

def book_get_name_req():
  print('book_get_name_req')

# Called from book(). Test to see if requested
# cabin is available
def book_search_availability():
  print('book_search_availability')


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

  # List of menu choices makes it easier to add more later
  menu_display = ['D to display current cabin chart',
                  'P to purchase an available cabin',
                  'Q to quit']

  print('Select choice from menu')
  for m in menu_display:
    print(m)

  # Receive user input of menu choice
  ch = input().lower().strip()

  # Run the menu choice selected
  menu(ch)

def menu(choice):
  if choice == 'd':
    display()
  elif choice == 'p':
    book()
  elif choice == 'q':
    msg = 'Exiting.'
    exit_program(msg)
  else:
    msg = 'You have selected an invalid menu choice.  Exiting.'
    exit_program(msg)




main()
