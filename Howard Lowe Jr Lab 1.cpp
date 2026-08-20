#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Person // task one: using class Person to have the following variables:
{
    public:

        string name;
        double kilograms;
        double heightMeters;
        double BMI;
        int age;

        void Greeting() // Task one: it will print to the standard output "Hello my name is 'name;"
       {
            cout << "Hello my name is " << name << endl;
       }

       void calculateBMI() // Task one: calculates BMI and prints to the standard output the persons BMI category
       {
            BMI = kilograms / (heightMeters * heightMeters);
            cout << "The BMI is: " << BMI << endl;

            if (BMI < 18.5)
            {
                cout << "BMI is underweight!"<< endl;
            }

            else if (BMI < 25)
            {
                cout << "BMI is at normal weight" << endl;

            }

            else if (BMI < 30)
            {
                cout << "BMI is overweight!" << endl;

            }

            else
            {
                cout << "You are obese!!!" << endl; 
            }
       }

      int GCD(int a, int b) // This is euclidean algorithm for task 3 being used in finding remainders until GCD is found
    {
        while (b != 0)
            {
                int rem = a % b;
                a = b;
                b = rem;
            }

    return a;
}


};

 int main()
       {
        int size = 3;

        Person people[size];


        // Task one: creating 3 separate instances that include assigning a name, kilograms and height meters
        Person person0;
        person0.name = "Matthew";
        person0.kilograms = 89;
        person0.heightMeters = 1.8;

        Person person1;
        person1.name = "Alice";
        person1.kilograms = 60;
        person1.heightMeters = 1.2;

        Person person2;
        person2.name = "George";
        person2.kilograms = 40;
        person2.heightMeters = 1.3;

        person0.Greeting(); // task 1: this will use Greeting function to greet the person with their correct name
        person0.calculateBMI(); // task1: this will use the calculateBMI function to calculate the BMI for the correct person

        person1.Greeting();
        person1.calculateBMI();

        person2.Greeting();
        person2.calculateBMI();

        
        //Task 2: below will allow creation of array of person objects
        people[0].name = "Aubrey Graham"; //using people instead of person so that the below will be used in the array list
        people[0].kilograms = 70;
        people[0].heightMeters = 1.72;

        people[1].name = "CJ Johnson";
        people[1].kilograms = 90;
        people[1].heightMeters = 1.903;

        people[2].name = "Rachel Green";
        people[2].kilograms = 34.00;
        people[2].heightMeters = 1.609;
        
        for (int i = 0; i < size; i++)
        {
            people[i].Greeting(); //this will go through every Person object in the array one at a time which is the time complexity of O(n)
            people[i].calculateBMI();
        }

        cout << "Sorting people by BMI..." << endl;
        
        //Task two: array below is the selection sort being used in ascending BMI
        for (int i = 0; i < size - 1; i++) // with time complexity of O(n^2)
        {
            int index = i;

            for(int k = i + 1; k < size; k++) // Task 2: this will check the remaining elements
            {
                if (people[k].BMI < people[index].BMI)// this will ensure that the index is remember if the smaller BMI is found
                {
                    index = k;
                }
            }
            swap(people[i], people[index]); // Task 2: it will swap Person objects when one is finished in the array
        }   

        cout << "Sorted List: " << endl; //Task 2: this will present the information from the array
        for (int i = 0; i < size; i++)
        {
            
           cout << i + 1 << ". " << people[i].name << " - BMI: " << people[i].BMI
            << endl;
        }

        int choice; // task 3: for this task choice variable was created to store the menu selection
        
        cout << "Welcome to the BMI Program!" << endl;

        do
        {
            cout << endl; // task 3
            cout << "Please select an option:" << endl; //allows users to select options from menu below
            cout << "1. Calculate BMI" << endl; // will calculate the BMI
            cout << "2. Sort people by BMI" << endl; // will use the BMI in a list to be sorted in order
            cout << "3. Compute GCD of two ages using the Euclidean Algorithm" << endl; // will determine the greatest common divisor
            cout << "4. Exit" << endl;
            cout << "Enter your choice: ";
            cin >> choice;

        if (choice == 1)
        {
            cin.ignore();

            Person persons0; // task 3: in this choice, user will enter their name

            cout << endl; // along with getting their height, weight and age and stored in persons object
            cout << "Enter name: ";
            getline(cin, persons0.name);

            cout << "Enter weight (kg): ";
            cin >> persons0.kilograms;

            cout << "Enter height (m): ";
            cin >> persons0.heightMeters;

            cout << "Enter age: ";
            cin >> persons0.age;

            cout << endl;

            persons0.Greeting();
            persons0.calculateBMI();

            people[1] = persons0;
        }
        else if (choice == 2)
        {
            cout << endl;
            cout << "Sorting people by BMI..." << endl;

            for (int i = 0; i < size - 1; i++) // Selection sort is applied again with time complexity - O(n^2) - this would also be the worst case time complexity
            {
                int minIndex = i; 
                for (int j = i + 1; j < size; j++)
                {
                    if (people[j].BMI < people[minIndex].BMI) // task 3: this will sort the BMI of the people in ascending order

                    {
                        minIndex = j;
                    }
                }

                swap(people[i], people[minIndex]);
            }

            cout << "Sorted List:" << endl;

            for (int i = 0; i < size; i++)
            {
                cout << i + 1 << ". " << people[i].name << " - BMI: " << people[i].BMI
                     << endl;
            }
        }
        else if (choice == 3)
        {
            int age1; // declaring two ages for users
            int age2;

            cout << endl;
            cout << "Enter first age: ";
            cin >> age1;

            cout << "Enter second age: ";
            cin >> age2;

            cout << "The GCD of " << age1 << " and "<< age2 << " is "
                 << person0.GCD(age1, age2)
                 << endl;
        }
        else if (choice == 4)
        {
            cout << endl;
            cout << "Exiting program... Goodbye!" << endl;
        }
        else
        {
            cout << endl;
            cout << "Choice is invalid." << endl; // This will show if the person put in a number besides 1-4
        }    
        } while (choice != 4);
        


        
        return 0;
       }