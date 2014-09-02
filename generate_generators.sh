#!/bin/bash

sed 's/AllIndicesContracted/OneIndexFree/g' < diracsimplify_generate1.sh > diracsimplify_generate2.sh
sed 's/AllIndicesContracted/TwoIndicesFree/g' < diracsimplify_generate1.sh > diracsimplify_generate3.sh
sed 's/AllIndicesContracted/ThreeIndicesFree/g' < diracsimplify_generate1.sh > diracsimplify_generate4.sh
sed 's/AllIndicesContracted/FourIndicesFree/g' < diracsimplify_generate1.sh > diracsimplify_generate5.sh

sed 's/AllIndicesContracted/OneSlashAllIndicesContracted/g;s/Standard/Slashes/g' < diracsimplify_generate1.sh > diracsimplify_slashes_generate1.sh
sed 's/AllIndicesContracted/TwoSlashesAllIndicesContracted/g;s/Standard/Slashes/g' < diracsimplify_generate1.sh > diracsimplify_slashes_generate2.sh
sed 's/AllIndicesContracted/ThreeSlashesAllIndicesContracted/g;s/Standard/Slashes/g' < diracsimplify_generate1.sh > diracsimplify_slashes_generate3.sh

sed 's/DiracSimplify/DiracTrace/g;s/simplify_indexed/dirac_trace/g;s/Naive/Kreimer/g' < diracsimplify_generate1.sh > diractrace_generate1.sh
sed 's/AllIndicesContracted/OneIndexFree/g;s/DiracSimplify/DiracTrace/g;s/simplify_indexed/dirac_trace/g;s/Naive/Kreimer/g' < diracsimplify_generate2.sh > diractrace_generate2.sh
sed 's/AllIndicesContracted/OneIndexFree/g;s/DiracSimplify/DiracTrace/g;s/simplify_indexed/dirac_trace/g;s/Naive/Kreimer/g' < diracsimplify_generate3.sh > diractrace_generate3.sh
sed 's/AllIndicesContracted/OneIndexFree/g;s/DiracSimplify/DiracTrace/g;s/simplify_indexed/dirac_trace/g;s/Naive/Kreimer/g' < diracsimplify_generate4.sh > diractrace_generate4.sh
sed 's/AllIndicesContracted/OneIndexFree/g;s/DiracSimplify/DiracTrace/g;s/simplify_indexed/dirac_trace/g;s/Naive/Kreimer/g' < diracsimplify_generate5.sh > diractrace_generate5.sh


sed 's/AllIndicesContracted/OneSlashAllIndicesContracted/g;s/Standard/Slashes/g;s/Naive/Kreimer/g' < diractrace_generate1.sh > diractrace_slashes_generate1.sh
sed 's/AllIndicesContracted/TwoSlashesAllIndicesContracted/g;s/Standard/Slashes/g;s/Naive/Kreimer/g' < diractrace_generate1.sh > diractrace_slashes_generate2.sh
sed 's/AllIndicesContracted/ThreeSlashesAllIndicesContracted/g;s/Standard/Slashes/g;s/Naive/Kreimer/g' < diractrace_generate1.sh > diractrace_slashes_generate3.sh

chmod +x *.sh
