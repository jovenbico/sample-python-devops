#!/usr/bin/env python3.11

# import time
from time import localtime, mktime, strftime

start_time = localtime()
print(f"Start time: {strftime('%X', start_time)}")

# prest Enther to stop the timer
input("Press 'Enter' to stop the timer")

end_time = localtime()

# Calculate the time taken
time_taken = mktime(end_time) - mktime(start_time)

# Print end time
print(f"End time: {strftime('%X', end_time)}")
# Print the time taken
print(f"Time taken: {time_taken} seconds")