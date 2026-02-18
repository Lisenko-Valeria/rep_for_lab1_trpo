/*
 * Тест для функции cblas_srotm
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_srotm...\n");

    float a_val = 1.0f, b_val = 2.0f, c_val = 0.5f, s_val = 0.5f;
    float d1_val = 1.0f, d2_val = 2.0f, b1_val = 3.0f, P_param[5] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
    // Создание тестовых векторов
    float x_data[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
    float y_data[] = {10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    float *x = x_data;
    float *y = y_data;
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
                cblas_srotm(n, x_data, inc, y_data, inc, P_param);
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}