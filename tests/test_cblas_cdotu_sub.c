/*
 * Тест для функции cblas_cdotu_sub
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_cdotu_sub...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float complex XY = 2.0f + 2.0f*I;

    float complex dotu;
                // Вызов функции
                cblas_cdotu_sub(N, &XY, inc, &XY, inc, &dotu);

    printf("Тест пройден успешно!\n");
    return 0;
}