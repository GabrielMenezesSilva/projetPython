# TODO Creer ici les fonctions qui recuperent les données des evaluations dans la base de données pour les analyses et pour la creation des graphiques et des statistiques. utiliser les librairies pandas,numpy, matplotlib, seaborn, wordcloud et autres pour les analyses et la creation des graphiques et des statistiques.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from app.config.mango_db import get_db

def get_evaluation_data():
    db = get_db()
    collection = db['evaluations']
    data = list(collection.find())
    return data

def analyze_data():
    data = get_evaluation_data()
    df = pd.DataFrame(data)
    
    # Exemplo de análise estatística
    print("Descrição estatística:")
    print(df.describe())
    
    # Exemplo de gráfico com matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(df['score'], bins=10, color='blue', edgecolor='black')
    plt.title('Distribuição dos Scores')
    plt.xlabel('Score')
    plt.ylabel('Frequência')
    plt.savefig('score_distribution.png')
    plt.close()
    
    # Exemplo de gráfico com seaborn
    plt.figure(figsize=(10, 6))
    plt.title('Boxplot de Scores por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Score')
    plt.savefig('boxplot_scores.png')
    plt.close()
    

if __name__ == "__main__":
    analyze_data()