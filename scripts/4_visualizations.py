"""
4. VISUALIZATIONS
==================

Ce script crée des visualisations avancées avec Matplotlib et Seaborn.

Objectifs:
- Créer des visualisations professionnelles et informatives
- Utiliser matplotlib et seaborn pour différents types de graphiques
- Générer des dashboards visuels
- Communiquer efficacement les insights

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")
sns.set_context("notebook", font_scale=1.1)

# Chemins
DATA_PATH = '../data/insurance_clean.csv'
OUTPUT_DIR = '../visualizations/features'
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*80)
print("CRÉATION DE VISUALISATIONS AVEC MATPLOTLIB ET SEABORN")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. CHARGEMENT DES DONNÉES")
print("-" * 40)

df = pd.read_csv(DATA_PATH)
print(f"✓ Dataset chargé: {df.shape[0]} lignes × {df.shape[1]} colonnes")

# ============================================================================
# 2. PAIRPLOT - VUE D'ENSEMBLE DES RELATIONS
# ============================================================================

print("\n2. CRÉATION DU PAIRPLOT")
print("-" * 40)

# Sélectionner les variables clés
pairplot_vars = ['age', 'bmi', 'children', 'charges']

# Créer le pairplot avec seaborn
print("Génération du pairplot (peut prendre quelques secondes)...")
pairplot = sns.pairplot(df[pairplot_vars + ['smoker']], hue='smoker',
                        diag_kind='kde', plot_kws={'alpha': 0.6},
                        palette=['lightgreen', 'lightcoral'])
pairplot.fig.suptitle('Relations entre Variables (coloré par Statut Fumeur)', 
                     y=1.02, fontsize=16, fontweight='bold')
plt.savefig(f'{OUTPUT_DIR}/07_pairplot_relations.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 07_pairplot_relations.png")

# ============================================================================
# 3. HEATMAP DES CHARGES PAR CATÉGORIES
# ============================================================================

print("\n3. CRÉATION DES HEATMAPS")
print("-" * 40)

# Heatmap: Âge × BMI
pivot_age_bmi = df.pivot_table(values='charges', index='age_category', 
                               columns='bmi_category', aggfunc='mean')

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_age_bmi, annot=True, fmt='.0f', cmap='YlOrRd',
            linewidths=1, cbar_kws={'label': 'Charges Moyennes ($)'})
plt.title('Charges Moyennes par Âge et BMI', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Catégorie de BMI', fontsize=12, fontweight='bold')
plt.ylabel('Catégorie d\'Âge', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/08_heatmap_age_bmi.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 08_heatmap_age_bmi.png")

# ============================================================================
# 4. VIOLIN PLOTS COMPARATIFS
# ============================================================================

print("\n4. CRÉATION DES VIOLIN PLOTS")
print("-" * 40)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Violin plot 1: Charges par sexe
sns.violinplot(data=df, x='sex', y='charges', ax=axes[0, 0], palette='Set2')
axes[0, 0].set_title('Distribution des Charges par Sexe', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Sexe', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')

# Violin plot 2: Charges par région
sns.violinplot(data=df, x='region', y='charges', ax=axes[0, 1], palette='Set3')
axes[0, 1].set_title('Distribution des Charges par Région', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0, 1].tick_params(axis='x', rotation=45)

# Violin plot 3: Charges par catégorie d'âge
sns.violinplot(data=df, x='age_category', y='charges', ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Distribution des Charges par Catégorie d\'Âge', 
                     fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Catégorie d\'Âge', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Violin plot 4: Charges par catégorie de BMI
sns.violinplot(data=df, x='bmi_category', y='charges', ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Distribution des Charges par Catégorie de BMI',
                     fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Catégorie de BMI', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/09_violin_plots_comparatifs.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 09_violin_plots_comparatifs.png")

# ============================================================================
# 5. SWARM PLOTS POUR VISUALISER LES DISTRIBUTIONS
# ============================================================================

print("\n5. CRÉATION DES SWARM PLOTS")
print("-" * 40)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Swarm plot 1: Enfants (petit dataset, adapté pour swarm)
sns.swarmplot(data=df, x='children', y='charges', hue='smoker', ax=axes[0],
             palette=['lightgreen', 'lightcoral'], alpha=0.6)
axes[0].set_title('Distribution des Charges par Nombre d\'Enfants et Statut Fumeur',
                 fontsize=14, fontweight='bold')
axes[0].set_xlabel('Nombre d\'Enfants', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0].legend(title='Fumeur', loc='upper right')

# Strip plot 2: Sexe
sns.stripplot(data=df, x='sex', y='charges', hue='smoker', ax=axes[1],
             palette=['lightgreen', 'lightcoral'], alpha=0.5, dodge=True)
axes[1].set_title('Distribution des Charges par Sexe et Statut Fumeur',
                 fontsize=14, fontweight='bold')
axes[1].set_xlabel('Sexe', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1].legend(title='Fumeur', loc='upper right')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/10_swarm_strip_plots.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 10_swarm_strip_plots.png")

# ============================================================================
# 6. JOINTPLOT - RELATION DÉTAILLÉE
# ============================================================================

print("\n6. CRÉATION DES JOINTPLOTS")
print("-" * 40)

# Jointplot: Âge vs Charges
joint_age = sns.jointplot(data=df, x='age', y='charges', kind='reg',
                          height=8, color='steelblue')
joint_age.fig.suptitle('Relation Détaillée: Âge vs Charges', 
                       y=1.02, fontsize=16, fontweight='bold')
plt.savefig(f'{OUTPUT_DIR}/11_jointplot_age_charges.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 11_jointplot_age_charges.png")

# Jointplot: BMI vs Charges
joint_bmi = sns.jointplot(data=df, x='bmi', y='charges', kind='hex',
                          height=8, cmap='YlOrRd')
joint_bmi.fig.suptitle('Relation Détaillée: BMI vs Charges',
                       y=1.02, fontsize=16, fontweight='bold')
plt.savefig(f'{OUTPUT_DIR}/12_jointplot_bmi_charges.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 12_jointplot_bmi_charges.png")

# ============================================================================
# 7. FACETGRID - VISUALISATIONS MULTIPLES
# ============================================================================

print("\n7. CRÉATION DES FACETGRIDS")
print("-" * 40)

# FacetGrid: Distribution des charges par région et statut fumeur
g = sns.FacetGrid(df, col='region', hue='smoker', height=4, aspect=1.2,
                 palette=['lightgreen', 'lightcoral'])
g.map(plt.hist, 'charges', bins=30, alpha=0.7, edgecolor='black')
g.add_legend(title='Fumeur')
g.fig.suptitle('Distribution des Charges par Région et Statut Fumeur',
              y=1.02, fontsize=16, fontweight='bold')
plt.savefig(f'{OUTPUT_DIR}/13_facetgrid_region_smoker.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 13_facetgrid_region_smoker.png")

# ============================================================================
# 8. BARPLOTS AVEC ERREURS
# ============================================================================

print("\n8. CRÉATION DES BARPLOTS AVEC BARRES D'ERREUR")
print("-" * 40)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Barplot 1: Charges moyennes par région avec erreur standard
sns.barplot(data=df, x='region', y='charges', ax=axes[0], 
           palette='Set2', ci='sd', capsize=0.1)
axes[0].set_title('Charges Moyennes par Région (avec écart-type)',
                 fontsize=14, fontweight='bold')
axes[0].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Charges Moyennes ($)', fontsize=12, fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True, alpha=0.3, axis='y')

# Barplot 2: Charges moyennes par catégorie d'âge et sexe
sns.barplot(data=df, x='age_category', y='charges', hue='sex', ax=axes[1],
           palette='Set1', ci='sd', capsize=0.1)
axes[1].set_title('Charges Moyennes par Âge et Sexe (avec écart-type)',
                 fontsize=14, fontweight='bold')
axes[1].set_xlabel('Catégorie d\'Âge', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Charges Moyennes ($)', fontsize=12, fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].legend(title='Sexe')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/14_barplots_with_errors.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 14_barplots_with_errors.png")

# ============================================================================
# 9. COUNTPLOTS - DISTRIBUTIONS CATÉGORIELLES
# ============================================================================

print("\n9. CRÉATION DES COUNTPLOTS")
print("-" * 40)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Countplot 1: Distribution par sexe et fumeur
sns.countplot(data=df, x='sex', hue='smoker', ax=axes[0, 0],
             palette=['lightgreen', 'lightcoral'])
axes[0, 0].set_title('Distribution par Sexe et Statut Fumeur',
                    fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Sexe', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Nombre d\'Observations', fontsize=12, fontweight='bold')
axes[0, 0].legend(title='Fumeur')

# Countplot 2: Distribution par région
sns.countplot(data=df, x='region', ax=axes[0, 1], palette='Set3')
axes[0, 1].set_title('Distribution par Région', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Nombre d\'Observations', fontsize=12, fontweight='bold')
axes[0, 1].tick_params(axis='x', rotation=45)

# Countplot 3: Distribution par catégorie de BMI
sns.countplot(data=df, x='bmi_category', ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Distribution par Catégorie de BMI', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Catégorie de BMI', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Nombre d\'Observations', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Countplot 4: Distribution par score de risque
sns.countplot(data=df, x='risk_score', ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Distribution par Score de Risque', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Score de Risque', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Nombre d\'Observations', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/15_countplots_distributions.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 15_countplots_distributions.png")

# ============================================================================
# 10. RÉSUMÉ DES VISUALISATIONS
# ============================================================================

print("\n" + "="*80)
print("RÉSUMÉ DES VISUALISATIONS CRÉÉES")
print("="*80)

print("\nTypes de visualisations avec Matplotlib et Seaborn:")
print("  ✓ Pairplot - Relations multivariées")
print("  ✓ Heatmap - Charges par catégories")
print("  ✓ Violin plots - Distributions comparatives")
print("  ✓ Swarm/Strip plots - Distributions détaillées")
print("  ✓ Jointplots - Relations bivariées détaillées")
print("  ✓ FacetGrid - Visualisations multiples")
print("  ✓ Barplots avec erreurs - Comparaisons avec incertitude")
print("  ✓ Countplots - Distributions catégorielles")

print(f"\n✓ Total de visualisations créées: 9")
print(f"✓ Fichiers sauvegardés dans: {OUTPUT_DIR}/")

print("\n" + "="*80)
print("VISUALISATIONS TERMINÉES AVEC SUCCÈS!")
print("="*80)

