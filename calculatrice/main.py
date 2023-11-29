class Calculatrice:
    def __init__(self):
        self.historique = []

    def demander_nombre(self, message="Entrez un nombre : "):
        while True:
            try:
                nombre = float(input(message))
                return nombre
            except ValueError:
                print("Erreur : Entrez un nombre valide.")

    def demander_operation(self):
        while True:
            operation = input("Entrez une opération (+, -, *, /) : ")
            if operation in ['+', '-', '*', '/']:
                return operation
            else:
                print("Erreur : Opération invalide. Veuillez entrer +, -, *, ou /.")

    def calculer(self, nombre1, nombre2, operation):
        if operation == '+':
            return nombre1 + nombre2
        elif operation == '-':
            return nombre1 - nombre2
        elif operation == '*':
            return nombre1 * nombre2
        elif operation == '/':
            if nombre2 == 0:
                print("Erreur : Division par zéro.")
                return None
            else:
                return nombre1 / nombre2

    def afficher_historique(self):
        print("Historique des opérations :")
        for operation in self.historique:
            print(operation)

    def effacer_historique(self):
        self.historique = []
        print("Historique effacé.")

    def executer_calculatrice(self):
        while True:
            nombre1 = self.demander_nombre()
            nombre2 = self.demander_nombre()
            operation = self.demander_operation()

            resultat = self.calculer(nombre1, nombre2, operation)
            if resultat is not None:
                print("Résultat : {}".format(resultat))
                self.historique.append("{} {} {} = {}".format(nombre1, operation, nombre2, resultat))

            continuer = input("Voulez-vous effectuer un autre calcul ? (Oui/Non) : ")
            if continuer.lower() != 'oui':
                break

        afficher_historique = input("Voulez-vous afficher l'historique des opérations ? (Oui/Non) : ")
        if afficher_historique.lower() == 'oui':
            self.afficher_historique()

        effacer_historique = input("Voulez-vous effacer l'historique des opérations ? (Oui/Non) : ")
        if effacer_historique.lower() == 'oui':
            self.effacer_historique()


# Exemple d'utilisation
calculatrice = Calculatrice()
calculatrice.executer_calculatrice()
