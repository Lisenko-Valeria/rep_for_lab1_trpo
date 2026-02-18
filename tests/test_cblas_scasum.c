/*
 * Тест для функции cblas_scasum
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {
    printf("Тестирование cblas_scasum...\n");

    // Создание тестовых векторов (комплексные)
    float complex x_data[] = {1.0f+1.0f*I, 2.0f+2.0f*I, 
                             3.0f+3.0f*I, 4.0f+4.0f*I,
                             5.0f+5.0f*I, 6.0f+6.0f*I,
                             7.0f+7.0f*I, 8.0f+8.0f*I,
                             9.0f+9.0f*I, 10.0f+10.0f*I};
    float complex y_data[] = {10.0f+10.0f*I, 9.0f+9.0f*I,
                             8.0f+8.0f*I, 7.0f+7.0f*I,
                             6.0f+6.0f*I, 5.0f+5.0f*I,
                             4.0f+4.0f*I, 3.0f+3.0f*I,
                             2.0f+2.0f*I, 1.0f+1.0f*I};
    float complex *x = x_data;
    float complex *y = y_data;
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
                cblas_scasum(n, (const float complex*)x_data, inc);
        }
    }

    printf("Тест пройден успешно!\n");
    return 0;
}