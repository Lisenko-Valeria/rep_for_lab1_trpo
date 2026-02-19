/*
 * Тест для функции cblas_icamax
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_icamax...\n");

    // Один буфер для всех векторов
    #define TEST_BUFFER_SIZE  10
    float complex test_buffer [TEST_BUFFER_SIZE ];
    for (int i = 0; i < TEST_BUFFER_SIZE ; i++) {
        test_buffer [i] = (i+1) + (i+1)*I;
    }
    // Массивы тестовых значений
    int n_values[] = {0, 1,2,3,5};
    int inc_values[] = {1, 2};
    int num_n = 5;
    int num_inc = 2;

    // Перебор всех комбинаций параметров
    for (int i_n = 0; i_n < num_n; i_n++) {
        int n = n_values[i_n];
        for (int i_inc = 0; i_inc < num_inc; i_inc++) {
            int inc = inc_values[i_inc];
                // Вызов функции
                cblas_icamax(n, (const float complex*)test_buffer, inc);
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}