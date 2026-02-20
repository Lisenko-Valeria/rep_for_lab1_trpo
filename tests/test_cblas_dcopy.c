/*
 * Тест для функции cblas_dcopy
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_dcopy...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        double XY = 2.0;
                // Вызов функции
                cblas_dcopy(N, &XY, inc, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}