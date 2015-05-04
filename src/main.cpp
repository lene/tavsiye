
#include "BenchmarkVienna.h"

#include "FileReader.h"
#include "CostFunction.h"

typedef float ScalarType;

int main() {

    viennacl::matrix<ScalarType> X = FileReader::X<ScalarType>(std::string(""));
    viennacl::vector<ScalarType> y = FileReader::y<ScalarType>(std::string(""));
    viennacl::vector<ScalarType> theta(y.size());

    CostFunction<ScalarType> cost_function(X, y);

    ScalarType cost = cost_function(theta);

    std::cout << "Cost: " << cost;

    return 0;
}
