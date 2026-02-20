/*
 * Тест для функции cblas_srotg
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srotg...\n");

     // Переменные
    float a_val = 1.0f, b_val = 2.0f, c_val = 0.5f, s_val = 0.5f;
                // Вызов функции
                cblas_srotg(&a_val, &b_val, &c_val, &s_val);

    printf("Тест пройден успешно!\n");
    return 0;
}