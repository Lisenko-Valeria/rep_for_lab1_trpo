#for lab6
CXX = g++
CXXFLAGS = -O3 -march=native -mtune=native -Wall -std=c++17 -I./OpenBLAS -I./OpenBLAS/lapack-netlib/CBLAS/include
LDFLAGS = -L./OpenBLAS -lopenblas -lpthread

TARGET = test_gemm
SOURCES = test_gemm.cpp

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $@ $< $(LDFLAGS)

run: $(TARGET)
	LD_LIBRARY_PATH=./OpenBLAS:$$LD_LIBRARY_PATH ./$(TARGET)

clean:
	rm -f $(TARGET)

