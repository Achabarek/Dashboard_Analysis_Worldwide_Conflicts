import streamlit as st
import altair as alt
import pandas as pd


st.title("Worldwide Conflicts Dashboard")
st.write("Data Analysis is Provided")

st.sidebar.title("Upload a Dataset")
upload_file = st.sidebar.file_uploader("Choose CSV File", type='csv')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.session_state["df"] = df

else:
    st.info("Please Upload a CSV file...")

if "df" in st.session_state:
    df = st.session_state["df"]

    # -----------------------------
    # Number of conflicts
    # -----------------------------
    num_conflicts = len(df)
    st.sidebar.write("No. of Conflicts: ", num_conflicts)


    total_eco_loss = df["Economic_Loss_USD_Billions"].sum()
    st.sidebar.write("Total Economic Loss", f"${total_eco_loss:.2f} B")

    # -----------------------------
    # Total deaths
    # -----------------------------
    military_deaths = (
            df["Military_Deaths_A"].sum()
            + df["Military_Deaths_B"].sum()
                      )

    total_deaths = (
            df["Military_Deaths_A"].sum()
            + df["Military_Deaths_B"].sum()
            + df["Civilian_Deaths"].sum()
                   )

    st.sidebar.subheader("Total Military Deaths")
    st.sidebar.write(military_deaths)
    st.sidebar.subheader("Total Deaths")
    st.sidebar.write(total_deaths)

    # -----------------------------
    # Sanctions
    # -----------------------------
    sanction_counts = (df['Sanctions'] == 'Yes').sum()
    no_sanction_counts = (df['Sanctions'] == 'No').sum()

    # -----------------------------
    # Ceasefire
    # -----------------------------
    ceasefire_counts = (df["Ceasefire"] == "Yes").sum()
    no_ceasefire_counts = (df["Ceasefire"] == "No").sum()

    st.sidebar.subheader("How Many Conflicts had")
    st.sidebar.write(f"Sanctions:  {sanction_counts}")
    st.sidebar.write(f"No Sanctions:  {no_sanction_counts}")
    st.sidebar.write(f"Ceasefire: {ceasefire_counts}")
    st.sidebar.write(f"No Ceasefire: {no_ceasefire_counts}")



    # -----------------------------
    # Top 10 Countries with Ceasefire Conflicts
    # -----------------------------


    st.subheader("Top 10 Countries with Ceasefire Conflicts")

    country_counts = (
        df[df["Ceasefire"] == "Yes"]
        ["Country_B"]
        .value_counts()
    )
    country_counts_df = (country_counts.reset_index())

    country_counts_df.columns = ["Country", "Ceasefire"]

    country_counts_df = (country_counts_df.sort_values("Ceasefire", ascending=False)
                         .head(10))

    st.bar_chart(country_counts_df, x="Country", y="Ceasefire")

    # -----------------------------
    # Conflicts that have the Highest Deaths Average
    # -----------------------------
    st.subheader("Conflicts that have the Highest Deaths Average")
    conflict_count_death = df.groupby("Conflict_Type")["Civilian_Deaths"].mean().sort_values(ascending=False)
    st.table(conflict_count_death)

    # -----------------------------
    # Conflict types have the highest economic loss
    # -----------------------------

    st.subheader("Conflict types have the highest economic loss")
    economic_by_type = (df.groupby("Conflict_Type")["Economic_Loss_USD_Billions"]
        .mean()
        .sort_values(ascending=False)
    )
    chart = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x=alt.X(
                "Conflict_Type:N",
                title="Conflict Type"
            ),
            y=alt.Y(
                "Economic_Loss_USD_Billions:Q",
                title="Economic Loss (USD Billions)"
            ),
            color=alt.Color(
                "Conflict_Type:N",
                title="Conflict Type"
            ),
            tooltip=[
                alt.Tooltip(
                    "Economic_Loss_USD_Billions:Q",
                    title="Economic Loss",
                    format=".2f"
                )
            ]
        )
    )
    st.altair_chart(chart, use_container_width=True)

    # -----------------------------
    # Conflicts by Type
    # -----------------------------
    st.subheader("Conflicts by Type")
    conflict_counts = df["Conflict_Type"].value_counts()
    st.bar_chart(conflict_counts)
    # -----------------------------
    # Conflicts Per Year
    # -----------------------------

    conflicts_per_year = (df.groupby("Year").size().reset_index(name="Conflict_Count").sort_values("Year"))
    st.subheader("Conflicts Per Year")

    chart1 = (
        alt.Chart(conflicts_per_year).mark_line().encode(
            x=alt.X(
                "Year:Q",
                title="Year",
                axis=alt.Axis(format="~f",tickCount=10)
                   ),
            y=alt.Y("Conflict_Count:Q",
                    title="Number of Conflicts"
                    )

        ).properties(
            height=200
        ))
    st.altair_chart(chart1, use_container_width=True)








