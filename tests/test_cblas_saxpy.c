/*
 * Тест для функции cblas_saxpy
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_saxpy...\n");

    // Создание тестовых векторов
    float x_data[] = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
    float y_data[] = {10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0};
    float *x = x_data;
    float *y = y_data;
    // Массивы тестовых значений
    float alpha_values[] = {0.0f, 1.0f, -2.5f, 0.5f, 3.0f};
    int num_alphas = 5;
    int n_values[] = {0, 5, 3, 1, 7};
    int inc_values[] = {1, 2, -1, 0};
    int num_n = 5;
    int num_inc = 4;

    // Перебор всех комбинаций параметров
    for (int i_n = 0; i_n < num_n; i_n++) {
        int n = n_values[i_n];
        for (int i_inc = 0; i_inc < num_inc; i_inc++) {
            int inc = inc_values[i_inc];
            for (int i_alpha = 0; i_alpha < num_alphas; i_alpha++) {
                float alpha = alpha_values[i_alpha];
                // Вызов функции
                cblas_saxpy(n, alpha, (const float*)x_data, inc, y_data, inc);
            }
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}