#include <stdio.h>
#include <stdlib.h>

#include "polynomial.h"

void poly_show(Poly p)
{
    int i;
    for (i = p->N - 1; i >= 0; i--)
    {
        if(p->a[i] != 0)
        {
            printf("(%f, x^%d) ", p->a[i], i);
        }
    }
    printf("\n");
}

Poly poly_term(float coeff, int exp)
{
    Poly t = malloc(sizeof *t);
    t->a = malloc((exp + 1) * sizeof(int));
    t->N = exp + 1;
    t->a[exp] = coeff;

    int i;
    for (i = 0; i < exp; i++)
    {
        t->a[i] = 0;
    }
    return t;
}

Poly poly_add(Poly p, Poly q)
{
    Poly t;
    if(p->N < q->N)
    {
        t = p;
        p = q;
        q = t;
    }
    int i;
    for (i = 0; i < q->N; i++)
    {
        p->a[i] += q->a[i];
    }
    return p;
}

Poly poly_mult(Poly p, Poly q)
{
    Poly t = poly_term(0, (p->N - 1) + (q->N - 1));
    int i, j;
    for (i = 0; i < p->N; i++)
    {
        for (j = 0; j < q->N; j++)
        {
            t->a[i+j] += p->a[i] * q->a[j];
        }
    }
    return t;
}

// use Horner's rule
// refer to: http://en.wikipedia.org/wiki/Horner%27s_method
float poly_eval(Poly p, float val)
{
    int i;
    double t = 0.0;
    for (i = p->N-1; i >= 0; i--)
    {
        t = t * val + p->a[i];
    }
    return t;
}

void poly_del(Poly p)
{
    if (p != NULL)
    {
        free(p);
    }
}

