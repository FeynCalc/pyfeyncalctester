#!/usr/bin/bash



if [ -a /usr/local/bin/MathematicaScript ]; then
   /usr/local/bin/MathematicaScript -script math_code.m $1 $2
else
   /mount/packs/Mathematica10.0/MathematicaScript -script math_code.m $1 $2
fi
