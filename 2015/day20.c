#include <stdio.h>
#include <math.h>

int p1(int n) {
    int i, sum = 0, end = sqrt(n);
    for (i = 1; i <= end; i++) {
        if ((n % i) == 0) sum += ((n/i) != i ? i + (n/i) : i);
    }
    return sum * 10;
}

int p2(int n) {
    int i, sum = 0, end = sqrt(n);
    for (i = 1; i <= end; i++) {
        if ((n % i) == 0) sum += ((n/i) <= 50 ? i : 0) +
                                 (i     <= 50 && (n/i) != i ? (n/i) : 0);
    }
    return sum * 11;
}

int search1(int n) {
   int i, lo = n / 45, hi = n / 10;
   for (i = lo; i <= hi; i+=5) if (p1(i) >= n) { hi = i; break; }
   for (i = lo; i <= hi; i++)  if (p1(i) >= n) return i;
   return -1;
}

int search2(int n) {
   int i, lo = n / 43, hi = n / 11;
   for (i = lo; i <= hi; i+=5) if (p2(i) >= n) { hi = i; break; }
   for (i = lo; i <= hi; i++)  if (p2(i) >= n) return i;
   return -1;
}

int main() {
    int presents_target = 33100000;
    printf("2015 day 20 part 1: %d\n", search1(presents_target));
    printf("2015 day 20 part 2: %d\n", search2(presents_target));
}
