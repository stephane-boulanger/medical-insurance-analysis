# 📊 Guide des Visualisations - Où Trouver le Code

## ✅ Confirmation : Le Code des Visualisations EST Présent !

Tous les scripts utilisent **matplotlib** et **seaborn** pour créer les visualisations. Voici où trouver chaque type de graphique dans le code.

---

## 📁 Répartition des Visualisations par Script

### 1️⃣ Script `1_eda.py` - Visualisations EDA (3 graphiques)

**Lignes 91-135** : Distribution des charges
```python
# Histogramme avec moyenne et médiane
axes[0].hist(df['charges'], bins=50, edgecolor='black', alpha=0.7, color='steelblue')
axes[0].axvline(df['charges'].mean(), color='red', linestyle='--', linewidth=2)

# Boxplot
axes[1].boxplot(df['charges'], vert=True, patch_artist=True)

# Distribution log
axes[2].hist(np.log10(df['charges']), bins=50, edgecolor='black', alpha=0.7, color='coral')
```

**Lignes 142-169** : Distribution des variables numériques
```python
# Histogrammes pour age, bmi, children
for idx, (col, color) in enumerate(zip(numerical_cols, colors)):
    axes[idx].hist(df[col], bins=30, edgecolor='black', alpha=0.7, color=color)
    # Boxplots correspondants
    axes[idx + 3].boxplot(df[col], vert=True, patch_artist=True)
```

**Lignes 176-196** : Distribution des variables catégorielles
```python
# Barplots pour sex, smoker, region
for idx, (col, color) in enumerate(zip(categorical_cols, colors_cat)):
    counts = df[col].value_counts()
    axes[idx].bar(counts.index, counts.values, edgecolor='black', alpha=0.7)
```

---

### 2️⃣ Script `3_feature_exploration.py` - Exploration Features (6 graphiques)

**Lignes 54-68** : Matrice de corrélation
```python
# Heatmap avec seaborn
sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='coolwarm',
            center=0, square=True, linewidths=1)
```

**Lignes 86-110** : Impact de l'âge
```python
# Scatter plot avec régression
axes[0].scatter(df['age'], df['charges'], alpha=0.5, s=30, color='steelblue')
z = np.polyfit(df['age'], df['charges'], 1)
p = np.poly1d(z)
axes[0].plot(df['age'], p(df['age']), "r--", linewidth=2)

# Boxplot par catégorie
df.boxplot(column='charges', by='age_category', ax=axes[1])
```

**Lignes 128-152** : Impact du BMI
```python
# Scatter plot avec régression
axes[0].scatter(df['bmi'], df['charges'], alpha=0.5, s=30, color='coral')

# Boxplot par catégorie
df.boxplot(column='charges', by='bmi_category', ax=axes[1])
```

**Lignes 175-214** : Impact du statut fumeur
```python
# Boxplot comparatif
smoker_data = [non_smoker_charges, smoker_charges]
bp = axes[0].boxplot(smoker_data, labels=['Non-fumeur', 'Fumeur'], patch_artist=True)

# Violin plot avec seaborn
sns.violinplot(data=df, x='smoker', y='charges', ax=axes[1])

# Bar plot des moyennes
smoker_means = df.groupby('smoker')['charges'].mean()
axes[2].bar(smoker_means.index, smoker_means.values)
```

**Lignes 230-258** : Impact du nombre d'enfants
```python
# Boxplot
df.boxplot(column='charges', by='children', ax=axes[0])

# Bar plot des moyennes
children_means = df.groupby('children')['charges'].mean()
axes[1].bar(children_means.index.astype(str), children_means.values)
```

**Lignes 272-297** : Interactions entre variables
```python
# Scatter plot: BMI vs Charges coloré par statut fumeur
for smoker_status in df['smoker'].unique():
    subset = df[df['smoker'] == smoker_status]
    axes[0].scatter(subset['bmi'], subset['charges'], label=f'Fumeur: {smoker_status}')

# Scatter plot: Âge vs Charges coloré par statut fumeur
for smoker_status in df['smoker'].unique():
    subset = df[df['smoker'] == smoker_status]
    axes[1].scatter(subset['age'], subset['charges'], label=f'Fumeur: {smoker_status}')
```

---

### 3️⃣ Script `4_visualizations.py` - Visualisations Avancées (9 graphiques)

