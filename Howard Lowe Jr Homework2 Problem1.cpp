#include <iostream>
#include <string>

using namespace std;

// this is the Selection Sort function being done
void SelectionSort(string hashtags[], int frequencies[], int n)
{
    // frquencies would store the frequencies
    //hashtags[] stores then names for the hashtags
    //n will represent the number of hashtags
    for (int i = 0; i < n - 1; i++) // 
    // using n - 1 is equivalent to n - 2 as n - 2 is in thenn -1 in this code
    {
        int maxIndex = i; // will determine that the current element is the largest

        for (int j = i + 1; j < n; j++) // 
        // with each loop both outer and inner, they would use time complexity
        //  O(n); therefore the overall program complexity is O(n^2)
        {
            if (frequencies[j] > frequencies[maxIndex])
            {
                maxIndex = j;
            }
        }

        // Swapping the frequencies
        int tempfreq = frequencies[i];

        frequencies[i] = frequencies[maxIndex];

        frequencies[maxIndex] = tempfreq;

        //swapping the hashtags i and hashtags maxIndex
        string temphash = hashtags[i];
        hashtags[i] = hashtags[maxIndex]; // 
        // will move the hashtag with the highest frequency

        hashtags[maxIndex] = temphash;
    }
}






int main()
{
    int n;

    cout << " Please enter the number of hashtags to analyze: ";
    cin >> n;

    int frequencies[n];

    string hashtags[n];

    

    // this will accept the hashtag-frequency pairs as inputs below:
    for (int i = 0; i < n; i++)
    { // repeating once for every hashtag
        cout << "\nEnter hashtag #" << i + 1 << ": ";
        cin >> hashtags[i];

        cout << "Enter the frequency for " << hashtags[i] << ": ";
        cin >> frequencies[i];
    }

    // this will display the Unsorted list of hashtags

    cout << "\n Unsorted Hashtag List " << endl;
    for (int i = 0; i < n; i++)
    {
        cout <<  hashtags[i]  << " : " << frequencies[i] << endl;
    }

    // Slection sort will play the part in sorting n - the hashtags
    SelectionSort(hashtags, frequencies, n);

    // Displaying the  sorted list with the highest frequency 
    cout << "\n  Sorted Hashtag List  " << endl;
    for (int i = 0; i < n; i++)
    {
        cout <<  hashtags[i] << " : " << frequencies[i] << endl;
    }

    return 0;
}