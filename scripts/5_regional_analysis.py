"""
5. REGIONAL ANALYSIS (BONUS)
==============================

Ce script effectue une analyse régionale détaillée des coûts d'assurance.

Objectifs:
- Comparer les charges entre régions
- Identifier les facteurs régionaux
- Effectuer des tests statistiques (ANOVA)
- Créer des visualisations régionales

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
sns.set_palette("Set2")

# Chemins
DATA_PATH = '../data/insurance_clean.csv'
OUTPUT_DIR = '../visualizations/regional'
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("="*80)
print("ANALYSE RÉGIONALE DES COÛTS D'ASSURANCE (BONUS)")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. CHARGEMENT DES DONNÉES")
print("-" * 40)

df = pd.read_csv(DATA_PATH)
print(f"✓ Dataset chargé: {df.shape[0]} lignes × {df.shape[1]} colonnes")

# ============================================================================
# 2. STATISTIQUES PAR RÉGION
# ============================================================================

print("\n2. STATISTIQUES DES CHARGES PAR RÉGION")
print("-" * 40)

regional_stats = df.groupby('region')['charges'].agg([
    ('Nombre', 'count'),
    ('Moyenne', 'mean'),
    ('Médiane', 'median'),
    ('Écart-type', 'std'),
    ('Minimum', 'min'),
    ('Maximum', 'max')
]).round(2)

print(regional_stats)

# ============================================================================
# 3. TEST ANOVA
# ============================================================================

print("\n3. ANALYSE ANOVA (ANALYSE DE VARIANCE)")
print("-" * 40)

# Préparer les données pour ANOVA
groups = [df[df['region'] == region]['charges'].values 
          for region in df['region'].unique()]
f_stat, p_value = stats.f_oneway(*groups)

print(f"Test ANOVA:")
print(f"  F-statistic: {f_stat:.4f}")
print(f"  p-value: {p_value:.4e}")
print(f"  Conclusion: {'Les moyennes régionales sont significativement différentes' if p_value < 0.05 else 'Pas de différence significative entre les régions'}")

# ============================================================================
# 4. ANALYSE DÉTAILLÉE PAR RÉGION
# ============================================================================

print("\n4. ANALYSE DÉTAILLÉE PAR RÉGION")
print("-" * 40)

for region in df['region'].unique():
    region_data = df[df['region'] == region]
    
    print(f"\n{region.upper()}:")
    print(f"  - Nombre d'observations: {len(region_data)}")
    print(f"  - Charges moyennes: ${region_data['charges'].mean():.2f}")
    print(f"  - Âge moyen: {region_data['age'].mean():.1f} ans")
    print(f"  - BMI moyen: {region_data['bmi'].mean():.2f}")
    print(f"  - Proportion de fumeurs: {(region_data['smoker'] == 'yes').sum() / len(region_data) * 100:.1f}%")
    print(f"  - Nombre moyen d'enfants: {region_data['children'].mean():.2f}")
    print(f"  - Répartition H/F: {(region_data['sex'] == 'male').sum()} H / {(region_data['sex'] == 'female').sum()} F")

# ============================================================================
# 5. VISUALISATIONS RÉGIONALES
# ============================================================================

print("\n5. GÉNÉRATION DES VISUALISATIONS RÉGIONALES")
print("-" * 40)

# Visualisation 1: Vue d'ensemble régionale
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Boxplot des charges par région
region_charges = [df[df['region'] == region]['charges'].values 
                 for region in df['region'].unique()]
bp = axes[0, 0].boxplot(region_charges, labels=df['region'].unique(), patch_artist=True)
for patch, color in zip(bp['boxes'], sns.color_palette("Set2", 4)):
    patch.set_facecolor(color)
axes[0, 0].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[0, 0].set_title('Distribution des Charges par Région', fontsize=14, fontweight='bold')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, alpha=0.3, axis='y')

# Bar plot des moyennes
region_means = df.groupby('region')['charges'].mean().sort_values(ascending=False)
bars = axes[0, 1].bar(region_means.index, region_means.values, 
                     color=sns.color_palette("Set2", 4), alpha=0.7, edgecolor='black')
axes[0, 1].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Charges Moyennes ($)', fontsize=12, fontweight='bold')
axes[0, 1].set_title('Charges Moyennes par Région', fontsize=14, fontweight='bold')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3, axis='y')

for i, v in enumerate(region_means.values):
    axes[0, 1].text(i, v + 200, f'${v:.0f}', ha='center', va='bottom', 
                   fontsize=10, fontweight='bold')

# Violin plot
sns.violinplot(data=df, x='region', y='charges', ax=axes[1, 0], palette="Set2")
axes[1, 0].set_xlabel('Région', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Charges ($)', fontsize=12, fontweight='bold')
axes[1, 0].set_title('Distribution Détaillée des Charges par Région', 
                    fontsize=14, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Pie chart de la répartition
region_counts = df['region'].value_counts()
axes[1, 1].pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%',
              startangle=90, colors=sns.color_palette("Set2", 4))
axes[1, 1].set_title('Répartition des Observations par Région', 
                    fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/01_analyse_regionale_overview.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 01_analyse_regionale_overview.png")

# Visualisation 2: Comparaisons régionales multivariées
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Âge moyen par région
age_by_region = df.groupby('region')['age'].mean().sort_values()
axes[0, 0].barh(age_by_region.index, age_by_region.values, alpha=0.7, 
               edgecolor='black', color='skyblue')
axes[0, 0].set_xlabel('Âge Moyen', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Région', fontsize=12, fontweight='bold')
axes[0, 0].set_title('Âge Moyen par Région', fontsize=14, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3, axis='x')

# BMI moyen par région
bmi_by_region = df.groupby('region')['bmi'].mean().sort_values()
axes[0, 1].barh(bmi_by_region.index, bmi_by_region.values, alpha=0.7,
               edgecolor='black', color='coral')
axes[0, 1].set_xlabel('BMI Moyen', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Région', fontsize=12, fontweight='bold')
axes[0, 1].set_title('BMI Moyen par Région', fontsize=14, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3, axis='x')

# Proportion de fumeurs par région
smoker_by_region = df.groupby('region')['smoker'].apply(
    lambda x: (x == 'yes').sum() / len(x) * 100).sort_values()
axes[1, 0].barh(smoker_by_region.index, smoker_by_region.values, alpha=0.7,
               edgecolor='black', color='lightcoral')
axes[1, 0].set_xlabel('Proportion de Fumeurs (%)', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Région', fontsize=12, fontweight='bold')
axes[1, 0].set_title('Proportion de Fumeurs par Région', fontsize=14, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3, axis='x')

# Nombre moyen d'enfants par région
children_by_region = df.groupby('region')['children'].mean().sort_values()
axes[1, 1].barh(children_by_region.index, children_by_region.values, alpha=0.7,
               edgecolor='black', color='lightgreen')
axes[1, 1].set_xlabel('Nombre Moyen d\'Enfants', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Région', fontsize=12, fontweight='bold')
axes[1, 1].set_title('Nombre Moyen d\'Enfants par Région', fontsize=14, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/02_comparaisons_regionales.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 02_comparaisons_regionales.png")

# Visualisation 3: Heatmap région × fumeur
pivot_table = df.pivot_table(values='charges', index='region', columns='smoker', aggfunc='mean')

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=1,
           cbar_kws={'label': 'Charges Moyennes ($)'})
plt.title('Charges Moyennes par Région et Statut Fumeur', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Statut Fumeur', fontsize=12, fontweight='bold')
plt.ylabel('Région', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/03_heatmap_region_fumeur.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Sauvegardé: 03_heatmap_region_fumeur.png")

# ============================================================================
# 6. RÉSUMÉ DE L'ANALYSE RÉGIONALE
# ============================================================================

print("\n" + "="*80)
print("RÉSUMÉ DE L'ANALYSE RÉGIONALE")
print("="*80)

print(f"\n✓ Régions analysées: {df['region'].nunique()}")
print(f"✓ Test ANOVA effectué: {'Différences significatives' if p_value < 0.05 else 'Pas de différence significative'}")
print(f"✓ Région la plus chère: {region_means.index[0]} (${region_means.values[0]:.2f})")
print(f"✓ Région la moins chère: {region_means.index[-1]} (${region_means.values[-1]:.2f})")
print(f"✓ Écart maximal: ${region_means.values[0] - region_means.values[-1]:.2f}")
print(f"✓ Visualisations créées: 3")
print(f"✓ Fichiers sauvegardés dans: {OUTPUT_DIR}/")

print("\n" + "="*80)
print("ANALYSE RÉGIONALE TERMINÉE AVEC SUCCÈS!")
print("="*80)

