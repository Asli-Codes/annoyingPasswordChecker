import streamlit as st

from passwordValidator import validatePassword


st.set_page_config(
    page_title="Try Again :)",
    page_icon="🔐",
    layout="centered"
)


st.title("🔐 Try Again :)")

st.write(
    "Dünyanın gereksiz derecede zor şifre kontrol sistemine hoş geldin."
)

st.caption(
    "Gerçek şifrelerini kullanma. Bu proje yalnızca eğitim ve eğlence amaçlıdır."
)

password = st.text_input(
    "Bir şifre oluştur:",
    type="password",
    placeholder="Buraya şifreni yaz..."
)


if st.button("Şifremi Kontrol Et", use_container_width=True):

    if not password:
        st.warning("Önce bir şifre yazman gerekiyor :)")

    else:
        isValid, message = validatePassword(password)

        if isValid:
            st.success(message)
            st.balloons()

        else:
            st.error(message)