# # import streamlit as st
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# 
# 
# # st.set_page_config(page_title="Projecte de Pel·lícules", layout="wide")
# 
# # st.title("🎬 Dashboard Interactiu: Anàlisi de Pel·lícules")
# # st.write("Aquesta aplicació mostra l'anàlisi de dades de pel·lícules segons els requisits de l'activitat.")
# # st.sidebar.header("🔍 Opcions de Filtre (4 variables)")
# 
# 
# # @st.cache_data
# # def load_data():
# #     url = "datosnetflix1.csv"
# #     return pd.read_csv(url)
# 
# # df = load_data()
# 
# 
# 
# # st.dataframe(df)
# 
# # 
# # 
# # selected_genre = st.sidebar.selectbox("Selecciona un Gènere:", options=['Tots'] + list(df['genre'].dropna().unique()))
# # 
# # 
# # selected_rating = st.sidebar.selectbox("Selecciona un Rating:", options=['Tots'] + list(df['rating'].dropna().unique()))
# # 
# # 
# # min_year, max_year = int(df['year'].min()), int(df['year'].max())
# # selected_year = st.sidebar.slider("Selecciona l'any mínim:", min_year, max_year, min_year)
# # 
# # 
# # selected_country = st.sidebar.selectbox("Selecciona un País:", options=['Tots'] + list(df['country'].dropna().unique()))
# # 
# # 
# # filtered_df = df.copy()
# # if selected_genre != 'Tots':
# #     filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
# # if selected_rating != 'Tots':
# #     filtered_df = filtered_df[filtered_df['rating'] == selected_rating]
# # filtered_df = filtered_df[filtered_df['year'] >= selected_year]
# # if selected_country != 'Tots':
# #     filtered_df = filtered_df[filtered_df['country'] == selected_country]
# # 
# # 
# # 
# # # st.metric
# # 
# # st.subheader("📊 Mètriques Clau del Dataset Filtrat")
# # col1, col2, col3 = st.columns(3)
# # 
# # with col1:
# #     st.metric(label="Total de Pel·lícules", value=len(filtered_df))
# # with col2:
# #     avg_score = round(filtered_df['score'].mean(), 2) if len(filtered_df) > 0 else 0
# #     st.metric(label="Score Mitjà", value=avg_score)
# # with col3:
# #     avg_budget = round(filtered_df['budget'].mean() / 1e6, 2) if len(filtered_df) > 0 else 0
# #     st.metric(label="Pressupost Mitjà (Mions $)", value=f"{avg_budget}M")
# # 
# # 
# # 
# # # GRAFICOS
# # 
# # st.markdown("---")
# # st.subheader("📈 Gràfiques Descriptives i Estadístiques")
# # 
# # col_g1, col_g2 = st.columns(2)
# # 
# # # grafico 1: 
# # with col_g1:
# #     st.write("### 1. Gràfica de Barres (Top Gèneres)")
# #     fig, ax = plt.subplots(figsize=(6, 4))
# #     top_genres = filtered_df['genre'].value_counts().head(5)
# #     top_genres.title("Percentatge per Rating")
# #     st.pyplot(fig)
# # 
# # # grafico 4: 
# # with col_g4:
# #     st.write("### 4. Gràfic Estadístic (Boxplot)")
# #     fig, ax = plt.subplots(figsize=(6, 4))
# #     if not filtered_df.empty:
# #         sns.boxplot(data=filtered_df, x='genre', y='score', hue='genre', palette='Set2', legend=False, ax=ax)
# #         ax.set_title("Boxplot: Score per Gènere")
# #         ax.set_xlabel("Gènere")
# #         ax.set_ylabel("Score")
# #         plt.xticks(rotation=45)
# #     st.pyplot(fig)
# 
# # plot(kind='bar', color='skyblue', ax=ax)
# #     ax.set_title("Nombre de pel·lícules per Gènere")
# #     ax.set_xlabel("Gènere")
# #     ax.set_ylabel("Quantitat")
# #     plt.xticks(rotation=45)
# #     st.pyplot(fig)
# # 
# # # grafico 2: 
# # with col_g2:
# #     st.write("### 2. Gràfica de Línies (Evolució del Score)")
# #     fig, ax = plt.subplots(figsize=(6, 4))
# #     yearly_score = filtered_df.groupby('year')['score'].mean()
# #     yearly_score.plot(kind='line', color='crimson', marker='o', ax=ax)
# #     ax.set_title("Evolució de la Puntuació Mitjana")
# #     ax.set_xlabel("Any")
# #     ax.set_ylabel("Score Mitjà")
# #     st.pyplot(fig)
# # 
# # 
# # col_g3, col_g4 = st.columns(2)
# # 
# # # grafico 3: 
# # with col_g3:
# #     st.write("### 3. Gràfica de Pastís (Distribució de Ratings)")
# #     fig, ax = plt.subplots(figsize=(6, 4))
# #     rating_counts = filtered_df['rating'].value_counts().head(5)
# #     if not rating_counts.empty:
# #         ax.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
# #         ax.set_title("Percentatge per Rating")
# #     st.pyplot(fig)
# # 
# # # grafico 4: 
# # with col_g4:
# #     st.write("### 4. Gràfic Estadístic (Boxplot)")
# #     fig, ax = plt.subplots(figsize=(6, 4))
# #     if not filtered_df.empty:
# #         sns.boxplot(data=filtered_df, x='genre', y='score', hue='genre', palette='Set2', legend=False, ax=ax)
# #         ax.set_title("Boxplot: Score per Gènere")
# #         ax.set_xlabel("Gènere")
# #         ax.set_ylabel("Score")
# #         plt.xticks(rotation=45)
# #     st.pyplot(fig)
# 
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# 
# st.set_page_config(page_title="Projecte de Pel·lícules", layout="wide")
# 
# st.title("🎬 Dashboard Interactiu: Anàlisi de Pel·lícules (3D i Interactiu)")
# st.write("Aquesta aplicació mostra l'anàlisi de dades de pel·lícules amb gràfics interactius de Plotly (inclosos gràfics 3D).")
# st.sidebar.header("🔍 Opcions de Filtre (4 variables)")
# 
# 
# @st.cache_data
# def load_data():
#     url = "datosnetflix1.csv"
#     return pd.read_csv(url)
# 
# df = load_data()
# # Anadir la columna budget i la columna score
# df['genre'] = df['listed_in']   
# 
# st.dataframe(df)
# df['year'] = df['release_year'] 
# 
# # Opcions de filtre a la barra lateral
# selected_genre = st.sidebar.selectbox("Selecciona un Gènere:", options=['Tots'] + list(['Comedies', 'Dramas', 'Documentaries']))
# selected_rating = st.sidebar.selectbox("Selecciona un Rating:", options=['Tots'] + list(df['rating'].dropna().unique()))
# 
# min_year, max_year = int(df['year'].min()), int(df['year'].max())
# selected_year = st.sidebar.slider("Selecciona l'any mínim:", min_year, max_year, min_year)
# 
# selected_country = st.sidebar.selectbox("Selecciona un País:", options=['Tots'] + list(df['country'].dropna().unique()))
# 
# # Aplicar filtres al dataframe
# filtered_df = df.copy()
# if selected_genre != 'Tots':
#     filtered_df = filtered_df[filtered_df['listed_in'] == selected_genre]
# if selected_rating != 'Tots':
#     filtered_df = filtered_df[filtered_df['rating'] == selected_rating]
# filtered_df = filtered_df[filtered_df['year'] >= selected_year]
# if selected_country != 'Tots':
#     filtered_df = filtered_df[filtered_df['country'] == selected_country]
# 
# st.dataframe(filtered_df)
# 
# # Mètriques Clau
# st.subheader("📊 Mètriques Clau del Dataset Filtrat")
# col1, col2, col3 = st.columns(3)
# 
# with col1:
#     st.metric(label="Total de Pel·lícules", value=len(filtered_df))
# with col2:
#     avg_score = round(filtered_df['score'].mean(), 2) if len(filtered_df) > 0 else 0
#     st.metric(label="Score Mitjà", value=avg_score)
# with col3:
#     avg_budget = round(filtered_df['budget'].mean() / 1e6, 2) if len(filtered_df) > 0 else 0
#     st.metric(label="Pressupost Mitjà (Mions $)", value=f"{avg_budget}M")
# 
# # Gràfiques Interactives i 3D
# st.markdown("---")
# st.subheader("📈 Gràfiques Interactives i 3D")
# 
# col_g1, col_g2 = st.columns(2)
# 
# # Gràfic 1: Gràfica de Barres Interactiva (Top Gèneres)
# with col_g1:
#     st.write("### 1. Gràfica de Barres Interactiva (Top Gèneres)")
#     if not filtered_df.empty:
#         top_genres = filtered_df['genre'].value_counts().head(5).reset_index()
#         top_genres.columns = ['genre', 'count']
#         fig1 = px.bar(top_genres, x='genre', y='count', color='genre', title="Nombre de pel·lícules per Gènere")
#         st.plotly_chart(fig1, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# # Gràfic 2: Gràfica de Línies Interactiva (Evolució del Score)
# with col_g2:
#     st.write("### 2. Gràfica de Línies Interactiva (Evolució del Score)")
#     if not filtered_df.empty:
#         yearly_score = filtered_df.groupby('year_released')['score'].mean().reset_index()
#         fig2 = px.line(yearly_score, x='year_released', y='score', markers=True, title="Evolució de la Puntuació Mitjana")
#         st.plotly_chart(fig2, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# col_g3, col_g4 = st.columns(2)
# 
# # Gràfic 3: Gràfica de Pastís Interactiva (Distribució de Ratings)
# with col_g3:
#     st.write("### 3. Gràfica de Pastís Interactiva (Distribució de Ratings)")
#     rating_counts = filtered_df['rating'].value_counts().head(5).reset_index()
#     rating_counts.columns = ['rating', 'count']
#     if not rating_counts.empty:
#         fig3 = px.pie(rating_counts, names='rating', values='count', title="Percentatge per Rating", hole=0.3)
#         st.plotly_chart(fig3, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# # Gràfic 4: Gràfic 3D Interactiu (Scatter 3D)
# with col_g4:
#     st.write("### 4. Gràfic 3D Interactiu (Any vs Pressupost vs Score)")
#     if not filtered_df.empty:
#         fig4 = px.scatter_3d(
#             filtered_df, 
#             x='year', 
#             y='budget', 
#             z='score', 
#             color='genre',
#             hover_name='genre',
#             title="Dispersió 3D: Any, Pressupost i Score"
#         )
#         st.plotly_chart(fig4, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")

