"""
1. EXPLORATORY DATA ANALYSIS (EDA)
===================================

Ce script effectue une analyse exploratoire complète du dataset d'assurance médicale.

Objectifs:
- Comprendre la structure des données
- Identifier les distributions des variables
- Détecter les valeurs manquantes et outliers
- Calculer les statistiques descriptives
- Créer des visualisations initiales

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)

# Chemins
DATA_PATH = '../data/insurance.csv'
OUTPUT_DIR = '../visualizations/eda'
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*80)
print("ANALYSE EXPLORATOIRE DES DONNÉES (EDA)")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. CHARGEMENT DES DONNÉES")
print("-" * 40)

df = pd.read_csv(DATA_PATH)
print(f"✓ Dataset chargé avec succès!")
print(f"  - Lignes: {df.shape[0]}")
print(f"  - Colonnes: {df.shape[1]}")
print(f"  - Variables: {list(df.columns)}")

# ============================================================================
# 2. APERÇU DES DONNÉES
# ============================================================================

print("\n2. APERÇU DES DONNÉES")
print("-" * 40)
print("\nPremières lignes:")
print(df.head(10))

print("\nDernières lignes:")
print(df.tail(5))

# ============================================================================
# 3. INFORMATIONS SUR LES TYPES DE DONNÉES
# ============================================================================

print("\n3. TYPES DE DONNÉES")
print("-" * 40)
print(df.info())

print("\nTypes de données par colonne:")
print(df.dtypes)

# ============================================================================
# 4. STATISTIQUES DESCRIPTIVES
# ============================================================================

print("\n4. STATISTIQUES DESCRIPTIVES")
print("-" * 40)

# Variables numériques
print("\nVariables numériques:")
print(df.describe())

# Variables catégorielles
print("\nVariables catégorielles:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col.upper()}:")
    print(df[col].value_counts())
    print(f"Pourcentage:")
    print(df[col].value_counts(normalize=True).mul(100).round(2))

# ============================================================================
# 5. VALEURS MANQUANTES
# ============================================================================

print("\n5. ANALYSE DES VALEURS MANQUANTES")
print("-" * 40)

missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100

missing_df = pd.DataFrame({
    'Colonne': missing.index,
    'Valeurs Manquantes': missing.values,
    'Pourcentage (%)': missing_pct.values
})

print(missing_df)

if missing.sum() == 0:
    print("\n✓ Aucune valeur manquante détectée!")
else:
    print(f"\n⚠ Total de valeurs manquantes: {missing.sum()}")

# ============================================================================
# 6. VALEURS DUPLIQUÉES
# ============================================================================

print("\n6. ANALYSE DES DOUBLONS")
print("-" * 40)

duplicates = df.duplicated().sum()
print(f"Nombre de lignes dupliquées: {duplicates}")

if duplicates > 0:
    print(f"Pourcentage: {(duplicates/len(df))*100:.2f}%")
else:
    print("✓ Aucun doublon détecté!")

# ============================================================================
# 7. ANALYSE DE LA VARIABLE CIBLE (CHARGES)
# ============================================================================

print("\n7. ANALYSE DE LA VARIABLE CIBLE: CHARGES")
print("-" * 40)

print(f"Moyenne: ${df['charges'].mean():.2f}")
print(f"Médiane: ${df['charges'].median():.2f}")
print(f"Écart-type: ${df['charges'].std():.2f}")
print(f"Minimum: ${df['charges'].min():.2f}")
print(f"Maximum: ${df['charges'].max():.2f}")
print(f"Skewness (asymétrie): {df['charges'].skew():.2f}")
print(f"Kurtosis (aplatissement): {df['charges'].kurtosis():.2f}")

# Quartiles
print(f"\nQuartiles:")
print(f"  Q1 (25%): ${df['charges'].quantile(0.25):.2f}")
print(f"  Q2 (50%): ${df['charges'].quantile(0.50):.2f}")
print(f"  Q3 (75%): ${df['charges'].quantile(0.75):.2f}")

# ============================================================================
# 8. DÉTECTION DES OUTLIERS
# ============================================================================

print("\n8. DÉTECTION DES OUTLIERS (Méthode IQR)")
print("-" * 40)

for col in ['age', 'bmi', 'charges']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    print(f"\n{col.upper()}:")
    print(f"  Q1: {Q1:.2f}")
    print(f"  Q3: {Q3:.2f}")
    print(f"  IQR: {IQR:.2f}")
    print(f"  Limites: [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"  Outliers: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")

# ============================================================================
# 9. VISUALISATIONS EDA
# ============================================================================

print("\n9. GÉNÉRATION DES VISUALISATIONS")
print("-" * 40)

# Visualisation 1: Distribution de la variable cible
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Histogramme
axes[0].hist(df['charges'], bins=50, edgecolor='black', alpha=0.7, color='steelblue')
axes[0].axvline(df['charges'].mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Moyenne: ${df["charges"].mean():.0f}')
axes[0].axvline(df['charges'].median(), color='green', linestyle='--', linewidth=2,
                label=f'Médiane: ${df["charges"].median():.0f}')
axes[0].set_xlabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Fréquence', fontsize=12, fontweight='bold')
axes[0].set_title('Distribution des Charges Médicales', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Boxplot
axes[1].boxplot(df['charges'], vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', alpha=0.7))
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Boxplot des Charges', fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='y')

# Distribution log
axes[2].hist(np.log10(df['charges']), bins=50, edgecolor='black', alpha=0.7, color='coral')
axes[2].set_xlabel('Log10(Charges)', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Fréquence', fontsize=12, fontweight='bold')
axes[2].set_title('Distribution Log des Charges', fontsize=14, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/01_distribution_charges.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 01_distribution_charges.png")

# Visualisation 2: Distribution des variables numériques
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

numerical_cols = ['age', 'bmi', 'children']
colors = ['skyblue', 'lightgreen', 'salmon']

for idx, (col, color) in enumerate(zip(numerical_cols, colors)):
    # Histogramme
    axes[idx].hist(df[col], bins=30, edgecolor='black', alpha=0.7, color=color)
    axes[idx].axvline(df[col].mean(), color='red', linestyle='--', linewidth=2,
                     label=f'Moyenne: {df[col].mean():.2f}')
    axes[idx].set_xlabel(col.upper(), fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Fréquence', fontsize=12, fontweight='bold')
    axes[idx].set_title(f'Distribution: {col.upper()}', fontsize=12, fontweight='bold')
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)
    
    # Boxplot
    axes[idx + 3].boxplot(df[col], vert=True, patch_artist=True,
                         boxprops=dict(facecolor=color, alpha=0.7))
    axes[idx + 3].set_ylabel(col.upper(), fontsize=12, fontweight='bold')
    axes[idx + 3].set_title(f'Boxplot: {col.upper()}', fontsize=12, fontweight='bold')
    axes[idx + 3].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/02_distribution_variables_numeriques.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 02_distribution_variables_numeriques.png")

# Visualisation 3: Distribution des variables catégorielles
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

categorical_cols = ['sex', 'smoker', 'region']
colors_cat = ['lightblue', 'lightcoral', 'lightgreen']

for idx, (col, color) in enumerate(zip(categorical_cols, colors_cat)):
    counts = df[col].value_counts()
    axes[idx].bar(counts.index, counts.values, edgecolor='black', alpha=0.7, color=color)
    axes[idx].set_xlabel(col.upper(), fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Nombre d\'observations', fontsize=12, fontweight='bold')
    axes[idx].set_title(f'Distribution: {col.upper()}', fontsize=14, fontweight='bold')
    axes[idx].grid(True, alpha=0.3, axis='y')
    
    # Ajouter les valeurs sur les barres
    for i, v in enumerate(counts.values):
        axes[idx].text(i, v + max(counts.values)*0.02, str(v), 
                      ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/03_distribution_variables_categorielles.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 03_distribution_variables_categorielles.png")

# ============================================================================
# 10. RÉSUMÉ EDA
# ============================================================================

print("\n" + "="*80)
print("RÉSUMÉ DE L'ANALYSE EXPLORATOIRE")
print("="*80)

print(f"\n✓ Dataset: {df.shape[0]} lignes × {df.shape[1]} colonnes")
print(f"✓ Valeurs manquantes: {missing.sum()}")
print(f"✓ Doublons: {duplicates}")
print(f"✓ Variables numériques: {len(df.select_dtypes(include=[np.number]).columns)}")
print(f"✓ Variables catégorielles: {len(categorical_cols)}")
print(f"✓ Visualisations créées: 3")
print(f"\n✓ Fichiers sauvegardés dans: {OUTPUT_DIR}/")

print("\n" + "="*80)
print("EDA TERMINÉE AVEC SUCCÈS!")
print("="*80)

