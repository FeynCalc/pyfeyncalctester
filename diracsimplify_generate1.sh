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

declare -a names=("fcstDiracSimplifyIn4dimsAllIndicesContracted"
                "fcstDiracSimplifyIn4dimsOneG5AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG7AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG5AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG6AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG7AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7AllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsAllIndicesContracted"
                "fcstDiracSimplifyInDdimsOneG5AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG7AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG5AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG6AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG7AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7AllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7AllIndicesContractedNaive"


)

mkdir -p DiracSimplify/Standard/Reports
mkdir -p DiracSimplify/Standard/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Standard/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Standard/Reports/DiracSimplifyAllIndicesContracted.txt &
done
