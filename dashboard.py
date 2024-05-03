import streamlit as st
import pandas as pd
import functions

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

@st.cache_data
def read_inbounds():
    return pd.read_excel('data/processed/un_inbounds_total.xlsx')
@st.cache_data
def read_df():
    return pd.read_csv('data/processed/final_df.csv')
@st.cache_data
def read_weigths():
    return pd.read_csv('data/processed/default_weights.csv').drop('Unnamed: 0', axis = 1)

inbounds = read_inbounds()
weights = read_weigths()
# weights['use'] = True
df = read_df()


st.title('Welcome to the Country Ranking Platform!')
st.image('fotos/foto mapa.png')

# st.header('Current tourism overview')
# st.plotly_chart(functions.grafico_top10(inbounds), use_container_width=True)

# with st.container():
    # st.header('Current tourism overview')
    # col1, col2 = st.columns(2)

    # with col1:
        # st.image('fotos/foto mapa.png')

    # with col2:
        # grafico1 = functions.grafico_top10(inbounds)
        # st.plotly_chart(grafico1, use_container_width=True)


# ranking explanation
with st.container():
    st.header('How does the ranking work?')
    st.write('Our ranking sysrem takes into account user criteria and rates countries accordingly. To use the tool, start by selecting the features that you would like to include in the analysis.') 
    st.write('Once the criteria have been chosen, feel free to adjust the weights of each parameter to reflect their importance. The weights will be used by our platform to assign a score to every country.')
    st.write('Each calculated country score is meaningless on its own, it needs to be compared against the others to get the best image of the current state of world tourism :)')
        

# features and weights
with st.container():

    st.subheader('Ranking Features')
    col1, col2 = st.columns(2)
    with col1:
        weights = st.data_editor(weights, use_container_width = True, hide_index= True)
        final_ranking = functions.obtener_ranking(df, weights)

    with col2:
        grafico_weights = functions.grafico_feature_importance(weights)
        st.plotly_chart(grafico_weights, use_container_width=True)


# top 5 
with st.container():
    st.subheader('Country ranking')
    final_ranking = functions.obtener_ranking(df, weights)
    ranking_paises = final_ranking['Country'].head(5)

    columns = st.columns(5)
    n = 0
    for col, pais in zip(columns, ranking_paises):
        n += 1
        with col.container(border = True):
            texto = str(str(n) + ' ' + pais)
            st.text(texto)


# ranking
with st.container():
    st.subheader('Complete Ranking')
    st.dataframe(final_ranking, use_container_width = True, hide_index=True)