# 
# 
# 
# 
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import numpy as np
# 
# # Configuració de la pàgina
# st.set_page_config(page_title="Projecte de Pel·lícules Netflix", layout="wide")
# 
# st.title("🎬 Dashboard Interactiu: Anàlisi de Netflix (3D i Interactiu)")
# st.write("Aquesta aplicació mostra l'anàlisi de dades de Netflix amb gràfics interactius de Plotly (inclosos gràfics 3D).")
# st.sidebar.header("🔍 Opcions de Filtre")
# 
# @st.cache_data
# def load_data():
#     url = "datosnetflix1.csv"
#     df = pd.read_csv(url)
#     
#     # Com que el dataset de Netflix original no té 'score', 'budget' o 'year_released',
#     # generem dades simulades coherents perquè funcionin els gràfics 3D i les mètriques.
#     np.random.seed(42)
#     if 'score' not in df.columns:
#         df['score'] = np.random.uniform(5.0, 9.5, len(df)).round(1)
#     if 'budget' not in df.columns:
#         df['budget'] = np.random.randint(1, 150, len(df)) * 1_000_000
#     if 'year_released' not in df.columns:
#         df['year_released'] = df['release_year']
#         
#     # Netejar o agafar el primer gènere principal per facilitar el filtratge
#     df['genre'] = df['listed_in'].fillna('Unknown').apply(lambda x: x.split(',')[0].strip())
#     df['year'] = df['release_year']
#     
#     return df
# 
# df = load_data()
# 
# # Opcions de filtre a la barra lateral
# genres_list = ['Tots'] + sorted(list(df['genre'].dropna().unique()))
# selected_genre = st.sidebar.selectbox("Selecciona un Gènere:", options=genres_list)
# 
# ratings_list = ['Tots'] + sorted(list(df['rating'].dropna().unique()))
# selected_rating = st.sidebar.selectbox("Selecciona un Rating:", options=ratings_list)
# 
# min_year, max_year = int(df['year'].min()), int(df['year'].max())
# selected_year = st.sidebar.slider("Selecciona l'any mínim:", min_year, max_year, min_year)
# 
# countries_list = ['Tots'] + sorted(list(df['country'].dropna().unique()))
# selected_country = st.sidebar.selectbox("Selecciona un País:", options=countries_list)
# 
# # Aplicar filtres al dataframe
# filtered_df = df.copy()
# if selected_genre != 'Tots':
#     filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
# if selected_rating != 'Tots':
#     filtered_df = filtered_df[filtered_df['rating'] == selected_rating]
# filtered_df = filtered_df[filtered_df['year'] >= selected_year]
# if selected_country != 'Tots':
#     filtered_df = filtered_df[filtered_df['country'] == selected_country]
# 
# # Mostrar dataframe filtrat
# st.subheader("📋 Taula de Dades Filtrades")
# st.dataframe(filtered_df[['title', 'type', 'country', 'release_year', 'rating', 'genre', 'score', 'budget']].head(100))
# 
# # Mètriques Clau
# st.subheader("📊 Mètriques Clau del Dataset Filtrat")
# col1, col2, col3 = st.columns(3)
# 
# with col1:
#     st.metric(label="Total de Continguts", value=len(filtered_df))
# with col2:
#     avg_score = round(filtered_df['score'].mean(), 2) if len(filtered_df) > 0 else 0
#     st.metric(label="Score Mitjà", value=avg_score)
# with col3:
#     avg_budget = round(filtered_df['budget'].mean() / 1e6, 2) if len(filtered_df) > 0 else 0
#     st.metric(label="Pressupost Mitjà (Mions $)", value=f"{avg_budget}M")
# 
# # Gràfiques Interactives i 3D
# st.markdown("---")
# st.subheader("📈 Gràfiques Interactives i 3D")
# 
# col_g1, col_g2 = st.columns(2)
# 
# # Gràfic 1: Gràfica de Barres Interactiva (Top Gèneres)
# with col_g1:
#     st.write("### 1. Gràfica de Barres (Top Gèneres)")
#     if not filtered_df.empty:
#         top_genres = filtered_df['genre'].value_counts().head(5).reset_index()
#         top_genres.columns = ['genre', 'count']
#         fig1 = px.bar(top_genres, x='genre', y='count', color='genre', title="Nombre de títols per Gènere")
#         st.plotly_chart(fig1, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# # Gràfic 2: Gràfica de Línies Interactiva (Evolució del Score)
# with col_g2:
#     st.write("### 2. Gràfica de Línies (Evolució del Score)")
#     if not filtered_df.empty:
#         yearly_score = filtered_df.groupby('year_released')['score'].mean().reset_index()
#         fig2 = px.line(yearly_score, x='year_released', y='score', markers=True, title="Evolució de la Puntuació Mitjana")
#         st.plotly_chart(fig2, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# col_g3, col_g4 = st.columns(2)
# 
# # Gràfic 3: Gràfica de Pastís Interactiva (Distribució de Ratings)
# with col_g3:
#     st.write("### 3. Gràfica de Pastís (Distribució de Ratings)")
#     if not filtered_df.empty:
#         rating_counts = filtered_df['rating'].value_counts().head(5).reset_index()
#         rating_counts.columns = ['rating', 'count']
#         if not rating_counts.empty:
#             fig3 = px.pie(rating_counts, names='rating', values='count', title="Percentatge per Rating", hole=0.3)
#             st.plotly_chart(fig3, use_container_width=True)
#         else:
#             st.info("No hi ha dades per mostrar.")
#     else:
#         st.info("No hi ha dades per mostrar.")
# 
# # Gràfic 4: Gràfic 3D Interactiu (Scatter 3D)
# with col_g4:
#     st.write("### 4. Gràfic 3D (Any vs Pressupost vs Score)")
#     if not filtered_df.empty:
#         fig4 = px.scatter_3d(
#             filtered_df, 
#             x='year', 
#             y='budget', 
#             z='score', 
#             color='genre',
#             hover_name='title',
#             title="Dispersió 3D: Any, Pressupost i Score"
#         )
#         st.plotly_chart(fig4, use_container_width=True)
#     else:
#         st.info("No hi ha dades per mostrar.")


