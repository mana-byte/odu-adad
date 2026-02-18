import streamlit as st

from pages.dfs import df_channels

def bar_plots_radio_tv():
    radio_col, tv_col = st.columns(2, gap="large")

    # Load data
    

    # TV Data
    with tv_col:
        tv = df_channels[df_channels["media"] == "tv"].copy()
        tv.loc[tv["women_expression_rate_2020"].isna(), "women_expression_rate_2020"] = (
            tv.loc[tv["women_expression_rate_2020"].isna(), "women_expression_rate_2019"]
        )
        tv = tv.sort_values("women_expression_rate_2020", ascending=False)
        tv = tv[tv["Editeur"] != "FRANCE 4"]
        tv["women_pct"] = tv["women_expression_rate_2020"] * 100

        st.write("### Chaînes TV classées par part de parole féminine (2020)")
        tv_chart = st.bar_chart(
            tv.set_index("Editeur")["women_pct"],
            use_container_width=True,
            horizontal=True,
            sort="-women_pct"
        )

    # Radio Data
    with radio_col:
        radio = df_channels[df_channels["media"] == "radio"].copy()
        radio.loc[
            radio["women_expression_rate_2020"].isna(), "women_expression_rate_2020"
        ] = radio.loc[
            radio["women_expression_rate_2020"].isna(), "women_expression_rate_2019"
        ]
        radio = radio.sort_values("women_expression_rate_2020", ascending=False)
        radio["women_pct"] = radio["women_expression_rate_2020"] * 100

        st.write("### Stations de radio classées par part de parole féminine (2020)")
        radio_chart = st.bar_chart(
            radio.set_index("Editeur")["women_pct"],
            use_container_width=True,
            horizontal=True,
            sort="-women_pct"
        )
