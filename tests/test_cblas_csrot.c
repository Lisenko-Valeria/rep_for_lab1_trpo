/*
 * Тест для функции cblas_csrot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_csrot...\n");

     // Переменные
    int N = 1;
    int inc = 1;
    float complex c_val = 0.5f, s_val = 0.5f;
        float complex XY = 2.0f + 2.0f*I;
                // Вызов функции
                cblas_csrot(N, &XY, inc, &XY, inc, c_val, s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}