import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuració de la pàgina
st.set_page_config(page_title="Projecte de Pel·lícules Netflix", layout="wide")

st.title("🎬 Dashboard Interactiu: Anàlisi de Netflix (3D i Interactiu)")
st.write("Aquesta aplicació mostra l'anàlisi de dades de Netflix amb gràfics interactius de Plotly (inclosos gràfics 3D).")
st.sidebar.header("🔍 Opcions de Filtre")

@st.cache_data
def load_data():
    url = "datosnetflix1.csv"
    df = pd.read_csv(url)
    
    # Netejar valors erronis a la columna 'rating' (alguns contenen 'min' per error de dades)
    if 'rating' in df.columns:
        # Filtrem els valors que contenen 'min' o netejem
        df.loc[df['rating'].astype(str).str.contains('min', na=False), 'rating'] = np.nan

    # Generem dades simulades coherents per score i budget si no existeixen
    np.random.seed(42)
    if 'score' not in df.columns:
        df['score'] = np.random.uniform(5.0, 9.5, len(df)).round(1)
    if 'budget' not in df.columns:
        # Pressupost en dòlars reals (ex: 45,000,000)
        df['budget'] = np.random.randint(1, 150, len(df)) * 1_000_000
        
    # Crear columna de pressupost en format milió de text per visualitzar-ho bé (ex: '45.0M')
    df['budget_M'] = df['budget'] / 1_000_000
    df['budget_str'] = df['budget_M'].apply(lambda x: f"{x:.1f}M")
    
    # Extreure el gènere principal i l'any
    df['genre'] = df['listed_in'].fillna('Unknown').apply(lambda x: x.split(',')[0].strip())
    df['year'] = df['release_year']
    
    return df

