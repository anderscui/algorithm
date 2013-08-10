#ifndef FCCOMPLEX_H_INCLUDED
#define FCCOMPLEX_H_INCLUDED

typedef struct complex
{
    float re;
    float im;
} *Complex;

Complex comp_new(float, float);
float comp_re(Complex);
float comp_im(Complex);
Complex comp_mult(Complex, Complex);

#endif // FCCOMPLEX_H_INCLUDED
