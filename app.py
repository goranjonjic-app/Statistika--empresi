
import streamlit as st
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Nalozi Dashboard", layout="wide")

def main():
    st.title("📊 Sustav za Analizu Naloga")
    if os.path.exists('ekstrakcija_podataka.json'):
        with open('ekstrakcija_podataka.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        st.write("Pregled baze podataka:")
        st.dataframe(df)
        
        st.subheader("Statistika radnika")
        counts = df['radnici'].explode().value_counts()
        st.bar_chart(counts)
    else:
        st.info("Učitajte 'ekstrakcija_podataka.json' u isti GitHub repozitorij.")

if __name__ == '__main__':
    main()
