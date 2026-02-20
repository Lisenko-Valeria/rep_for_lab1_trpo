/*
 * Тест для функции cblas_csscal
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_csscal...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float complex alpha = 2.0f;
        float complex XY = 2.0f + 2.0f*I;
                // Вызов функции
                cblas_csscal(N, alpha, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}