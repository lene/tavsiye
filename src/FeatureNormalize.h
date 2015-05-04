//
// Created by lene on 04.05.15.
//

#ifndef TAVSIYE_FEATURENORMALIZE_H
#define TAVSIYE_FEATURENORMALIZE_H

#include <viennacl/vector.hpp>
#include <viennacl/matrix.hpp>

template <typename ScalarType>
class FeatureNormalize {
public:
    FeatureNormalize(const viennacl::matrix<ScalarType> &X):
            original_matrix_(X), normalized_matrix_(X.size1(), X.size2()), mu_(X.size1()), sigma_(X.size2()) {}

    const viennacl::matrix<ScalarType, viennacl::row_major, 1> &getNormalizedMatrix() {
        return normalized_matrix_;
    }

private:
    const viennacl::matrix<ScalarType> &original_matrix_;
    viennacl::matrix<ScalarType> normalized_matrix_;
    viennacl::vector<ScalarType> mu_;
    viennacl::vector<ScalarType> sigma_;
};


#endif //TAVSIYE_FEATURENORMALIZE_H
