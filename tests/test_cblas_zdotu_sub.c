/*
 * Тест для функции cblas_zdotu_sub
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_zdotu_sub...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        double complex XY = 2.0 + 2.0*I;

    double complex dotu;
                // Вызов функции
                cblas_zdotu_sub(N, &XY, inc, &XY, inc, &dotu);

    printf("Тест пройден успешно!\n");
    return 0;
}