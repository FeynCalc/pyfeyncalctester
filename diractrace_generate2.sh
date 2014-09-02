#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsOneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG6OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG7OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG5OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG6OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG7OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneIndexFree" \
                "fcstDiracGammasInAlldimsOneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG6OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG7OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG5OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG6OneIndexFree" \
                "fcstDiracGammasInAlldimsTwoG7OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneIndexFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneIndexFree"

)

declare -a names=("fcstDiracTraceIn4dimsOneIndexFree"
                "fcstDiracTraceIn4dimsOneG5OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsOneG7OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG5OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG6OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG7OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7OneIndexFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneIndexFree"
                "fcstDiracTraceInDdimsOneG5OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneG6OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneG7OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsTwoG5OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsTwoG6OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsTwoG7OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7OneIndexFreeKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7OneIndexFreeKreimer"


)

mkdir -p DiracTrace/Standard/Reports
mkdir -p DiracTrace/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceOneIndexFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceOneIndexFree.txt &
done
