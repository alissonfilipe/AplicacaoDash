import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# =========================
# 1. Ler dados
# =========================
df = pd.read_csv("ecommerce_estatistica.csv")

# =========================
# 2. Criar gráficos
# =========================

# Histograma
fig_hist = px.histogram(
    df,
    x="Preço",
    nbins=30,
    title="Distribuição de Preços"
)

# Dispersão
fig_scatter = px.scatter(
    df,
    x="Preço",
    y="Nota",
    title="Preço vs Nota",
    trendline="ols"
)

# Heatmap
corr = df.corr(numeric_only=True)
fig_heatmap = px.imshow(
    corr,
    title="Mapa de Calor das Correlações",
    text_auto=True
)

# Barras
preco_marca = df.groupby("Marca")["Preço"].mean().reset_index()
fig_bar = px.bar(
    preco_marca,
    x="Marca",
    y="Preço",
    title="Preço Médio por Marca"
)

# Pizza
fig_pie = px.pie(
    df,
    names="Gênero",
    title="Distribuição por Gênero"
)

# Densidade
fig_density = px.density_contour(
    df,
    x="Preço",
    y="Nota",
    title="Densidade: Preço vs Nota"
)

# Regressão
fig_reg = px.scatter(
    df,
    x="N_Avaliações",
    y="Nota",
    trendline="ols",
    title="Regressão: Avaliações vs Nota"
)

# =========================
# 3. Criar aplicação Dash
# =========================
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Dashboard de E-commerce", style={"textAlign": "center"}),

    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_heatmap),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_density),
    dcc.Graph(figure=fig_reg),
])

# =========================
# 4. Rodar aplicação
# =========================
if __name__ == "__main__":
    app.run(debug=True)