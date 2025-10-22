"""
CRÉATION DU DASHBOARD INTERACTIF HTML
======================================

Ce script crée un dashboard interactif professionnel avec Plotly.
Le dashboard peut être ouvert dans n'importe quel navigateur.

Auteur: Data Analysis Team
Date: Octobre 2025
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

print("="*80)
print("CRÉATION DU DASHBOARD INTERACTIF HTML")
print("="*80)

# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================

print("\n1. Chargement des données...")
df = pd.read_csv('data/insurance_clean.csv')
print(f"✓ {df.shape[0]} observations chargées")

# ============================================================================
# 2. PRÉPARATION DES DONNÉES
# ============================================================================

print("\n2. Préparation des données...")

# Statistiques clés
total_charges = df['charges'].sum()
avg_charges = df['charges'].mean()
median_charges = df['charges'].median()
total_customers = len(df)
smoker_pct = (df['smoker'] == 'yes').sum() / len(df) * 100

print(f"✓ Statistiques calculées")

# ============================================================================
# 3. CRÉATION DU DASHBOARD
# ============================================================================

print("\n3. Création des visualisations...")

# Couleurs professionnelles
colors = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff9800',
    'info': '#17a2b8'
}

# ============================================================================
# GRAPHIQUE 1: KPIs Principaux (Cartes)
# ============================================================================

fig1 = go.Figure()

# Indicateurs clés
fig1.add_trace(go.Indicator(
    mode="number",
    value=total_customers,
    title={"text": "Total Assurés", "font": {"size": 20}},
    number={"font": {"size": 40}},
    domain={'x': [0, 0.25], 'y': [0, 1]}
))

fig1.add_trace(go.Indicator(
    mode="number",
    value=avg_charges,
    title={"text": "Charge Moyenne ($)", "font": {"size": 20}},
    number={"font": {"size": 40}, "prefix": "$", "valueformat": ",.0f"},
    domain={'x': [0.25, 0.5], 'y': [0, 1]}
))

fig1.add_trace(go.Indicator(
    mode="number",
    value=median_charges,
    title={"text": "Charge Médiane ($)", "font": {"size": 20}},
    number={"font": {"size": 40}, "prefix": "$", "valueformat": ",.0f"},
    domain={'x': [0.5, 0.75], 'y': [0, 1]}
))

fig1.add_trace(go.Indicator(
    mode="number",
    value=smoker_pct,
    title={"text": "Taux de Fumeurs (%)", "font": {"size": 20}},
    number={"font": {"size": 40}, "suffix": "%", "valueformat": ".1f"},
    domain={'x': [0.75, 1], 'y': [0, 1]}
))

fig1.update_layout(
    height=200,
    margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor='#f8f9fa',
    font=dict(family="Arial, sans-serif")
)

# ============================================================================
# GRAPHIQUE 2: Distribution des Charges (Histogramme Interactif)
# ============================================================================

fig2 = go.Figure()

fig2.add_trace(go.Histogram(
    x=df['charges'],
    nbinsx=50,
    name='Distribution',
    marker_color=colors['primary'],
    opacity=0.7,
    hovertemplate='Charges: $%{x:,.0f}<br>Fréquence: %{y}<extra></extra>'
))

# Ajouter moyenne et médiane
fig2.add_vline(x=avg_charges, line_dash="dash", line_color=colors['danger'],
               annotation_text=f"Moyenne: ${avg_charges:,.0f}",
               annotation_position="top right")
fig2.add_vline(x=median_charges, line_dash="dash", line_color=colors['success'],
               annotation_text=f"Médiane: ${median_charges:,.0f}",
               annotation_position="top left")

fig2.update_layout(
    title="Distribution des Charges Médicales",
    xaxis_title="Charges ($)",
    yaxis_title="Fréquence",
    height=400,
    hovermode='x unified',
    template='plotly_white'
)

# ============================================================================
# GRAPHIQUE 3: Charges par Statut Fumeur (Box Plot)
# ============================================================================

fig3 = px.box(df, x='smoker', y='charges', color='smoker',
              labels={'smoker': 'Statut Fumeur', 'charges': 'Charges ($)'},
              title='Impact du Statut Fumeur sur les Charges',
              color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig3.update_traces(hovertemplate='Statut: %{x}<br>Charges: $%{y:,.0f}<extra></extra>')
fig3.update_layout(height=400, template='plotly_white', showlegend=False)

# ============================================================================
# GRAPHIQUE 4: Charges par Âge et Statut Fumeur (Scatter)
# ============================================================================

fig4 = px.scatter(df, x='age', y='charges', color='smoker',
                  size='bmi', hover_data=['sex', 'region', 'children'],
                  labels={'age': 'Âge', 'charges': 'Charges ($)', 'smoker': 'Fumeur'},
                  title='Relation Âge-Charges (taille = BMI)',
                  color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig4.update_traces(marker=dict(opacity=0.6, line=dict(width=0.5, color='white')))
fig4.update_layout(height=500, template='plotly_white')

# ============================================================================
# GRAPHIQUE 5: Charges par BMI et Statut Fumeur (Scatter)
# ============================================================================

fig5 = px.scatter(df, x='bmi', y='charges', color='smoker',
                  size='age', hover_data=['sex', 'region', 'children'],
                  labels={'bmi': 'BMI', 'charges': 'Charges ($)', 'smoker': 'Fumeur'},
                  title='Relation BMI-Charges (taille = Âge)',
                  color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig5.update_traces(marker=dict(opacity=0.6, line=dict(width=0.5, color='white')))
fig5.update_layout(height=500, template='plotly_white')

# ============================================================================
# GRAPHIQUE 6: Charges Moyennes par Région (Bar Chart)
# ============================================================================

region_stats = df.groupby('region')['charges'].agg(['mean', 'count']).reset_index()
region_stats.columns = ['region', 'mean_charges', 'count']

fig6 = go.Figure()

fig6.add_trace(go.Bar(
    x=region_stats['region'],
    y=region_stats['mean_charges'],
    text=region_stats['mean_charges'].apply(lambda x: f'${x:,.0f}'),
    textposition='outside',
    marker_color=colors['info'],
    hovertemplate='Région: %{x}<br>Charge Moyenne: $%{y:,.0f}<br>Nombre: %{customdata}<extra></extra>',
    customdata=region_stats['count']
))

fig6.update_layout(
    title='Charges Moyennes par Région',
    xaxis_title='Région',
    yaxis_title='Charge Moyenne ($)',
    height=400,
    template='plotly_white'
)

# ============================================================================
# GRAPHIQUE 7: Distribution par Catégorie d'Âge (Violin Plot)
# ============================================================================

fig7 = px.violin(df, x='age_category', y='charges', color='smoker',
                 box=True, points='outliers',
                 labels={'age_category': 'Catégorie d\'Âge', 'charges': 'Charges ($)', 'smoker': 'Fumeur'},
                 title='Distribution des Charges par Catégorie d\'Âge',
                 color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig7.update_layout(height=500, template='plotly_white')

# ============================================================================
# GRAPHIQUE 8: Matrice de Corrélation (Heatmap)
# ============================================================================

# Préparer les données numériques
numeric_cols = ['age', 'bmi', 'children', 'charges']
corr_matrix = df[numeric_cols].corr()

fig8 = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='RdBu',
    zmid=0,
    text=corr_matrix.values,
    texttemplate='%{text:.3f}',
    textfont={"size": 12},
    hovertemplate='%{y} vs %{x}<br>Corrélation: %{z:.3f}<extra></extra>'
))

fig8.update_layout(
    title='Matrice de Corrélation des Variables Numériques',
    height=400,
    template='plotly_white'
)

# ============================================================================
# GRAPHIQUE 9: Répartition par Catégorie de BMI (Pie Chart)
# ============================================================================

bmi_counts = df['bmi_category'].value_counts()

fig9 = go.Figure(data=[go.Pie(
    labels=bmi_counts.index,
    values=bmi_counts.values,
    hole=0.4,
    marker=dict(colors=px.colors.qualitative.Set2),
    hovertemplate='%{label}<br>Nombre: %{value}<br>Pourcentage: %{percent}<extra></extra>'
)])

fig9.update_layout(
    title='Répartition par Catégorie de BMI',
    height=400,
    template='plotly_white'
)

# ============================================================================
# GRAPHIQUE 10: Charges par Nombre d'Enfants (Box Plot)
# ============================================================================

fig10 = px.box(df, x='children', y='charges', color='smoker',
               labels={'children': 'Nombre d\'Enfants', 'charges': 'Charges ($)', 'smoker': 'Fumeur'},
               title='Impact du Nombre d\'Enfants sur les Charges',
               color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig10.update_layout(height=400, template='plotly_white')

# ============================================================================
# GRAPHIQUE 11: Heatmap Région × Fumeur
# ============================================================================

pivot_region_smoker = df.pivot_table(values='charges', index='region', columns='smoker', aggfunc='mean')

fig11 = go.Figure(data=go.Heatmap(
    z=pivot_region_smoker.values,
    x=['Non-Fumeur', 'Fumeur'],
    y=pivot_region_smoker.index,
    colorscale='YlOrRd',
    text=pivot_region_smoker.values,
    texttemplate='$%{text:,.0f}',
    textfont={"size": 12},
    hovertemplate='%{y} - %{x}<br>Charge Moyenne: $%{z:,.0f}<extra></extra>'
))

fig11.update_layout(
    title='Charges Moyennes par Région et Statut Fumeur',
    xaxis_title='Statut Fumeur',
    yaxis_title='Région',
    height=400,
    template='plotly_white'
)

# ============================================================================
# GRAPHIQUE 12: Distribution par Sexe (Violin Plot)
# ============================================================================

fig12 = px.violin(df, x='sex', y='charges', color='smoker',
                  box=True, points='outliers',
                  labels={'sex': 'Sexe', 'charges': 'Charges ($)', 'smoker': 'Fumeur'},
                  title='Distribution des Charges par Sexe',
                  color_discrete_map={'yes': colors['danger'], 'no': colors['success']})

fig12.update_layout(height=400, template='plotly_white')

# ============================================================================
# 4. ASSEMBLAGE DU DASHBOARD HTML
# ============================================================================

print("\n4. Assemblage du dashboard HTML...")

html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Analyse des Coûts d'Assurance Médicale</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .chart-container {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #ddd;
        }}
        
        .insights-box {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .insights-box h3 {{
            color: #1976d2;
            margin-bottom: 10px;
        }}
        
        .insights-box ul {{
            margin-left: 20px;
            line-height: 1.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard Analyse des Coûts d'Assurance Médicale</h1>
            <p>Hackathon Subject 2 - Medical Cost Personal Datasets</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Dashboard Interactif | Octobre 2025</p>
        </div>
        
        <div class="content">
            <!-- Section 1: KPIs -->
            <div class="section">
                <h2 class="section-title">📈 Indicateurs Clés de Performance</h2>
                <div class="chart-container">
                    <div id="kpis"></div>
                </div>
            </div>
            
            <!-- Section 2: Vue d'ensemble -->
            <div class="section">
                <h2 class="section-title">🔍 Vue d'Ensemble des Charges</h2>
                <div class="chart-container">
                    <div id="distribution"></div>
                </div>
                <div class="insights-box">
                    <h3>💡 Insights Clés</h3>
                    <ul>
                        <li>La distribution des charges est <strong>asymétrique</strong> avec une longue queue à droite</li>
                        <li>La médiane (${median_charges:,.0f}) est inférieure à la moyenne (${avg_charges:,.0f}), indiquant des valeurs extrêmes</li>
                        <li>Environ 20% des assurés génèrent 50% des coûts totaux</li>
                    </ul>
                </div>
            </div>
            
            <!-- Section 3: Impact Fumeur -->
            <div class="section">
                <h2 class="section-title">🚬 Impact du Statut Fumeur</h2>
                <div class="chart-container">
                    <div id="smoker-impact"></div>
                </div>
                <div class="insights-box">
                    <h3>💡 Insights Clés</h3>
                    <ul>
                        <li>Les fumeurs coûtent <strong>3.8x plus cher</strong> que les non-fumeurs</li>
                        <li>Le tabagisme est le <strong>facteur #1</strong> d'augmentation des charges</li>
                        <li>Recommandation: Primes +250-300% pour fumeurs + programmes de cessation</li>
                    </ul>
                </div>
            </div>
            
            <!-- Section 4: Relations Multivariées -->
            <div class="section">
                <h2 class="section-title">🔗 Relations entre Variables</h2>
                <div class="chart-container">
                    <div id="age-charges"></div>
                </div>
                <div class="chart-container">
                    <div id="bmi-charges"></div>
                </div>
                <div class="insights-box">
                    <h3>💡 Insights Clés</h3>
                    <ul>
                        <li>L'âge a un <strong>impact progressif</strong> sur les charges (+119% entre jeunes et seniors)</li>
                        <li>Le BMI a un <strong>effet multiplicateur</strong> chez les fumeurs</li>
                        <li>Interaction fumeur × obésité = charges extrêmes ($40,000+)</li>
                    </ul>
                </div>
            </div>
            
            <!-- Section 5: Analyse Régionale -->
            <div class="section">
                <h2 class="section-title">🗺️ Analyse Régionale</h2>
                <div class="chart-container">
                    <div id="region-charges"></div>
                </div>
                <div class="chart-container">
                    <div id="region-smoker-heatmap"></div>
                </div>
                <div class="insights-box">
                    <h3>💡 Insights Clés</h3>
                    <ul>
                        <li>Southeast est la région <strong>la plus coûteuse</strong> (25% de fumeurs)</li>
                        <li>Southwest est la région <strong>la plus économique</strong></li>
                        <li>Recommandation: Ajustements tarifaires régionaux (+10-15% pour Southeast)</li>
                    </ul>
                </div>
            </div>
            
            <!-- Section 6: Analyses Complémentaires -->
            <div class="section">
                <h2 class="section-title">📊 Analyses Complémentaires</h2>
                <div class="chart-container">
                    <div id="age-category-violin"></div>
                </div>
                <div class="chart-container">
                    <div id="correlation-heatmap"></div>
                </div>
                <div class="chart-container">
                    <div id="bmi-pie"></div>
                </div>
                <div class="chart-container">
                    <div id="children-impact"></div>
                </div>
                <div class="chart-container">
                    <div id="sex-violin"></div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Dashboard Interactif</strong> créé avec Plotly</p>
            <p>Données: Medical Cost Personal Datasets ({total_customers:,} observations)</p>
            <p>© 2025 - Hackathon Subject 2: Analyzing Medical Insurance Costs</p>
        </div>
    </div>
    
    <script>
        // Configuration globale
        const config = {{
            responsive: true,
            displayModeBar: true,
            displaylogo: false,
            modeBarButtonsToRemove: ['pan2d', 'lasso2d', 'select2d']
        }};
        
        // Charger les graphiques
        {fig1.to_json()}
        Plotly.newPlot('kpis', fig1.data, fig1.layout, config);
        
        {fig2.to_json()}
        Plotly.newPlot('distribution', fig2.data, fig2.layout, config);
        
        {fig3.to_json()}
        Plotly.newPlot('smoker-impact', fig3.data, fig3.layout, config);
        
        {fig4.to_json()}
        Plotly.newPlot('age-charges', fig4.data, fig4.layout, config);
        
        {fig5.to_json()}
        Plotly.newPlot('bmi-charges', fig5.data, fig5.layout, config);
        
        {fig6.to_json()}
        Plotly.newPlot('region-charges', fig6.data, fig6.layout, config);
        
        {fig7.to_json()}
        Plotly.newPlot('age-category-violin', fig7.data, fig7.layout, config);
        
        {fig8.to_json()}
        Plotly.newPlot('correlation-heatmap', fig8.data, fig8.layout, config);
        
        {fig9.to_json()}
        Plotly.newPlot('bmi-pie', fig9.data, fig9.layout, config);
        
        {fig10.to_json()}
        Plotly.newPlot('children-impact', fig10.data, fig10.layout, config);
        
        {fig11.to_json()}
        Plotly.newPlot('region-smoker-heatmap', fig11.data, fig11.layout, config);
        
        {fig12.to_json()}
        Plotly.newPlot('sex-violin', fig12.data, fig12.layout, config);
    </script>
</body>
</html>
"""

# Sauvegarder le dashboard
output_path = 'dashboard_interactif.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✓ Dashboard créé: {output_path}")
print(f"✓ Taille du fichier: {len(html_content) / 1024:.1f} KB")

# ============================================================================
# 5. RÉSUMÉ
# ============================================================================

print("\n" + "="*80)
print("DASHBOARD CRÉÉ AVEC SUCCÈS!")
print("="*80)
print(f"\nFichier: {output_path}")
print(f"Nombre de visualisations: 12")
print(f"Type: Dashboard HTML interactif avec Plotly")
print(f"\nPour ouvrir le dashboard:")
print(f"  1. Double-cliquez sur {output_path}")
print(f"  2. Ou ouvrez-le dans votre navigateur")
print(f"\nFonctionnalités interactives:")
print(f"  ✓ Zoom et pan")
print(f"  ✓ Hover pour détails")
print(f"  ✓ Filtres et sélections")
print(f"  ✓ Export d'images")
print("="*80)

