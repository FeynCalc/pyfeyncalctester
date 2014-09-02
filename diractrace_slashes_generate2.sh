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

declare -a names=("fcstDiracTraceIn4dimsTwoSlashesAllIndicesContracted"
                "fcstDiracTraceIn4dimsOneG5TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG5TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoSlashesAllIndicesContracted"
                "fcstDiracTraceInDdimsOneG5TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG5TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7TwoSlashesAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7TwoSlashesAllIndicesContractedKreimer"


)

mkdir -p DiracTrace/Slashes/Reports
mkdir -p DiracTrace/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceTwoSlashesAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceTwoSlashesAllIndicesContracted.txt &
done
