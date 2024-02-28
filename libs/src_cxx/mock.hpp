/*
 * Copyright (c) 2024 MPI-M, Clara Bayley
 * 
 * ----- GoodSciProjTemplate -----
 * File: mock.hpp
 * Project: src_cxx
 * Created Date: Tuesday 27th February 2024
 * Author: Clara Bayley (CB)
 * Additional Contributors:
 * -----
 * Last Modified: Wednesday 28th February 2024
 * Modified By: CB
 * -----
 * License: BSD 3-Clause "New" or "Revised" License
 * https://opensource.org/licenses/BSD-3-Clause
 * -----
 * File Description:
 * source file for mock c++ header library
 */


#ifndef LIBS_SRC_CXX_MOCK_HPP_
#define LIBS_SRC_CXX_MOCK_HPP_

#include <numbers>
#include <pybind11/pybind11.h>

/**
 * \brief Calculates the area of a circle given its radius.
 *
 * This function calculates the area of a circle using the formula:
 * \f$ A = \pi \times r^2 \f$
 * where \f$ A \f$ is the area and \f$ r \f$ is the radius.
 *
 * \param radius The radius of the circle.
 * \return The area of the circle.
 */
inline double area_circle(const double radius) {
  return std::numbers::pi * radius * radius;
}

/**
 * @brief Adds two integers.
 *
 * This function takes two integers and returns their sum.
 *
 * @param ii The first integer.
 * @param jj The second integer.
 * @return The sum of ii and jj.
 */
inline int add(const int ii, const int jj) {
  return ii + jj;
}

#endif   // LIBS_SRC_CXX_MOCK_HPP_
