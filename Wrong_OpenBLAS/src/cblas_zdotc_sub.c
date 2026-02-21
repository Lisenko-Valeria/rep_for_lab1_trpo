#include <stdio.h>

void cblas_zdotc_sub( int *N, const void *X, const int incX,
                      const void *Y, const int incY, void *dotc)
{
   printf("N value = %d\n", *N);  
}