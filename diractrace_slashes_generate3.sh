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

declare -a names=("fcstDiracTraceIn4dimsThreeSlashesAllIndicesContracted"
                "fcstDiracTraceIn4dimsOneG5ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG5ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsThreeSlashesAllIndicesContracted"
                "fcstDiracTraceInDdimsOneG5ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG5ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7ThreeSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7ThreeSlashesAllIndicesContractedKreimer"


)

mkdir -p DiracTrace/Slashes/Reports
mkdir -p DiracTrace/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceThreeSlashesAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceThreeSlashesAllIndicesContracted.txt &
done
