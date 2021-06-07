import json

schedule_dict = {}                                 #main dictionary that stores data
def add_event():
    date = input('Enter a date: ')
    time = input('Enter time: ')
    event = input('Enter event name: ')

    if date in schedule_dict.keys():               #adds event when:
        if time in schedule_dict[date].keys():     #both date and time already exist in dict
            schedule_dict[date][time].append(event)

        else:                                      #date exist, time doesnt 
            l = []
            schedule_dict[date][time] = l
            l.append(event)
            
    else:                                          #both date and time doesnt exist
        schedule_dict[date] = {time:[]}
        schedule_dict[date][time].append(event)

    print("Event added\n")


def remove_event():
    date = input('Enter the date: ')

    if date in schedule_dict.keys():               #removes event if:
        event = input('Enter event to be removed: ')
        for i in schedule_dict[date].values():
            l = i

            if event in l:                            #date and event exist
                l.remove(event)
                print('Event has been removed\n')

                for i in schedule_dict[date].copy():  #removes the whole date, if no event exist
                    if not schedule_dict[date][i]:    #after removing that earlier event
                        schedule_dict[date].pop(i)                
                return 0
        else:                                      
            print('Event doesnt exist\n')       
    else:
        print('Date doesnt exist\n')               


def rename_event():
    date = input('Enter the date of event: ')

    if date in schedule_dict.keys():               #renames event if:
        event = input('Enter name of event to be renamed: ')
        for i in schedule_dict[date].values():
            l = i

        for i in range(len(l)):
            if event == l[i]:                      #event and date exist
                rename = input('Enter a new name for event: ')
                l[i] = rename
                print("Event renamed succesfully\n")
                return 0

            else:
                print('Event doesnt exist\n')        #event doesnt exist
    else:
        print('Date doesnt exist\n')                 #date doesnt exist


def change_datetime():
    date_old = input('Enter the date of the event: ')
    if date_old in schedule_dict.keys():           
        event = input('Enter name of event to be changed: ')

        for i in schedule_dict[date_old].values():
            l = i

        if event in l:
            l.remove(event)                        #removes existing event

            for i in schedule_dict[date].copy():   #removes the whole date, if no event exist
                    if not schedule_dict[date][i]: #after removing that earlier event
                        schedule_dict[date].pop(i)   
        else:
            print("Event doesnt exist\n")

        date = input('Enter new date: ')
        time = input('Enter new time: ')

        if date in schedule_dict.keys():            #Creats a new event with edited date/time when:        
            if time in schedule_dict[date].keys():  #both date and time already exist in dict
                schedule_dict[date][time].append(event)
            else:                                   #date exist, time doesnt 
                l = []
                schedule_dict[date][time] = l
                l.append(event)         
        else:                                       #both date and time doesnt exist
            schedule_dict[date] = {time:[]}
            schedule_dict[date][time].append(event)
        
        print("Event's time/date changed succesfully\n")
        
    else:
        print('Date doesnt exist\n')

def print_all():
    for date in schedule_dict:
        print(date.upper(), ':', sep='')
        for time in schedule_dict[date].keys():
            print(' '*5,time, ':', sep='')
            for i in schedule_dict[date][time]:
                print(' '*8,'-', i, sep='')
            print(' ')
    print(' ')

def print_event_of_date():
    date = input('Enter the date: ')
    if date in schedule_dict.keys():
        print(date.upper(), ':', sep='')
        for time in schedule_dict[date].keys():
            print(' '*5,time, ':', sep='')
            for i in schedule_dict[date][time]:
                print(' '*8,'-', i, sep='')
            print(' ')
        print(' ')
    else:
        print("date doesnt exist\n")

def is_event_present():
    event = input('Enter name of even to be checked: ')
    for date in schedule_dict.keys():
        for time in schedule_dict[date].values():
            for i in time:
                if i == event:
                    print(event, '- Event is present on', date,'\n')
                    return 0
    else:
        print('Event doesnt exist\n')
        
    

def save_data():                                    #writes the data into a .txt file
    with open('To-Do List data.txt', 'w+') as f:
        f.write(str(schedule_dict))
    print('data saved succesfully\n')

def load_data():                                    #reads the data from the .txt file
    with open('To-Do List data.txt', 'r') as f:
        global schedule_dict
        schedule_dict = eval(f.read())
    print('data loaded succesfully\n')


def main():
    run = True
    print('''
            0. stop program
            1. add event
            2. remove event
            3. rename event
            4. edit date/time of an event
            5. print all event
            6. print events of a specific day
            7. to see if an event exist
            8. save data into a .txt file
            9. load data
        ''')

    while True:
        a = input('>> Enter a command no: ')

        if a == '0':
            break
        elif a == '1':
            add_event()
        elif a == '2':
            remove_event()
        elif a == '3':
            rename_event()
        elif a == '4':
            change_datetime()
        elif a == '5':
            print_all()
        elif a == '6':
            print_event_of_date()
        elif a == '7':
            is_event_present()
        elif a == '8':
            save_data()
        elif a == '9':
            load_data()
        else:
            print('Wrong command')
            main()


print('''
                           To-Do list Program

This program allows you to make events as a reminder for specific time of a day
''')
main()
