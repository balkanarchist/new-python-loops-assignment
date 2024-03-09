# Create a while loop that runs indefinitely, printing out the current time.
# Use a break statement to exit the loop if a certain condition is met
# (e.g., if the current time matches a target time).
# Discuss how the break statement can be used to exit a loop based on a condition.

import time

def print_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S")  # Apparently, this will get you the current time
        print(f"Current time: {current_time}")

        if current_time == "11:13:00":
            print("Target time reached. Exiting the loop.")
            break

        time.sleep(2) # Used to slow down infinite output to only once every two seconds - cool hack

# Example usage:
print_current_time()

'''
The break statement is used to stop infinite loops. Note that it should be written
after the print statement so that the user can see that the condition has been met
and that the code will now stop running (per the break statement).
'''