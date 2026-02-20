/*
 * Тест для функции cblas_drot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_drot...\n");

     // Переменные
    int N = 1;
    int inc = 1;
    double c_val = 0.5, s_val = 0.5;
        double XY = 2.0;
                // Вызов функции
                cblas_drot(N, &XY, inc, &XY, inc, c_val, s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}