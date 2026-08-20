// Problem 2
#include <iostream>
#include <vector>

using namespace std;

// Convert exponent to binary
vector<int> BinaryExponent(int e)
{
    vector<int> K;

    int tmp = e;
    int i = 0;

    while (tmp > 0) // time complexity being performed O(Log e) as exponent is being converted to binary
    {
        
        // this while loop will keep repeating unti the tmp becomes zero
        K.push_back(tmp % 2); // this will store last bit as it will add the last binary digit to the vector i.e the remainder
        
        tmp = (tmp - K[i]) / 2; // performing calculation; removing last binary digit then dividing by 2

        i++;

    }

    return K;
}

// this is the function that will compute M^emodN
int ModularExponentiation(int M, vector<int> K, int N)
{
    if (N == 1) // ensuring that  N = 1
        return 0;

    int result = 1;

    if (K.empty() == 0) // making sure if the exponent has any binary digits
        return result;

    int A = M % N;

    if (K[0] == 1)
        result = M % N; //so if first binary bit = 1, it will initialize result with base

    for (int i = 1; i <  K.empty();  i++) // loops through the remaining bases
                                    // O(Log e) is performed again in this square-and-multiply algorithm
    // square the base
    {
        A = (A * A) % N; // A will store the modulo base

        if (K[i] == 1)
        {
            result = (A * result) % N; // this will update the answer
        }
    }

    return result;
}

int main()
{
    int M, N;
    int exponent;

    cout << "Enter the base (M): ";
    cin >> M;

    cout << "Enter the exponent (e or d): ";
    cin >> exponent;

    cout << "Enter the modulus (N): ";
    cin >> N;

    vector<int> K = BinaryExponent(exponent);

    cout << "\nBinary representation of exponent (LSB -> MSB): ";

    for (int bit : K)
    {
        cout << bit;
    }

    cout << endl;
    //this will be computing the M^emodN using the Square-and-Multiply method 
    int result = ModularExponentiation (M, K, N);

    cout << "\nResult: " << result << endl;

    return 0;
}
