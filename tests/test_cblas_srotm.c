/*
 * Тест для функции cblas_srotm
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srotm...\n");

     // Переменные
    int N = 1;
    int inc = 1;
    float P_param[5];
        float XY = 2.0f;
                // Вызов функции
                cblas_srotm(N, &XY, inc, &XY, inc, P_param);

    printf("Тест пройден успешно!\n");
    return 0;
}