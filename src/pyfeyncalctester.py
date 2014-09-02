#!/usr/bin/python2.7


import ntpath
import re
import time

import argparse
import swiginac

import listcreator
class TestGenerator():

    in_D_dimensions = False
    letter_i = 'i'
    letter_j = 'j'
    letter_k = 'k'
    letter_l = 'l'

    letter_m = 'm'
    letter_n = 'n'
    letter_o = 'o'
    letter_p = 'p'
    replacement_dirac_gamma = 'GA'

    def vsTupleToString(self, mylist):
        newlist = []
        dims = '4'
        if self.in_D_dimensions:
            dims = 'D'
        for d in mylist:
            # for j in d:
            newstr = str(d).replace(
                ',', '*').replace('\'', '').replace('comma', ',').replace('dims', dims)
            newlist.append(newstr)

        return newlist

    def vsRenameIndices(self, mylist, mypattern, letterlist):
        mynewlist = []
        for d in mylist:

            newstr = d
            for l in letterlist:
                if re.search(mypattern, newstr) is not None:
                    newstr = newstr.replace(
                        re.search(mypattern, newstr).group(), l)

            mynewlist.append(newstr)
        return mynewlist

    def vsToggleVariance(self, mylist, letterlist):
        mynewlist = []
        for d in mylist:
            newstr = d

            for l in letterlist:
                if re.search("(" + l + ")", newstr) is not None:
                    newstr = newstr.replace(
                        "(" + l + ")", "(" + l + ".toggle_variance())", 1)
            mynewlist.append(newstr)
        return mynewlist

    def ConvertToMMA(self, mystring):
        mystring = re.sub('dirac\_gamma5\(\)', 'GA[5]', mystring)
        mystring = re.sub('dirac\_gammaR\(\)', 'GA[6]', mystring)
        mystring = re.sub('dirac\_gammaL\(\)', 'GA[7]', mystring)
        mystring = re.sub('dirac\_gamma\((?P<index1>.)\)',
                          self.replacement_dirac_gamma + '[\g<index1>]', mystring)
        mystring = re.sub('dirac\_gamma\((?P<index1>..)\)',
                          self.replacement_dirac_gamma + '[\g<index1>]', mystring)

        mystring = re.sub(
            'dirac\_slash\((?P<index1>..) , D\)', 'GSD[\g<index1>]', mystring)
        mystring = re.sub(
            'dirac\_slash\((?P<index1>..) , 4\)', 'GS[\g<index1>]', mystring)

        mystring = re.sub('\*', '.', mystring)

        return mystring

    def CreatePyAndMmaLists(self, mylist):
        t0 = time.clock()
        print 'Start  creating lists ... '

        temp_list = list(set(self.vsRenameIndices(self.vsTupleToString(mylist),
                                                  "<[0-9]>", ["(" + self.letter_i + ")", "(" + self.letter_j + ")",
                                                              "(" + self.letter_k +
                                                              ")", "(" +
                                                              self.letter_l +
                                                              ")",
                                                              "(" + self.letter_m +
                                                              ")", "(" +
                                                              self.letter_n +
                                                              ")",
                                                              "(" + self.letter_o + ")", "(" + self.letter_p + ")"])))

        py_list = self.vsToggleVariance(temp_list,
                                        [self.letter_i, self.letter_j, self.letter_k, self.letter_l,
                                         self.letter_m, self.letter_n, self.letter_o, self.letter_p])

        self.replacement_dirac_gamma = 'GA'
        if self.in_D_dimensions:
            self.replacement_dirac_gamma = 'GAD'
        mma_list = [self.ConvertToMMA(el) for el in temp_list]
        print 'End: ', (time.clock() - t0), 'sec'
        return py_list, mma_list

    def GinacToMMA(self, evaluated_element):



