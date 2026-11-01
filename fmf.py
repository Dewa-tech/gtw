import streamlit as st

st.title("=== Sign in ===")

nama = st.text_input("nama lengkap:").strip().lower()
sandi = st.text_input("angka sandi :", type="password")

if st.button("Masuk"):
    if nama == "made andra suwangga suputra" and sandi == "1560":
        st.markdown("**===Andraaa! kau sahabat terbaikku! jangan sampe lost kontak bro===**")
    elif nama == "i putu aray oktara sudjana" and sandi == "1290":
        st.markdown("**===Baek, ga sopan, pinter. itulah Aray===**")
    elif nama == "gede rezwa sara prismawan" and sandi == "1478":
        st.markdown("**===baek,penolong,overthingkinger,kadang egois. Rezwa, jangan kebanyakan mikirin hal yang udah lewat yaa===**")
    else:
        st.error("beneran orang kepilih nich??")