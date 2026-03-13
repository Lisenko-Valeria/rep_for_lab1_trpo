#include <iostream>
#include <complex>

using namespace std;

//s, d, c, z 
// gemm ( transA, transB, m, n, k, alpha, A, ldA, B, ldB, beta, C, ldC ) 
// C = α*A∗B∗ + βC 

template<typename T>
void gemm_(int m, int n, int k, T alpha, T* A, T* B, T beta, T* C, int lda, int ldb, int ldc, char transA, char transB) {

    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            T sum = 0;
            for (int p=0; p<k; p++) {
                T a, b;

                if (transA == 'N') {
                    a = A[i*lda+p];
                } else {
                    a = A[p*lda+i];
                }
                
                
                if (transB == 'N') {
                    b = B[p*ldb+j];
                } else {
                    b = B[j*ldb+p];
                }
                
                sum += a * b;

            }
            C[i*ldc+j] = alpha*sum + beta*C[i*ldc+j];
        }
    }
}

template<typename T>
void gemm_(int m, int n, int k, complex<T> alpha, complex<T>* A, complex<T>* B, complex<T> beta, complex<T>* C, int lda, int ldb, int ldc, char transA, char transB) {
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            complex<T> sum = 0;
            for (int p = 0; p < k; p++) {
                complex<T> a, b;
                
                if (transA == 'N') {
                    a = A[i * lda + p];
                } else if (transA == 'T') {
                    a = A[p * lda + i];
                } else { // 'C' - сопряженное транспонирование
                    a = conj(A[p * lda + i]);
                }
                
                if (transB == 'N') {
                    b = B[p * ldb + j];
                } else if (transB == 'T') {
                    b = B[j * ldb + p];
                } else {
                    b = conj(B[j * ldb + p]);
                }
                
                sum += a * b;
            }
            C[i * ldc + j] = alpha * sum + beta * C[i * ldc + j];
        }
    }
}

template<typename T>
void gemm(int m, int n, int k, T alpha, T* A, T* B, T beta, T* C, int lda, int ldb, int ldc, char transA, char transB) {
    gemm_(m, n, k, alpha, A, B, beta, C, lda, ldb, ldc, transA, transB);
}



int main(){
    //test

        int m = 2, n = 2, k = 2;
        complex<double> A[4] = {{1,1}, {2,2}, {3,3}, {4,4}};
        complex<double> B[4] = {{1,0}, {0,1}, {1,1}, {1,1}};
        complex<double> C[4] = {0, 0, 0, 0};
        complex<double> alpha = {1,0};
        complex<double> beta = {0,0};

        
        gemm(m, n, k, alpha, A, B, beta, C, k, n, m, 'C', 'N');
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cout << C[i * m + j] << " ";
            }
            cout << "\n";
        }

    
}
