/*
 * Тест для функции cblas_scnrm2
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_scnrm2...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float complex XY = 2.0f + 2.0f*I;
                // Вызов функции
                cblas_scnrm2(N, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}