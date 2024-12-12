import random

class DecoupageAdministratifJeu:
    def __init__(self):
        # Dictionnaire des régions de Côte d'Ivoire (région: chef-lieu)
        self.regions = {
            "Agneby-Tiassa": "Agboville",
            "Bélier": "Yamoussoukro",
            "Béré": "Mankono",
            "Boukani": "Téhini",
            "Cavally": "Guiglo",
            "District Autonome d'Abidjan": "Abidjan",
            "District Autonome de Yamoussoukro": "Yamoussoukro",
            "Dix-Huit Montagnes": "Man",
            "Fromager": "Gagnoa",
            "Gbêkê": "Bouaké",
            "Goh": "Gohitafla",
            "Grands-Ponts": "Dabou",
            "Hauts-Bassins": "Bamoro",
            "Indénié-Djuablin": "Abengourou",
            "Kabadougou": "Séguéla",
            "Lôh-Djiboua": "Divo",
            "Marahoué": "Zouénoula",
            "Moronou": "Bongouanou",
            "Nawa": "Soubré",
            "Poro": "Korhogo",
            "San-Pedro": "San-Pedro",
            "Sassandra": "Sassandra",
            "Sud-Bandama": "Dimbokro",
            "Sud-Comoé": "Aboisso",
            "Tchologo": "Ferkessedougou",
            "Tonkpi": "Man",
            "Worodougou": "Boundiali",
            "Zanzan": "Bondoukou"
        }
        
        self.scores = []
    
    def afficher_meilleurs_scores(self):
        print("\n🏆 TOP 5 MEILLEURS SCORES 🏆")
        scores_tries = sorted(self.scores, reverse=True)[:5]
        
        for i, score in enumerate(scores_tries, 1):
            print(f"{i}. {score}/10")
    
    def poser_question(self):
        # Sélectionner une région au hasard
        region = random.choice(list(self.regions.keys()))
        return region
    
    def jouer(self):
        print("\n🇨🇮 JEU DU DÉCOUPAGE ADMINISTRATIF DE CÔTE D'IVOIRE 🇨🇮")
        
        self.afficher_meilleurs_scores()
        
        questions_posees = set()
        score = 0
        
        for tour in range(1, 11):
            while True:
                region = self.poser_question()
                if region not in questions_posees:
                    questions_posees.add(region)
                    break
            
            print(f"\nQuestion {tour}/10 : Quel est le chef-lieu de la région {region} ?")
            reponse_utilisateur = input("Votre réponse : ").strip()
            
            if reponse_utilisateur.lower() == self.regions[region].lower():
                print("✅ Bonne réponse !")
                score += 1
            else:
                print(f"❌ Mauvaise réponse. Le chef-lieu de {region} est {self.regions[region]}.")
        
        print(f"\n🎉 Fin du jeu ! Votre score : {score}/10")
        self.scores.append(score)
    
    def commencer_jeu(self):
        while True:
            self.jouer()
            
            rejouer = input("\nVoulez-vous rejouer ? (O/N) : ").upper()
            if rejouer != 'O':
                break
        
        print("Merci d'avoir joué !")

# Lancement du jeu
jeu = DecoupageAdministratifJeu()
jeu.commencer_jeu()