from datetime import datetime
import random
import time

# Get the current date and time
now = datetime.now()

# Identity the blood groups
blood_groups = ['A-', ' B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

# Use a dictionary as an analysis function
analysis = {'A-': 'MAYBE', ' B+': 'MAYBE', 'B-': 'MAYBE', 'O+': 'PERFECT', 'O-': 'GOOD', 'AB+': 'POSSIBLE', 'AB-': 'POSSIBLE'}

# Generate a row of data using a random ID and blood group
data = {'id': random.randint(1, 500), 'blood_group': random.choice(blood_groups)}

# Start the analysis
dt_string = now.strftime("%Y-%m-%d %H:%M")
print("{} Beginning analysis".format(dt_string))

# Simulate the analysis time by sleeping for up to 1 minute
time.sleep(random.randint(1, 60))

# Report the analysis
print("CANDIDATE  : {}".format(data['id']))
print("BLOOD GROUP: {}".format(data['blood_group']))
print("ANALYSIS   : {}".format(analysis[data['blood_group']]))
