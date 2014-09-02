#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsTwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7TwoSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7TwoSlashesAllIndicesContracted"

)

declare -a names=("fcstDiracSimplifyIn4dimsTwoSlashesAllIndicesContracted"
                "fcstDiracSimplifyIn4dimsOneG5TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG5TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoSlashesAllIndicesContracted"
                "fcstDiracSimplifyInDdimsOneG5TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG5TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7TwoSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7TwoSlashesAllIndicesContractedNaive"


)

mkdir -p DiracSimplify/Slashes/Reports
mkdir -p DiracSimplify/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyTwoSlashesAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyTwoSlashesAllIndicesContracted.txt &
done
