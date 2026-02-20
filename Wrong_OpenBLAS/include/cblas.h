// Wrong_OpenBLAS/include/cblas.h
#ifndef CBLAS_H
#define CBLAS_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Тип для индексов (как в оригинале) */
typedef int CBLAS_INDEX;

// правильные прототипы соответствующие тестам 
/* Прототипы только для 5 функций, которые мы будем "портить" */
void cblas_saxpy(int *N, const float alpha, const float *X, const int incX, float *Y, const int incY);
void cblas_dswap(double *X, int N, const int incX, double *Y, const int incY);
float cblas_sdot(int N, const float *X, int incX, const float *Y, int incY, float *extra_var);
void cblas_drot(double *X, const int N, int incX, double *Y, int incY, double c, double s);
void cblas_zdotc_sub(int *N, const void *X, int incX, const void *Y, int incY, void *dotc); 

#ifdef __cplusplus
}
#endif

#endif