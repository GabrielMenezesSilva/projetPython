import json
import pandas as pd
from .dto.response import AnalyseResponse
from .analyse_reposiotory import AnalyseRepository
from .analyse import Analyse
from datetime import datetime
from ..cours.cours_service import CoursService

class AnalyseService:
    def __init__(self):
        # Inicializa o repositório responsável por interagir com as avaliações
        self.repository = AnalyseRepository()

    def compute_analyse_per_course(self, cours_id: str) -> dict:
        """Calcula a análise das avaliações para um curso específico."""
        # Recupera todas as avaliações associadas ao ID do curso
        evaluations = self.repository.get_all_evaluations_by_course(cours_id)

        # Debug: Exibe os dados das avaliações no console (remover em produção)
        print("Dados das avaliações por curso:", evaluations)

        # Converte a lista de avaliações em um DataFrame para manipulação
        df = self.evaluations_to_dataframe(evaluations)
        if df.empty:  # Caso não haja dados, retorna um objeto vazio formatado
            return [self.format_to_json(
                Analyse(
                    name=cours_id,
                    date=datetime.now().strftime("%Y-%m-%d"),
                    x=[],  # Lista vazia para eixo X
                    y=[],  # Lista vazia para eixo Y
                    chart_type=None  # Define nenhum gráfico devido à falta de dados
                )
            )]

        # Agrupa os dados por data de formação e calcula a média de rating
        grouped = df.groupby('Datesdelaformation')['rating'].mean().reset_index()

        # Retorna os dados da análise no formato JSON
        return [self.format_to_json(
            Analyse(
                name=cours_id,
                date=datetime.now().strftime("%Y-%m-%d"),
                x=grouped['Datesdelaformation'].astype(str).tolist(),  # Eixo X: Datas
                y=grouped['rating'].tolist(),  # Eixo Y: Médias de avaliação
                chart_type="line"  # Define o tipo de gráfico como linha
            )
        )]

    def calculate_rating(self, evaluation):
        """Calcula uma nota de 0 a 5 com base nas respostas qualitativas."""
        score = 0  # Armazena a soma dos pontos
        total_questions = 0  # Armazena o total de perguntas avaliadas

        # Campos qualitativos das avaliações
        qualitative_fields = [
            'JugerEnseignementNull', 'JugerEnseignementBasique', 'JugerEnseignementMoyen',
            'JugerEnseignementBon', 'JugerEnseignementExcellent', 'Methodedidactique',
            'CompetancesProfessionelles', 'ClarteDidactique', 'Disponibilite', 'Support',
            'Equipments', 'locaux', 'Ambiance', 'moduleTravailtresUtile', 'dossierProjetUtile',
            'jugezTresefficace'
        ]

        # Itera sobre os campos qualitativos para calcular a pontuação
        for field in qualitative_fields:
            value = evaluation.get(field)  # Obtém o valor do campo na avaliação
            print(f"Field: {field}, Value: {value}")  # Debug: Imprime campo e valor
            if value:
                # Atribui pontuação baseada no valor qualitativo
                if value == "excellent" or value is True:
                    score += 5
                elif value == "bon":
                    score += 4
                elif value == "moyen":
                    score += 3
                elif value == "mauvais" or value == "basique":
                    score += 2
                else:
                    score += 0
                total_questions += 1  # Incrementa o número de perguntas avaliadas

        # Verifica se nenhuma pergunta foi respondida
        if total_questions == 0:
            print("Nenhuma pergunta respondida. Retornando 0.")
            return 0

        # Calcula a média das avaliações
        rating = score / total_questions
        print(f"Score total: {score}, Total de perguntas: {total_questions}, Rating: {rating}")
        return rating

    def evaluations_to_dataframe(self, evaluations):
        """Converte avaliações em um DataFrame pandas para manipulação de dados."""
        df = pd.DataFrame(evaluations)  # Cria um DataFrame a partir das avaliações
        print("DataFrame das avaliações:", df)  # Debug: Exibe o DataFrame criado

        # Adiciona uma coluna 'rating' calculada para cada avaliação
        df['rating'] = df.apply(self.calculate_rating, axis=1)

        # Converte a coluna 'Datesdelaformation' para o tipo datetime, tratando erros
        if 'Datesdelaformation' in df.columns:
            df['Datesdelaformation'] = pd.to_datetime(df['Datesdelaformation'], errors='coerce')
        return df

    def analyse_all_courses_per_time(self) -> dict:
        """Realiza a análise para todos os cursos disponíveis no sistema."""
        cs = CoursService()  # Serviço para manipular dados dos cursos
        l_cours = cs.get_all_courses()  # Obtém todos os cursos
        courses_analysis = []  # Lista para armazenar análises de cada curso
        for cours in l_cours:
            # Adiciona as análises de cada curso à lista
            courses_analysis += self.compute_analyse_per_course(cours.id)
        return courses_analysis

    def format_to_json(self, analyse: Analyse) -> dict:
        """Formata o objeto de análise para o formato JSON utilizado pelo frontend."""
        return analyse.to_dict()  # Converte o objeto 'Analyse' para um dicionário
