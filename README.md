# 🏥 Analyse des Coûts d'Assurance Médicale

## 📋 Description du Projet

Ce projet analyse les coûts d'assurance médicale en fonction de divers facteurs démographiques et de style de vie tels que l'âge, le sexe, l'IMC, le nombre de personnes à charge, les habitudes tabagiques et la région de résidence.

**Hackathon Subject 2**: Analyzing Medical Insurance Costs

---

## 🎯 Objectifs

- Effectuer une **analyse exploratoire complète** (EDA) du dataset
- **Prétraiter et nettoyer** les données
- Explorer l'**impact des différentes features** sur les coûts
- Créer des **visualisations professionnelles** avec Matplotlib et Seaborn
- Analyser les **variations régionales** des coûts (bonus)
- Fournir des **insights exploitables** pour les stratégies de tarification

---

## 📁 Structure du Projet

```
medical-insurance-analysis/
├── data/
│   ├── insurance.csv                    # Dataset original
│   ├── insurance_clean.csv              # Dataset nettoyé (généré)
│   └── insurance_clean_essential.csv    # Version essentielle (généré)
│
├── scripts/
│   ├── 1_eda.py                        # Analyse exploratoire des données
│   ├── 2_preprocessing.py              # Prétraitement et nettoyage
│   ├── 3_feature_exploration.py        # Exploration des features
│   ├── 4_visualizations.py             # Visualisations Matplotlib/Seaborn
│   └── 5_regional_analysis.py          # Analyse régionale (bonus)
│
├── visualizations/
│   ├── eda/                            # 3 visualisations EDA
│   ├── features/                       # 15 visualisations features
│   └── regional/                       # 3 visualisations régionales
│
├── outputs/
│   └── insights_report.md              # Rapport d'insights (à générer)
│
├── README.md                           # Ce fichier
├── requirements.txt                    # Dépendances Python
└── run_all.py                         # Script pour exécuter tout le pipeline
```

---

## 🚀 Installation

### Prérequis

- Python 3.11+
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

Les packages requis sont :
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- scikit-learn

---

## 💻 Utilisation

### Option 1 : Exécuter tout le pipeline

```bash
python run_all.py
```

Cette commande exécute automatiquement toutes les étapes dans l'ordre.

### Option 2 : Exécuter les scripts individuellement

```bash
# Depuis le dossier scripts/
cd scripts/

# 1. Analyse exploratoire
python 1_eda.py

# 2. Prétraitement
python 2_preprocessing.py

# 3. Exploration des features
python 3_feature_exploration.py

# 4. Visualisations
python 4_visualizations.py

# 5. Analyse régionale (bonus)
python 5_regional_analysis.py
```

---

## 📊 Étapes de l'Analyse

### 1️⃣ Exploratory Data Analysis (EDA)

**Script**: `scripts/1_eda.py`

**Objectifs**:
- Comprendre la structure des données (1338 lignes × 7 colonnes)
- Identifier les distributions des variables
- Détecter les valeurs manquantes (aucune) et outliers
- Calculer les statistiques descriptives
- Créer des visualisations initiales

**Outputs**:
- 3 visualisations dans `visualizations/eda/`
- Statistiques descriptives affichées dans la console

**Insights clés**:
- Aucune valeur manquante détectée
- 1 doublon identifié
- 139 outliers dans les charges (10.39%)
- Distribution asymétrique des charges (skewness positif)

---

### 2️⃣ Data Preprocessing

**Script**: `scripts/2_preprocessing.py`

**Objectifs**:
- Gérer les valeurs manquantes (si présentes)
- Encoder les variables catégorielles (Label Encoding + One-Hot Encoding)
- Normaliser les variables numériques (StandardScaler)
- Créer de nouvelles features

**Nouvelles features créées**:
1. `age_category` - 5 catégories d'âge
2. `bmi_category` - 5 catégories de BMI
3. `smoker_bmi_interaction` - Interaction fumeur × BMI
4. `charges_category` - 4 catégories de charges
5. `is_overweight` - Indicateur de surpoids (BMI ≥ 25)
6. `has_many_children` - Indicateur famille nombreuse (≥ 3 enfants)
7. `risk_score` - Score de risque composite (0-6)

