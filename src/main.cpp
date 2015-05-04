
#include "BenchmarkVienna.h"

typedef float ScalarType;

const unsigned MATRIX_SIZE = 400;

int main() {

    BenchmarkVienna<ScalarType> bench;

    bench.run(MATRIX_SIZE);

    return 0;
}