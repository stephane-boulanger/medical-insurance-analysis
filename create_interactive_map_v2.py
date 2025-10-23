import pandas as pd
import plotly.express as px

# Charger les données nettoyées
df = pd.read_csv("data/insurance_clean.csv")

# Calculer les charges moyennes par région
region_avg_charges = df.groupby("region")["charges"].mean().reset_index()
region_avg_charges.columns = ["Region", "Average Charges"]

# Définir les centroïdes (approximatifs) pour chaque région
# Ces coordonnées sont utilisées pour placer un marqueur représentatif de la région
region_coords = {
    "northeast": {"lat": 42.36, "lon": -71.06, "full_name": "Northeast US"},  # Boston
    "southeast": {"lat": 33.75, "lon": -84.39, "full_name": "Southeast US"},  # Atlanta
    "southwest": {"lat": 34.05, "lon": -118.24, "full_name": "Southwest US"},  # Los Angeles
    "northwest": {"lat": 47.61, "lon": -122.33, "full_name": "Northwest US"}   # Seattle
}

# Ajouter les coordonnées et les noms complets au DataFrame
region_avg_charges["lat"] = region_avg_charges["Region"].map(lambda x: region_coords[x]["lat"])
region_avg_charges["lon"] = region_avg_charges["Region"].map(lambda x: region_coords[x]["lon"])
region_avg_charges["Full Region Name"] = region_avg_charges["Region"].map(lambda x: region_coords[x]["full_name"])

# Créer une carte interactive avec des marqueurs
# Chaque marqueur représente une région et sa couleur/taille indique la charge moyenne
fig = px.scatter_geo(
    region_avg_charges,
    lat="lat",
    lon="lon",
    color="Average Charges",  # La couleur du marqueur sera basée sur la charge moyenne
    size="Average Charges",   # La taille du marqueur sera basée sur la charge moyenne
    hover_name="Full Region Name",
    hover_data={
        "Region": True,
        "Average Charges": ":$,.2f",  # Formatage monétaire
        "lat": False,  # Ne pas afficher les coordonnées dans le hover
        "lon": False   # Ne pas afficher les coordonnées dans le hover
    },
    projection="albers usa",  # Projection centrée sur les USA
    scope="usa",              # Limiter la vue aux USA
    color_continuous_scale=px.colors.sequential.Plasma, # Échelle de couleurs
    title="Charges Moyennes d'Assurance par Région aux USA"
)

fig.update_geos(
    showland=True, landcolor="lightgray",
    showocean=True, oceancolor="lightblue",
    showlakes=True, lakecolor="lightblue",
    showrivers=True, rivercolor="lightblue",
    showsubunits=True, subunitcolor="white"
)

fig.update_layout(
    margin={"r":0,"t":50,"l":0,"b":0},
    coloraxis_colorbar=dict(
        title="Charge Moyenne",
        tickprefix="$"
    )
)

# Sauvegarder la carte interactive en HTML
output_path = "interactive_map_usa_regions_v2.html"
fig.write_html(output_path)

print(f"✓ Carte interactive générée: {output_path}")
print(f"Pour l'ouvrir, double-cliquez sur le fichier {output_path} ou ouvrez-le dans votre navigateur.")

