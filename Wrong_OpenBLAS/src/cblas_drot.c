#include <stdio.h>

void cblas_drot(double *X, const int N, const int incX,
   double *Y, const int incY, const double c, const double s)
{
   printf("N value = %f\n", *X);  
}