**Outputs**:
- `data/insurance_clean.csv` - Dataset complet nettoyé
- `data/insurance_clean_essential.csv` - Version essentielle

---

### 3️⃣ Feature Exploration

**Script**: `scripts/3_feature_exploration.py`

**Objectifs**:
- Analyser l'impact de chaque variable sur les charges
- Calculer les corrélations
- Tester les interactions entre variables
- Effectuer des tests statistiques (t-test)

**Facteurs d'influence** (par ordre d'importance):
1. **Statut Fumeur** ⭐⭐⭐⭐⭐ - Corrélation: 0.787
2. **Âge** ⭐⭐⭐ - Corrélation: 0.299
3. **BMI** ⭐⭐ - Corrélation: 0.198
4. **Enfants** ⭐ - Corrélation: 0.068

**Insights majeurs**:
- Les fumeurs ont des charges **3.8x plus élevées** que les non-fumeurs
- Différence statistiquement significative (p-value < 0.001)
- Interaction forte entre statut fumeur et BMI

**Outputs**:
- 6 visualisations dans `visualizations/features/`
- Tests statistiques (t-test pour fumeur vs non-fumeur)

---

### 4️⃣ Visualizations (Matplotlib & Seaborn)

**Script**: `scripts/4_visualizations.py`

**Objectifs**:
- Créer des visualisations professionnelles et informatives
- Utiliser différents types de graphiques
- Communiquer efficacement les insights

**Types de visualisations créées**:
- **Pairplot** - Relations multivariées
- **Heatmap** - Charges par catégories (Âge × BMI)
- **Violin plots** - Distributions comparatives (sexe, région, âge, BMI)
- **Swarm/Strip plots** - Distributions détaillées
- **Jointplots** - Relations bivariées détaillées (Âge-Charges, BMI-Charges)
- **FacetGrid** - Distributions par région et statut fumeur
- **Barplots** - Comparaisons avec barres d'erreur
- **Countplots** - Distributions catégorielles

**Outputs**:
- 9 visualisations haute résolution (300 DPI) dans `visualizations/features/`

---

### 5️⃣ Regional Analysis (BONUS)

**Script**: `scripts/5_regional_analysis.py`

**Objectifs**:
- Comparer les charges entre les 4 régions (northeast, southeast, southwest, northwest)
- Identifier les facteurs régionaux
- Effectuer des tests statistiques (ANOVA)

**Résultats ANOVA**:
- Test F: Différences significatives entre régions (p < 0.05)
- Région la plus chère: **Southeast** ($14,735)
- Région la moins chère: **Southwest** ($12,347)
- Écart maximal: **$2,388**

**Facteurs régionaux**:
- Proportion de fumeurs varie selon les régions
- BMI moyen légèrement différent
- Âge moyen similaire entre régions

**Outputs**:
- 3 visualisations dans `visualizations/regional/`
- Statistiques détaillées par région

---

## 📈 Insights Clés et Recommandations

### Top 5 des Facteurs d'Influence

1. **Statut Fumeur** (Impact: ⭐⭐⭐⭐⭐)
   - Augmentation moyenne des charges: **+$23,616**
   - Ratio: **3.8x plus élevé**
   - Recommandation: Programmes de cessation tabagique

2. **Âge** (Impact: ⭐⭐⭐)
   - Corrélation positive modérée
   - Augmentation progressive avec l'âge
   - Recommandation: Plans adaptés par tranche d'âge

3. **BMI** (Impact: ⭐⭐)
   - Impact amplifié chez les fumeurs
   - Obésité (BMI > 30) = charges plus élevées
   - Recommandation: Programmes de gestion du poids

4. **Région** (Impact: ⭐⭐)
   - Variations significatives entre régions
   - Southeast: charges les plus élevées
   - Recommandation: Ajustements tarifaires régionaux

5. **Nombre d'Enfants** (Impact: ⭐)
   - Impact faible mais mesurable
   - Légère augmentation avec le nombre d'enfants
   - Recommandation: Offres familiales

