#include <complex>

using namespace std;

//s, d, c, z 
// gemm ( transA, transB, m, n, k, alpha, A, ldA, B, ldB, beta, C, ldC ) 

template<typename T>
void gemm_(char transA, char transB, int m, int n, int k, T alpha, T* A, int lda, T* B, int ldb, T beta, T* C, int ldc) {

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
void gemm_(char transA, char transB, int m, int n, int k, complex<T> alpha, complex<T>* A, int lda, complex<T>* B, int ldb, complex<T> beta, complex<T>* C, int ldc) {    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            complex<T> sum = 0;
            for (int p = 0; p < k; p++) {
                complex<T> a, b;
                
                if (transA == 'N') {
                    a = A[i * lda + p];
                } else if (transA == 'T') {
                    a = A[p * lda + i];
                } else { 
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
void gemm(char transA, char transB, int m, int n, int k, T alpha, T* A, int lda, T* B, int ldb, T beta, T* C, int ldc) {
    gemm_(transA, transB, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc);
}

