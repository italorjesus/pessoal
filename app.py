import streamlit as st
import math

st.title("Calculadora de Percentual de Gordura Corporal")

st.markdown("""
Esta aplicação calcula o percentual de gordura com base na fórmula da Marinha dos EUA.  
**Para homens:**  
&nbsp;&nbsp;&nbsp;&nbsp;BF% = 495 / (1.0324 - 0.19077 * log10(cintura - pescoço) + 0.15456 * log10(altura)) - 450  

**Para mulheres:**  
&nbsp;&nbsp;&nbsp;&nbsp;BF% = 495 / (1.29579 - 0.35004 * log10(cintura + quadril - pescoço) + 0.22100 * log10(altura)) - 450  

> *Observação:* Certifique-se de informar as medidas em centímetros e que os valores informados façam sentido (por exemplo, cintura > pescoço para homens e cintura + quadril > pescoço para mulheres).
""")

# Entrada de dados
gender = st.selectbox("Selecione o sexo:", ["Masculino", "Feminino"])
height = st.number_input("Altura (cm):", min_value=0.0, format="%.2f")
neck = st.number_input("Circunferência do pescoço (cm):", min_value=0.0, format="%.2f")
waist = st.number_input("Circunferência da cintura (cm):", min_value=0.0, format="%.2f")

if gender == "Feminino":
    hip = st.number_input("Circunferência do quadril (cm):", min_value=0.0, format="%.2f")

# Botão para calcular
if st.button("Calcular"):
    if height <= 0:
        st.error("A altura deve ser maior que zero.")
    else:
        try:
            if gender == "Masculino":
                # Verifica se cintura - pescoço é positivo
                if waist <= neck:
                    st.error("Para homens, a medida da cintura deve ser maior que a do pescoço.")
                else:
                    resultado = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
                    st.success(f"Percentual de Gordura: {resultado:.2f}%")
            else:
                # Verifica se (cintura + quadril) - pescoço é positivo
                if (waist + hip) <= neck:
                    st.error("Para mulheres, a soma da cintura e quadril deve ser maior que a do pescoço.")
                else:
                    resultado = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450
                    st.success(f"Percentual de Gordura: {resultado:.2f}%")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
