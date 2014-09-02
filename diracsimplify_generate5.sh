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

declare -a names=("fcstDiracSimplifyIn4dimsFourIndicesFree"
                "fcstDiracSimplifyIn4dimsOneG5FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG7FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG5FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG6FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsTwoG7FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7FourIndicesFreeNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsFourIndicesFree"
                "fcstDiracSimplifyInDdimsOneG5FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG7FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG5FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG6FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsTwoG7FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7FourIndicesFreeNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7FourIndicesFreeNaive"


)

mkdir -p DiracSimplify/Standard/Reports
mkdir -p DiracSimplify/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyFourIndicesFree.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyFourIndicesFree.txt &
done