### Profils à Risque Identifiés

**Profil Haut Risque**:
- Fumeur + BMI élevé + Âge > 50 ans
- Charges moyennes: **$40,000+**

**Profil Bas Risque**:
- Non-fumeur + BMI normal + Âge < 30 ans
- Charges moyennes: **$3,000-5,000**

### Recommandations Stratégiques

1. **Tarification Différenciée**
   - Appliquer des primes significativement plus élevées pour les fumeurs
   - Ajuster selon l'âge et le BMI

2. **Programmes de Prévention**
   - Incitations pour arrêter de fumer
   - Programmes de gestion du poids
   - Suivi médical préventif pour les 50+

3. **Segmentation Régionale**
   - Adapter les tarifs selon les régions
   - Analyser les causes des variations régionales

4. **Offres Personnalisées**
   - Plans famille pour les assurés avec enfants
   - Réductions pour mode de vie sain

---

## 📊 Visualisations Générées

### EDA (3 visualisations)
1. Distribution des charges médicales
2. Distribution des variables numériques
3. Distribution des variables catégorielles

### Features (15 visualisations)
1. Matrice de corrélation
2. Impact de l'âge
3. Impact du BMI
4. Impact du statut fumeur
5. Impact du nombre d'enfants
6. Interactions entre variables
7. Pairplot des relations
8. Heatmap Âge × BMI
9. Violin plots comparatifs
10. Swarm/Strip plots
11. Jointplot Âge-Charges
12. Jointplot BMI-Charges
13. FacetGrid Région-Fumeur
14. Barplots avec erreurs
15. Countplots distributions

### Régionales (3 visualisations)
1. Analyse régionale overview
2. Comparaisons régionales multivariées
3. Heatmap Région × Fumeur

**Total: 21 visualisations haute résolution (300 DPI)**

---

## 🛠️ Technologies Utilisées

- **Python 3.11** - Langage de programmation
- **pandas** - Manipulation de données
- **numpy** - Calculs numériques
- **matplotlib** - Visualisations de base
- **seaborn** - Visualisations statistiques avancées
- **scipy** - Tests statistiques
- **scikit-learn** - Preprocessing et normalisation

---

## 📝 Livrables

✅ **Code Source**
- 5 scripts Python modulaires et bien commentés
- Script d'exécution automatique (run_all.py)

✅ **Données**
- Dataset original (insurance.csv)
- Dataset nettoyé (insurance_clean.csv)
- Version essentielle (insurance_clean_essential.csv)

✅ **Visualisations**
- 21 graphiques haute résolution (300 DPI)
- Organisés par catégorie (EDA, Features, Regional)

✅ **Documentation**
- README complet avec instructions
- Commentaires détaillés dans le code
- Insights et recommandations

---

## 🎓 Critères d'Évaluation du Hackathon

### ✅ Profondeur de l'Analyse
- Analyse exploratoire complète avec statistiques descriptives
- Tests statistiques (t-test, ANOVA)
- Exploration approfondie des interactions

### ✅ Créativité dans l'Exploration
- Création de 7 nouvelles features
- Analyse multivariée (interactions fumeur × BMI, âge × fumeur)
- Score de risque composite

### ✅ Clarté et Efficacité des Visualisations
- 21 visualisations professionnelles
- Utilisation variée de matplotlib et seaborn
- Graphiques informatifs et esthétiques

### ✅ Qualité des Insights et Recommandations
- Identification claire des facteurs d'influence
- Profils à risque définis
- Recommandations stratégiques exploitables

---

## 👥 Auteur

**Data Analysis Team**  
Hackathon Subject 2 - Medical Insurance Cost Analysis  
Octobre 2025

---

## 📄 Licence

Ce projet est développé dans le cadre d'un hackathon éducatif.

---

## 🙏 Remerciements

- Dataset source: Medical Cost Personal Datasets
- Bibliothèques open-source: pandas, matplotlib, seaborn, scikit-learn

---

## 📞 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.

---

**Dernière mise à jour**: Octobre 2025

