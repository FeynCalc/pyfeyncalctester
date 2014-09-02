#!/bin/bash


declare -a types=("fcstDiracGammasInAlldimsOneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG5OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsTwoG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG6OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG5OneG7OneSlashAllIndicesContracted" \
                "fcstDiracGammasInAlldimsOneG6OneG7OneSlashAllIndicesContracted"

)

declare -a names=("fcstDiracSimplifyIn4dimsOneSlashAllIndicesContracted"
                "fcstDiracSimplifyIn4dimsOneG5OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG5OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsTwoG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG5OneG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyIn4dimsOneG6OneG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneSlashAllIndicesContracted"
                "fcstDiracSimplifyInDdimsOneG5OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG5OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsTwoG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG6OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG5OneG7OneSlashAllIndicesContractedNaive"
                "fcstDiracSimplifyInDdimsOneG6OneG7OneSlashAllIndicesContractedNaive"


)

mkdir -p DiracSimplify/Slashes/Reports
mkdir -p DiracSimplify/Slashes/Det
for i in {0..9}
do
    nohup ./src/pyfeyncalctester.py -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyOneSlashAllIndicesContracted.txt &
done

for i in {10..19}
do
    nohup ./src/pyfeyncalctester.py -D -t "${types[$i]}"  -f "DiracSimplify/Slashes/""${names[$i]}"".test" -m DiracSimplify -g simplify_indexed  >> DiracSimplify/Slashes/Reports/DiracSimplifyOneSlashAllIndicesContracted.txt &
done
