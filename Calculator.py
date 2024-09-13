import os

def main():
    print("Calculator")
    if not os.path.exists('history.txt'):
        with open('history.txt', 'w'):
            pass
    num_calculations = sum(1 for line in open('history.txt')) if os.path.exists('history.txt') else 0
    print(f"{num_calculations} calculations stored in history")
    print("Commands:")
    print("0 - end program")
    print("1 - calculate addition (+)")
    print("2 - calculate subtraction (-)")
    print("3 - calculate multiplication (*)")
    print("4 - calculate division (/)")
    print("5 - show history")
    print("6 - empty history")
    print("7 - show commands")
    select_command()

def select_command():
    command = int(input("Select command: "))
    if command == 0:
        print("Shutting down program...")
        return
    elif command == 1:
        calculate("addition", "+")
    elif command == 2:
        calculate("subtraction", "-")
    elif command == 3:
        calculate("multiplication", "*")
    elif command == 4:
        calculate("division", "/")
    elif command == 5:
        show_history()
    elif command == 6:
        empty_history()
    elif command == 7:
        main()
    else:
        print("Invalid command")
        select_command()

def calculate(operation, operator):
    num1 = float(input(f"Input number: "))
    num2 = float(input(f"Input number: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    print(f"Result: {result}")
    with open('history.txt', 'a') as file:
        file.write(f"{num1};{operator};{num2};{result}\n")
    select_command()

def show_history():
  if os.path.exists('history.txt'):
      num_calculations = sum(1 for line in open('history.txt'))
      if num_calculations == 0:
          print("No history available.")
      else:
          print(f"{num_calculations} calculations in history:")
          with open('history.txt','r') as file:
              for line in file:
                  print(line.strip())
  else:
      print("No history available.")
  select_command()

def empty_history():
    if os.path.exists('history.txt'):
        open('history.txt', 'w').close()
        print("History cleared.")
    else:
        print("No history available.")
    select_command()


if __name__ == "__main__":
    main()