**Lignes 50-60** : Pairplot avec Seaborn
```python
# Pairplot avec hue
pairplot = sns.pairplot(df[pairplot_vars + ['smoker']], hue='smoker',
                        diag_kind='kde', plot_kws={'alpha': 0.6})
```

**Lignes 68-78** : Heatmap Âge × BMI
```python
# Pivot table et heatmap
pivot_age_bmi = df.pivot_table(values='charges', index='age_category', 
                               columns='bmi_category', aggfunc='mean')
sns.heatmap(pivot_age_bmi, annot=True, fmt='.0f', cmap='YlOrRd')
```

**Lignes 86-120** : Violin plots comparatifs
```python
# 4 violin plots avec seaborn
sns.violinplot(data=df, x='sex', y='charges', ax=axes[0, 0])
sns.violinplot(data=df, x='region', y='charges', ax=axes[0, 1])
sns.violinplot(data=df, x='age_category', y='charges', ax=axes[1, 0])
sns.violinplot(data=df, x='bmi_category', y='charges', ax=axes[1, 1])
```

**Lignes 128-150** : Swarm et Strip plots
```python
# Swarm plot avec seaborn
sns.swarmplot(data=df, x='children', y='charges', hue='smoker', ax=axes[0])

# Strip plot avec seaborn
sns.stripplot(data=df, x='sex', y='charges', hue='smoker', ax=axes[1])
```

**Lignes 158-172** : Jointplots
```python
# Jointplot Âge vs Charges
joint_age = sns.jointplot(data=df, x='age', y='charges', kind='reg', height=8)

# Jointplot BMI vs Charges
joint_bmi = sns.jointplot(data=df, x='bmi', y='charges', kind='hex', height=8)
```

**Lignes 180-190** : FacetGrid
```python
# FacetGrid avec seaborn
g = sns.FacetGrid(df, col='region', hue='smoker', height=4, aspect=1.2)
g.map(plt.hist, 'charges', bins=30, alpha=0.7)
g.add_legend()
```

**Lignes 198-225** : Barplots avec erreurs
```python
# Barplot avec seaborn et barres d'erreur
sns.barplot(data=df, x='region', y='charges', ax=axes[0], ci='sd', capsize=0.1)
sns.barplot(data=df, x='age_category', y='charges', hue='sex', ax=axes[1], ci='sd')
```

**Lignes 233-270** : Countplots
```python
# 4 countplots avec seaborn
sns.countplot(data=df, x='sex', hue='smoker', ax=axes[0, 0])
sns.countplot(data=df, x='region', ax=axes[0, 1])
sns.countplot(data=df, x='bmi_category', ax=axes[1, 0])
sns.countplot(data=df, x='risk_score', ax=axes[1, 1])
```

---

### 4️⃣ Script `5_regional_analysis.py` - Analyse Régionale (3 graphiques)

**Lignes 74-130** : Vue d'ensemble régionale
```python
# Boxplot des charges par région
bp = axes[0, 0].boxplot(region_charges, labels=df['region'].unique())

# Bar plot des moyennes
axes[0, 1].bar(region_means.index, region_means.values)

# Violin plot avec seaborn
sns.violinplot(data=df, x='region', y='charges', ax=axes[1, 0])

# Pie chart de la répartition
axes[1, 1].pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%')
```

**Lignes 137-175** : Comparaisons régionales multivariées
```python
# 4 barplots horizontaux
axes[0, 0].barh(age_by_region.index, age_by_region.values)  # Âge moyen
axes[0, 1].barh(bmi_by_region.index, bmi_by_region.values)  # BMI moyen
axes[1, 0].barh(smoker_by_region.index, smoker_by_region.values)  # % fumeurs
axes[1, 1].barh(children_by_region.index, children_by_region.values)  # Enfants
```

**Lignes 182-192** : Heatmap Région × Fumeur
```python
# Pivot table et heatmap
pivot_table = df.pivot_table(values='charges', index='region', columns='smoker')
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd')
```

---

## 📚 Bibliothèques Utilisées

