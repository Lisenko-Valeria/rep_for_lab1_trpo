#include <iostream>

using namespace std;

//s, d, c, z 
// gemm ( transA, transB, m, n, k, alpha, A, ldA, B, ldB, beta, C, ldC ) 
// C = α*A∗B∗ + βC 

void gemm(int m, int n, int k, float alpha, float* A, float* B, float beta, float* C, int lda, int ldb, int ldc) {
    // C = alpha*A*B + beta*C
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            float sum = 0;
            for (int p=0; p<k; p++) {
                sum += A[i*lda+p] * B[p*ldb+j];
            }
            C[i*ldc+j] = alpha*sum + beta*C[i*ldc+j];
        }
    }
}

int main(){
    //test
    int m=3,n=2,k=1;
    float A[3] = {1,2,3} ;
    float B[2] = {1,2};
    float C[6] = {0,0,0,0,0,0};
    float a=1, b=1;

    gemm(m, n, k, a, A, B, b, C, k, n, n);
    
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            cout << C[i*n+j] << " ";
        }
        cout << "\n";
    }
}
