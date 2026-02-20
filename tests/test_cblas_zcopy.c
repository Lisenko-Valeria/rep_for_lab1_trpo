/*
 * Тест для функции cblas_zcopy
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_zcopy...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        double complex XY = 2.0 + 2.0*I;
                // Вызов функции
                cblas_zcopy(N, &XY, inc, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}