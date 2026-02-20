/*
 * Тест для функции cblas_srot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srot...\n");

     // Переменные
    int N = 1;
    int inc = 1;
    float c_val = 0.5f, s_val = 0.5f;
        float XY = 2.0f;
                // Вызов функции
                cblas_srot(N, &XY, inc, &XY, inc, c_val, s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}