import streamlit as st

# Título da página
st.title("Calculadora de Fórmula")

# Inputs dos dados
sexo = st.selectbox("Sexo", ["Feminino", "Masculino"])
idade = st.number_input("Idade", min_value=0, max_value=150, value=30)
D10 = st.number_input("Valor D10", min_value=0.0, value=78.0)
D11 = st.number_input("Valor D11", min_value=0.0, value=48.0)
D13 = st.number_input("Valor D13", min_value=0.0, value=34.0)

# Lógica da fórmula
if sexo == "Feminino" and idade > 26:
    resultado = (D10 * 0.4682) + (D11 * 0.4886) - (D13 * 0.5703) - 18.4
elif sexo == "Masculino" and idade > 26:
    resultado = (D10 * 0.4147) + (D11 * 0.3558) - (D13 * 1.1814) - 15
elif sexo == "Feminino" and idade <= 26:
    resultado = (D10 * 0.5276) + (D11 * 0.8184) - (D13 * 1.6967) - 19.6
elif sexo == "Masculino" and idade <= 26:
    resultado = (D10 * 1.4564) + (D11 * 0.5157) - (D13 * 2.1382) - 10.2
else:
    resultado = "Dados inválidos"

# Exibir o resultado
st.write("Resultado:", resultado / 100)
