//
// Created by lene on 04.05.15.
//

#include "CostFunction.h"

#include "viennacl/linalg/inner_prod.hpp"

template <typename ScalarType>
CostFunction<ScalarType>::CostFunction(
        const viennacl::matrix<ScalarType> &X,
        const viennacl::vector<ScalarType> &y): _X(X), _y(y) { }


/**
function J = computeCostMulti(X, y, theta)
  m = length(y); % number of training examples
  h_theta = X*theta;
  summand_linear = h_theta-y;
  summand_squared = summand_linear .^ 2;
  J = sum(summand_squared)/2/m;
 */
template <typename ScalarType>
viennacl::scalar<ScalarType> CostFunction<ScalarType>::operator()(const viennacl::vector<ScalarType> &theta) {
    viennacl::vector<ScalarType> h_theta = viennacl::linalg::prod(_X, theta);
    viennacl::vector<ScalarType> deviation = h_theta-_y;
    return viennacl::linalg::inner_prod(deviation, deviation);
}
