# 🚀 Guide d'Utilisation du Dashboard Streamlit

## 📊 Qu'est-ce que Streamlit ?

**Streamlit** est un framework Python qui permet de créer des applications web interactives en quelques lignes de code. C'est utilisé par des entreprises comme Uber, Google, et des milliers de data scientists dans le monde.

**Avantages** :
- ✅ **Vraiment interactif** : Filtres, sliders, sélections
- ✅ **Professionnel** : Look moderne et épuré
- ✅ **Facile à utiliser** : Interface intuitive
- ✅ **Fonctionne sur Mac, Windows, Linux**
- ✅ **Gratuit et open-source**

---

## 🎯 Installation et Lancement (5 minutes)

### Étape 1 : Installer Streamlit

**Sur Mac/Linux** :
```bash
pip3 install streamlit plotly
```

**Sur Windows** :
```bash
pip install streamlit plotly
```

### Étape 2 : Naviguer vers le Dossier du Projet

```bash
cd medical-insurance-analysis-v2
```

### Étape 3 : Lancer le Dashboard

```bash
streamlit run dashboard_app.py
```

**Résultat** : Votre navigateur s'ouvre automatiquement avec le dashboard !

**URL locale** : http://localhost:8501

---

## 📊 Contenu du Dashboard

### 🏠 Header

- **Titre principal** : Dashboard Analyse des Coûts d'Assurance Médicale
- **4 KPIs** : Total Assurés, Charge Moyenne, Charge Médiane, Taux Fumeurs

### 🔍 Sidebar (Barre Latérale Gauche)

**Filtres interactifs** :
- ✅ Statut Fumeur (multiselect)
- ✅ Région (multiselect)
- ✅ Sexe (multiselect)
- ✅ Tranche d'Âge (slider)
- ✅ Tranche de BMI (slider)

**Compteur** : Affiche le nombre d'observations filtrées

### 📑 4 Onglets Principaux

#### Onglet 1 : Vue d'Ensemble
- **Histogramme** : Distribution des charges avec moyenne/médiane
- **Box plot** : Impact du statut fumeur
- **Insights** : 3 insights clés
- **Statistiques descriptives** : Tableau avec mean, std, min, max
- **Pie charts** : Répartition par sexe et région

#### Onglet 2 : Analyse Détaillée
- **Scatter plot Âge × Charges** : Taille = BMI, couleur = fumeur
- **Scatter plot BMI × Charges** : Taille = Âge, couleur = fumeur
- **Matrice de corrélation** : Heatmap interactive
- **Violin plots** : Distributions par catégorie d'âge et BMI

#### Onglet 3 : Analyse Régionale
- **Bar chart** : Charges moyennes par région
- **Heatmap** : Région × Statut Fumeur
- **Tableau récapitulatif** : Statistiques complètes par région

#### Onglet 4 : Insights et Recommandations
- **Top 5 facteurs** : Tableau avec impact et corrélation
- **Recommandations stratégiques** : 5 actions prioritaires
- **Profils à risque** : Haut, Modéré, Bas
- **Impact financier** : Scénario actuel vs optimisé

---

## 🎮 Comment Utiliser le Dashboard

### Filtrer les Données

1. **Ouvrez la sidebar** (barre latérale gauche)
2. **Sélectionnez les filtres** :
   - Cliquez sur "Statut Fumeur" et choisissez yes/no
   - Sélectionnez une ou plusieurs régions
   - Ajustez les sliders pour l'âge et le BMI
3. **Les graphiques se mettent à jour automatiquement** !

### Naviguer entre les Onglets

1. **Cliquez sur les onglets** en haut : Vue d'Ensemble, Analyse Détaillée, etc.
2. **Scrollez** pour voir tous les graphiques
3. **Interagissez** avec les graphiques :
   - **Hover** : Passez la souris pour voir les détails
   - **Zoom** : Cliquez et glissez pour zoomer
   - **Pan** : Déplacez-vous dans le graphique
   - **Reset** : Double-cliquez pour réinitialiser

