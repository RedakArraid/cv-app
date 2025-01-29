import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="CV Khadara Diarrassouba", layout="wide", page_icon="📄")

# Charger ta photo
photo = Image.open("photo-khadara.jpeg")

# Convertir l'image en base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

photo_base64 = image_to_base64(photo)

# Style CSS pour améliorer l'apparence
st.markdown("""
<style>
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    .section-title {
        font-size: 24px !important;
        color: #1E90FF;
        border-bottom: 2px solid #1E90FF;
        padding-bottom: 5px;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        margin: 5px;
    }
    /* Style pour le bouton actif */
    .stButton>button.active {
        background-color: #FF0000; /* Rouge */
    }
    /* Style pour la photo avec des bords arrondis */
    .rounded-img {
        border-radius: 50%;
        border: 3px solid #1E90FF;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 150px;
        height: 150px;
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de l'état de la section
if "section" not in st.session_state:
    st.session_state.section = "Accueil"

# Fonction pour définir la section
def set_section(section_name):
    st.session_state.section = section_name

# Afficher la bio et les boutons en permanence
def display_bio_and_buttons():
    # Utiliser des colonnes pour placer la photo à droite
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Khadara Diarrassouba")
        st.markdown('<p class="big-font">Bientôt diplômé en Big Data et IA, je recherche une opportunité en Data Analyst.</p>', unsafe_allow_html=True)
        st.write("Disponible dès septembre, motivé à valoriser vos données.")
    with col2:
        # Afficher la photo avec des bords arrondis en utilisant du HTML/CSS
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="data:image/jpeg;base64,{photo_base64}" class="rounded-img">'
            f'</div>',
            unsafe_allow_html=True
        )

    # Boutons de navigation
    st.markdown("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        # Appliquer le style "active" si la section est "Coordonnées"
        button_style = "active" if st.session_state.section == "Coordonnées" else ""
        if st.button("Coordonnées", key="coordonnees"):
            set_section("Coordonnées")
    with col2:
        button_style = "active" if st.session_state.section == "Compétences" else ""
        if st.button("Compétences", key="competences"):
            set_section("Compétences")
    with col3:
        button_style = "active" if st.session_state.section == "Expériences" else ""
        if st.button("Expériences", key="experiences"):
            set_section("Expériences")
    with col4:
        button_style = "active" if st.session_state.section == "Formations" else ""
        if st.button("Formations", key="formations"):
            set_section("Formations")
    with col5:
        button_style = "active" if st.session_state.section == "Contact" else ""
        if st.button("Contact", key="contact"):
            set_section("Contact")
    with col6:
        button_style = "active" if st.session_state.section == "Télécharger" else ""
        if st.button("Télécharger", key="telecharger"):
            set_section("Télécharger")

# Afficher la bio et les boutons en permanence
display_bio_and_buttons()

# Afficher la section sélectionnée
if st.session_state.section == "Coordonnées":
    st.markdown('<p class="section-title">📌 Coordonnées</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("📞 **Téléphone:** 0766848029")
        st.write("📧 **Email:** kader.diarrassouba9@gmail.com")
    with col2:
        st.write("📍 **Localisation:** Île-de-France")
        st.write("[🔗 LinkedIn](https://www.linkedin.com/in/khadara-diarrassouba/)")
        st.write("[🐱 GitHub](https://github.com/RedakArraid)")

elif st.session_state.section == "Compétences":
    st.markdown('<p class="section-title">💻 Compétences</p>', unsafe_allow_html=True)
    
    # Hard Skills
    st.subheader("Hard Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Bases de données et data viz:**")
        st.write("- SQL")
        st.write("- Python / Excel VBA")
        st.write("- Power BI / Tableau")
    with col2:
        st.write("**Data Science/Data Analyst:**")
        st.write("- Python / Matlab")
        st.write("- R")
        st.write("- Deep Learning")
    with col3:
        st.write("**Cloud et ERP:**")
        st.write("- MS Learn")
        st.write("- ML Studio")
        st.write("- SAP")

    # Soft Skills
    st.subheader("Soft Skills")
    st.write("- Curiosité et autonomie")
    st.write("- Créativité et communication")
    st.write("- Dynamisme et esprit d'équipe")

    # Langues
    st.subheader("🌍 Langues")
    st.write("- Anglais : B2")
    st.write("- Espagnol : Niveau lycée")

elif st.session_state.section == "Expériences":
    st.markdown('<p class="section-title">📂 Expériences</p>', unsafe_allow_html=True)
    
    # Alternance
    st.subheader("Alternant Data & Business Analyst")
    st.write("**Zumtobel Lighting Group France** | Août 2023 - Aujourd'hui")
    st.write("- Création, gestion et automatisation de rapports et analyses")
    st.write("- Analyse des offres émises par la force de vente")
    st.write("- Analyse des données clients")
    st.write("- Création des premiers rapports Power BI")

    # Projets
    st.subheader("Projets")
    st.write("**Solution basée sur l'IA pour résumer des articles de presse**")
    st.write("- Gestion de l'outil de communication NOTION")
    st.write("- Consommation d'API")
    st.write("- Méthode de travail agile")

    st.write("**Détection d'anomalies sur des images de radiographie**")
    st.write("Novembre 2022 - Janvier 2023")
    st.write("- Conception d'un réseau de neurones CNN : Python (TensorFlow)")
    st.write("- Création d'un site web pour analyser les images radios (HTML/CSS/JS)")

elif st.session_state.section == "Formations":
    st.markdown('<p class="section-title">🎓 Formations</p>', unsafe_allow_html=True)
    
    st.write("**École Centrale d'Électronique de Paris (ECE)**")
    st.write("Deuxième et troisième années du cycle ingénieur en informatique | Septembre 2023 - Juillet 2025")

    st.write("**EFREI Paris / Mobilité ACH en Pologne**")
    st.write("Première année de cycle ingénieur informatique | Août 2022 - Juillet 2023")

    st.write("**Institut National Polytechnique Félix Houphouët Boigny (INPHB)**")
    st.write("Ingénieur en exploitation et traitement des eaux | 2017-2022")

elif st.session_state.section == "Contact":
    st.markdown('<p class="section-title">📧 Contact</p>', unsafe_allow_html=True)
    
    # Formulaire de contact
    with st.form("contact_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.success(f"Merci {name}, votre message a été envoyé !")

elif st.session_state.section == "Télécharger":
    st.markdown('<p class="section-title">📄 Télécharger mon CV en PDF</p>', unsafe_allow_html=True)
    with open("CvKhadara.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Télécharger",
        data=PDFbyte,
        file_name="CV_Khadara_Diarrassouba.pdf",
        mime="application/pdf",
    )
