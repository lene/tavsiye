//
// Created by lene on 04.05.15.
//

#ifndef TAVSIYE_FEATURENORMALIZE_H
#define TAVSIYE_FEATURENORMALIZE_H

#include <viennacl/vector.hpp>
#include <viennacl/matrix.hpp>
#include <viennacl/linalg/inner_prod.hpp>

template <typename ScalarType>
class FeatureNormalize {
public:
    FeatureNormalize(const viennacl::matrix<ScalarType> &X):
            original_matrix_(X), normalized_matrix_(X.size1(), X.size2()), mu_(X.size1()), sigma_(X.size2()) {
        runNormalization();
    }

    const viennacl::matrix<ScalarType> &normalize() {
        return normalized_matrix_;
    }

    viennacl::matrix<ScalarType> restore(const viennacl::matrix<ScalarType> &matrix);

private:

    viennacl::scalar<ScalarType> sum(const viennacl::vector<ScalarType> &v) {
        viennacl::vector<ScalarType> ones = viennacl::scalar_vector<ScalarType>(v.size(), 1.0);
        return viennacl::linalg::inner_prod(v, ones);
    }

    viennacl::scalar<ScalarType> mean(const viennacl::vector<ScalarType> &v) {
        return sum(v) / v.size();
    }

    viennacl::scalar<ScalarType> variance(const viennacl::vector<ScalarType> &v) {
        viennacl::vector<ScalarType> mean = viennacl::scalar_vector<ScalarType>(v.size(), mean(v));
        viennacl::vector<ScalarType> difference = v - mean;

    }

    viennacl::scalar<ScalarType> stddev(const viennacl::vector<ScalarType> &v) {
        return sqrt(variance(v));
    }
    void runNormalization() {
        unsigned long len = original_matrix_.size2();
        for (unsigned long i = 0; i < len; ++i) {
            viennacl::vector<ScalarType> column = viennacl::column(original_matrix_, i);
            mu_(i) = mean(column);
            viennacl::vector<ScalarType> normalized_column = viennacl::column(normalized_matrix_, i);
            normalized_column -= viennacl::scalar_vector<ScalarType>(normalized_column.size(), 1.0) * mu_(i);
            sigma_(i) = stddev(normalized_column);
            normalized_column /= sigma_(i);
        }

    }

    const viennacl::matrix<ScalarType> &original_matrix_;
    viennacl::matrix<ScalarType> normalized_matrix_;
    viennacl::vector<ScalarType> mu_;
    viennacl::vector<ScalarType> sigma_;
};


#endif //TAVSIYE_FEATURENORMALIZE_H
