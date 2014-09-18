# PyFeynCalcTester

PyFeynCalcTester is a Python program that can automatically generate tests
for FeynCalc and evaluate them with other packages for QFT computations.
At the moment PyFeynCalcTester can use [GiNaC](http://www.ginac.de/) to evaluate Dirac algebra.

# License

This software is covered by the GNU Lesser General Public License 3.

Copyright (C) 2014      Vladyslav Shtabovenko

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Installation
* To use PyFeynCalcTester you need *ginac*, *swig*, *swiginac* and *Mathematica* installed on your system.
* On Fedora, first run

    `sudo yum install ginac ginac-devel swig`
* Then download the latest swiginac [release](http://sourceforge.net/projects/swiginac.berlios/files/?source=navbar), unzip it and follow the instructions inside *INSTALL.txt*

* Clone the repository via

    `git clone https://github.com/FeynCalc/pyfeyncalctester.git`
* Run

    `./generate_generators.sh`

    to create generators of different test types

* Run

    `./generate_tests.sh`

    to create the tests for FeynCalc. Since the tests created in parallel, it is better to use a multicore machine for this step.

* Run

    `./make_deterministic.sh`

    to fix the ordering of the terms in a way as Mathematica would normally do it.
