import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = px.data.gapminder()
    return df

df = load_data()

st.sidebar.header("Filter Options")
years = st.sidebar.multiselect(
    label="Select Years",
    options=sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)
continents = st.sidebar.multiselect(
    label="Select Continents",
    options=df["continent"].unique(),
    default=df["continent"].unique()
)
gdp_min, gdp_max = st.sidebar.slider(
    label="GDP per Capita Range",
    min_value=float(df["gdpPercap"].min()),
    max_value=float(df["gdpPercap"].max()),
    value=(float(df["gdpPercap"].min()), float(df["gdpPercap"].quantile(0.75))),
    step=100.0
)
pop_min, pop_max = st.sidebar.slider(
    label="Population Range",
    min_value=int(df["pop"].min()),
    max_value=int(df["pop"].max()),
    value=(int(df["pop"].min()), int(df["pop"].quantile(0.75))),
    step=1000000
)

df_filtered = df[
    (df["year"].isin(years)) &
    (df["continent"].isin(continents)) &
    (df["gdpPercap"] >= gdp_min) & (df["gdpPercap"] <= gdp_max) &
    (df["pop"] >= pop_min) & (df["pop"] <= pop_max)
]

st.title("🌍 Gapminder Interactive Dashboard")

with st.expander("Show Filtered Dataframe"):
    st.dataframe(df_filtered)

fig1 = px.scatter(
    df_filtered,
    x="gdpPercap", y="lifeExp",
    size="pop", color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="GDP per Capita vs Life Expectancy"
)
st.plotly_chart(fig1, use_container_width=True)

if len(years) > 1:
    fig2 = px.line(
        df_filtered.groupby(["year", "continent"]).agg({
            "lifeExp": "mean",
            "gdpPercap": "mean"
        }).reset_index(),
        x="year", y="lifeExp", color="continent",
        markers=True,
        title="Average Life Expectancy Over Time by Continent"
    )
    st.plotly_chart(fig2, use_container_width=True)

country = st.sidebar.selectbox(
    label="Select Country for Detail",
    options=sorted(df["country"].unique())
)
country_df = df[df["country"] == country]

st.subheader(f"📈 {country} Metrics Over Years")
fig3 = px.line(
    country_df,
    x="year",
    y=["lifeExp", "gdpPercap", "pop"],
    markers=True,
    title=f"{country}: Life Expectancy, GDP per Capita, and Population"
)
st.plotly_chart(fig3, use_container_width=True)
