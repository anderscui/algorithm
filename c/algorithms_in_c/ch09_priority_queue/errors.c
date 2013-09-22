#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int errno;

//int main(int argc, char *argv[])
//{
//    FILE *pf;
//    int errnum;
//    pf = fopen("not_existing.txt", "rb");
//    if (pf == NULL)
//    {
//        errnum = errno;
//        fprintf(stderr, "Value of errno: %d \n", errno);
//        perror("Error printed by perror");
//        fprintf(stderr, "Error opening file: %s \n", strerror(errnum));
//    }
//    else
//    {
//        fclose(pf);
//    }
//
//    return 0;
//}

int main(int argc, char *argv[])
{
    int dividend = 20;
    int divisor = 0;
    int quotient;

    if (divisor == 0)
    {
        fprintf(stderr, "Division by zero! Exiting... \n");
        exit(EXIT_FAILURE);
    }
    quotient = dividend / divisor;
    fprintf(stderr, "Value of quotient : %d \n", quotient);

    exit(EXIT_SUCCESS);
}
