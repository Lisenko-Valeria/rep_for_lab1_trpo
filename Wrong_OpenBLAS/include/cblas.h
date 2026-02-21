
#ifndef CBLAS_H //защита от мн вкл
#define CBLAS_H



#ifdef __cplusplus
extern "C" { //с стиль именования
#endif



// правильные прототипы соответствующие тестам 
void cblas_saxpy(int N, const float alpha, const float *X, const int incX, float *Y, const int incY);
void cblas_dswap(int N, double *X, const int incX, double *Y, const int incY);
float cblas_sdot(int N, const float *X, int incX, const float *Y, int incY);
void cblas_drot(const int N, double *X, int incX, double *Y, int incY, double c, double s);
void cblas_zdotc_sub(int N, const void *X, int incX, const void *Y, int incY, void *dotc); 

#ifdef __cplusplus
}
#endif

#endif