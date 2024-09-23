
import pandas as pd
from pyspark.sql import SparkSession
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Iniciar uma sessão do Spark
spark = SparkSession.builder.appName("RecommenderSystem").getOrCreate()

# Função para carregar e processar dados
def load_data():
    users_df = pd.read_csv('data/users.csv')
    courses_df = pd.read_csv('data/courses.csv')
    
    # Convertendo para Spark DataFrame
    users_spark_df = spark.createDataFrame(users_df)
    courses_spark_df = spark.createDataFrame(courses_df)
    
    return users_df, courses_df, users_spark_df, courses_spark_df

# Função para recomendar cursos
def recommend_courses(user_id, users_df, courses_df):
    user = users_df[users_df['user_id'] == user_id]
    
    if user.empty:
        return f"Usuário com ID {user_id} não encontrado."
    
    user_experience = user['experience_level'].values[0]
    
    # Filtrar cursos adequados para o nível de experiência do usuário
    recommended_courses = courses_df[courses_df['difficulty'] == user_experience]
    
    if recommended_courses.empty:
        return "Nenhum curso recomendado para esse perfil."
    
    return recommended_courses[['course_name']].to_string(index=False)

# Função principal para execução
def main():
    # Carregar dados
    users_df, courses_df, users_spark_df, courses_spark_df = load_data()
    
    print("Plataforma de Recomendação de Cursos")
    print("===================================")
    
    user_id = int(input("Digite o ID do usuário: "))
    
    # Recomendar cursos
    recommendations = recommend_courses(user_id, users_df, courses_df)
    
    print(f"\nRecomendações para o usuário {user_id}:\n{recommendations}")

if __name__ == "__main__":
    main()
