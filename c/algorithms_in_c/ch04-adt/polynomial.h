#ifndef POLYNOMIAL_H_INCLUDED
#define POLYNOMIAL_H_INCLUDED

typedef struct
{
    int N;
    float *a;
} *Poly;

void poly_show(Poly p);
Poly poly_term(float coeff, int exp);
Poly poly_add(Poly p, Poly q);
Poly poly_mult(Poly p, Poly q);
float poly_eval(Poly p, float val);
void poly_del(Poly p);

#endif // POLYNOMIAL_H_INCLUDED
