#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7ThreeSlashesAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7ThreeSlashesAllIndicesContracted"

)

declare -a names=("fcstDiracSimplifyIn4dimsThreeSlashesAllIndicesContracted"
                "fcstDiracSimplifyIn4dimsOneG5ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG5ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsThreeSlashesAllIndicesContracted"
                "fcstDiracSimplifyInDdimsOneG5ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG5ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7ThreeSlashesAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7ThreeSlashesAllIndicesContractedNaive"


)

mkdir -p DiracSimplify/Slashes/Reports
mkdir -p DiracSimplify/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyThreeSlashesAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyThreeSlashesAllIndicesContracted.txt &
done
