import sqlite3 as sqlite
import os as os
from time import strftime
from quick_sort import *


def get_score(nbr_cases, nbr_bombes):  # Récupération des scores de parties similaire dans la base de données
    connector = sqlite.connect(os.path.join('ressources', 'sauvegarde_demineur.db'))  # Création du connecteur et du curseur
    cursor = connector.cursor()

    cursor.execute(f"SELECT * FROM parties_save WHERE nbr_cases = {nbr_cases} AND nbr_bombes = {nbr_bombes}")  # Recherche des parties similaires

    results = cursor.fetchall()  # Récupération du résultat
    quick_sort_scores(results, 0, len(results) - 1)  # Trie des résultats par leur temps indiqué dans la base de données
    connector.close()
    return results


def add_record(nbr_cases, nbr_bombes, play_time, name):  # Ajout d'une sauvegarde de la partie venant d'être joué dans la base de données
    date = strftime("%d/%m/%Y")  # Récupération de la date sous la forme jj/mm/aa
    connector = sqlite.connect(os.path.join('ressources', 'sauvegarde_demineur.db'))
    cursor = connector.cursor()

    # Ajout de la ligne de données dans la table de la base de données
    cursor.execute("INSERT INTO parties_save (nbr_cases, nbr_bombes, temps, nom, date) VALUES (?, ?, ?, ?, ?)", (nbr_cases, nbr_bombes, play_time, name, date))
    connector.commit()  # Sauvegarde des changements de la base de données
    connector.close()


def update_scores(messages_top5, nbr_cases, nbr_bombes):  # Fonction permettant de récupérer le nouveau top 5 après l'ajout d'une ligne dans la table
    scores = get_score(nbr_cases, nbr_bombes)  # Récupération des sauvegardes triés en fonction de leur temps
    longueur_scores = len(scores)
    for k in range(0, 5):
        if longueur_scores < k + 1:
            text = " - vide"
        else:
            text = f" - {scores[k][2]}sec par {scores[k][3]} le {scores[k][4]}"
        messages_top5[k].change_message(text)
