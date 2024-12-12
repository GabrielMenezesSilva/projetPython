import json
import pandas as pd
from .dto.response import AnalyseResponse
from .analyse_reposiotory import AnalyseRepository
from .analyse import Analyse
from datetime import datetime

class AnalyseService:
    def __init__(self):
        self.repository = AnalyseRepository()

    def compute_analyse_per_course(self, cours_id: str) -> dict:
        # Recupera todas as avaliações para um curso específico
        evaluations = self.repository.get_all_evaluations_by_course(cours_id)

        # Exibe os dados brutos para referência (pode ser removido em produção)
        print("Dados das avaliações por curso:", evaluations)

        # Converter para DataFrame e calcular a média
        df = self.evaluations_to_dataframe(evaluations)
        if df.empty:
            return self.format_to_json(
                Analyse(
                    name="Sem dados para análise",
                    date=datetime.now().strftime("%Y-%m-%d"),
                    x=[],
                    y=[]
                ),
                "bar"  # Tipo de gráfico padrão no caso de ausência de dados
            )

        grouped = df.groupby('Datesdelaformation')['rating'].mean().reset_index()

        # Retornar os dados formatados
        return self.format_to_json(
            Analyse(
                name=cours_id,
                date=datetime.now().strftime("%Y-%m-%d"),
                x=grouped['Datesdelaformation'].astype(str).tolist(),
                y=grouped['rating'].tolist(),
                chart_type="line"  # Gráfico de linha como padrão para análise de cursos
            ) # Gráfico de linha como padrão para análise de cursos
        )

    def compute_analyse_per_professor(self, professor_id: str) -> dict:
        # Recupera todas as avaliações para um professor específico
        evaluations = self.repository.get_all_evaluations_by_professor(professor_id)

        # Exibe os dados brutos para referência
        print("Dados das avaliações por professor:", evaluations)

        # Converter para DataFrame e calcular a média
        df = self.evaluations_to_dataframe(evaluations)
        if df.empty:
            return self.format_to_json(
                Analyse(
                    name="Sem dados para análise",
                    date=datetime.now().strftime("%Y-%m-%d"),
                    x=[],
                    y=[]
                ),
                "bar"  # Tipo de gráfico padrão no caso de ausência de dados
            )

        grouped = df.groupby('Formationsuivie')['rating'].mean().reset_index()

        # Retornar os dados formatados
        return self.format_to_json(
            Analyse(
                name="Análise por Professor",
                date=datetime.now().strftime("%Y-%m-%d"),
                x=grouped['Formationsuivie'].tolist(),
                y=grouped['rating'].tolist()
            ),
            "line"  # Gráfico de barras como padrão para análise de professores
        )

    def analyze_data(self):
        # Recupera todas as avaliações da base de dados
        all_evaluations = self.repository.get_all_evaluations()
        print("Dados brutos de todas as avaliações:", all_evaluations)
        return all_evaluations

    def evaluations_to_dataframe(self, evaluations):
        """Converte avaliações em um DataFrame pandas."""
        df = pd.DataFrame(evaluations)
        print("DataFrame das avaliações:", df)

        # Normalizar campos de data e rating se existirem
        if 'Datesdelaformation' in df.columns:
            df['Datesdelaformation'] = pd.to_datetime(df['Datesdelaformation'], errors='coerce')
        if 'rating' in df.columns:
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
        else:
            df['rating'] = 0 # TODO: compute the rating automatically given the form

        return df

    def format_to_json(self, analyse: Analyse) -> dict:
        """Formata o objeto de análise para JSON no padrão esperado pelo frontend."""
        return analyse.to_dict()
        # return AnalyseResponse.dump(analyse, chart_type)
        # response = AnalyseResponse(
        #     x=analyse.x,
        #     y=analyse.y,
        #     type_chart=chart_type  # Define o tipo de gráfico dinamicamente
        # )
        # return response.dict()