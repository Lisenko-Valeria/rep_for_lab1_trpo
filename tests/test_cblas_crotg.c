/*
 * Тест для функции cblas_crotg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_crotg...\n");

     // Переменные
    float complex a_val = 1.0f + 1.0f*I, b_val = 2.0f + 2.0f*I;
    float c_val = 0.5f;
    float complex s_val = 0.5f + 0.5f*I;
                // Вызов функции
                cblas_crotg(&a_val, &b_val, &c_val, &s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}