#         evaluated_element = evaluated_element.replace('*[diracone object]', '').replace('[diracone object]*', '').replace(
#             '[diracgamma5 object]', 'DiracGamma[5]').replace('gammaR', 'DiracGamma[6]').replace('gammaL', 'DiracGamma[7]').replace('**', '^')



        evaluated_element = re.sub('\[diracone object\]\*', '', evaluated_element)
        evaluated_element = re.sub('\*\[diracone object\]', '', evaluated_element)
        evaluated_element = re.sub('\[diracgamma5 object\]', 'DiracGamma[5]', evaluated_element)
        evaluated_element = re.sub('gammaR', 'DiracGamma[6]', evaluated_element)
        evaluated_element = re.sub('gammaL', 'DiracGamma[7]', evaluated_element)
        evaluated_element = re.sub('\*\*', '^', evaluated_element)

        evaluated_element = re.sub(
            'DiracGamma\[5\]\*DiracGamma\[6\]', 'DiracGamma[5].DiracGamma[6]', evaluated_element)
        evaluated_element = re.sub(
            'DiracGamma\[5\]\*DiracGamma\[5\]', 'DiracGamma[6].DiracGamma[5]', evaluated_element)

        evaluated_element = re.sub(
            'DiracGamma\[5\]\*DiracGamma\[7\]', 'DiracGamma[5].DiracGamma[7]', evaluated_element)
        evaluated_element = re.sub(
            'DiracGamma\[7\]\*DiracGamma\[5\]', 'DiracGamma[7].DiracGamma[5]', evaluated_element)

# D dimensions

        if self.in_D_dimensions:
            old_element = ''
            while True:
                evaluated_element = re.sub(
                    'DiracGamma\[5\]\*\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)', 'DiracGamma[5].[diracgamma object].\g<index1>', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[6\]\*\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)', 'DiracGamma[6].[diracgamma object].\g<index1>', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[7\]\*\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)', 'DiracGamma[7].[diracgamma object].\g<index1>', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\*DiracGamma\[5\]', '[diracgamma object].\g<index1>.DiracGamma[5]', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\*DiracGamma\[6\]', '[diracgamma object].\g<index1>.DiracGamma[6]', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\*DiracGamma\[7\]', '[diracgamma object].\g<index1>.DiracGamma[7]', evaluated_element)
                evaluated_element = re.sub('\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\*\[diracgamma object\]\.(?P<index2>iD|jD|kD|lD|mD|nD|oD|pD)',
                                           '[diracgamma object].\g<index1>.[diracgamma object].\g<index2>', evaluated_element)
                evaluated_element = re.sub('\[tensepsilon object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\.(?P<index2>iD|jD|kD|lD|mD|nD|oD|pD)\.(?P<index3>iD|jD|kD|lD|mD|nD|oD|pD)\.(?P<index4>iD|jD|kD|lD|mD|nD|oD|pD)',
                                           'Eps[LorentzIndex[\g<index1>,D], LorentzIndex[\g<index2>,D], LorentzIndex[\g<index3>,D], LorentzIndex[\g<index4>,D]]', evaluated_element)

                evaluated_element = re.sub(
                    'DiracGamma\[5\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[5].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[6\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[6].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[7\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[7].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[5\]', '\g<index1>~0.DiracGamma[5]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[6\]', '\g<index1>~0.DiracGamma[6]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[7\]', '\g<index1>~0.DiracGamma[7]', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\*(?P<index2>p1|p2|p3|p4)~0', '[diracgamma object].\g<index1>.\g<index2>~0', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index2>p1|p2|p3|p4)~0\*\[diracgamma object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)', '\g<index2>~0.[diracgamma object].\g<index1>', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index2>p1|p2|p3|p4)~0\*(?P<index1>p1|p2|p3|p4)~0', '\g<index2>~0.\g<index1>~0', evaluated_element)

                evaluated_element = re.sub(
                    '(?P<index1>..)\~symbol(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)\*(?P<index3>..)\.symbol(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D] ]', evaluated_element)
                evaluated_element_test = re.sub(
                    '(?P<index1>..)\~(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)\*(?P<index3>..)\.(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D] ]', evaluated_element)

                evaluated_element = re.sub(
                    '(?P<index1>..)\.symbol(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)\*(?P<index3>..)\~symbol(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D] ]', evaluated_element)
                evaluated_element_test = re.sub(
                    '(?P<index1>..)\.(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)\*(?P<index3>..)\~(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D] ]', evaluated_element)

                if old_element == evaluated_element:
                    break
                else:
                    old_element = evaluated_element

            # print "Slash catcher 1", evaluated_element
            evaluated_element = re.sub(
                    '(?P<index>p1|p2|p3|p4)\.0', 'DiracGamma[Momentum[\g<index>,D],D]', evaluated_element)
            evaluated_element = re.sub(
                    '(?P<index>p1|p2|p3|p4)\~0', 'DiracGamma[Momentum[\g<index>,D],D]', evaluated_element)
            # print "Slash catcher 2", evaluated_element

            old_element = ''

            while True:
                if old_element == evaluated_element:
                    break
                else:
                    old_element = evaluated_element

                # print "search", evaluated_element
                first_pos = re.search("p[1-3](\.|\~)", evaluated_element)

                if first_pos != None:
                    # print "found", first_pos.group()
                    first_pos = first_pos.group()
                evaluated_element_test = evaluated_element

                if first_pos == "p1." or first_pos == "p2." or first_pos == "p3.":
                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\.symbol(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)(?P<All>.*?)\*(?P<index3>..)\~symbol(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D]] \g<All> ', evaluated_element, 1)
                    # print ". 1.1", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print ". 1.1", evaluated_element

                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\.(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)(?P<All>.*?)\*(?P<index3>..)\~(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D]] \g<All> ', evaluated_element, 1)
                    # print ". 1.2", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print ". 1.2", evaluated_element

                elif first_pos == "p1~" or first_pos == "p2~" or first_pos == "p3~":
                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\~symbol(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)(?P<All>.*?)\*(?P<index3>..)\.symbol(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D]] \g<All> ', evaluated_element, 1)
                    # print "~ 1.1", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print "~ 1.1", evaluated_element



                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\~(?P<index2>[0-9]+|iD|jD|kD|lD|mD|nD|oD|pD)(?P<All>.*?)\*(?P<index3>..)\.(?P=index2)', 'Pair[Momentum[\g<index1>,D], Momentum[\g<index3>,D]] \g<All> ', evaluated_element, 1)
                    # print "~ 1.2", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print "~ 1.2", evaluated_element

                else:
                    pass


            evaluated_element = re.sub(
                '\[diracgamma object\]\.(?P<index>iD|jD|kD|lD|mD|nD|oD|pD)', 'DiracGamma[LorentzIndex[\g<index>,D],D]', evaluated_element)
            evaluated_element = re.sub('\[minkmetric object\]\.(?P<index1>iD|jD|kD|lD|mD|nD|oD|pD)\.(?P<index2>iD|jD|kD|lD|mD|nD|oD|pD)',
                                       'Pair[LorentzIndex[\g<index1>,D], LorentzIndex[\g<index2>,D]]', evaluated_element)



