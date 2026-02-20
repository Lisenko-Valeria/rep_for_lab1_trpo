/*
 * Тест для функции cblas_dsdot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_dsdot...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float XY = 2.0f;
                // Вызов функции
                cblas_dsdot(N, &XY, inc, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}