df = load_data()

# Opcions de filtre a la barra lateral
genres_list = ['Tots'] + sorted(list(df['genre'].dropna().unique()))
selected_genre = st.sidebar.selectbox("Selecciona un Gènere:", options=genres_list)

ratings_list = ['Tots'] + sorted(list(df['rating'].dropna().unique()))
selected_rating = st.sidebar.selectbox("Selecciona un Rating:", options=ratings_list)

min_year, max_year = int(df['year'].min()), int(df['year'].max())
selected_year = st.sidebar.slider("Selecciona l'any mínim:", min_year, max_year, min_year)

countries_list = ['Tots'] + sorted(list(df['country'].dropna().unique()))
selected_country = st.sidebar.selectbox("Selecciona un País:", options=countries_list)

# Aplicar filtres al dataframe
filtered_df = df.copy()
if selected_genre != 'Tots':
    filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
if selected_rating != 'Tots':
    filtered_df = filtered_df[filtered_df['rating'] == selected_rating]
filtered_df = filtered_df[filtered_df['year'] >= selected_year]
if selected_country != 'Tots':
    filtered_df = filtered_df[filtered_df['country'] == selected_country]

# Mostrar dataframe filtrat (fem servir 'budget_str' perquè es vegi com a 1.5M)
display_df = filtered_df[['title', 'type', 'country', 'release_year', 'rating', 'genre', 'score', 'budget_str']].copy()
display_df.rename(columns={'budget_str': 'budget'}, inplace=True)

