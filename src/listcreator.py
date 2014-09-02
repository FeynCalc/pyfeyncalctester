#!/usr/bin/python
import itertools

class ListCreator():
    current_list = None



    def fcstDiracGammasInAlldimsAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>'])))

    def fcstDiracGammasInAlldimsOneG5AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>', 'dirac_gamma5()'])))


    def fcstDiracGammasInAlldimsOneG6AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>',
                                     'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>',
                                     'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>', 'dirac_gammaL()'])))


    def fcstDiracGammasInAlldimsTwoG5AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gamma5()'])))


    def fcstDiracGammasInAlldimsTwoG6AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma5()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def  fcstDiracGammasInAlldimsOneG5OneG7AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma5()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaL()'])))
    def fcstDiracGammasInAlldimsOneG6OneG7AllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gammaR()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gammaR()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaL()'])))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def  fcstDiracGammasInAlldimsOneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>']))
        + list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>']))
        + list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>', 'dirac_gamma<5>'])))

    def fcstDiracGammasInAlldimsOneG5OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma5()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaL()'])))


    def fcstDiracGammasInAlldimsOneG6OneG7OneIndexFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gammaR()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaL()'])))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fcstDiracGammasInAlldimsTwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>'])))

    def fcstDiracGammasInAlldimsOneG5TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma5()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG6OneG7TwoIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gammaR()', 'dirac_gammaL()'])))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fcstDiracGammasInAlldimsThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>'])))

    def fcstDiracGammasInAlldimsOneG5ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()' ])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()' ])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaL()' ])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma5()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG6OneG7ThreeIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gammaR()', 'dirac_gammaL()'])))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fcstDiracGammasInAlldimsFourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>' ])))

    def fcstDiracGammasInAlldimsOneG5FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gamma5()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG6OneG7FourIndicesFree(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<5>', 'dirac_gammaR()', 'dirac_gammaL()'])))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def  fcstDiracGammasInAlldimsOneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)']))
        + list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_slash(p1 comma dims)']))
        + list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_gamma<4>', 'dirac_gamma<4>', 'dirac_slash(p1 comma dims)'])))

    def fcstDiracGammasInAlldimsOneG5OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_gamma<3>', 'dirac_gamma<3>', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()'])))


    def fcstDiracGammasInAlldimsOneG6OneG7OneSlashAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()'])))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def fcstDiracGammasInAlldimsTwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)'])))

    def fcstDiracGammasInAlldimsOneG5TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_gamma<2>', 'dirac_gamma<2>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsTwoG6TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsTwoG7TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG5OneG6TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG5OneG7TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsOneG6OneG7TwoSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()'])))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    def fcstDiracGammasInAlldimsThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)'])))

    def fcstDiracGammasInAlldimsOneG5ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()'])))

    def fcstDiracGammasInAlldimsOneG6ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()'])))

    def fcstDiracGammasInAlldimsOneG7ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])) +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()'])))

    def fcstDiracGammasInAlldimsTwoG5ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gamma5()']))[0:600])

    def fcstDiracGammasInAlldimsTwoG6ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaR()']))[0:600])


    def fcstDiracGammasInAlldimsTwoG7ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaL()', 'dirac_gammaL()']))[0:600])

    def fcstDiracGammasInAlldimsOneG5OneG6ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaR()']))[0:600])

    def fcstDiracGammasInAlldimsOneG5OneG7ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gamma5()', 'dirac_gammaL()']))[0:600])


    def fcstDiracGammasInAlldimsOneG6OneG7ThreeSlashesAllIndicesContracted(self):
        self.current_list = set(
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p3 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p2 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()']))[0:600] +
        list(itertools.permutations(['dirac_gamma<1>', 'dirac_gamma<1>', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_slash(p1 comma dims)', 'dirac_gammaR()', 'dirac_gammaL()']))[0:600])




















