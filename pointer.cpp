// link : https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

#include <stdio.h>

void update(int *a,int *b) {
    int temp = *a;
    *a = *a + *b;
    *b = temp - *b;
    *b = *b * ((*b > 0) - (*b < 0));
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
