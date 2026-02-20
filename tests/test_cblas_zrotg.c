/*
 * Тест для функции cblas_zrotg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_zrotg...\n");

     // Переменные
    double complex a_val = 1.0 + 1.0*I, b_val = 2.0 + 2.0*I;
    double c_val = 0.5;
    double complex s_val = 0.5 + 0.5*I;
                // Вызов функции
                cblas_zrotg(&a_val, &b_val, &c_val, &s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}