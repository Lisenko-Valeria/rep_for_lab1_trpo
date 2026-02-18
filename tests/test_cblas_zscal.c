/*
 * Тест для функции cblas_zscal
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_zscal...\n");

    // Создание тестовых векторов (комплексные)
    double complex x_data[] = {1.0+1.0*I, 2.0+2.0*I, 
                             3.0+3.0*I, 4.0+4.0*I,
                             5.0+5.0*I, 6.0+6.0*I,
                             7.0+7.0*I, 8.0+8.0*I,
                             9.0+9.0*I, 10.0+10.0*I};
    double complex y_data[] = {10.0+10.0*I, 9.0+9.0*I,
                             8.0+8.0*I, 7.0+7.0*I,
                             6.0+6.0*I, 5.0+5.0*I,
                             4.0+4.0*I, 3.0+3.0*I,
                             2.0+2.0*I, 1.0+1.0*I};
    double complex *x = x_data;
    double complex *y = y_data;
    // Массивы тестовых значений
    double alpha_values[] = {0.0, 1.0, -2.5, 0.5, 3.0};
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
                double alpha = alpha_values[i_alpha];
                // Вызов функции
                cblas_zscal(n, &alpha, x_data, inc);
            }
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}