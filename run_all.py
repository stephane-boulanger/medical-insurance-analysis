"""
RUN ALL - PIPELINE COMPLET D'ANALYSE
======================================

Ce script exécute toutes les étapes de l'analyse dans l'ordre.

Étapes:
1. Exploratory Data Analysis (EDA)
2. Data Preprocessing
3. Feature Exploration
4. Visualizations
5. Regional Analysis (Bonus)

Usage:
    python run_all.py

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import subprocess
import sys
import time
import os

def run_script(script_path, script_name):
    """
    Exécute un script Python et affiche le résultat.
    
    Args:
        script_path (str): Chemin vers le script
        script_name (str): Nom du script pour l'affichage
    """
    print("\n" + "="*80)
    print(f"EXÉCUTION: {script_name}")
    print("="*80)
    
    start_time = time.time()
    
    try:
        # Changer le répertoire de travail vers scripts/
        original_dir = os.getcwd()
        os.chdir('scripts')
        
        # Exécuter le script
        result = subprocess.run([sys.executable, os.path.basename(script_path)], 
                              capture_output=False, 
                              text=True,
                              check=True)
        
        # Retourner au répertoire original
        os.chdir(original_dir)
        
        elapsed_time = time.time() - start_time
        
        print("\n" + "-"*80)
        print(f"✓ {script_name} terminé avec succès!")
        print(f"  Temps d'exécution: {elapsed_time:.2f} secondes")
        print("-"*80)
        
        return True
        
    except subprocess.CalledProcessError as e:
        # Retourner au répertoire original en cas d'erreur
        os.chdir(original_dir)
        
        elapsed_time = time.time() - start_time
        
        print("\n" + "-"*80)
        print(f"❌ Erreur lors de l'exécution de {script_name}")
        print(f"  Code d'erreur: {e.returncode}")
        print(f"  Temps écoulé: {elapsed_time:.2f} secondes")
        print("-"*80)
        
        return False

def main():
    """
    Fonction principale qui exécute tous les scripts dans l'ordre.
    """
    print("\n" + "="*80)
    print("PIPELINE COMPLET D'ANALYSE DES COÛTS D'ASSURANCE MÉDICALE")
    print("="*80)
    print("\nCe script va exécuter toutes les étapes de l'analyse:")
    print("  1. Exploratory Data Analysis (EDA)")
    print("  2. Data Preprocessing")
    print("  3. Feature Exploration")
    print("  4. Visualizations (Matplotlib & Seaborn)")
    print("  5. Regional Analysis (Bonus)")
    print("\nCela peut prendre plusieurs minutes...")
    print("="*80)
    
    # Définir les scripts à exécuter
    scripts = [
        ("scripts/1_eda.py", "1. Exploratory Data Analysis (EDA)"),
        ("scripts/2_preprocessing.py", "2. Data Preprocessing"),
        ("scripts/3_feature_exploration.py", "3. Feature Exploration"),
        ("scripts/4_visualizations.py", "4. Visualizations"),
        ("scripts/5_regional_analysis.py", "5. Regional Analysis (Bonus)")
    ]
    
    # Compteurs
    total_scripts = len(scripts)
    successful = 0
    failed = 0
    
    # Temps de départ global
    global_start_time = time.time()
    
    # Exécuter chaque script
    for script_path, script_name in scripts:
        if run_script(script_path, script_name):
            successful += 1
        else:
            failed += 1
            print(f"\n⚠ Erreur détectée. Arrêt du pipeline.")
            break
    
    # Temps total
    total_time = time.time() - global_start_time
    
    # Résumé final
    print("\n" + "="*80)
    print("RÉSUMÉ DE L'EXÉCUTION")
    print("="*80)
    print(f"\nScripts exécutés: {successful + failed}/{total_scripts}")
    print(f"  ✓ Réussis: {successful}")
    print(f"  ❌ Échoués: {failed}")
    print(f"\nTemps total d'exécution: {total_time:.2f} secondes ({total_time/60:.2f} minutes)")
    
    # Vérifier les fichiers générés
    print("\n" + "-"*80)
    print("FICHIERS GÉNÉRÉS")
    print("-"*80)
    
    # Dataset nettoyé
    if os.path.exists('data/insurance_clean.csv'):
        size = os.path.getsize('data/insurance_clean.csv') / 1024
        print(f"✓ Dataset nettoyé: data/insurance_clean.csv ({size:.2f} KB)")
    else:
        print("❌ Dataset nettoyé non trouvé")
    
    if os.path.exists('data/insurance_clean_essential.csv'):
        size = os.path.getsize('data/insurance_clean_essential.csv') / 1024
        print(f"✓ Dataset essentiel: data/insurance_clean_essential.csv ({size:.2f} KB)")
    
    # Visualisations
    viz_dirs = ['visualizations/eda', 'visualizations/features', 'visualizations/regional']
    total_viz = 0
    
    for viz_dir in viz_dirs:
        if os.path.exists(viz_dir):
            files = [f for f in os.listdir(viz_dir) if f.endswith('.png')]
            total_viz += len(files)
            print(f"✓ {viz_dir}: {len(files)} visualisations")
    
    print(f"\nTotal de visualisations créées: {total_viz}")
    
    # Message final
    print("\n" + "="*80)
    if failed == 0:
        print("🎉 PIPELINE TERMINÉ AVEC SUCCÈS!")
    else:
        print("⚠ PIPELINE TERMINÉ AVEC DES ERREURS")
    print("="*80)
    
    if failed == 0:
        print("\nProchaines étapes:")
        print("  1. Consultez les visualisations dans le dossier visualizations/")
        print("  2. Examinez le dataset nettoyé: data/insurance_clean.csv")
        print("  3. Créez votre présentation PowerPoint avec les insights")
        print("  4. Préparez votre rapport final")
    
    print("\n" + "="*80)
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

