import pandas as pd
import plotly.express as px
import json

# Charger les données nettoyées
df = pd.read_csv('data/insurance_clean.csv')

# Calculer les charges moyennes par région
region_avg_charges = df.groupby('region')['charges'].mean().reset_index()
region_avg_charges.columns = ['Region', 'Average Charges']

# Définir les centroïdes (approximatifs) pour les régions des USA
# Ces coordonnées sont pour placer des marqueurs ou pour une visualisation conceptuelle
# Elles ne sont pas utilisées pour un choropleth direct des états, mais pour un choropleth de régions customisées
region_centroids = {
    'northeast': {'lat': 42.36, 'lon': -71.06, 'full_name': 'Northeast US'},
    'southeast': {'lat': 33.75, 'lon': -84.39, 'full_name': 'Southeast US'},
    'southwest': {'lat': 34.05, 'lon': -118.24, 'full_name': 'Southwest US'},
    'northwest': {'lat': 47.61, 'lon': -122.33, 'full_name': 'Northwest US'}
}

# Ajouter les coordonnées et les noms complets au DataFrame
region_avg_charges['lat'] = region_avg_charges['Region'].map(lambda x: region_centroids[x]['lat'])
region_avg_charges['lon'] = region_avg_charges['Region'].map(lambda x: region_centroids[x]['lon'])
region_avg_charges['Full Region Name'] = region_avg_charges['Region'].map(lambda x: region_centroids[x]['full_name'])

# Créer la carte choropleth des États-Unis
# Comme les régions de votre dataset ne correspondent pas aux états standards, 
# nous allons utiliser une carte des États-Unis et colorer des régions conceptuelles.
# Plotly Express ne permet pas de colorer des régions arbitraires sur une carte choropleth d'états sans un fichier GeoJSON correspondant.
# Une alternative est d'utiliser une carte de type 'scatter_geo' avec des marqueurs colorés ou une carte choropleth par états 
# où les états sont regroupés en régions.

# Pour une carte choropleth par régions (plus complexe sans GeoJSON customisé), 
# nous allons simuler cela en utilisant la carte des USA et en colorant les états 
# qui appartiennent à ces régions. Cela nécessite un mapping état-région.

# Mapping des états aux régions (simplifié pour l'exemple)
state_to_region = {
    'ME': 'northeast', 'NH': 'northeast', 'VT': 'northeast', 'MA': 'northeast', 'RI': 'northeast', 'CT': 'northeast', 'NY': 'northeast', 'PA': 'northeast', 'NJ': 'northeast',
    'DE': 'southeast', 'MD': 'southeast', 'VA': 'southeast', 'NC': 'southeast', 'SC': 'southeast', 'GA': 'southeast', 'FL': 'southeast', 'AL': 'southeast', 'MS': 'southeast', 'LA': 'southeast', 'TN': 'southeast', 'KY': 'southeast', 'WV': 'southeast',
    'TX': 'southwest', 'OK': 'southwest', 'NM': 'southwest', 'AZ': 'southwest', 'NV': 'southwest', 'CA': 'southwest', 'UT': 'southwest', 'CO': 'southwest',
    'WA': 'northwest', 'OR': 'northwest', 'ID': 'northwest', 'MT': 'northwest', 'WY': 'northwest', 'ND': 'northwest', 'SD': 'northwest', 'NE': 'northwest', 'KS': 'northwest'
}

# Créer un DataFrame pour la carte choropleth par état
# Nous allons attribuer la charge moyenne de la région à chaque état de cette région
state_data = pd.DataFrame(list(state_to_region.items()), columns=['State', 'Region'])
state_data = pd.merge(state_data, region_avg_charges, on='Region', how='left')

# Créer la carte choropleth
fig = px.choropleth(
    state_data,
    locations='State',
    locationmode='USA-states',
    color='Average Charges',
    scope='usa',
    color_continuous_scale='Plasma',
    title='Charges Moyennes d\'Assurance par Région aux USA',
    hover_name='Full Region Name',
    hover_data={'State': True, 'Region': False, 'Average Charges': ':, .2f'}
)

fig.update_layout(
    geo_scope='usa',
    margin={"r":0,"t":50,"l":0,"b":0},
    coloraxis_colorbar=dict(
        title="Charge Moyenne ($)",
        tickprefix="$"
    )
)

# Sauvegarder la carte interactive en HTML
output_path = 'interactive_map_usa_regions.html'
fig.write_html(output_path)

print(f"✓ Carte interactive générée: {output_path}")
print(f"Pour l'ouvrir, double-cliquez sur le fichier {output_path} ou ouvrez-le dans votre navigateur.")

