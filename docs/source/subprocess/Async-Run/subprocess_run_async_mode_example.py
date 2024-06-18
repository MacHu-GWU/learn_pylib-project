# -*- coding: utf-8 -*-

import subprocess
from datetime import datetime

def run_script_async(script):
    process = subprocess.Popen(['python', script])
    return process

# Start the timer
start_time = datetime.now()

# Run script1 and script2 concurrently
script1_process = run_script_async("script3.py")
script2_process = run_script_async("script4.py")

# Wait for both scripts to complete
response1 = script1_process.wait()
response2 = script2_process.wait()
print(f"{response1 = }")
print(f"{response2 = }")

# Calculate the total execution time
execution_time = (datetime.now() - start_time).total_seconds()

print(f"Total execution time: {execution_time:.2f} seconds")