/*
 * Тест для функции cblas_ddot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_ddot...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        double XY = 2.0;
                // Вызов функции
                cblas_ddot(N, &XY, inc, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}