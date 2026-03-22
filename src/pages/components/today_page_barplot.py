import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from data.dfs import df_channels


def bar_plots_radio_tv():
    radio_col, tv_col = st.columns(2, gap="large")

    # Load data

    # TV Data
    with tv_col:
        tv = df_channels[df_channels["media"] == "tv"].copy()
        tv.loc[
            tv["women_expression_rate_2020"].isna(), "women_expression_rate_2020"
        ] = tv.loc[
            tv["women_expression_rate_2020"].isna(), "women_expression_rate_2019"
        ]
        tv = tv.sort_values("women_expression_rate_2020", ascending=False)
        tv = tv[tv["Editeur"] != "FRANCE 4"]
        tv["women_pct"] = tv["women_expression_rate_2020"] * 100

        st.markdown(
            "### <span style='font-size: 20px;'>Chaînes TV classées par part de parole féminine (2020)</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <span style='font-size: 18px;'>
        Les femmes occupent une part beaucoup moins importante que celle des hommes à la télévision, et cela même de nos jours. On remarque notamment des scores particulièrement bas pour les chaînes proposant du contenu sportif.
        </span>
        """,
            unsafe_allow_html=True,
        )

        # Create custom bar chart with alternating colors
        colors = ["#19d2c9", "#66b3ff"] * (len(tv) // 2 + 1)
        fig_tv = go.Figure(
            data=[
                go.Bar(
                    y=tv["Editeur"],
                    x=tv["women_pct"],
                    orientation="h",
                    marker=dict(color=colors[: len(tv)]),
                    text=tv["women_pct"].round(1).astype(str) + "%",
                    textposition="outside",
                    textfont=dict(size=16, color="white"),
                    hovertemplate="<b>%{y}</b><br>%{x:.1f}%<extra></extra>",
                    hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
                )
            ]
        )

        fig_tv.update_layout(
            height=600,
            width=800,
            xaxis_title="Pourcentage de parole féminine",
            yaxis_title="",
            xaxis=dict(title_font=dict(size=18), tickfont=dict(size=16)),
            yaxis=dict(tickfont=dict(size=16)),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=30, b=20),
            showlegend=False,
        )

        st.plotly_chart(fig_tv, use_container_width=True)

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

        st.markdown(
            "### <span style='font-size: 20px;'>Stations de radio classées par part de parole féminine (2020)</span>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <span style='font-size: 18px;'>
        Bien que la radio soit un média ancien, la place des femmes y reste limitée de nos jours, à l'exception notable de Fip qui fait figure d'exception.
        </span>
        """,
            unsafe_allow_html=True,
        )

        # Create custom bar chart with alternating colors
        colors = ["#19d2c9", "#66b3ff"] * (len(radio) // 2 + 1)
        fig_radio = go.Figure(
            data=[
                go.Bar(
                    y=radio["Editeur"],
                    x=radio["women_pct"],
                    orientation="h",
                    marker=dict(color=colors[: len(radio)]),
                    text=radio["women_pct"].round(1).astype(str) + "%",
                    textposition="outside",
                    textfont=dict(size=16, color="white"),
                    hovertemplate="<b>%{y}</b><br>%{x:.1f}%<extra></extra>",
                    hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
                )
            ]
        )

        fig_radio.update_layout(
            height=600,
            width=800,
            xaxis_title="Pourcentage de parole féminine",
            yaxis_title="",
            xaxis=dict(title_font=dict(size=18), tickfont=dict(size=16)),
            yaxis=dict(tickfont=dict(size=16)),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=30, b=20),
            showlegend=False,
        )

        st.plotly_chart(fig_radio, use_container_width=True)
