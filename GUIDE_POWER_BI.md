# 📊 Guide Complet : Créer le Dashboard Power BI

## 🎯 Objectif

Créer un dashboard professionnel Power BI en **30 minutes** pour présenter l'analyse des coûts d'assurance médicale.

---

## 📥 Étape 1 : Installation de Power BI Desktop (5 minutes)

### Téléchargement

1. **Allez sur** : https://powerbi.microsoft.com/fr-fr/desktop/
2. **Cliquez sur** "Télécharger gratuitement"
3. **Installez** Power BI Desktop (fichier .exe)
4. **Lancez** l'application

> ⚠️ **Note** : Power BI Desktop est **gratuit** et fonctionne sur Windows uniquement.  
> Pour Mac : Utilisez Parallels Desktop ou le dashboard HTML.

---

## 📂 Étape 2 : Préparation des Données (2 minutes)

### Fichier à Utiliser

Utilisez le fichier : **`data/insurance_clean.csv`**

Ce fichier contient :
- ✅ Données nettoyées et prétraitées
- ✅ 7 nouvelles features créées
- ✅ 1,337 observations
- ✅ 17 colonnes

### Vérification

Ouvrez le fichier dans Excel pour vérifier :
- Colonnes : age, sex, bmi, children, smoker, region, charges, age_category, bmi_category, etc.
- Pas de valeurs manquantes
- Format correct

---

## 🚀 Étape 3 : Import des Données dans Power BI (3 minutes)

### 3.1 Ouvrir Power BI Desktop

1. **Lancez** Power BI Desktop
2. **Fermez** l'écran de démarrage si nécessaire

### 3.2 Importer le CSV

1. **Cliquez sur** "Obtenir les données" (Get Data) dans le ruban
2. **Sélectionnez** "Texte/CSV"
3. **Naviguez vers** `data/insurance_clean.csv`
4. **Cliquez sur** "Ouvrir"

### 3.3 Vérifier les Données

1. Power BI affiche un **aperçu** des données
2. **Vérifiez** que les colonnes sont correctement détectées
3. **Cliquez sur** "Charger" (Load)

✅ **Les données sont maintenant chargées dans Power BI !**

---

## 🎨 Étape 4 : Création du Dashboard (20 minutes)

### Page 1 : Vue d'Ensemble

#### 4.1 Ajouter des Cartes KPI (5 minutes)

**KPI 1 : Total Assurés**

