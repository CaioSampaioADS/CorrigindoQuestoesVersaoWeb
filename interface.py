import streamlit as st
import streamlit.components.v1 as components
import MachineLearning

algoritmos = st.sidebar.selectbox(
    "Escolha qual algoritmo deseja usar",
    ('Redes neurais', 'KNN', 'SVM', 'Reg. logística')
)

if algoritmos == "KNN":
    qtdK = st.sidebar.number_input('Quantidades K',value=5)

pergunta = st.sidebar.selectbox(
    "Escolha a pergunta",
    ('O que é estatística', 'Principios do direito ambiental')
)

if algoritmos == 'Redes neurais' or algoritmos == 'Reg. logística':
    confiabilidade = st.sidebar.slider('Grau de confiabilidade', 50, 90, 50)


resposta = st.text_area('Sua resposta')
btn = st.button('corrigir')

if btn:
    x, y, respostasTotais = MachineLearning.preprocessamento(pergunta)

    if algoritmos == 'Redes neurais':
        corr = MachineLearning.redesNeurais(x, y, resposta, respostasTotais)
        if corr > confiabilidade / 100:
            st.write('Sua resposta está correta - algoritmo RNN')
        elif corr < (100 - confiabilidade) / 100:
            st.write('Sua resposta esta errada - algoritmo RNN')
        else:
            st.write('Não temos uma certeza tão grande diminua o grau de confiabilidade para obter um resultado - algoritmo RNN')


    if algoritmos == 'KNN':
        corr = MachineLearning.knn(x, y, resposta, respostasTotais, int(qtdK))
        if corr == 1:
            st.write('Sua resposta está correta - algoritimo KNN')
        elif corr == 0:
            st.write('Sua resposta esta errada - algoritimo KNN')

    if algoritmos == 'SVM':
        corr = MachineLearning.svm(x, y, resposta, respostasTotais)
        if corr == 1:
            st.write('Sua resposta está correta - SVM')
        elif corr == 0:
            st.write('Sua resposta esta errada - SVM')

    if algoritmos == 'Reg. logística':
        corr = MachineLearning.reglog(x, y, resposta, respostasTotais)
        if corr > confiabilidade / 100:
            st.write('Sua resposta está correta - REG. LOG')
        elif corr < (100 - confiabilidade) / 100:
            st.write('Sua resposta esta errada - REG. LOG')


