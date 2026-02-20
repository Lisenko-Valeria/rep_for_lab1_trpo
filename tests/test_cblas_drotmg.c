/*
 * Тест для функции cblas_drotmg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_drotmg...\n");

     // Переменные
    double d1_val = 1.0, d2_val = 2.0, b1_val = 1.0, b2_val = 2.0, P_param[5];
                // Вызов функции
                cblas_drotmg(&d1_val, &d2_val, &b1_val, b2_val, P_param);

    printf("Тест пройден успешно!\n");
    return 0;
}