import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Voyage au Japon 🎌", page_icon="🎎", layout="wide")

# --- Style Sakura ---
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffe4e1 0%, #ffffff 100%);
}
h1, h2, h3, h4 {
    color: #d6336c;
    font-family: 'Arial Rounded MT Bold', sans-serif;
}
.stButton>button {
    background-color: #ffb7c5;
    color: black;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-weight: bold;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Titre et message d'accueil ---
st.title("🎂 Joyeux anniversaire !")
st.subheader("Bienvenue sur ton site spécial pour ton voyage au Japon 🇯🇵✈️ !")
st.divider()

# --- Planning Tokyo ---
st.header("🗼 Semaine 1 : Tokyo")
planning_tokyo = pd.DataFrame({
    "Jour": [f"Jour {i}" for i in range(1, 8)],
    "Quartier/Activité": [
        "Asakusa (Temple Senso-ji, Tokyo Skytree)",
        "Ueno (Parc et Gare)",
        "Tsukiji (Petit-déjeuner marché) - Resto Ichiba Dori & Tempura Kurokawa",
        "Ginza (Quartier luxe) - Gyoza chez Chao Chao, balade vers Yurakucho",
        "Akihabara (Quartier manga et tech)",
        "Ochanomizu (Sport, musique) & Roppongi (Sortie fête)",
        "Shinjuku, Harajuku (Takeshita street), Omotesando, Shibuya (Nintendo/Pokémon store)"
    ]
})
st.dataframe(planning_tokyo, use_container_width=True)

st.divider()

# --- Planning Kyoto ---
st.header("⛩️ Semaine 2 : Kyoto")
planning_kyoto = pd.DataFrame({
    "Jour": [f"Jour {i}" for i in range(8, 15)],
    "Quartier/Activité": [
        "Arashiyama (Bambouseraie + Singes)",
        "Fushimi Inari (Torii rouges célèbres)",
        "Kiyomizu-dera, Gion (quartier traditionnel)",
        "Philosopher's Path (balade zen)",
        "Château de Nijō",
        "Nishiki Market (marché local)",
        "Libre (shopping, détente)"
    ]
})
st.dataframe(planning_kyoto, use_container_width=True)

st.divider()

# --- Galerie Photo (bientôt à compléter) ---
st.header("📸 Galerie photos de ton voyage")
st.write("*(à venir : magnifiques souvenirs à ajouter ici !)*")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/5/50/Cherry_blossoms_in_Japan.jpg",
    caption="Cerisiers en fleurs au Japon 🌸",
    use_column_width=True
)

st.divider()

# --- Lien Cagnotte ---
st.header("🎁 Ton cadeau collectif")
if st.button("Voir la cagnotte 🎁"):
    st.link_button("👉 Clique ici pour accéder à la cagnotte", url="https://www.example.com/ta-cagnotte")

st.divider()

# --- Message final ---
st.markdown("<h2 style='text-align: center;'>Bon voyage et encore joyeux anniversaire 🎂🎎🎌 !</h2>", unsafe_allow_html=True)


