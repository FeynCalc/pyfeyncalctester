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

declare -a names=("fcstDiracSimplifyIn4dimsThreeIndicesFree"
                "fcstDiracSimplifyIn4dimsOneG5ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG5ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsThreeIndicesFree"
                "fcstDiracSimplifyInDdimsOneG5ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG5ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7ThreeIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7ThreeIndicesFreeNaive"


)

mkdir -p DiracSimplify/Standard/Reports
mkdir -p DiracSimplify/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyThreeIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyThreeIndicesFree.txt &
done
