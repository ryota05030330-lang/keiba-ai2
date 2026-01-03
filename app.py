import streamlit as st
import pandas as pd

st.title("競馬AI｜回収率重視（テンプレ）")

race_name = st.text_input("レース名を入力")

if st.button("予想する"):
    st.info("※ テンプレ動作中")
    st.write("買い馬はまだありません（次ステップで自動化）")
