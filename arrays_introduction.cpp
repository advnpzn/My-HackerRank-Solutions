// link : https://www.hackerrank.com/challenges/arrays-introduction/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    int nums[n]; 
    for (int i = 0; i <= n; i++) {
        cin >> nums[i];
    }
    for (int i = n - 1; i >= 0; i--) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
