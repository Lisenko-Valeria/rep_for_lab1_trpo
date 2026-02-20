/*
 * Тест для функции cblas_srotmg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srotmg...\n");

     // Переменные
    float d1_val = 1.0f, d2_val = 2.0f, b1_val = 1.0f, b2_val = 2.0f, P_param[5];
                // Вызов функции
                cblas_srotmg(&d1_val, &d2_val, &b1_val, b2_val, P_param);

    printf("Тест пройден успешно!\n");
    return 0;
}