class EventNode:
    #this node will store  Event ID, Event Name and Date

    def __init__(self, eventid, eventname, date):
        self.event_id = eventid
        self.event_name = eventname
        self.event_date = date
        self.prev = None
        self.next = None


class EventLog: # this  class creates the doubly linked list

    def __init__(self):
        self.start = None
        self.end = None


# function below  will check whether event id is already stored in 
#the linked list(doubly)

    def event_exists(self, eventid):

        #time complexity is O(n) because the loops tranverse the list one node at a time, 
        #until the event ID is reached/ end is reached.

        current = self.start

        while current is not None:
            if current.event_id == eventid:
                return True

            current = current.next

        return False

    def append_event(self, eventid, eventname, date):

        # this function would add a new event to the end of the linked list

        if self.event_exists(eventid):

            print("Sorry! That Event ID already exists.")
            return False

        new_event = EventNode(
            eventid,
            eventname,
            date
        )

        if self.start is None:
            self.start = new_event
            self.end = new_event
        else:
            new_event.prev = self.end
            self.end.next = new_event
            self.end = new_event

        print("\nEvent logged successfully.")
        return True

# this allows the user to register multiple events


    def log_n_events(self, number_of_events):

        # Time complexity is O(n) as the function executes every event enter once,
        # but worst case may be O(n^2) due to every insertion in this loop will cause an O(n)
        for number in range(1, number_of_events + 1):
            # for loop will repeat for event the user enters once
            print(f"\nEnter information for Event {number}")

            event_id = input("Event ID: ").strip() # i'm using .strip() to remove unnecessary spaces

            while self.event_exists(event_id):
                print("Sorry. That Event ID already exists.")
                event_id = input("Please. Enter a different Event ID").strip()

                # program asks for event name and date
            event_name = input("Event Name: ").strip() 

            event_date = input( "Event Date (MM-DD-YYYY): ").strip()

            self.append_event(
                event_id,
                event_name,
                event_date
            )

            

    def insert_beginning(self):
        # function will insert a new event at the beginning

        print("\nEnter the new event information")

        event_id = input("Event ID: ").strip()

        if self.event_exists(event_id):
            print("\nError: That Event ID already exists.")
            return

        event_name = input("Event Name: ").strip()

        event_date = input( "Event Date (MM-DD-YYYY): ").strip()

        new_event = EventNode(
            event_id,
            event_name,
            event_date
        )

        if self.start is None:
            self.start = new_event

            self.end = new_event
        else:
            new_event.next = self.start
            self.start.prev = new_event

            self.start = new_event

        print("\nEvent inserted at the beginning successfully.")


# the function will delete recently added event at the end
    def delete_recent_event(self):
        if self.end is None:

            print("\nThere are no events to delete.")

            return

        deleted_event = self.end

        if self.start == self.end:
            self.start = None

            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

            deleted_event.prev = None
            # time complexity used is O(1) as uses the end pointer

        print("\nMost recent event deleted successfully.")

        print("Event ID   :", deleted_event.event_id)
        print("Event Name :", deleted_event.event_name)

        print("Event Date :", deleted_event.event_date)


    def display_events(self):
        # displaying all the events from the first node to the last node
        if self.start is None:

            print("\nThere are no events recorded.")

            return

        
        print("              EVENT LOG            ")
        

        current = self.start

        event_number = 1

        while current is not None: # this while loop will run until loop goes past final node
            print(f"\nEvent {event_number}")
            
            print("Event ID   :", current.event_id)
            print("Event Name :", current.event_name)
            print("Event Date :", current.event_date)

            current = current.next
            event_number += 1

        
        print("Total Events:", event_number - 1)


def get_positive_integer(message):
    while True:
        try: # 
            #using try as converting txt to int can produce a value error
            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    event_log = EventLog() # this would create empty EventLog doubly linked list

    while True:
        print()
        print("         THE EVENT LOGGING SYSTEM      ")
        print("  ")
        print("1. Log 'n' events")
        print("2. Insert an event at the beginning")
        print("3. Delete the most recent event")
        print("4. Display all events")
        print("5. Exit")
        

        choice = input("Please. Enter your choice: ").strip()

        if choice == "1":
            number_of_events = get_positive_integer("\n. Thanks! Next!How many events would you like to log? ")

            event_log.log_n_events(number_of_events)

        elif choice == "2":
            event_log.insert_beginning()

        elif choice == "3":
            event_log.delete_recent_event()

        elif choice == "4":
            event_log.display_events()

        elif choice == "5":
            print("\nThank you for using The Event Logging System.")
            print("Goodbye!")
            break

        else:
            print("\nSorry. Invalid menu choice.")
            print("Please, select a option from 1 through 5.")


if __name__ == "__main__":
    main()