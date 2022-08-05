// link : https://www.hackerrank.com/challenges/c-tutorial-functions/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d);


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int a, int b, int c, int d)
{
    int max; 
    max = a > b ? a : b;
    max = c > max ? c : max;
    max = d > max ? d : max;
    
    return max;
}

//------------------------------------------------------------------------------------------

// If you're going to use std::max() then it would look like
int max_of_four(int a, int b, int c, int d)
{
    return std::max(a, max(b, max(c, d)));
}