### Exporter des Graphiques

1. **Passez la souris** sur un graphique
2. **Cliquez sur l'icône caméra** en haut à droite
3. **Le graphique est téléchargé** en PNG haute résolution

---

## 🎯 Pour la Présentation du Hackathon

### Préparation (10 minutes avant)

1. **Lancez le dashboard** :
   ```bash
   streamlit run dashboard_app.py
   ```

2. **Testez les filtres** pour vous familiariser

3. **Préparez votre storytelling** :
   - Commencez par la Vue d'Ensemble
   - Montrez l'impact du statut fumeur
   - Passez à l'Analyse Détaillée
   - Terminez par les Insights et Recommandations

### Pendant la Présentation

**Scénario recommandé** (5-7 minutes) :

**1. Introduction (30 secondes)**
- "Nous avons analysé 1,338 dossiers d'assurance médicale"
- "Voici notre dashboard interactif créé avec Streamlit"
- Montrez les 4 KPIs en haut

**2. Vue d'Ensemble (1 minute)**
- Cliquez sur l'onglet "Vue d'Ensemble"
- Montrez l'histogramme : "La distribution est asymétrique"
- Montrez le box plot : "Les fumeurs coûtent 3.8x plus cher"

**3. Démonstration de l'Interactivité (1 minute)**
- Ouvrez la sidebar
- Filtrez sur "Fumeurs uniquement" : "Regardez comment les KPIs changent"
- Filtrez sur "Southeast" : "Cette région est la plus coûteuse"
- Réinitialisez les filtres

**4. Analyse Détaillée (1.5 minutes)**
- Cliquez sur "Analyse Détaillée"
- Montrez le scatter plot Âge × Charges : "Relation positive, amplifiée chez les fumeurs"
- Montrez la matrice de corrélation : "Statut fumeur = corrélation la plus forte (0.787)"
- Hover sur un point : "Chaque point est interactif"

**5. Insights et Recommandations (2 minutes)**
- Cliquez sur "Insights"
- Montrez le Top 5 : "Statut fumeur est le facteur #1"
- Montrez les recommandations : "5 actions prioritaires"
- Montrez l'impact financier : "Amélioration de +$23M/an avec nos recommandations"

**6. Questions (1 minute)**
- Utilisez les filtres pour répondre aux questions
- "Vous voulez voir les charges pour les femmes de 30-40 ans ?" → Filtrez en direct

### Astuces pour Impressionner

- ✅ **Montrez l'interactivité** : Utilisez les filtres en direct
- ✅ **Hover sur les graphiques** : Montrez les détails au survol
- ✅ **Zoomez** : Montrez qu'on peut zoomer sur les scatter plots
- ✅ **Changez d'onglet** : Navigation fluide entre les sections
- ✅ **Mentionnez Streamlit** : "Nous avons créé cette application avec Streamlit, un framework Python moderne"

---

## 🛠️ Personnalisation (Optionnel)

### Changer les Couleurs

Éditez le fichier `dashboard_app.py`, section CSS (lignes 30-70) :

```python
# Changer le dégradé du header
background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
# Remplacez par vos couleurs préférées
```

### Ajouter un Logo

Ajoutez dans la sidebar :

```python
st.sidebar.image("logo.png", width=200)
```

### Modifier le Titre

Ligne 58 :
```python
st.markdown('<h1 class="main-header">📊 Votre Titre Ici</h1>', unsafe_allow_html=True)
```

---

## 🆘 Résolution de Problèmes

### Problème 1 : "streamlit: command not found"

**Solution** :
```bash
pip3 install --upgrade streamlit
```

### Problème 2 : "ModuleNotFoundError: No module named 'plotly'"

**Solution** :
```bash
pip3 install plotly
```

### Problème 3 : "FileNotFoundError: data/insurance_clean.csv"

