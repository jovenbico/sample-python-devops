#!/usr/bin/env python3

import time

start_time = time.localtime()
print(f"Start time: {time.strftime('%X', start_time)}")

# prest Enther to stop the timer
input("Press 'Enter' to stop the timer")

end_time = time.localtime()

# Calculate the time taken
time_taken = time.mktime(end_time) - time.mktime(start_time)

# Print end time
print(f"End time: {time.strftime('%X', end_time)}")
# Print the time taken
print(f"Time taken: {time_taken} seconds")