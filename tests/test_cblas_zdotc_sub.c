/*
 * Тест для функции cblas_zdotc_sub
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_zdotc_sub...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        double complex XY = 2.0 + 2.0*I;

    double complex dotc;
                // Вызов функции
                cblas_zdotc_sub(N, &XY, inc, &XY, inc, &dotc);

    printf("Тест пройден успешно!\n");
    return 0;
}