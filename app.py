import streamlit as st

# --- Configuration de la page
st.set_page_config(
    page_title="Voyage au Japon 🎌",
    page_icon="🎎",
    layout="wide"
)

# --- CSS Personnalisé
st.markdown(
    """
    <style>
    body {
        background-image: url('https://i.imgur.com/U9KcuRz.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
    }
    h1, h2, h3, p {
        color: #4B2E2E;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Contenu
st.title("🎂 Joyeux anniversaire !")
st.subheader("🇯🇵 Bienvenue sur ton site spécial pour ton voyage au Japon ✈️🌸")

st.markdown("---")

# Planning Tokyo
st.header("🗼 Planning Tokyo (Semaine 1)")
st.write("""
- **Jour 1** : Arrivée et installation
- **Jour 2** : Shibuya & Harajuku
- **Jour 3** : Asakusa & Skytree
- **Jour 4** : Shinjuku et Golden Gai
- **Jour 5** : Excursion Kamakura
- **Jour 6** : Akihabara & Ginza
- **Jour 7** : Libre
""")

st.markdown("---")

# Planning Kyoto
st.header("⛩ Planning Kyoto (Semaine 2)")
st.write("""
- **Jour 8** : Arashiyama (forêt de bambous)
- **Jour 9** : Fushimi Inari (portails rouges)
- **Jour 10** : Kiyomizu-dera & Gion
- **Jour 11** : Philosopher’s Path
- **Jour 12** : Château de Nijō
- **Jour 13** : Nishiki Market
- **Jour 14** : Détente & shopping
""")

st.markdown("---")

# Message final
st.markdown("<h2 style='text-align: center;'>🎉 Bon voyage et encore joyeux anniversaire 🎂🎈</h2>", unsafe_allow_html=True)



