/*
 * Тест для функции cblas_srot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srot...\n");

    float a_val = 1.0f, b_val = 2.0f, c_val = 0.5f, s_val = 0.5f;
    float d1_val = 1.0f, d2_val = 2.0f, b1_val = 3.0f, P_param[5] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
    // Один буфер для всех векторов
    #define TEST_BUFFER_SIZE  10
    float test_buffer [TEST_BUFFER_SIZE ];
    for (int i = 0; i < TEST_BUFFER_SIZE ; i++) {
        test_buffer [i] = (float)(i + 1);
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
                cblas_srot(n, test_buffer, inc, test_buffer, inc, c_val, s_val);
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}