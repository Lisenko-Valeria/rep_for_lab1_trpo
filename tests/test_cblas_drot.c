/*
 * Тест для функции cblas_drot
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_drot...\n");

    double a_val = 1.0, b_val = 2.0, c_val = 0.5, s_val = 0.5;
    double d1_val = 1.0, d2_val = 2.0, b1_val = 3.0, P_param[5] = {1.0, 2.0, 3.0, 4.0, 5.0};
    // Создание тестовых векторов
    double x_data[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
    double y_data[] = {10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    double *x = x_data;
    double *y = y_data;
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
                cblas_drot(n, x_data, inc, y_data, inc, c_val, s_val);
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}