### Matplotlib (utilisé dans tous les scripts)
```python
import matplotlib.pyplot as plt

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')  # ou 'seaborn-v0_8-whitegrid'

# Types de graphiques utilisés:
- plt.hist()          # Histogrammes
- plt.scatter()       # Scatter plots
- plt.plot()          # Lignes de régression
- plt.bar()           # Bar charts
- plt.barh()          # Bar charts horizontaux
- plt.boxplot()       # Box plots
- plt.pie()           # Pie charts
- plt.axvline()       # Lignes verticales (moyenne, médiane)
```

### Seaborn (utilisé dans scripts 3, 4, 5)
```python
import seaborn as sns

# Configuration
sns.set_palette("Set2")  # ou "husl", "coolwarm", etc.
sns.set_context("notebook", font_scale=1.1)

# Types de graphiques utilisés:
- sns.heatmap()       # Heatmaps (corrélation, pivot tables)
- sns.violinplot()    # Violin plots
- sns.swarmplot()     # Swarm plots
- sns.stripplot()     # Strip plots
- sns.jointplot()     # Joint plots (bivariés)
- sns.pairplot()      # Pair plots (multivariés)
- sns.FacetGrid()     # Grilles de graphiques multiples
- sns.barplot()       # Bar plots avec erreurs
- sns.countplot()     # Count plots
```

---

## 🎨 Caractéristiques des Visualisations

### Qualité
- **Résolution**: 300 DPI (haute qualité pour impression)
- **Format**: PNG avec transparence
- **Taille**: Adaptée pour présentations (figsize optimisé)

### Style
- **Couleurs**: Palettes professionnelles (Set2, husl, coolwarm)
- **Grilles**: Activées pour meilleure lisibilité
- **Labels**: Titres, axes et légendes en français
- **Annotations**: Valeurs affichées sur les graphiques

### Organisation
```python
# Sauvegarde avec paramètres optimaux
plt.savefig(f'{OUTPUT_DIR}/nom_fichier.png', 
            dpi=300,                    # Haute résolution
            bbox_inches='tight')        # Pas d'espace blanc
```

---

## 🔍 Comment Vérifier le Code

### Méthode 1 : Ouvrir les Scripts Directement

```bash
# Dans VS Code, ouvrez:
scripts/1_eda.py                    # Lignes 91-196 (visualisations)
scripts/3_feature_exploration.py    # Lignes 54-297 (visualisations)
scripts/4_visualizations.py         # Lignes 50-270 (visualisations)
scripts/5_regional_analysis.py      # Lignes 74-192 (visualisations)
```

### Méthode 2 : Rechercher dans le Code

```bash
# Rechercher toutes les utilisations de matplotlib
grep -n "plt\." scripts/*.py

# Rechercher toutes les utilisations de seaborn
grep -n "sns\." scripts/*.py

# Rechercher toutes les sauvegardes de graphiques
grep -n "savefig" scripts/*.py
```

### Méthode 3 : Exécuter et Observer

```bash
cd medical-insurance-analysis-v2/scripts

# Exécuter un script et voir les visualisations se créer
python 1_eda.py
# ✓ Sauvegardé: 01_distribution_charges.png
# ✓ Sauvegardé: 02_distribution_variables_numeriques.png
# ✓ Sauvegardé: 03_distribution_variables_categorielles.png
```

---

## ✅ Récapitulatif

| Script | Lignes de Code Viz | Nb Graphiques | Bibliothèques |
|--------|-------------------|---------------|---------------|
| `1_eda.py` | 91-196 (105 lignes) | 3 | matplotlib |
| `2_preprocessing.py` | - | 0 | - |
| `3_feature_exploration.py` | 54-297 (243 lignes) | 6 | matplotlib + seaborn |
| `4_visualizations.py` | 50-270 (220 lignes) | 9 | matplotlib + seaborn |
| `5_regional_analysis.py` | 74-192 (118 lignes) | 3 | matplotlib + seaborn |
| **TOTAL** | **686 lignes** | **21 graphiques** | **matplotlib + seaborn** |

---

## 🎯 Conclusion

**Le code des visualisations est bien présent et complet** dans les scripts Python. Chaque graphique est créé avec matplotlib et/ou seaborn, avec :

✅ Code source complet et commenté  
✅ Paramètres de style professionnels  
✅ Sauvegarde haute résolution (300 DPI)  
✅ Organisation claire par catégorie  
✅ 21 visualisations au total  

**Aucun code n'est manquant !** Tous les graphiques sont générés programmatiquement par les scripts.

