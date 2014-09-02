#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsFourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsFourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG5FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsTwoG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG6FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG5OneG7FourIndicesFree" \
                "fcstDiracGammasInAlldimsOneG6OneG7FourIndicesFree"

)

declare -a names=("fcstDiracTraceIn4dimsFourIndicesFree"
                "fcstDiracTraceIn4dimsOneG5FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG7FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG5FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG6FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsTwoG7FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG6FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG5OneG7FourIndicesFreeKreimer"
                "fcstDiracTraceIn4dimsOneG6OneG7FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsFourIndicesFree"
                "fcstDiracTraceInDdimsOneG5FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG7FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG5FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG6FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsTwoG7FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG6FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG5OneG7FourIndicesFreeKreimer"
                "fcstDiracTraceInDdimsOneG6OneG7FourIndicesFreeKreimer"


)

mkdir -p DiracTrace/Standard/Reports
mkdir -p DiracTrace/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceFourIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracTrace/Standard/""${names[$i]}"".test" -m DiracTrace -g dirac_trace  >> DiracTrace/Standard/Reports/DiracTraceFourIndicesFree.txt &
done
