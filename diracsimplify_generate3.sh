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

declare -a names=("fcstDiracSimplifyIn4dimsTwoIndicesFree"
                "fcstDiracSimplifyIn4dimsOneG5TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG5TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoIndicesFree"
                "fcstDiracSimplifyInDdimsOneG5TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG5TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7TwoIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7TwoIndicesFreeNaive"


)

mkdir -p DiracSimplify/Standard/Reports
mkdir -p DiracSimplify/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyTwoIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyTwoIndicesFree.txt &
done