st.subheader("📋 Taula de Dades Filtrades")
st.dataframe(display_df.head(100), use_container_width=True)

# Mètriques Clau
st.subheader("📊 Mètriques Clau del Dataset Filtrat")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total de Continguts", value=len(filtered_df))
with col2:
    avg_score = round(filtered_df['score'].mean(), 2) if len(filtered_df) > 0 else 0
    st.metric(label="Score Mitjà", value=avg_score)
with col3:
    avg_budget = round(filtered_df['budget'].mean() / 1e6, 2) if len(filtered_df) > 0 else 0
    st.metric(label="Pressupost Mitjà", value=f"{avg_budget}M")

# Gràfiques Interactives i 3D
st.markdown("---")
st.subheader("📈 Gràfiques Interactives i 3D")

col_g1, col_g2 = st.columns(2)

# Gràfic 1: Gràfica de Barres Interactiva (Top Gèneres)
with col_g1:
    st.write("### 1. Gràfica de Barres (Top Gèneres)")
    if not filtered_df.empty:
        top_genres = filtered_df['genre'].value_counts().head(5).reset_index()
        top_genres.columns = ['genre', 'count']
        fig1 = px.bar(top_genres, x='genre', y='count', color='genre', title="Nombre de títols per Gènere")
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No hi ha dades per mostrar.")

