#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7ThreeIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7ThreeIndicesFree"

)

declare -a names=("fcstDiracTraceIn4dimsThreeIndicesFree"
                "fcstDiracTraceIn4dimsOneG5ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG5ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsThreeIndicesFree"
                "fcstDiracTraceInDdimsOneG5ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG5ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7ThreeIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7ThreeIndicesFreeKreimer"


)

mkdir -p DiracTrace/Standard/Reports
mkdir -p DiracTrace/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceThreeIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceThreeIndicesFree.txt &
done
