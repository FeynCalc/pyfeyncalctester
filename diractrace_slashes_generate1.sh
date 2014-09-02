#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsOneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneSlashAllIndicesContracted"

)

declare -a names=("fcstDiracTraceIn4dimsOneSlashAllIndicesContracted"
                "fcstDiracTraceIn4dimsOneG5OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG5OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneSlashAllIndicesContracted"
                "fcstDiracTraceInDdimsOneG5OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG5OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7OneSlashAllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7OneSlashAllIndicesContractedKreimer"


)

mkdir -p DiracTrace/Slashes/Reports
mkdir -p DiracTrace/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceOneSlashAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Slashes/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Slashes/Reports/DiracTraceOneSlashAllIndicesContracted.txt &
done
