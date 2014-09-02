#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7AllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7AllIndicesContracted"

)

declare -a names=("fcstDiracTraceIn4dimsAllIndicesContracted"
                "fcstDiracTraceIn4dimsOneG5AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG7AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG5AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG6AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsTwoG7AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7AllIndicesContractedKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsAllIndicesContracted"
                "fcstDiracTraceInDdimsOneG5AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG7AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG5AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG6AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsTwoG7AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7AllIndicesContractedKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7AllIndicesContractedKreimer"


)

mkdir -p DiracTrace/Standard/Reports
mkdir -p DiracTrace/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceAllIndicesContracted.txt &
done
