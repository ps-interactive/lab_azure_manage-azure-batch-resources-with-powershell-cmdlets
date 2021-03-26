import sys
import random

blood_groups = ['A-', ' B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
analysis = {'A-': 'MAYBE', ' B+': 'MAYBE', 'B-': 'MAYBE', 'O+': 'PERFECT', 'O-': 'GOOD', 'AB+': 'POSSIBLE', 'AB-': 'POSSIBLE'}

data = {'id': random.randint(1,500), 'blood_group': random.choice(blood_groups)}

print("CANDIDATE  : {}".format(data['id']))
print("BLOOD GROUP: {}".format(data['blood_group']))
print("ANALYSIS   : {}".format(analysis[data['blood_group']]))
