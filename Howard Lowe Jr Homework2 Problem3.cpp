
//Problem 3
#include <iostream>
#include <map> // allowing the use of maps
#include <vector>
#include <string>


using namespace std;

int main()
{
    // declarations
    int n;
    string date;
    double surge;

    // map will store each date along with its price surges
    map<string, vector<double>> DailySurges; // using both string and double vector for DailySurges



    cout << " Please enter the number of records: ";
    cin >> n;

    // recording the information from the user
    for (int i = 0; i < n; i++)
    {
        cout << "\n Enter the date (YYYY-MM-DD): ";
        cin >> date;

        cout << "Enter price surge: ";
        cin >> surge;

        DailySurges[date].push_back(surge); // 
        // will add surge to vector that belongs to its date
    }

    cout << "\n++ Top Two Surges For Each Date +" << endl;

    //   Looping through every date in the map
    for (pair<string, vector<double>> day : DailySurges)
    {   //getting the current date
        string currentdate = day.first;

        //this will get the surges for the current date
        vector<double> A = day.second;

        // initializing the largest   using the first surge
        double large_1 = A[0];

        double large_2 = A[0];

        // so if there is more than one surge,  determine which large is larger
        if (A.size() > 1)
        {
            if (A[1] > A[0]) // will help determine that large_1 is larger
            {
                large_1 = A[1];
                large_2 = A[0];
            }
            else
            {                //will help determine that large_2 is larger than 1
                large_1 = A[0];
                large_2 = A[1];
            }

            // Check the remaining surges; Time complexity used was the O(n)
            for (int i = 2; i < A.size(); i++) // surge is processed exactly once therefore the total work is O(n)
            {
                if (A[i] > large_1) // if  largest surge is found
                {
                    large_2 = large_1;
                    large_1 = A[i];
                }
                else if (A[i] > large_2) // if second surge that is largest is found
                {
                    large_2 = A[i];
                }
            }
        }
        
        // Displaying the results:
        cout << "Date: " << currentdate << "  The largest surges are: ";

        if (A.size() == 1)
        {
            cout << large_1 << " (Only one surge got recorded!)";
        }
        else
        {
            cout << large_1 << ", " << large_2;
        }

        cout << endl;
    }

    return 0; // The overall time complexity used was O(n) as every stock price surge is only examined once after being grouped by date
}