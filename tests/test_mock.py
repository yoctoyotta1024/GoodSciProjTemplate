'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- GoodSciProjTemplate -----
File: test_mock.py
Project: tests
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Tuesday 27th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
package for tests of python mock module
'''


import numpy as np
from libs.src_py import mock

def test_area_circle():
	assert mock.area_circle(1.0) == np.pi