# 4 dimensions

        else:
            old_element = ''
            while True:
                evaluated_element = re.sub(
                    'DiracGamma\[5\]\*\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)', 'DiracGamma[5].[diracgamma object].\g<inex1>', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[6\]\*\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)', 'DiracGamma[6].[diracgamma object].\g<inex1>', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[7\]\*\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)', 'DiracGamma[7].[diracgamma object].\g<inex1>', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)*DiracGamma\[5\]', '[diracgamma object].\g<inex1>.DiracGamma[5]', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)*DiracGamma\[6\]', '[diracgamma object].\g<inex1>.DiracGamma[6]', evaluated_element)
                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<inex1>i|j|k|l|m|n|o|p)*DiracGamma\[7\]', '[diracgamma object].\g<inex1>.DiracGamma[7]', evaluated_element)
                evaluated_element = re.sub('\[diracgamma object\]\.(?P<index1>i|j|k|l|m|n|o|p)\*\[diracgamma object\].(?P<index2>i|j|k|l|m|n|o|p)',
                                           '[diracgamma object].\g<index1>.[diracgamma object].\g<index2>', evaluated_element)
                evaluated_element = re.sub('\[tensepsilon object\]\.(?P<index1>i|j|k|l|m|n|o|p)\.(?P<index2>i|j|k|l|m|n|o|p)\.(?P<index3>i|j|k|l|m|n|o|p)\.(?P<index4>i|j|k|l|m|n|o|p)',
                                           'Eps[LorentzIndex[\g<index1>], LorentzIndex[\g<index2>], LorentzIndex[\g<index3>], LorentzIndex[\g<index4>]]', evaluated_element)

                evaluated_element = re.sub(
                    'DiracGamma\[5\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[5].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[6\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[6].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    'DiracGamma\[7\]\*(?P<index1>p1|p2|p3|p4)~0', 'DiracGamma[7].\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[5\]', '\g<index1>~0.DiracGamma[5]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[6\]', '\g<index1>~0.DiracGamma[6]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>p1|p2|p3|p4)~0\*DiracGamma\[7\]', '\g<index1>~0.DiracGamma[7]', evaluated_element)


                evaluated_element = re.sub(
                    '\[diracgamma object\]\.(?P<index1>i|j|k|l|m|n|o|p)\*(?P<index2>p1|p2|p3|p4)~0', '[diracgamma object].\g<index1>.\g<index2>~0', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index2>p1|p2|p3|p4)~0\*\[diracgamma object\]\.(?P<index1>i|j|k|l|m|n|o|p)', '\g<index2>~0.[diracgamma object].\g<index1>', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index2>p1|p2|p3|p4)~0\*(?P<index1>p1|p2|p3|p4)~0', '\g<index2>~0.\g<index1>~0', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>..)\.symbol(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)\*(?P<index3>..)\~symbol(?P=index2)', 'Pair[ Momentum[\g<index1>], Momentum[\g<index3>] ]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>..)\~symbol(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)\*(?P<index3>..)\.symbol(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>] ]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>..)\.(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)\*(?P<index3>..)\~(?P=index2)', 'Pair[ Momentum[\g<index1>], Momentum[\g<index3>] ]', evaluated_element)
                evaluated_element = re.sub(
                    '(?P<index1>..)\~(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)\*(?P<index3>..)\.(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>] ]', evaluated_element)



                if old_element == evaluated_element:
                    break
                else:
                    old_element = evaluated_element


            # print "Slash catcher 1", evaluated_element
            evaluated_element = re.sub(
                    '(?P<index>p1|p2|p3|p4)\.0', 'DiracGamma[Momentum[\g<index>]]', evaluated_element)
            evaluated_element = re.sub(
                    '(?P<index>p1|p2|p3|p4)\~0', 'DiracGamma[Momentum[\g<index>]]', evaluated_element)
            # print "Slash catcher 2", evaluated_element

            old_element = ''

            while True:
                if old_element == evaluated_element:
                    break
                else:
                    old_element = evaluated_element

                # print "search", evaluated_element
                first_pos = re.search("p[1-3](\.|\~)", evaluated_element)

                if first_pos != None:
                    # print "found", first_pos.group()
                    first_pos = first_pos.group()
                evaluated_element_test = evaluated_element

                if first_pos == "p1." or first_pos == "p2." or first_pos == "p3.":
                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\.symbol(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)(?P<All>.*?)\*(?P<index3>..)\~symbol(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>]] \g<All> ', evaluated_element, 1)
                    # print ". 1.1", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print ". 1.1", evaluated_element

                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\.(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)(?P<All>.*?)\*(?P<index3>..)\~(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>]] \g<All> ', evaluated_element, 1)
                    # print ". 1.2", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print ". 1.2", evaluated_element

                elif first_pos == "p1~" or first_pos == "p2~" or first_pos == "p3~":
                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\~symbol(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)(?P<All>.*?)\*(?P<index3>..)\.symbol(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>]] \g<All> ', evaluated_element, 1)
                    # print "~ 1.1", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print "~ 1.1", evaluated_element

                    evaluated_element_test = re.sub(
                    '(?P<index1>..)\~(?P<index2>[0-9]+|i|j|k|l|m|n|o|p)(?P<All>.*?)\*(?P<index3>..)\.(?P=index2)', 'Pair[Momentum[\g<index1>], Momentum[\g<index3>]] \g<All> ', evaluated_element, 1)
                    # print "~ 1.2", evaluated_element_test
                    if evaluated_element_test != evaluated_element:
                        evaluated_element = evaluated_element_test
                        continue
                    # print "~ 1.2", evaluated_element

                else:
                    pass



            evaluated_element = re.sub('\[minkmetric object\]\.(?P<index1>i|j|k|l|m|n|o|p)\.(?P<index2>i|j|k|l|m|n|o|p)',
                                       'Pair[LorentzIndex[\g<index1>], LorentzIndex[\g<index2>]]', evaluated_element)
            evaluated_element = re.sub(
                '\[diracgamma object\]\.(?P<index>i|j|k|l|m|n|o|p)', 'DiracGamma[LorentzIndex[\g<index>]]', evaluated_element)


        return evaluated_element

    def CreateTestFile(self, py_list, mma_list, file_str, mma_routine, ginac_routine):
        t0 = time.clock()
        print 'Start  writing test file ... '
        list_str = ntpath.basename(file_str).split('.')[0]

        evaluated_elements = []
        for element_id in xrange(len(mma_list)):

            evaluated_element = str(
            eval('simplify_indexed(' + ginac_routine + '(' + py_list[element_id] + '))'))
            evaluated_element = self.GinacToMMA(evaluated_element)

            evaluated_elements.append(evaluated_element)

        text_file = open(file_str, "w")
        text_file.write(
            list_str + '= { \n')

        for element_id in xrange(len(mma_list)):
            text_file.write('{"' + list_str + '-ID' + str(element_id) +
                            '","' + mma_routine + '[' + mma_list[element_id] + ']","' + evaluated_elements[element_id] + '"}')
            if element_id != (len(mma_list) - 1):
                text_file.write(', \n')
            else:
                text_file.write('}  \n \n  \n')

        text_file.close()

        print 'End: ', (time.clock() - t0), 'sec'
        print len(mma_list), ' items saved \n'

