/*
 * Тест для функции cblas_sscal
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_sscal...\n");

     // Переменные
    int N = 1;
    int inc = 1;
        float alpha = 2.0f;
        float XY = 2.0f;
                // Вызов функции
                cblas_sscal(N, alpha, &XY, inc);

    printf("Тест пройден успешно!\n");
    return 0;
}