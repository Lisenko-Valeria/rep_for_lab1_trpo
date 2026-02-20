#include "/home/valeria/sem4/Trpo/rep_for_lab1_trpo/Wrong_OpenBLAS/include/cblas.h"
#include <stdio.h>

void cblas_zdotc_sub( int *N, const void *X, const int incX,
                      const void *Y, const int incY, void *dotc)
{
   printf("N value = %d\n", *N);  
}