
def get_item(item_num):
  if item_num == 1:
    return "Cheeseburger"
  if item_num == 2:
    return "Fries"
  if item_num == 3:
    return "Soda"
  if item_num == 4:
    return "Ice Cream"
  if item_num == 5:
    return "Cookie"

def welcome():
  print("Welcome to McDonalds! Menu Items: ")
  print("Cheeseburger, Fries, Soda, Ice Cream, Cookie")


def main():
  item_num = int(input("What item number would you like?"))
  return item_num

welcome()
item = main()
print(get_item(item))