**Solution** : Assurez-vous d'être dans le bon dossier :
```bash
cd medical-insurance-analysis-v2
streamlit run dashboard_app.py
```

### Problème 4 : Le dashboard ne s'ouvre pas dans le navigateur

**Solution** : Ouvrez manuellement http://localhost:8501

### Problème 5 : Port 8501 déjà utilisé

**Solution** : Utilisez un autre port :
```bash
streamlit run dashboard_app.py --server.port 8502
```

---

## 📤 Partage du Dashboard

### Option 1 : Streamlit Cloud (Gratuit)

1. **Créez un compte** sur https://streamlit.io/cloud
2. **Connectez votre repository GitHub**
3. **Déployez** en un clic
4. **Partagez le lien** avec votre équipe

**Avantage** : Dashboard accessible en ligne 24/7

### Option 2 : Enregistrement Vidéo

1. **Lancez le dashboard**
2. **Enregistrez votre écran** avec QuickTime (Mac) ou OBS (Windows/Mac/Linux)
3. **Montrez la vidéo** pendant la présentation

**Avantage** : Pas de risque technique pendant la présentation

### Option 3 : Captures d'Écran

1. **Prenez des screenshots** de chaque onglet
2. **Créez un PowerPoint** avec les images
3. **Mentionnez** que c'est un dashboard interactif

**Avantage** : Backup si problème technique

---

## ✅ Checklist Avant Présentation

- [ ] Streamlit et Plotly installés
- [ ] Dashboard lancé avec succès (http://localhost:8501)
- [ ] Tous les onglets fonctionnent
- [ ] Les filtres sont réactifs
- [ ] Les graphiques s'affichent correctement
- [ ] Vous avez testé votre storytelling
- [ ] Vous savez comment utiliser les filtres
- [ ] Vous avez préparé des réponses aux questions
- [ ] Backup : Screenshots ou vidéo enregistrée

---

## 🎓 Avantages pour le Hackathon

### Critère 1 : Profondeur de l'Analyse
✅ **4 onglets** couvrant tous les aspects
✅ **12+ visualisations** interactives
✅ **Filtres dynamiques** pour exploration approfondie

### Critère 2 : Créativité
✅ **Application web interactive** (pas juste des graphiques statiques)
✅ **Design moderne** avec dégradés et couleurs professionnelles
✅ **Streamlit** : Framework moderne et reconnu

### Critère 3 : Clarté des Visualisations
✅ **Navigation par onglets** : Organisation claire
✅ **Filtres interactifs** : Exploration facile
✅ **Hover et zoom** : Détails à la demande

### Critère 4 : Qualité des Insights
✅ **Onglet dédié** aux insights et recommandations
✅ **Top 5 facteurs** clairement présentés
✅ **Impact financier** quantifié

---

## 🚀 Commandes Rapides

```bash
# Lancer le dashboard
streamlit run dashboard_app.py

# Lancer sur un port spécifique
streamlit run dashboard_app.py --server.port 8502

# Lancer en mode développement (auto-reload)
streamlit run dashboard_app.py --server.runOnSave true

# Arrêter le dashboard
# Appuyez sur Ctrl+C dans le terminal
```

---

## 📚 Ressources Complémentaires

- **Documentation Streamlit** : https://docs.streamlit.io/
- **Galerie d'exemples** : https://streamlit.io/gallery
- **Forum communautaire** : https://discuss.streamlit.io/
- **Tutoriels vidéo** : https://www.youtube.com/c/Streamlit

---

## 🎉 Résumé

**Temps d'installation** : 5 minutes  
**Temps de lancement** : 10 secondes  
**Nombre de visualisations** : 12+  
**Filtres interactifs** : 5  
**Onglets** : 4  

**Résultat** : Dashboard professionnel et interactif prêt pour votre présentation ! 🚀

**Bonne chance pour le hackathon !** 🎓