1. **Cliquez sur** "Carte" dans les visualisations
2. **Glissez** "age" dans "Champs"
3. **Changez l'agrégation** : Clic droit > "Nombre (distinct)"
4. **Formatez** :
   - Titre : "Total Assurés"
   - Taille de police : 40
   - Couleur : Bleu (#1f77b4)

**KPI 2 : Charge Moyenne**

1. **Ajoutez** une nouvelle carte
2. **Glissez** "charges" dans "Champs"
3. **L'agrégation** est automatiquement "Moyenne"
4. **Formatez** :
   - Titre : "Charge Moyenne ($)"
   - Format : Devise ($)
   - Taille de police : 40

**KPI 3 : Charge Médiane**

1. **Ajoutez** une nouvelle carte
2. **Glissez** "charges" dans "Champs"
3. **Changez l'agrégation** : Clic droit > "Médiane"
4. **Formatez** : Titre "Charge Médiane ($)"

**KPI 4 : Taux de Fumeurs**

1. **Ajoutez** une nouvelle carte
2. **Créez une mesure** :
   - Clic droit sur la table > "Nouvelle mesure"
   - Formule : `Taux Fumeurs = DIVIDE(COUNTROWS(FILTER('insurance_clean', 'insurance_clean'[smoker] = "yes")), COUNTROWS('insurance_clean')) * 100`
3. **Glissez** la mesure dans la carte
4. **Formatez** : Titre "Taux de Fumeurs (%)"

#### 4.2 Histogramme des Charges (3 minutes)

1. **Sélectionnez** "Histogramme" dans les visualisations
2. **Axe X** : charges
3. **Axe Y** : Nombre (count)
4. **Formatez** :
   - Titre : "Distribution des Charges Médicales"
   - Couleur : Bleu
   - Bins : 50

#### 4.3 Box Plot par Statut Fumeur (2 minutes)

1. **Sélectionnez** "Box and Whisker" (si disponible) ou "Graphique en colonnes"
2. **Axe X** : smoker
3. **Axe Y** : charges (Moyenne)
4. **Formatez** :
   - Titre : "Impact du Statut Fumeur"
   - Couleurs : Vert (no), Rouge (yes)

---

### Page 2 : Analyse Détaillée

#### 4.4 Scatter Plot Âge vs Charges (3 minutes)

1. **Sélectionnez** "Nuage de points" (Scatter chart)
2. **Axe X** : age
3. **Axe Y** : charges
4. **Légende** : smoker
5. **Taille** : bmi
6. **Formatez** :
   - Titre : "Relation Âge-Charges (taille = BMI)"
   - Couleurs : Vert (no), Rouge (yes)

#### 4.5 Scatter Plot BMI vs Charges (2 minutes)

1. **Dupliquez** le graphique précédent (Ctrl+C, Ctrl+V)
2. **Changez l'axe X** : bmi
3. **Changez la taille** : age
4. **Formatez** : Titre "Relation BMI-Charges (taille = Âge)"

#### 4.6 Bar Chart par Région (2 minutes)

1. **Sélectionnez** "Graphique en barres"
2. **Axe Y** : region
3. **Axe X** : charges (Moyenne)
4. **Formatez** :
   - Titre : "Charges Moyennes par Région"
   - Tri : Décroissant

#### 4.7 Heatmap Région × Fumeur (3 minutes)

1. **Sélectionnez** "Matrice"
2. **Lignes** : region
3. **Colonnes** : smoker
4. **Valeurs** : charges (Moyenne)
5. **Formatez** :
   - Titre : "Charges par Région et Statut Fumeur"
   - Mise en forme conditionnelle : Échelle de couleurs (Jaune-Orange-Rouge)

---

### Page 3 : Insights et Recommandations

#### 4.8 Ajouter des Zones de Texte

1. **Insérez** une zone de texte
2. **Titre** : "💡 Top 5 Facteurs d'Influence"
3. **Contenu** :
   ```
   1. Statut Fumeur ⭐⭐⭐⭐⭐
      Impact: +$23,616 (+280%)
   
   2. Âge ⭐⭐⭐
      Progression: +119% entre jeunes et seniors
   
   3. BMI ⭐⭐
      Obésité: +45% de charges
   
   4. Région ⭐⭐
      Écart: $2,388 entre régions
   
   5. Nombre d'Enfants ⭐
      Impact faible et non linéaire
   ```

#### 4.9 Ajouter un Tableau de Recommandations

1. **Insérez** un tableau
2. **Colonnes** : Recommandation, Priorité, Impact Estimé
3. **Lignes** :
   - Tarification différenciée fumeurs | Haute | +$12M/an
   - Programmes anti-tabac | Haute | +$8M/an
   - Ajustements régionaux | Moyenne | +$3M/an
   - Offres bas risque | Haute | +$5M/an

---

## 🎨 Étape 5 : Personnalisation et Design (5 minutes)

### 5.1 Thème et Couleurs

1. **Allez dans** "Affichage" > "Thèmes"
2. **Sélectionnez** un thème professionnel (ex: "Executive")
3. **Ou créez** votre palette :
   - Primaire : #1f77b4 (Bleu)
   - Secondaire : #ff7f0e (Orange)
   - Danger : #d62728 (Rouge)
   - Success : #2ca02c (Vert)

### 5.2 Mise en Page

1. **Alignez** les visualisations avec la grille
2. **Espacez** uniformément les éléments
3. **Groupez** les KPIs en haut
4. **Organisez** les graphiques en 2 colonnes

### 5.3 Titres et Labels

1. **Ajoutez** un titre principal : "Dashboard Analyse des Coûts d'Assurance Médicale"
2. **Sous-titre** : "Hackathon Subject 2 - Medical Cost Personal Datasets"
3. **Formatez** : Police Arial, Taille 28, Gras

### 5.4 Filtres Interactifs

1. **Ajoutez** un segment (Slicer) pour "smoker"
2. **Ajoutez** un segment pour "region"
3. **Ajoutez** un segment pour "age_category"
4. **Positionnez** les segments sur le côté gauche

---

## 🔍 Étape 6 : Mesures DAX Avancées (Optionnel - 10 minutes)

### Mesure 1 : Différence Fumeur vs Non-Fumeur

```dax
Écart Fumeur = 
VAR ChargeFumeur = CALCULATE(AVERAGE('insurance_clean'[charges]), 'insurance_clean'[smoker] = "yes")
VAR ChargeNonFumeur = CALCULATE(AVERAGE('insurance_clean'[charges]), 'insurance_clean'[smoker] = "no")
RETURN ChargeFumeur - ChargeNonFumeur
```

### Mesure 2 : Pourcentage au-dessus de la Moyenne

```dax
% Au-dessus Moyenne = 
VAR MoyenneGlobale = AVERAGE('insurance_clean'[charges])
VAR NombreAuDessus = COUNTROWS(FILTER('insurance_clean', 'insurance_clean'[charges] > MoyenneGlobale))
VAR Total = COUNTROWS('insurance_clean')
RETURN DIVIDE(NombreAuDessus, Total) * 100
```

### Mesure 3 : Score de Risque Moyen

```dax
Score Risque Moyen = AVERAGE('insurance_clean'[risk_score])
```

### Utilisation des Mesures

1. **Créez** les mesures (clic droit sur la table > "Nouvelle mesure")
2. **Ajoutez** des cartes pour afficher ces mesures
3. **Formatez** avec des couleurs conditionnelles

---

## 📤 Étape 7 : Export et Partage (2 minutes)

### 7.1 Sauvegarder le Fichier

1. **Fichier** > **Enregistrer sous**
2. **Nom** : `Dashboard_Assurance_Medicale.pbix`
3. **Emplacement** : Dossier du projet

### 7.2 Exporter en PDF (pour présentation)

1. **Fichier** > **Exporter** > **PDF**
2. **Sélectionnez** les pages à exporter
3. **Enregistrez** : `Dashboard_Assurance_Medicale.pdf`

### 7.3 Exporter en PowerPoint

1. **Fichier** > **Exporter** > **PowerPoint**
2. Power BI crée un fichier `.pptx` avec vos visualisations
3. **Utilisez** ce fichier pour votre présentation

### 7.4 Publier sur Power BI Service (Optionnel)

1. **Cliquez sur** "Publier" dans le ruban
2. **Connectez-vous** avec votre compte Microsoft
3. **Sélectionnez** un espace de travail
4. **Partagez** le lien avec votre équipe

---

## 📋 Checklist Finale

Avant la présentation, vérifiez que vous avez :

- [ ] **3 pages** : Vue d'ensemble, Analyse détaillée, Insights
- [ ] **4 KPIs** en haut de la première page
- [ ] **Histogramme** des charges
- [ ] **Box plot** fumeur vs non-fumeur
- [ ] **2 scatter plots** (âge et BMI)
- [ ] **Bar chart** par région
- [ ] **Heatmap** région × fumeur
- [ ] **Filtres interactifs** (smoker, region, age_category)
- [ ] **Zones de texte** avec insights
- [ ] **Tableau** de recommandations
- [ ] **Thème** professionnel appliqué
- [ ] **Titres** et labels clairs
- [ ] **Fichier sauvegardé** (.pbix)
- [ ] **Export PDF** pour backup

---

## 🎯 Astuces pour une Présentation Réussie

### Pendant la Création

1. **Testez** l'interactivité : Cliquez sur les éléments pour voir les filtres croisés
2. **Vérifiez** les couleurs : Cohérentes et professionnelles
3. **Simplifiez** : Pas trop de visualisations sur une page
4. **Annotez** : Ajoutez des flèches et des zones de texte pour guider

### Pendant la Présentation

1. **Commencez** par la vue d'ensemble (Page 1)
2. **Utilisez** les filtres interactifs pour montrer l'interactivité
3. **Passez** à l'analyse détaillée (Page 2)
4. **Terminez** par les insights et recommandations (Page 3)
5. **Soyez prêt** à répondre aux questions avec les données

### Storytelling

1. **Introduction** : "Nous avons analysé 1,337 dossiers d'assurance..."
2. **Problématique** : "Quels sont les facteurs qui influencent les coûts ?"
3. **Découverte** : "Le statut fumeur est le facteur #1 avec +280% de charges"
4. **Insights** : "Voici les 5 facteurs clés..."
5. **Recommandations** : "Nous proposons 4 actions prioritaires..."
6. **Impact** : "Amélioration estimée de +$23M/an"

---

## 🆘 Résolution de Problèmes

### Problème 1 : "Power BI ne s'installe pas"

**Solution** : Vérifiez que vous avez Windows 10/11 et les droits administrateur.

### Problème 2 : "Les données ne se chargent pas"

**Solution** : Vérifiez que le fichier CSV est bien encodé en UTF-8.

### Problème 3 : "Les visualisations sont lentes"

**Solution** : Réduisez le nombre de points dans les scatter plots (filtrez sur un échantillon).

### Problème 4 : "Je ne trouve pas une visualisation"

**Solution** : Cliquez sur "..." dans les visualisations > "Obtenir plus de visuels" > Téléchargez depuis le marketplace.

### Problème 5 : "Les couleurs ne correspondent pas"

**Solution** : Allez dans "Format" > "Couleurs des données" > Personnalisez manuellement.

---

## 📚 Ressources Complémentaires

### Documentation Officielle

- **Power BI Desktop** : https://docs.microsoft.com/fr-fr/power-bi/
- **Formules DAX** : https://dax.guide/
- **Galerie de visuels** : https://appsource.microsoft.com/fr-fr/marketplace/apps?product=power-bi-visuals

### Tutoriels Vidéo

- **Microsoft Learn** : https://learn.microsoft.com/fr-fr/training/powerplatform/power-bi
- **YouTube** : Recherchez "Power BI tutorial français"

### Communauté

- **Forum Power BI** : https://community.powerbi.com/
- **Reddit** : r/PowerBI

---

## ✅ Résumé

**Temps total** : 30-40 minutes

**Résultat** : Dashboard professionnel avec :
- 4 KPIs
- 8+ visualisations interactives
- 3 pages organisées
- Insights et recommandations
- Export PDF/PowerPoint

**Avantages Power BI** :
- ✅ Gratuit
- ✅ Professionnel
- ✅ Interactif
- ✅ Reconnu en entreprise
- ✅ Facile à partager

**Bonne chance pour votre présentation ! 🚀**

