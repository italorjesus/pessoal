import streamlit as st

def calcular_gordura(sexo, idade, abdominal, coxa, antebraco, panturrilha, braco_superior, nadegas):
    if sexo == "Feminino":
        if idade <= 26:
            return (abdominal * 0.5276) + (coxa * 0.8184) - (antebraco * 1.6967) - 14.6
        else:
            return (abdominal * 0.4682) + (coxa * 0.4886) - (panturrilha * 0.5703) - 13.4
    elif sexo == "Masculino":
        if idade <= 26:
            return (braco_superior * 1.4564) + (abdominal * 0.5157) - (antebraco * 2.1382) - 5.2
        else:
            return (nadegas * 0.4147) + (abdominal * 0.3558) - (antebraco * 1.1814) - 10.0
    else:
        return "Erro: Sexo inválido"

# Interface Streamlit
st.title("Calculadora de Gordura Corporal")

# Entradas do usuário
sexo = st.selectbox("Selecione o sexo", ["Masculino", "Feminino"])
idade = st.number_input("Idade", min_value=1, step=1)
abdominal = st.number_input("Circunferência Abdominal (cm)", min_value=0.0, format="%.2f")
coxa = st.number_input("Circunferência da Coxa (cm)", min_value=0.0, format="%.2f")
antebraco = st.number_input("Circunferência do Antebraço (cm)", min_value=0.0, format="%.2f")
panturrilha = st.number_input("Circunferência da Panturrilha (cm)", min_value=0.0, format="%.2f")
braco_superior = st.number_input("Circunferência do Braço Superior (cm)", min_value=0.0, format="%.2f")
nadegas = st.number_input("Circunferência do Quadril (cm)", min_value=0.0, format="%.2f")

# Botão para calcular
if st.button("Calcular % de Gordura Corporal"):
    resultado = calcular_gordura(sexo, idade, abdominal, coxa, antebraco, panturrilha, braco_superior, nadegas)
    try:
        st.success(f"Percentual estimado de gordura corporal: {resultado:.2f}%. Não esqueça de tirar um print desta página e enviar junto com suas fotos.")
    except Exception as e:
        st.error(f"Erro: {resultado}")