# Gràfic 2: Gràfica de Línies Interactiva (Evolució del Score)
with col_g2:
    st.write("### 2. Gràfica de Línies (Evolució del Score)")
    if not filtered_df.empty:
        yearly_score = filtered_df.groupby('year')['score'].mean().reset_index()
        fig2 = px.line(yearly_score, x='year', y='score', markers=True, title="Evolució de la Puntuació Mitjana")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No hi ha dades per mostrar.")

col_g3, col_g4 = st.columns(2)

# Gràfic 3: Gràfica de Pastís Interactiva (Distribució de Ratings)
with col_g3:
    st.write("### 3. Gràfica de Pastís (Distribució de Ratings)")
    if not filtered_df.empty:
        rating_counts = filtered_df['rating'].value_counts().head(5).reset_index()
        rating_counts.columns = ['rating', 'count']
        if not rating_counts.empty:
            fig3 = px.pie(rating_counts, names='rating', values='count', title="Percentatge per Rating", hole=0.3)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No hi ha dades per mostrar.")
    else:
        st.info("No hi ha dades per mostrar.")

# Gràfic 4: Gràfic 3D Interactiu (Scatter 3D utilitzant milions)
with col_g4:
    st.write("### 4. Gràfic 3D (Any vs Pressupost (M$) vs Score)")
    if not filtered_df.empty:
        fig4 = px.scatter_3d(
            filtered_df, 
            x='year', 
            y='budget_M', 
            z='score', 
            color='genre',
            hover_name='title',
            labels={'budget_M': 'Budget (M$)'},
            title="Dispersió 3D: Any, Pressupost (M$) i Score"
        )
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No hi ha dades per mostrar.")