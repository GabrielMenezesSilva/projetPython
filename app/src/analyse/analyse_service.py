import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .analyse_reposiotory import AnalyseRepository

class AnalyseService:
    def __init__(self):
        self.repository = AnalyseRepository()

    def compute_analyse_per_course(self, cours_id: str) -> dict:
        get_evaluations: list = self.repository.get_all_evaluations_by_course(cours_id)
        get_evaluations[0].pop('_id')
        print(get_evaluations)

    def analyze_data(self):
        all_evaluations = self.repository.get_all_evaluations()
        return all_evaluations

    def evaluations_to_dataframe(self, evaluations):
        """Convertir les évaluations en DataFrame."""
        df = pd.DataFrame(evaluations)
        
        # Normaliser les colonnes imbriquées
        for col in ['Formationsuivie', 'professor']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else str(x))
        
        return df

    def plot_average_rating_per_formation(self, df):
        """Moyenne des évaluations par formation et professor."""
        if 'Formationsuivie' not in df.columns or 'professor' not in df.columns:
            print("Colonnes requises non trouvées!")
            return
        avg_ratings = df.groupby(['Formationsuivie', 'professor'])['rating'].mean().reset_index()
        plt.figure(figsize=(12, 8))
        sns.barplot(data=avg_ratings, x='Formationsuivie', y='rating', hue='professor')
        plt.title('Moyenne des évaluations par formation et professor')
        plt.xlabel('Formation')
        plt.ylabel('Moyenne des évaluations')
        plt.legend(title='professor', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_professor_formation_comparison(self, df, professor_name):
        """Comparaison des évaluations d'un professor spécifique par formation."""
        if 'Formationsuivie' not in df.columns or 'professor' not in df.columns:
            print("Colonnes requises non trouvées!")
            return
        professor_data = df[df['professor'] == professor_name]
        if professor_data.empty:
            print(f"Nenhum dado encontrado para o professor {professor_name}.")
            return
        avg_ratings = professor_data.groupby('Formationsuivie')['rating'].mean().reset_index()
        plt.figure(figsize=(8, 6))
        sns.barplot(data=avg_ratings, x='Formationsuivie', y='rating', palette='viridis')
        plt.title(f'Avaliações do Professor {professor_name} por Formação')
        plt.xlabel('Formação')
        plt.ylabel('Média de Avaliações')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Código principal
if __name__ == "__main__":
    # Criar instância da classe
    service = AnalyseService()

    # Inserir dados simulados
    service.repository.insert_sample_data(num_entries=100)

    # Realizar análise de dados
    all_evaluations = service.analyze_data()

    # Converter avaliações para DataFrame
    df_all = service.evaluations_to_dataframe(all_evaluations)

    # Verificar se o DataFrame não está vazio
    if not df_all.empty:
        # Gráfico 1: Média das Avaliações por Formação e Professor
        service.plot_average_rating_per_formation(df_all)
        
        # Gráfico 2: Comparação de um professor específico
        service.plot_professor_formation_comparison(df_all, "Antonio Pisanello")
    else:
        print("Aucune donnée à afficher.")


