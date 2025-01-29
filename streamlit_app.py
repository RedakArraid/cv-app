import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Khadara Diarrassouba", layout="wide", page_icon="📄")

# Sidebar pour la navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Choisir une section", ["Accueil", "Compétences", "Expériences", "Formations", "Contact"])

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
</style>
""", unsafe_allow_html=True)

# Section Accueil
if section == "Accueil":
    st.title("Khadara Diarrassouba")
    st.markdown('<p class="big-font">Bientôt diplômé en Big Data et IA, je recherche une opportunité en Data Analyst.</p>', unsafe_allow_html=True)
    st.write("Disponible dès septembre, motivé à transformer les données en valeur.")

    # Coordonnées
    st.markdown("---")
    st.header("📌 Coordonnées")
    col1, col2 = st.columns(2)
    with col1:
        st.write("📞 **Téléphone:** 0766848029")
        st.write("📧 **Email:** kader.diarrassouba9@gmail.com")
    with col2:
        st.write("📍 **Localisation:** Île-de-France")
        st.write("[🔗 LinkedIn](https://www.linkedin.com/in/khadara-diarrassouba/)")
        st.write("[🐱 GitHub](https://github.com/RedakArraid)")

# Section Compétences
elif section == "Compétences":
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

# Section Expériences
elif section == "Expériences":
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

# Section Formations
elif section == "Formations":
    st.markdown('<p class="section-title">🎓 Formations</p>', unsafe_allow_html=True)
    
    st.write("**École Centrale d'Électronique de Paris (ECE)**")
    st.write("Deuxième et troisième années du cycle ingénieur en informatique | Septembre 2023 - Juillet 2025")

    st.write("**EFREI Paris / Mobilité ACH en Pologne**")
    st.write("Première année de cycle ingénieur informatique | Août 2022 - Juillet 2023")

    st.write("**Institut National Polytechnique Félix Houphouët Boigny (INPHB)**")
    st.write("Ingénieur en exploitation et traitement des eaux | 2017-2022")

# Section Contact
elif section == "Contact":
    st.markdown('<p class="section-title">📧 Contact</p>', unsafe_allow_html=True)
    
    # Formulaire de contact
    with st.form("contact_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.success(f"Merci {name}, votre message a été envoyé !")

# Télécharger le CV en PDF
st.sidebar.markdown("---")
st.sidebar.write("📄 Télécharger mon CV en PDF")
with open("CvKhadara-3 (1).pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.sidebar.download_button(
    label="Télécharger",
    data=PDFbyte,
    file_name="CV_Khadara_Diarrassouba.pdf",
    mime="application/pdf",
)
