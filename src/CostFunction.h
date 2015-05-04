//
// Created by lene on 04.05.15.
//

#ifndef TAVSIYE_COSTFUNCTION_H
#define TAVSIYE_COSTFUNCTION_H


#include <viennacl/vector.hpp>

template<typename ScalarType>
class CostFunction {

public:
    /**
     *  X: features
     *  y: training examples (y_i = f(X_i)
     *  theta: hypothesis parameters
     */
    CostFunction(
            const viennacl::matrix<ScalarType> &X,
            const viennacl::vector<ScalarType> &y
    );

    viennacl::scalar<ScalarType> operator()(const viennacl::vector<ScalarType> &theta);

private:
    const viennacl::matrix<ScalarType> &_X;
    const viennacl::vector<ScalarType> &_y;
};

#include "CostFunction.impl.h"

#endif //TAVSIYE_COSTFUNCTION_H
