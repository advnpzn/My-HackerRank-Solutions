// link : https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

std::string int_to_str(int num);
std::string even_odd(int num);

int main() {
    int a, b;
    cin >> a >> b;
    
    
    if (b <= 9)
    {
        for (int i = a; i <= b; i++)
        {
            cout << int_to_str(i) << "\n";
        }
    }
    else 
    {
        for (int i = a; i <= 9; i++)
        {
            cout << int_to_str(i) << "\n";
        }
        for (int i = 10; i <= b; i++)
        {
            cout << even_odd(i) << "\n";
        }
    }
    
    return 0;
}

std::string int_to_str(int num)
{
    switch (num) {
    case 1:
        return "one";
        break;
    case 2:
        return "two";
        break;
    case 3:
        return "three";
        break;
    case 4:
        return "four";
        break;
    case 5:
        return "five";
        break;
    case 6:
        return "six";
        break;
    case 7:
        return "seven";
        break;
    case 8:
        return "eight";
        break;
    default:
        return "nine";
        break;
    }
    
}

std::string even_odd(int num){
    if (num % 2 == 0)
        return "even";
    else
        return "odd";
}
