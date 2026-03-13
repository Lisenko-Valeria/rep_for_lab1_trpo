#include <iostream>

using namespace std;

//s, d, c, z 
// gemm ( transA, transB, m, n, k, alpha, A, ldA, B, ldB, beta, C, ldC ) 
// C = α*A∗B∗ + βC 

template<typename T>
void gemm(int m, int n, int k, T alpha, T* A, T* B, T beta, T* C, int lda, int ldb, int ldc, char transA, char transB) {

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



int main(){
    //test
    int m=3,n=2,k=1;
    double A[3] = {1,2,3} ;
    double B[2] = {1,2};
    double C[6] = {0,0,0,0,0,0};
    double a=1, b=1;

    gemm(m, n, k, a, A, B, b, C, k, n, n, 'N', 'N');
    
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            cout << C[i*n+j] << " ";
        }
        cout << "\n";
    }
}
