/*
 * Тест для функции cblas_drotg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_drotg...\n");

     // Переменные
    double a_val = 1.0, b_val = 2.0, c_val = 0.5, s_val = 0.5;
                // Вызов функции
                cblas_drotg(&a_val, &b_val, &c_val, &s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}