'''
1) Ross is an event organizer. He has received data regarding the participation of 
employees in two different events. Some employees have participated in only one event 
and others have participated in both events. Ross now needs to count the number of 
employees who have taken part in both events. The records received by Ross consist 
of employee ids, which are unique. Write a program that accepts the employee ids 
participating in each event (the first line relates to the first event and the second 
line relates to the second event). The program should print the number of common employee 
ids in both the events.

Suppose the following input is given to the program, where each line represents a different event:

1001,1002,1003,1004,1005
1106,1008,1005,1003,1016,1017,1112

Now the common employee ids are 1003 and 1005, so the program should give the output as:

========================================================================
'''
event_one = {1001, 1002, 1003, 1004, 1005}
print(" IDs of employees of event One:", event_one)

event_two = {1106, 1008, 1005, 1003, 1016, 1017, 1112}
print("\n IDs of employees of event two:", event_two)

print("\n Common employees IDs are:", event_one.intersection(event_two))