if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument('-D', '--D_dimensions', help='compute in D spacetime dimensions',
                        action='store_true')
    parser.add_argument(
        '-t', '--test_type', help='type of the test to generate')

    parser.add_argument(
        '-f', '--file_name', help='output file name for the test')

    parser.add_argument(
        '-m', '--mma_routine', help='FeynCalc routine to apply to the functions')

    parser.add_argument(
        '-g', '--ginac_routine', help='GiNaC routine to apply to the functions')


    args = parser.parse_args()

    D_dimensions = args.D_dimensions
    test_type = args.test_type
    file_name = args.file_name
    mma_routine = args.mma_routine
    ginac_routine = args.ginac_routine

    print 'Start preparing ' + file_name

    MyTestGenerator = TestGenerator()
    MyListCreator = listcreator.ListCreator()

    dirac_gamma = swiginac.dirac_gamma
    dirac_slash = swiginac.dirac_slash
    dirac_gamma5 = swiginac.dirac_gamma5
    dirac_gammaR = swiginac.dirac_gammaR
    dirac_gammaL = swiginac.dirac_gammaL
    simplify_indexed = swiginac.simplify_indexed
    dirac_trace = swiginac.dirac_trace

    D = swiginac.symbol("D")
    i = swiginac.varidx(swiginac.symbol("i"), 4)
    j = swiginac.varidx(swiginac.symbol("j"), 4)
    k = swiginac.varidx(swiginac.symbol("k"), 4)
    l = swiginac.varidx(swiginac.symbol("l"), 4)

    m = swiginac.varidx(swiginac.symbol("m"), 4)
    n = swiginac.varidx(swiginac.symbol("n"), 4)
    o = swiginac.varidx(swiginac.symbol("o"), 4)
    p = swiginac.varidx(swiginac.symbol("p"), 4)

    iD = swiginac.varidx(swiginac.symbol("iD"), D)
    jD = swiginac.varidx(swiginac.symbol("jD"), D)
    kD = swiginac.varidx(swiginac.symbol("kD"), D)
    lD = swiginac.varidx(swiginac.symbol("lD"), D)

    mD = swiginac.varidx(swiginac.symbol("mD"), D)
    nD = swiginac.varidx(swiginac.symbol("nD"), D)
    oD = swiginac.varidx(swiginac.symbol("oD"), D)
    pD = swiginac.varidx(swiginac.symbol("pD"), D)

    p1 = swiginac.symbol("p1")
    p2 = swiginac.symbol("p2")
    p3 = swiginac.symbol("p3")

    if D_dimensions:
        MyTestGenerator.in_D_dimensions = True
        MyTestGenerator.letter_i = 'iD'
        MyTestGenerator.letter_j = 'jD'
        MyTestGenerator.letter_k = 'kD'
        MyTestGenerator.letter_l = 'lD'

        MyTestGenerator.letter_m = 'mD'
        MyTestGenerator.letter_n = 'nD'
        MyTestGenerator.letter_o = 'oD'
        MyTestGenerator.letter_p = 'pD'

    eval('MyListCreator.' + test_type + '()')
    mylist_py, mylist_mma = MyTestGenerator.CreatePyAndMmaLists(
        MyListCreator.current_list)
    MyTestGenerator.CreateTestFile(
        mylist_py, mylist_mma, file_name, mma_routine, ginac_routine)
