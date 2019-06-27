"""
Autour N'TSOUAGLO Kokou Gawonou

"""
import logging
from abc import ABC, abstractmethod
import sys 


MSG_SOL_FICHIER = "	\nEntrez le nom de fichier : "
MSG_ERR_NON_TROUVE = "\nLe fichier n'a pas été trouvé."
MSG_ERR_NON_LU = "\nErreur de lecture du fichier."
MSG_ERR_PILE = "\nErreur! La pile est vide. \n\tMot: '%s' ligne: %d colonne: %d."
MSG_ERR_ZERO = "\nErreur! division par zéro. Mot: '%s' ligne: %d colonne: %d."
CHOIX_MAL_ENTRE = "\nLe choix mal entré"
FIN_LOGICIEL = "\n Fin du logiciel"
MENU ='\n\t\t1- Calculatrice.'+'\n\t\t2- Profil.'+'\n\t\t3- Mistere.'+'\n\t\t4- Fin du logiciel.\n'+ '\nEntrez votre choix : '

logging.basicConfig(filename='test.log', level=logging.DEBUG,
	                 format='%(asctime)s:%(levelname)s:%(message)s')


class Expression(ABC):
	@classmethod
	@abstractmethod
	def interprete(self, contexte):
		pass


class ContexteInterpretation(ABC):

	@abstractmethod
	def a(self, motA):
		pass


	@abstractmethod
	def a(self, motAv):
		pass
     


	@abstractmethod
	def b(self, motB):
		pass


	@abstractmethod
	def b(self, motBv):
		pass


	@abstractmethod
	def c(self, motC):
		pass


	@abstractmethod
	def c(self, motCv):
		pass


	@abstractmethod
	def d(self, motD):
		pass

	@abstractmethod
	def d(self, motDv):
		pass



	@abstractmethod
	def e(self, motE):
		pass


	@abstractmethod
	def f(self, motF):
		pass


	@abstractmethod
	def g(self, motG):
		pass
	

class Mot:
	def __init__(self, _mots, _ligne, _colonne):
		self.__mots = _mots
		self.__ligne = _ligne
		self.__colonne = _colonne
	
	@property
	def getMot(self):
		return self.__mots

	@property	
	def getLigne(self):
		return self.__ligne

	@property
	def getColonne(self):
		return self.__colonne



class Motv(Mot):
	def __init__(self,  _mots, _valeur, _ligne, _colonne):
		super().__init__(self, _mots, _ligne, _colonne)
		self__valeur = _valeur


	@property
	def getValeur(self):
		return self.__valeur



def fichierlu():
	la_ligne = []
	Nomfichier = input(MSG_SOL_FICHIER)
	try:
	    with open(Nomfichier, "r") as ff:
	    	for line in ff :
	    		la_ligne.append(line)
	except FileNotFoundError as file1 :
		print(file1)
		exit(2)
	return la_ligne


def Motvalide(m):
	MotVrais = False
	if m == 'a' or m == 'b' or m =='c' or m == 'd' or \
		m == 'e' or m == 'f' or m == 'g' or m == '(' or \
		m == ')' or m == '-' or m == '+' or m.isnumeric():
		MotVrais = True
	return MotVrais

def Ingorechar(m):
	IngoreMot = False
	if m == ' ' or m == '\t' or m == '\n':
		IngoreMot = True
	return IngoreMot

def valideligne(list):
	Les_ligne = []
	lign = 0
	for line in list:
		col = 0
		lign += 1
		for mot in line:
			col += 1
			if Motvalide(mot):
				logging.debug('mot = {} ligne ={} colonne = {}'.format(mot, lign, col))
				Les_ligne.append(Mot(mot, lign, col))
			elif Ingorechar(mot):
				col += 1
			else :
				print("\nErreur de syntaxe mot {0} à la ligne {1} colonne {2} .".format(mot, lign, col))
				sys.exit()
	return Les_ligne





def main():
	tt = valideligne(fichierlu())
	print("#################################")
	print(len(tt))
	for l in tt :
		print(l.getMot, l.getLigne, l.getColonne)

if __name__ == "__main__":
	main()
