#ifndef CMN_LIB_H_INCLUDED
#define CMN_LIB_H_INCLUDED

#define MAX(A, B) (A > B) ? A : B

void nl();

int rand_int();
int rand_int_less_than(int less_than);
float rand_float();

void show_array(int a[], int n);

#endif // CMN_LIB_H_INCLUDED
