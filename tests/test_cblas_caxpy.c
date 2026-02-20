/*
 * Тест для функции cblas_caxpy
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_caxpy...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float complex alpha = 2.0f + 2.0f*I;
        float complex XY = 2.0f + 2.0f*I;
                // Вызов функции
                cblas_caxpy(N, &alpha, &XY, inc, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}