
from prettytable import PrettyTable


print("\nMy TO-DO List.")

instructions = "\n1. Add Task.\n2. Delete Task.\n3. Update Task.\n4. Exit.\n5. Check List."

print(instructions)

my_todo_list = []

x = PrettyTable()

def my_list():
	x.field_names = ["Item Names"]
	for i in my_todo_list:
		x.add_row([i])			#This will add new task
	print(x.get_string(title="TO DO List"))			#This will give title
	x.clear_rows() 		#Clear the table

running = True
while running:
	
	user_input = input("\nWhat do You want to do? (1, 2, 3, 4, 5): ")
	if user_input == "1":
		new_todo = input("\nPlease enter your new task: ")
		print(f"\nYour new task is {new_todo}.")
		my_todo_list.append(new_todo)
	

	#Delete
	elif user_input == "2":
		
		while True:
			
			item_name = input("Please enter the task that you want to Delete: ")
			
			try:
				if item_name in my_todo_list:
					choice = input("Confirm to Delete {item_name} from your list. (y/n) ")
					if choice == "y":
						my_todo_list.remove(item_name)
						print("Task Updated.")
						my_list()
						break
				else:
					print("Task not found.")
			
			except Exception:
				print("Something Went wrong.")

	#Update
	elif user_input == "3":
		while True:
			item_name = input("Please enter the task that you want to Update: ")

			try:
				if item_name in my_todo_list:
					choice = input(f"\nAre you sure to update {item_name}from your list? (y/n) ")
					if choice == "y":
						update_item = input(f"Please enter a name you want to Update {item_name} with. ")
						index = my_todo_list.index(item_name)
						my_todo_list[index] = update_item
						print("Your updated TO-DO List")
						my_list()
						break
				else:
					print("Item not found.")
			except Exception:
				print("Something Went wrong.")
			
				
	elif user_input == "4":
		ask_user = input("\nAre you sure to exit? (y/n): ")
		if ask_user == "y":
			running = False
	elif user_input == "5":
			my_list()
	elif user_input == "" or user_input == " ":
		print("Please enter something.")
	else:
		print("Please enter a valid value.")