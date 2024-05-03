import pandas as pd
import plotly.express as px

# MAIN PAGE 

def grafico_top10(df):
    top10 = df.query('year == 2022').sort_values(by = 'inbounds_tourists', ascending = False).head(20)

    fig = px.bar(x = top10['country'], y = top10['inbounds_tourists'], barmode = 'stack', color_discrete_sequence=['skyblue'])
    fig.update_layout(yaxis_title='Inbounds', xaxis_title='Country', height = 400)
    return fig

def grafico_feature_importance(weights):
    w_graph = weights.query('use').sort_values(by = 'weight', ascending = False)
    fig = px.bar(x = w_graph['variable'], y = w_graph['weight'], barmode = 'stack', color_discrete_sequence=['blue'])
    fig.update_layout(yaxis_title=f'Weight', xaxis_title = 'Variables', width = 800, height = 400)
    # fig.update_traces(marker=dict(line=dict(width=2))) 
    return fig


def obtener_ranking(df_24, weights):
    salida = df_24.melt('Country')
    salida = salida.merge(weights, on = 'variable')
    salida['Score'] = salida.value * salida.weight * salida.use.astype(int)
    ranking = salida.groupby('Country').sum()[['Score']].reset_index()
    ranking = ranking.sort_values(by = 'Score', ascending= False)
    # ranking['rank'] = range(1, len(ranking) + 1)
    ranking['Position'] = ranking['Score'].rank(method='min', ascending=False).astype(int)
    return ranking


# PAGE COUNTRIES

def grafico_turismo_pais(df, country):
    grafico = df.query(f'country == "{country}"')[['year', 'inbounds_tourists']]
    fig = px.bar(x = grafico['year'], y = grafico['inbounds_tourists'], barmode = 'stack', color_discrete_sequence=['tomato'])
    fig.update_layout(yaxis_title=f'Inbounds {country}')
    return fig
