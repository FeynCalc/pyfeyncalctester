#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsTwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7TwoIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7TwoIndicesFree"

)

declare -a names=("fcstDiracTraceIn4dimsTwoIndicesFree"
                "fcstDiracTraceIn4dimsOneG5TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG7TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG5TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG6TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG7TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7TwoIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoIndicesFree"
                "fcstDiracTraceInDdimsOneG5TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG7TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG5TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG6TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG7TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7TwoIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7TwoIndicesFreeKreimer"


)

mkdir -p DiracTrace/Standard/Reports
mkdir -p DiracTrace/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceTwoIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceTwoIndicesFree.txt &
done
