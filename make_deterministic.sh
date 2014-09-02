#!/bin/bash

current_dir=$(pwd)"/"

./math_runner.sh "$current_dir"DiracSimplify/Standard "$current_dir"DiracSimplify/Standard/Det
./math_runner.sh "$current_dir"DiracSimplify/Slashes "$current_dir"DiracSimplify/Slashes/Det
./math_runner.sh "$current_dir"DiracTrace/Standard "$current_dir"DiracTrace/Standard/Det
./math_runner.sh "$current_dir"DiracTrace/Slashes "$current_dir"DiracTrace/Slashes/Det
