
#include "BenchmarkVienna.h"

#include "FileReader.h"
#include "CostFunction.h"

typedef float ScalarType;

const unsigned MATRIX_SIZE = 400;

int main() {

//    BenchmarkVienna<ScalarType> bench;
//    bench.run(MATRIX_SIZE);

    viennacl::matrix<ScalarType> X = FileReader::X<ScalarType>(std::string(""));
    viennacl::vector<ScalarType> y = FileReader::y<ScalarType>(std::string(""));
    viennacl::vector<ScalarType> theta(y.size());

    CostFunction<ScalarType> cost_function(X, y, theta);

    std::cout << "Cost: " << cost_function();

    return 0;
}
