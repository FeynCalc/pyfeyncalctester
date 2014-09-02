#!/mount/packs/Mathematica10.0/MathematicaScript -script


(*#!/usr/local/bin/MathematicaScript -script*)




(*https://stackoverflow.com/questions/8362170/how-to-find-line-where-error-occurred-in-mathematica-notebook*)
ClearAll[debug];
SetAttributes[debug, HoldAll];
debug[code_] :=
 Internal`InheritedBlock[{Message},
   Module[{inMessage},
     Unprotect[Message];
     Message[args___] /; ! MatchQ[First[Hold[args]], _$Off] :=
       Block[{inMessage = True},
         Print[{
            Shallow /@ Replace[#, HoldForm[f_[___]] :> HoldForm[f], 1],
            Style[Map[Short, Last[#], {2}], Red]
           } &@Drop[Drop[Stack[_], -7], 4]
         ];
         Message[args];
         Throw[$Failed, Message];
       ] /; ! TrueQ[inMessage];
    Protect[Message];
   ];
   Catch[StackComplete[code], Message]]

Eps[args__] := Signature[{args}] Eps@@ Sort[{args}] /; !OrderedQ[{args}]
Pair[args__] := Pair @@ Sort[{args}] /; ! OrderedQ[{args}]


pathToTests=$ScriptCommandLine[[2]];

pathToNewTests=$ScriptCommandLine[[3]];

fcstDeterministicOrdering[list_,listName_, path_] := Block[{},

  newlist = debug[Map[{#[[1]], #[[2]], ToString[InputForm[ToExpression[#[[3]]]]] }&, list]];

  newfile = OpenWrite[((path <> "/") <> listName) <> ".test"];
   pathname = listName <> "=";
   WriteString[newfile, pathname];
   Write[newfile, newlist];
  (*Map[Write[newfile, #] &, newlist];*)
  Close[newfile];
  ]

tests = FileNames["*.test",pathToTests];
Map[Get, tests];
varnames = Map[FileBaseName, tests];
vars = Map[ToExpression[#]&,varnames];

MapIndexed[fcstDeterministicOrdering[#,varnames[[#2]], pathToNewTests] &, vars]
