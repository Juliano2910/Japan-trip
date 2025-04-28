import streamlit as st

# --- Configuration de la page
st.set_page_config(
    page_title="Voyage au Japon 🎌",
    page_icon="🎎",
    layout="wide"
)

# --- Style CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sawarabi+Mincho&display=swap');

    body {
        background-image: url('https://i.imgur.com/AVbM8iK.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Sawarabi Mincho', sans-serif;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
    }
    h1, h2 {
        color: #A52A2A;
    }
    </style>
""", unsafe_allow_html=True)

# --- Contenu
st.title("🎂 Joyeux anniversaire !")
st.write("""
🇯🇵 Bienvenue sur ton site spécial pour ton voyage au Japon ✈️🌸  
Ce projet a été créé avec amour par ta famille et tes amis pour t'accompagner dans cette aventure inoubliable !
""")

st.markdown("---")

st.header("🗼 Planning Tokyo (Semaine 1)")
st.image("https://i.imgur.com/nWvOogW.jpg", caption="Bienvenue à Tokyo", use_column_width=True)

st.markdown("""
- **Jour 1** : Arrivée et installation dans ton hôtel traditionnel.
- **Jour 2** : Découverte de **Shibuya** et ses ruelles animées.
- **Jour 3** : Balade au temple **Asakusa** et montée de la **Skytree**.
- **Jour 4** : Soirée dans **Golden Gai**, quartier emblématique.
- **Jour 5** : Excursion à **Kamakura**, au bord de l'océan.
- **Jour 6** : Shopping geek à **Akihabara** et luxe à **Ginza**.
- **Jour 7** : Journée libre pour explorer selon tes envies.
""")

st.markdown("---")

st.header("⛩️ Planning Kyoto (Semaine 2)")
st.image("https://i.imgur.com/8DOnwbf.jpg", caption="Sérénité à Kyoto", use_column_width=True)

st.markdown("""
- **Jour 8** : Balade à travers la **forêt de bambous** d'Arashiyama.
- **Jour 9** : Visite des célèbres **torii rouges** de Fushimi Inari.
- **Jour 10** : Exploration du quartier **Gion** et du temple Kiyomizu-dera.
- **Jour 11** : Visite historique du **Château de Nijō**.
- **Jour 12** : Promenade méditative sur le **Philosopher’s Path**.
- **Jour 13** : Journée libre pour vivre ta propre aventure.
- **Jour 14** : Retour et souvenirs plein le cœur.
""")

st.markdown("---")

st.write("🌸 Que ce voyage soit aussi inoubliable que les liens qui nous unissent !")





