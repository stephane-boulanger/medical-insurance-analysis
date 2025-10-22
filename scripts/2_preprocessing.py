"""
2. DATA PREPROCESSING
======================

Ce script effectue le prétraitement et le nettoyage des données.

Objectifs:
- Gérer les valeurs manquantes (si présentes)
- Encoder les variables catégorielles
- Normaliser les variables numériques
- Créer de nouvelles features
- Sauvegarder le dataset nettoyé

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

# Configuration
pd.set_option('display.max_columns', None)

# Chemins
DATA_PATH = '../data/insurance.csv'
OUTPUT_PATH = '../data/insurance_clean.csv'

print("="*80)
print("PRÉTRAITEMENT DES DONNÉES")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. CHARGEMENT DES DONNÉES")
print("-" * 40)

df = pd.read_csv(DATA_PATH)
print(f"✓ Dataset chargé: {df.shape[0]} lignes × {df.shape[1]} colonnes")

# Créer une copie pour le preprocessing
df_clean = df.copy()

# ============================================================================
# 2. GESTION DES VALEURS MANQUANTES
# ============================================================================

print("\n2. GESTION DES VALEURS MANQUANTES")
print("-" * 40)

missing_before = df_clean.isnull().sum().sum()
print(f"Valeurs manquantes avant traitement: {missing_before}")

if missing_before > 0:
    print("\nStratégie de remplissage:")
    
    # Pour les variables numériques: remplir avec la médiane
    numerical_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        if df_clean[col].isnull().sum() > 0:
            median_val = df_clean[col].median()
            df_clean[col].fillna(median_val, inplace=True)
            print(f"  - {col}: rempli avec la médiane ({median_val:.2f})")
    
    # Pour les variables catégorielles: remplir avec le mode
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df_clean[col].isnull().sum() > 0:
            mode_val = df_clean[col].mode()[0]
            df_clean[col].fillna(mode_val, inplace=True)
            print(f"  - {col}: rempli avec le mode ({mode_val})")
    
    missing_after = df_clean.isnull().sum().sum()
    print(f"\nValeurs manquantes après traitement: {missing_after}")
else:
    print("✓ Aucune valeur manquante détectée!")

# ============================================================================
# 3. SUPPRESSION DES DOUBLONS
# ============================================================================

print("\n3. SUPPRESSION DES DOUBLONS")
print("-" * 40)

duplicates_before = df_clean.duplicated().sum()
print(f"Doublons avant traitement: {duplicates_before}")

if duplicates_before > 0:
    df_clean.drop_duplicates(inplace=True)
    duplicates_after = df_clean.duplicated().sum()
    print(f"Doublons après traitement: {duplicates_after}")
    print(f"✓ {duplicates_before} doublons supprimés")
else:
    print("✓ Aucun doublon détecté!")

# ============================================================================
# 4. ENCODAGE DES VARIABLES CATÉGORIELLES
# ============================================================================

print("\n4. ENCODAGE DES VARIABLES CATÉGORIELLES")
print("-" * 40)

# Label Encoding pour créer des versions encodées
label_encoders = {}
categorical_cols = ['sex', 'smoker', 'region']

for col in categorical_cols:
    le = LabelEncoder()
    df_clean[f'{col}_encoded'] = le.fit_transform(df_clean[col])
    label_encoders[col] = le
    
    print(f"\n{col.upper()}:")
    mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    for key, value in mapping.items():
        print(f"  {key} -> {value}")

# One-Hot Encoding (créer des colonnes binaires)
print("\nOne-Hot Encoding:")
df_encoded = pd.get_dummies(df_clean, columns=['sex', 'smoker', 'region'], 
                            prefix=['sex', 'smoker', 'region'], drop_first=False)

print(f"✓ Nouvelles colonnes créées: {df_encoded.shape[1] - df_clean.shape[1]}")

# Fusionner les colonnes encodées dans df_clean
for col in df_encoded.columns:
    if col not in df_clean.columns:
        df_clean[col] = df_encoded[col]

# ============================================================================
# 5. NORMALISATION DES VARIABLES NUMÉRIQUES
# ============================================================================

print("\n5. NORMALISATION DES VARIABLES NUMÉRIQUES")
print("-" * 40)

# Sélectionner les variables à normaliser
numerical_cols_to_scale = ['age', 'bmi', 'children', 'charges']

# Créer le scaler
scaler = StandardScaler()

# Normaliser et créer de nouvelles colonnes
scaled_data = scaler.fit_transform(df_clean[numerical_cols_to_scale])
scaled_df = pd.DataFrame(scaled_data, 
                         columns=[f'{col}_scaled' for col in numerical_cols_to_scale],
                         index=df_clean.index)

# Ajouter les colonnes normalisées
df_clean = pd.concat([df_clean, scaled_df], axis=1)

print("✓ Variables normalisées (StandardScaler):")
for col in numerical_cols_to_scale:
    print(f"  - {col} -> {col}_scaled")

print("\nStatistiques après normalisation:")
print(scaled_df.describe().round(3))

# ============================================================================
# 6. CRÉATION DE NOUVELLES FEATURES
# ============================================================================

print("\n6. CRÉATION DE NOUVELLES FEATURES")
print("-" * 40)

# Feature 1: Catégories d'âge
df_clean['age_category'] = pd.cut(df_clean['age'], 
                                  bins=[0, 25, 35, 45, 55, 100],
                                  labels=['18-25', '26-35', '36-45', '46-55', '56+'])
print("✓ age_category: 5 catégories (18-25, 26-35, 36-45, 46-55, 56+)")

# Feature 2: Catégories de BMI
df_clean['bmi_category'] = pd.cut(df_clean['bmi'],
                                  bins=[0, 18.5, 25, 30, 35, 100],
                                  labels=['Underweight', 'Normal', 'Overweight', 'Obese', 'Extremely Obese'])
print("✓ bmi_category: 5 catégories (Underweight, Normal, Overweight, Obese, Extremely Obese)")

# Feature 3: Interaction smoker × BMI
df_clean['smoker_bmi_interaction'] = df_clean['smoker_encoded'] * df_clean['bmi']
print("✓ smoker_bmi_interaction: Interaction entre statut fumeur et BMI")

# Feature 4: Catégories de charges
df_clean['charges_category'] = pd.cut(df_clean['charges'],
                                      bins=[0, 5000, 10000, 20000, 100000],
                                      labels=['Low', 'Medium', 'High', 'Very High'])
print("✓ charges_category: 4 catégories (Low, Medium, High, Very High)")

# Feature 5: Indicateur de surpoids
df_clean['is_overweight'] = (df_clean['bmi'] >= 25).astype(int)
print("✓ is_overweight: Indicateur binaire (BMI >= 25)")

# Feature 6: Indicateur de famille nombreuse
df_clean['has_many_children'] = (df_clean['children'] >= 3).astype(int)
print("✓ has_many_children: Indicateur binaire (>= 3 enfants)")

# Feature 7: Score de risque composite
df_clean['risk_score'] = 0
df_clean.loc[df_clean['smoker'] == 'yes', 'risk_score'] += 3
df_clean.loc[df_clean['bmi'] >= 30, 'risk_score'] += 2
df_clean.loc[df_clean['age'] >= 50, 'risk_score'] += 1
print("✓ risk_score: Score de risque composite (0-6)")

print(f"\nTotal de nouvelles features créées: 7")

# ============================================================================
# 7. VÉRIFICATION DES DONNÉES NETTOYÉES
# ============================================================================

print("\n7. VÉRIFICATION DES DONNÉES NETTOYÉES")
print("-" * 40)

print(f"\nDimensions finales: {df_clean.shape[0]} lignes × {df_clean.shape[1]} colonnes")
print(f"Valeurs manquantes: {df_clean.isnull().sum().sum()}")
print(f"Doublons: {df_clean.duplicated().sum()}")

print("\nAperçu des nouvelles colonnes:")
new_cols = [col for col in df_clean.columns if col not in df.columns]
print(f"Nombre de nouvelles colonnes: {len(new_cols)}")
print(f"Colonnes: {new_cols[:10]}...")  # Afficher les 10 premières

# ============================================================================
# 8. SAUVEGARDE DU DATASET NETTOYÉ
# ============================================================================

print("\n8. SAUVEGARDE DU DATASET NETTOYÉ")
print("-" * 40)

df_clean.to_csv(OUTPUT_PATH, index=False)
print(f"✓ Dataset nettoyé sauvegardé: {OUTPUT_PATH}")
print(f"  Taille du fichier: {os.path.getsize(OUTPUT_PATH) / 1024:.2f} KB")

# Sauvegarder aussi une version avec seulement les colonnes essentielles
essential_cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges',
                  'age_category', 'bmi_category', 'charges_category', 'risk_score']
df_essential = df_clean[essential_cols]
essential_path = '../data/insurance_clean_essential.csv'
df_essential.to_csv(essential_path, index=False)
print(f"✓ Version essentielle sauvegardée: {essential_path}")

# ============================================================================
# 9. RÉSUMÉ DU PREPROCESSING
# ============================================================================

print("\n" + "="*80)
print("RÉSUMÉ DU PRÉTRAITEMENT")
print("="*80)

print(f"\n✓ Dataset original: {df.shape[0]} × {df.shape[1]}")
print(f"✓ Dataset nettoyé: {df_clean.shape[0]} × {df_clean.shape[1]}")
print(f"✓ Nouvelles features: {len(new_cols)}")
print(f"✓ Variables encodées: {len(categorical_cols)}")
print(f"✓ Variables normalisées: {len(numerical_cols_to_scale)}")
print(f"\n✓ Fichiers générés:")
print(f"  - {OUTPUT_PATH}")
print(f"  - {essential_path}")

print("\n" + "="*80)
print("PRÉTRAITEMENT TERMINÉ AVEC SUCCÈS!")
print("="*80)

# Afficher un aperçu final
print("\nAperçu du dataset nettoyé:")
print(df_clean.head())

