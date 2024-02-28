'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: text_mock_cxx.py
Project: tests
Created Date: Wednesday 28th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 28th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
test package for tests of mock C++ module via Pybind11 Python bindings
'''


import sys
import pathlib
import numpy as np

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path+'/../build/') # add path to mock_cxx to PATH
import mock_cxx as m

def test_area_circle():
     assert m.area_circle(4.0) == np.pi*4.0*4.0

def test_add():
     assert m.add(1, 2) == 3