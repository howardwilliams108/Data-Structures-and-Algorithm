

# Program 1: Singly List
class PatientNode: # this class would contain unique Patient ID, Name and Disease

    def __init__(self, patient_id,name, disease):

        
        self.patient_id = patient_id #    this stores  the patient's ID

        # this will store the patient's name
        self.name = name

        
        self.disease = disease # self.disease stores the patient's disease

        # Point to the next patient node
        self.next = None


#  the class will have the singly linked list
class patientLinkedList:

    def __init__(self):

        
        self.head = None# what this means is that list will be currently empty


    
    # the function would check if the patient's id existed
    
    def patient_id_exists(self, patient_id):

        
        current = self.head # would check from the first node

        
        while current is not None: # this loop would continue until the end of the list

            # the if loop will compare the current id with requested id
            if current.patient_id == patient_id:
                return True

            
            current = current.next # changing to the next patient in the list

        # The ID was not found
        return False
        # Time complexity used is O(n) as it traverses the linked list from the  beginning to end,
        # but the worst case, would be checking every patient in the list

    
    # function will count the patients currently in list
    
    def count_patients(self):

        count = 0

        
        current = self.head

        
        while current is not None:

            count += 1 # this will ensure every node is visited

            
            current = current.next

        return count
        #Time complexity used here is O(N) with each node visited counted once,

    
    # Adding one patient to the end of the list
    
    def register_patient(self, patient_id, name, disease):

        #added to prevent duplicate patient ids

        if self.patient_id_exists(patient_id): # if the statement is true

            print("Sorry! That Patient ID already exists.")
            return False

        # Creating a patient node

        new_patient = PatientNode(
            patient_id,
            name,
            disease
        )

        #If the list is empty
        if self.head is None:

            # The new patient becomes the first node
            self.head = new_patient

        # if the list already contains patients
        else:

            # Begin at the first node
            current = self.head

            # Move until current reaches the last node
            while current.next is not None:
                current = current.next

            # Connect the last node to the new patient
            current.next = new_patient

        print("\nPatient registered successfully.")
        return True


    
    # Register number of patients patients
    
    def register_multiple_patients(self, numberofpatients):

        # repeating once for each patient
        for number in range(1, numberofpatients+1):

            print(f"\nEnter information for Patient {number}")

            patient_id = input("Patient ID: ").strip()

            # while loop will keep asking until a unique ID is entered
            while self.patient_id_exists(patient_id):

                print("That Patient ID already exists.")

                patient_id = input("Enter a different Patient ID: ").strip()


            name = input("Patient Name: ").strip()

            disease = input("Disease: ").strip()

            # adding the patient to the end
            self.register_patient(
                patient_id,
                name,
                disease
            )
            # O(n) is time complexity used as linked list is searched to ensure each ID is unique
            # worst case is O(n^2) because every insertion will cause an O(n)

    
    # inserting a new patient into the middle
   
    def insert_in_middle(self):

        print(" Enter the new patient's information")

        patient_id = input(" Patient ID: ").strip()

        # Prevent duplicate IDs
        if self.patient_id_exists(patient_id):

            print("Sorry! That Patient ID already exists.")
            return

        name = input("Patient Name: ").strip()

        disease = input("Disease: ").strip()

        # Create the new node
        new_patient = PatientNode(
            patient_id,
            name,
            disease
        )

        # Find the number of nodes
        number_of_patients =  self.count_patients()

        
        if self.head is None:

            self.head = new_patient

            print("\nThe list was empty.")
            print("The patient was added as the first record.")
            return

      
        if number_of_patients == 1:

            # Insert the new patient after the first node
            new_patient.next = self.head.next

            self.head.next = new_patient

            print("\nThe patient was inserted after the first record.")
            return

        # Determine where the middle begins
        middle_position = number_of_patients // 2

        # Begin at the first node
        current = self.head

        # Move to the node directly before the middle
        for _ in range(middle_position - 1):
            current = current.next

        # The new patient points to the next node
        new_patient.next = current.next

        # The current node points to the new patient
        current.next = new_patient

        print("\nPatient inserted into the middle successfully.")


    
    # Delete a patient from the middle
    
    def delete_from_middle(self):

        # Counts the patients
        numberofpatients = self.count_patients()

        # if the list is empty
        if self.head is None:

            print("\nThe patient list is empty currently.")
            print("There is no patient to delete.")
            return

        # if there is only one patient
        if numberofpatients == 1:

            # Save the patient being deleted
            deleted_patient = self.head

            # Make the list empty
            self.head = None

            print("\nThe only patient was deleted.")
            print("Patient ID:", deleted_patient.patient_id)
            print("Patient Name:", deleted_patient.name)
            print("Disease:", deleted_patient.disease)
            return

        # calculates the middle position within list to find middle position
        middle_position = numberofpatients // 2

        
        previous = None

        # Current begins at the first node
        current = self.head

        # Move current to the middle node
        for _ in range(middle_position):

            previous = current
            current = current.next


        # making previous skip the middle node
        previous.next = current.next


        print("\nMiddle patient deleted successfully.")
        print("Patient ID:",  current.patient_id)
        print("Patient Name:",  current.name)
        print("Disease:",  current.disease)


    
    # function is used to display every patient
    
    def display_patients(self):

        # Check for an empty list
        if self.head is None:

            print("\nThe patient list is empty.")
            return

        print("\n")
        print("          PATIENT RECORDS   ")
        

        # Begin with the first patient
        current = self.head

        patient_number = 1

        # Continue until every patient is displayed
        while current is not None:

            print(f"\nPatient {patient_number}")
            
            print("Patient ID :", current.patient_id)
            print("Name       :", current.name)
            print("Disease    :", current.disease)

            # Move to the next node
            current = current.next

            patient_number += 1

        print("\n")
        print("Total Patients:", patient_number - 1)



# this will ensure that a positive integer is received from the user

def get_positive_integer(message):

    while True:

        try:

            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:

            print("Invalid input. Please, enter a whole number.")





def main():

    # this will create an empty patient linked list
    patient_list = patientLinkedList()

    
    while True:
        # this will present the menu to user and only exit when if user chooses option
        print("\n")
        print("      THE PATIENT RECORD SYSTEM         ")
        print("")
        print("1. Register 'n' patients")
        print("2. Insert a new patient in the middle")
        print("3. Delete a patient from the middle")
        print("4. Display all the patient records")
        print("5. Exit")
        print("")

        choice = input("Please. Enter your choice: ").strip()

        # Register number of  patients
        if choice == "1":

            numberofpatients = get_positive_integer("\nHow many patients would you like to register today? ")

            patient_list.register_multiple_patients(numberofpatients )

        # Inserting a patient in the middle
        elif choice == "2":

            patient_list.insert_in_middle()

        # deletes the middle patient
        elif choice == "3":

            patient_list.delete_from_middle()

        # this will display all patients
        elif choice == "4":

            patient_list.display_patients()

        # user ends the program if 5 is chosen
        elif choice == "5":

            print("\nThank you for using The Patient Record System.")
            print("Goodbye.")
            break

        # Invalid menu option!
        else:

            print("Invalid choice.")
            print("Please select a number from 1 through 5.")



if __name__ == "__main__":
    main()