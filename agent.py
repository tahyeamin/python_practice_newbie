table={('NM','NS' ,'NGB'):'Do Nothing',
       ('NM', 'SD', 'NGB'):'Active Fire Suppression' , 
       ('NM', 'SD', 'NGB'): 'Send Alert', 
       ('NM', 'NS', 'GDB'): 'Sound Alarm ', 
       ('NM', 'NS', 'GDB'): 'Send Alert', 
       ('NM', 'SD', 'GDB'): 'Sound Alarm',
       ('NM', 'SD', 'GDB'): 'Active Fire Suppression',
       ('NM', 'SD', 'GDB'): 'Send Alert', 
       ('MD' , 'NS' , 'NGB'):'Sound Alarm',
       ('MD' , 'NS' , 'NGB'):'Send Alert',
       ('MD' , 'SD' , 'NGB'):'Active Fire Suppression',
       ('MD' , 'SD' , 'NGB'):'Sound Alarm',
       ('MD' , 'SD' , 'NGB'):'Send Alert',
       ('MD' , 'NS' , 'GBD'):'Sound Alarm',
       ('MD' , 'NS' , 'GBD'):'Send Alert',
       ('MD' , 'SD' , 'GBD'):'Active Fire Suppression',
        ('MD' , 'SD' , 'GBD'):'Send Alert',
       ('MD' , 'SD' , 'GBD'):'Sound Alarm',
      }


percepts=[]  # to store percept history

def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept) # updating percept history
    action = table[percept]
    return action


import random


# simulating the first perception randomly
# NM for no motion
action = random.choice(['NM', 'MD' , 'NS' , 'SD' , 'NGB' , 'GBD'])
Condition = random.choice(['Active Fire Suppression','Sound Alarm' , 'Send Alert'])

# to perceieve environment repeatedly
while True:
    # the agent program is being called with current perception
    action = table_driven_agent((action, Condition))
    print('Action Performed: '+ action)

    # user control to allow next perception
    cmd = input('Type x to exit! or any key to continue.')
    if(cmd == 'x'): break

    # simulating the next perception
    # if the previous action was 'Go Right' then in the next perception loc=B is obvious
    if action == 'Do Nothing':
    
        Condition = random.choice(['NM','NS' ,'NGB'])

    # if the previous action was 'Go Left' then in the next perception loc=A is obvious
    elif action == 'Sound Alarm' and  'Send Alert':
       
        Condition = random.choice(['NM', 'SD', 'NGB'])
    # if the previous action was 'Remove Dirt' then in the next perception loc remains same and the status=Clean is obvious
    
    elif action == 'Sound Alarm' and  'Send Alert':
       
        Condition = random.choice(['NM', 'NS', 'GDB'])


    elif action == 'Active Fire Suppression' and  'Send Alert':
        
        Condition = random.choice(['NM', 'SD', 'GDB'])
    
    elif action == 'Sound Alarm' and  'Send Alert':
       
        Condition = random.choice(['MD' , 'NS' , 'NGB'])


    elif action == 'Sound Alarm' and  'Send Alert' and 'Active Fire Suppression':
       
        Condition = random.choice(['MD' , 'SD' , 'NGB'])

    
    elif action == 'Sound Alarm' and  'Send Alert':
      
        Condition = random.choice(['MD' , 'NS' , 'GBD'])



    elif action == 'Sound Alarm' and  'Send Alert' and 'Active Fire Suppression':
       
        Condition = random.choice(['MD' , 'SD' , 'GBD'])


   
    
  
