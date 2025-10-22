"""
3. FEATURE EXPLORATION
=======================

Ce script explore l'impact des différentes features sur les charges médicales.

Objectifs:
- Analyser l'impact de chaque variable sur les charges
- Identifier les corrélations
- Tester les interactions entre variables
- Effectuer des tests statistiques

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Chemins
DATA_PATH = '../data/insurance_clean.csv'
OUTPUT_DIR = '../visualizations/features'
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*80)
print("EXPLORATION DES FEATURES ET IMPACT SUR LES CHARGES")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. CHARGEMENT DES DONNÉES")
print("-" * 40)

df = pd.read_csv(DATA_PATH)
print(f"✓ Dataset chargé: {df.shape[0]} lignes × {df.shape[1]} colonnes")

# ============================================================================
# 2. MATRICE DE CORRÉLATION
# ============================================================================

print("\n2. MATRICE DE CORRÉLATION")
print("-" * 40)

# Sélectionner les colonnes numériques pour la corrélation
corr_cols = ['age', 'bmi', 'children', 'charges', 
             'sex_encoded', 'smoker_encoded', 'region_encoded']

correlation_matrix = df[corr_cols].corr()
print("\nMatrice de corrélation:")
print(correlation_matrix.round(3))

# Corrélations avec charges
print("\nCorrélations avec CHARGES (triées par valeur absolue):")
charges_corr = correlation_matrix['charges'].drop('charges').sort_values(key=abs, ascending=False)
for feature, corr in charges_corr.items():
    print(f"  {feature:20s}: {corr:7.3f}")

# Visualisation de la matrice de corrélation
plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='coolwarm',
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            mask=mask, vmin=-1, vmax=1)
plt.title('Matrice de Corrélation des Variables', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/01_matrice_correlation.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✓ Sauvegardé: 01_matrice_correlation.png")

# ============================================================================
# 3. IMPACT DE L'ÂGE SUR LES CHARGES
# ============================================================================

print("\n3. IMPACT DE L'ÂGE SUR LES CHARGES")
print("-" * 40)

age_corr = df['age'].corr(df['charges'])
print(f"Corrélation âge-charges: {age_corr:.3f}")

# Statistiques par catégorie d'âge
print("\nCharges moyennes par catégorie d'âge:")
age_stats = df.groupby('age_category')['charges'].agg(['mean', 'median', 'std', 'count'])
print(age_stats.round(2))

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot avec régression
axes[0].scatter(df['age'], df['charges'], alpha=0.5, s=30, color='steelblue')
z = np.polyfit(df['age'], df['charges'], 1)
p = np.poly1d(z)
axes[0].plot(df['age'], p(df['age']), "r--", linewidth=2, 
            label=f'Régression: y={z[0]:.2f}x+{z[1]:.2f}')
axes[0].set_xlabel('Âge', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_title(f'Relation Âge-Charges (r={age_corr:.3f})', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Boxplot par catégorie
df.boxplot(column='charges', by='age_category', ax=axes[1], patch_artist=True)
axes[1].set_xlabel('Catégorie d\'Âge', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Charges par Catégorie d\'Âge', fontsize=14, fontweight='bold')
axes[1].get_figure().suptitle('')  # Supprimer le titre automatique
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/02_impact_age.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 02_impact_age.png")

# ============================================================================
# 4. IMPACT DU BMI SUR LES CHARGES
# ============================================================================

print("\n4. IMPACT DU BMI SUR LES CHARGES")
print("-" * 40)

bmi_corr = df['bmi'].corr(df['charges'])
print(f"Corrélation BMI-charges: {bmi_corr:.3f}")

# Statistiques par catégorie de BMI
print("\nCharges moyennes par catégorie de BMI:")
bmi_stats = df.groupby('bmi_category')['charges'].agg(['mean', 'median', 'std', 'count'])
print(bmi_stats.round(2))

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot avec régression
axes[0].scatter(df['bmi'], df['charges'], alpha=0.5, s=30, color='coral')
z = np.polyfit(df['bmi'], df['charges'], 1)
p = np.poly1d(z)
axes[0].plot(df['bmi'], p(df['bmi']), "r--", linewidth=2,
            label=f'Régression: y={z[0]:.2f}x+{z[1]:.2f}')
axes[0].set_xlabel('BMI', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_title(f'Relation BMI-Charges (r={bmi_corr:.3f})', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Boxplot par catégorie
df.boxplot(column='charges', by='bmi_category', ax=axes[1], patch_artist=True)
axes[1].set_xlabel('Catégorie de BMI', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Charges par Catégorie de BMI', fontsize=14, fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].get_figure().suptitle('')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/03_impact_bmi.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 03_impact_bmi.png")

# ============================================================================
# 5. IMPACT DU STATUT FUMEUR (FACTEUR MAJEUR)
# ============================================================================

print("\n5. IMPACT DU STATUT FUMEUR SUR LES CHARGES")
print("-" * 40)

# Statistiques
non_smoker_charges = df[df['smoker'] == 'no']['charges']
smoker_charges = df[df['smoker'] == 'yes']['charges']

print(f"Charges moyennes (non-fumeur): ${non_smoker_charges.mean():.2f}")
print(f"Charges moyennes (fumeur): ${smoker_charges.mean():.2f}")
print(f"Différence: ${smoker_charges.mean() - non_smoker_charges.mean():.2f}")
print(f"Ratio: {smoker_charges.mean() / non_smoker_charges.mean():.2f}x")

# Test statistique
t_stat, p_value = stats.ttest_ind(non_smoker_charges, smoker_charges)
print(f"\nTest t de Student:")
print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.4e}")
print(f"  Significatif (α=0.05): {'OUI' if p_value < 0.05 else 'NON'}")

# Visualisation
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Boxplot
smoker_data = [non_smoker_charges, smoker_charges]
bp = axes[0].boxplot(smoker_data, labels=['Non-fumeur', 'Fumeur'], patch_artist=True)
bp['boxes'][0].set_facecolor('lightgreen')
bp['boxes'][1].set_facecolor('lightcoral')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_title('Charges: Fumeur vs Non-fumeur', fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.3, axis='y')

# Violin plot
sns.violinplot(data=df, x='smoker', y='charges', ax=axes[1], palette=['lightgreen', 'lightcoral'])
axes[1].set_xlabel('Statut Fumeur', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Distribution des Charges par Statut Fumeur', fontsize=14, fontweight='bold')

# Bar plot des moyennes
smoker_means = df.groupby('smoker')['charges'].mean()
bars = axes[2].bar(smoker_means.index, smoker_means.values, 
                   color=['lightgreen', 'lightcoral'], alpha=0.7, edgecolor='black')
axes[2].set_xlabel('Statut Fumeur', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Charges Moyennes ($)', fontsize=12, fontweight='bold')
axes[2].set_title('Charges Moyennes par Statut Fumeur', fontsize=14, fontweight='bold')
axes[2].grid(True, alpha=0.3, axis='y')

for i, v in enumerate(smoker_means.values):
    axes[2].text(i, v + 500, f'${v:.0f}', ha='center', va='bottom', 
                fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/04_impact_fumeur.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 04_impact_fumeur.png")

# ============================================================================
# 6. IMPACT DU NOMBRE D'ENFANTS
# ============================================================================

print("\n6. IMPACT DU NOMBRE D'ENFANTS SUR LES CHARGES")
print("-" * 40)

children_corr = df['children'].corr(df['charges'])
print(f"Corrélation children-charges: {children_corr:.3f}")

print("\nCharges moyennes par nombre d'enfants:")
children_stats = df.groupby('children')['charges'].agg(['mean', 'median', 'count'])
print(children_stats.round(2))

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Boxplot
df.boxplot(column='charges', by='children', ax=axes[0], patch_artist=True)
axes[0].set_xlabel('Nombre d\'Enfants', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_title('Charges par Nombre d\'Enfants', fontsize=14, fontweight='bold')
axes[0].get_figure().suptitle('')
axes[0].grid(True, alpha=0.3, axis='y')

# Bar plot des moyennes
children_means = df.groupby('children')['charges'].mean()
axes[1].bar(children_means.index.astype(str), children_means.values, 
           alpha=0.7, edgecolor='black', color='skyblue')
axes[1].set_xlabel('Nombre d\'Enfants', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges Moyennes ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Charges Moyennes par Nombre d\'Enfants', fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='y')

for i, v in enumerate(children_means.values):
    axes[1].text(i, v + 300, f'${v:.0f}', ha='center', va='bottom', 
                fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/05_impact_enfants.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 05_impact_enfants.png")

# ============================================================================
# 7. INTERACTIONS ENTRE VARIABLES
# ============================================================================

print("\n7. INTERACTIONS ENTRE VARIABLES")
print("-" * 40)

# Interaction Fumeur × BMI
print("\nInteraction Fumeur × BMI:")
interaction_stats = df.groupby(['smoker', 'bmi_category'])['charges'].mean().unstack()
print(interaction_stats.round(2))

# Visualisation
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot: BMI vs Charges coloré par statut fumeur
for smoker_status in df['smoker'].unique():
    subset = df[df['smoker'] == smoker_status]
    axes[0].scatter(subset['bmi'], subset['charges'], 
                   label=f'Fumeur: {smoker_status}', alpha=0.6, s=30)
axes[0].set_xlabel('BMI', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].set_title('Interaction BMI × Statut Fumeur', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Scatter plot: Âge vs Charges coloré par statut fumeur
for smoker_status in df['smoker'].unique():
    subset = df[df['smoker'] == smoker_status]
    axes[1].scatter(subset['age'], subset['charges'],
                   label=f'Fumeur: {smoker_status}', alpha=0.6, s=30)
axes[1].set_xlabel('Âge', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].set_title('Interaction Âge × Statut Fumeur', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/06_interactions_variables.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 06_interactions_variables.png")

# ============================================================================
# 8. RÉSUMÉ DE L'EXPLORATION DES FEATURES
# ============================================================================

print("\n" + "="*80)
print("RÉSUMÉ DE L'EXPLORATION DES FEATURES")
print("="*80)

print("\nFacteurs d'influence (par ordre d'importance):")
print(f"1. Statut Fumeur: Corrélation = {df['smoker_encoded'].corr(df['charges']):.3f} ⭐⭐⭐⭐⭐")
print(f"2. Âge: Corrélation = {age_corr:.3f} ⭐⭐⭐")
print(f"3. BMI: Corrélation = {bmi_corr:.3f} ⭐⭐")
print(f"4. Enfants: Corrélation = {children_corr:.3f} ⭐")

print(f"\n✓ Visualisations créées: 6")
print(f"✓ Tests statistiques effectués: 1 (t-test)")
print(f"✓ Fichiers sauvegardés dans: {OUTPUT_DIR}/")

print("\n" + "="*80)
print("EXPLORATION DES FEATURES TERMINÉE AVEC SUCCÈS!")
print("="*80)

