# TODO Creer ici les fonctions qui recuperent les données des evaluations dans la base de données pour les analyses et pour la creation des graphiques et des statistiques. utiliser les librairies pandas,numpy, matplotlib, seaborn, wordcloud et autres pour les analyses et la creation des graphiques et des statistiques.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from app.models.config import get_db

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
    sns.boxplot(x='category', y='score', data=df)
    plt.title('Boxplot de Scores por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Score')
    plt.savefig('boxplot_scores.png')
    plt.close()
    
    # Exemplo de nuvem de palavras
    text = ' '.join(df['comments'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nuvem de Palavras dos Comentários')
    plt.savefig('wordcloud_comments.png')
    plt.close()

    # Criar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Análise de Avaliações", ln=True, align='C')
    
    pdf.image('score_distribution.png', x=10, y=30, w=180)
    pdf.add_page()
    pdf.image('boxplot_scores.png', x=10, y=30, w=180)
    pdf.add_page()
    pdf.image('wordcloud_comments.png', x=10, y=30, w=180)
    
    pdf.output("analysis_report.pdf")

def send_email():
    from_address = "mrgabrielmenezes@icloud.com"
    to_address = "mrgabrielmenezes@icloud.com"
    subject = "Relatório de Análise de Avaliações"
    body = "Segue em anexo o relatório de análise de avaliações."

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    from email.mime.text import MIMEText
    msg.attach(MIMEText(body, 'plain'))

    attachment = open("analysis_report.pdf", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= analysis_report.pdf")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, "Condessa2020")
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

if __name__ == "__main__":
    analyze_data()
    send_email()