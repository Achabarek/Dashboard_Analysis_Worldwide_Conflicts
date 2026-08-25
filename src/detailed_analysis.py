import pandas as pd
import altair as alt
import streamlit as st


st.title("Worldwide Conflicts Analysis")
st.write("Detailed Data Analysis is Provided")

if "df" in st.session_state:
    df = st.session_state["df"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Do conflicts last longer with a ceasefire on average?")

        duration_by_ceasefire = (df.groupby("Ceasefire")["Duration_Days"].mean())

        no_ceasefire_avg = duration_by_ceasefire["No"]
        yes_ceasefire_avg = duration_by_ceasefire["Yes"]

        chart = (alt.Chart(duration_by_ceasefire.reset_index()).mark_bar(size=25).encode(
            x=alt.X("Ceasefire:N", title="Ceasefire"),
            y=alt.Y("Duration_Days:Q", title="Average Duration (Days")
        ))

        st.altair_chart(chart, use_container_width=True)
        st.write(f"Average Duration with ceasefire: {yes_ceasefire_avg:.2f} days")
        st.write(f"Average Duration with no ceasefire: {no_ceasefire_avg:.2f} days")


    with col2:
        st.subheader("Do Sanctions relate to different conflict outcomes?")


        sanction_outs = pd.crosstab(df["Sanctions"], df["Outcome"], normalize="index") * 100

        st.dataframe(sanction_outs.round(1))

        sanction_outs_chart = (
            sanction_outs.reset_index().melt(id_vars=["Sanctions"], var_name="Outcome", value_name="Percentage")
                                )

        # st.write(sanction_outs_chart)
        chart2 = (alt.Chart(sanction_outs_chart)
                  .mark_bar()
                  .encode(
                     x=alt.X("Sanctions:N", title="Sanctions"
                     ),
                     y=alt.Y("Percentage:Q", title="Percentage of Conflicts", scale=alt.Scale(domain=[0, 100])
                     ),
                     color = alt.Color("Outcome:N", title="Outcome"
                     ),
                     tooltip=[
                            alt.Tooltip("Sanctions:N", title="Sanctions"),
                            alt.Tooltip("Outcome:N", title="Outcome"),
                            alt.Tooltip(
                                "Percentage:Q",
                                title="Percentage",
                                format=".1f"
                                       )
                           ]
                        )
                  )
        st.altair_chart(chart2, use_container_width=True)

        st.caption(
            "The chart compares the percentage distribution of conflict "
            "outcomes within conflicts with and with no sanctions."
        )

        difference = (sanction_outs.loc["Yes"] - sanction_outs.loc["No"])
        # find the outcome with the largest absolute difference
        largest_difference = difference.abs().idxmax()
        difference_value = difference[largest_difference]
        st.write(
            f"The largest difference is observed for "
            f"{largest_difference}: "
            f"{difference_value:+.1f} percentage points"
        )

    with col3:
        refugees_by_type = (
            df.groupby("Conflict_Type")["Refugees_Millions"]
            .mean()
            .sort_values(ascending=False)
        )
        st.write("What is the average number of refugees associated with each conflict type?")
        st.bar_chart(refugees_by_type)


    def outcome_distribution_chart(df, group_col):
        outcome_data = (pd.crosstab(df[group_col], df["Outcome"], normalize="index") * 100)
        chart_data = (outcome_data.reset_index().melt(id_vars=group_col, var_name="Outcome", value_name="Percentage"))
        chart = (
            alt.Chart(chart_data).mark_bar().encode(
                x=alt.X(f"{group_col}:N", title=group_col),
                y=alt.Y("Percentage:Q", title="Percentage of Conflicts", scale=alt.Scale(domain=[0, 100])),
                color=alt.Color("Outcome:N", title="Outcome"),
                tooltip=[
                    alt.Tooltip(f"{group_col}:N"),
                    alt.Tooltip("Outcome:N"),
                    alt.Tooltip("Percentage:Q", format=".1f")
                ]
            )
        )

        return outcome_data, chart

    col4, col5 = st.columns(2)
    with col4:
        sanction_data, sanction_chart = outcome_distribution_chart(
            df,
            "Sanctions"
        )

        st.dataframe(sanction_data.round(1))
        st.altair_chart(
            sanction_chart,
            use_container_width=True
        )

    with col5:

        un_data, un_chart = outcome_distribution_chart(
            df,
            "UN_Involvement"
        )

        st.dataframe(un_data.round(1))
        st.altair_chart(
            un_chart,
            use_container_width=True
        )













