#ifndef COMPLEX_H_INCLUDED
#define COMPLEX_H_INCLUDED

typedef struct
{
    float re;
    float im;
} Complex;

Complex comp_new(float, float);
float comp_re(Complex);
float comp_im(Complex);
Complex comp_mult(Complex, Complex);

#endif // COMPLEX_H_INCLUDED
