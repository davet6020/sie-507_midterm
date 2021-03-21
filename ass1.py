def menu(choice):
  menu = {
    'd': 'display_chart',
    'p': 'purchase_cabin',
    'q': 'exit_program',
  }
  if choice not in menu:
    print('Invalid menu option selected.')
    exit()
  else:
    return menu.get(choice, 1)

def display_chart():
  print('display that chart')


def purchase_cabin():
  print('purchase that cabin')


def exit_program():
  exit()


# Take input choice and run the menu choices it is associated to
  print('1')
  ch = input().lower().strip()
  run = globals()[menu(ch)]
  run()

