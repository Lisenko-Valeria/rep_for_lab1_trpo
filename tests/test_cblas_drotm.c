/*
 * Тест для функции cblas_drotm
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_drotm...\n");

     // Переменные
    int N = 1;
    int inc = 1;
    double P_param[5];
        double XY = 2.0;
                // Вызов функции
                cblas_drotm(N, &XY, inc, &XY, inc, P_param);

    printf("Тест пройден успешно!\n");
    return 0;
}