# Define the table for the agent's actions based on sensor perceptions
table = {
    ('NM', 'NS', 'NGB'): 'Do Nothing',
    ('NM', 'SD', 'NGB'): 'Active Fire Suppression, Send Alert',
    ('NM', 'NS', 'GBD'): 'Sound Alarm, Send Alert',
    ('NM', 'SD', 'GBD'): 'Sound Alarm, Active Fire Suppression, Send Alert',
    ('MD', 'NS', 'NGB'): 'Sound Alarm, Send Alert',
    ('MD', 'SD', 'NGB'): 'Active Fire Suppression, Sound Alarm, Send Alert',
    ('MD', 'NS', 'GBD'): 'Sound Alarm, Send Alert',
    ('MD', 'SD', 'GBD'): 'Active Fire Suppression, Sound Alarm, Send Alert'
}

# List to store percept history
percepts = []

def table_driven_agent(percept):
    print('Perception Received: ' + str(percept))
    percepts.append(percept)  # Updating percept history
    action = table.get(percept, 'Invalid Perception Combination')
    return action

import random

# Simulate initial perceptions
motion_states = ['NM', 'MD']  # NM: No Motion, MD: Motion Detected
smoke_states = ['NS', 'SD']   # NS: No Smoke, SD: Smoke Detected
glass_states = ['NGB', 'GBD'] # NGB: No Glass Break, GBD: Glass Break Detected

# Start perception-action cycle
while True:
    # Randomly generate perception for motion, smoke, and glass break
    motion = random.choice(motion_states)
    smoke = random.choice(smoke_states)
    glass_break = random.choice(glass_states)
    
    # The agent program is being called with the current perception
    action = table_driven_agent((motion, smoke, glass_break))
    print('Action Performed: ' + action)
    
    # User control to allow next perception
    cmd = input('Type x to exit, or any key to continue: ')
    if cmd == 'x':
        break