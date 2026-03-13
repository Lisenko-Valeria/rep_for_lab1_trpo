#include <iostream>
#include <chrono>
#include <vector>
#include <random>
#include <cmath>
#include <cblas.h> 
#include "gemm.cpp"

using namespace std;
using namespace std::chrono;

void fill_random(float* matrix, int size) {
    static random_device rd;
    static mt19937 gen(rd());
    uniform_real_distribution<float> dist(-1.0f, 1.0f);
    for (int i = 0; i < size; i++) matrix[i] = dist(gen);
}

class Timer {
private:
    high_resolution_clock::time_point start_time;
public:
    void start() { start_time = high_resolution_clock::now(); }
    double elapsed_seconds() {
        auto end = high_resolution_clock::now();
        return duration<double>(end - start_time).count();
    }
};

struct TestTimes {
    vector<double> my_times;
    vector<double> blas_times;
};

TestTimes run_test_with_blas(const string& name, int m, int n, int k, int repeat_count) {
    cout << "\n"<< name << " " << m << "x" << n << "x" << k << " (m,n,k):\n";
    
    int lda_my = m, ldb_my = k, ldc_my = m;
    int lda_blas = k, ldb_blas = n, ldc_blas = n;  
    int sizeA = m * k, sizeB = k * n, sizeC = m * n;
    
    vector<float> A(sizeA), B(sizeB), C_my(sizeC, 0), C_blas(sizeC, 0);
    fill_random(A.data(), sizeA);
    fill_random(B.data(), sizeB);
    
    Timer timer;
    TestTimes result;
    
    for (int r = 0; r < repeat_count; r++) {
        fill(C_my.begin(), C_my.end(), 0);
        timer.start();
        gemm('N', 'N', m, n, k, 1.0f, A.data(), lda_my,
             B.data(), ldb_my, 0.0f, C_my.data(), ldc_my);
        result.my_times.push_back(timer.elapsed_seconds());
        
        fill(C_blas.begin(), C_blas.end(), 0);
        timer.start();
        cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
                    m, n, k, 1.0f, A.data(), lda_blas,
                    B.data(), ldb_blas, 0.0f, C_blas.data(), ldc_blas);
        result.blas_times.push_back(timer.elapsed_seconds());
    }
    return result;
}

int main() {
    auto times = run_test_with_blas("Тест", 3000, 3000, 3000, 10);
    
    cout << "\nРезультаты (mine    | BLAS):\n";
    double total_my = 0, total_blas = 0;
    for (size_t i = 0; i < times.my_times.size(); i++) {
        printf("  Run %zu: %.4f сек | %.4f сек\n", 
               i+1, times.my_times[i], times.blas_times[i]);
        total_my += times.my_times[i];
        total_blas += times.blas_times[i];
    }
    printf("\nСреднее время:\n");
    printf("  Моя реализация: %.4f сек\n", total_my / times.my_times.size());
    printf("  OpenBLAS: %.4f сек\n", total_blas / times.blas_times.size());
    printf("  Отношение (BLAS/моя): %.2f\n", 
           (total_blas / times.blas_times.size()) / (total_my / times.my_times.size()));
    
    return 0;
}