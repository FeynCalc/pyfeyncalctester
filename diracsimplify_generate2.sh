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

declare -a names=("fcstDiracSimplifyIn4dimsOneIndexFree"
                "fcstDiracSimplifyIn4dimsOneG5OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG7OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG5OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG6OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG7OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7OneIndexFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneIndexFree"
                "fcstDiracSimplifyInDdimsOneG5OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneG7OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG5OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG6OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG7OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7OneIndexFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7OneIndexFreeNaive"


)

mkdir -p DiracSimplify/Standard/Reports
mkdir -p DiracSimplify/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyOneIndexFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyOneIndexFree.txt &
done
