
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from config import PURPLE, BLUE, CYAN, MAGENTA, TEAL, ORANGE


def render_performance_chart(data):
    bands = pd.cut(
        data["final_marks"],
        bins=[-0.01, 39.99, 59.99, 74.99, 100],
        labels=[
            "Needs support", "Developing", "Good", "Excellent"
        ],
    )

    counts = bands.value_counts().reindex(
        ["Needs support", "Developing", "Good", "Excellent"],
        fill_value=0,
    )

    colors = [MAGENTA, CYAN, TEAL, PURPLE]

    chart_col, legend_col = st.columns([1, 1.15])

    with chart_col:
        fig, ax = plt.subplots(figsize=(4, 3.1))
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        ax.pie(
            counts.values,
            startangle=90,
            colors=colors,
            wedgeprops={
                "width": 0.27,
                "edgecolor": "white",
                "linewidth": 3,
            },
        )

        ax.text(
            0, 0.08,
            f"{data['final_marks'].mean():.1f}%",
            ha="center", va="center",
            fontsize=20, fontweight="bold",
            color="#454653",
        )

        ax.text(
            0, -0.16, "AVG MARKS",
            ha="center", va="center",
            fontsize=8, color="#858595",
        )

        ax.axis("equal")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with legend_col:
        st.write("")

        for i, (label, count) in enumerate(counts.items()):
            percentage = count / len(data) * 100

            st.markdown(
                f"""
                <div style="margin:13px 0;">
                    <div style="display:flex;
                                justify-content:space-between;
                                font-size:12px;color:#555565;">
                        <span>
                            <span style="color:{colors[i]};
                                         font-size:17px;">●</span>
                            &nbsp;{label}
                        </span>
                        <b>{count}</b>
                    </div>
                    <div style="height:7px;background:#efedf6;
                                border-radius:8px;margin-top:6px;">
                        <div style="height:7px;width:{percentage:.1f}%;
                                    max-width:100%;
                                    background:{colors[i]};
                                    border-radius:8px;"></div>
                    </div>
                    <div style="font-size:10px;color:#9393a0;
                                margin-top:3px;">
                        {percentage:.1f}% of records
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_academic_chart(data):
    labels = [
        "Previous marks", "Assignments",
        "Attendance", "Final marks",
    ]

    columns = [
        "previous_marks", "assignments_score",
        "attendance", "final_marks",
    ]

    colors = [PURPLE, BLUE, ORANGE, CYAN]
    averages = [data[column].mean() for column in columns]

    fig, ax = plt.subplots(figsize=(7, 3.5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    bars = ax.bar(labels, averages, color=colors, width=0.57)

    ax.set_ylim(0, 110)
    ax.set_ylabel("Average score (%)", color="#777687")
    ax.tick_params(axis="x", labelsize=9, colors="#555565")
    ax.tick_params(axis="y", labelsize=8, colors="#858595")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#dedee8")
    ax.spines["bottom"].set_color("#dedee8")

    ax.grid(axis="y", alpha=0.18)
    ax.set_axisbelow(True)

    ax.bar_label(
        bars,
        labels=[f"{value:.1f}%" for value in averages],
        padding=4, fontsize=9, color="#454653",
    )

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def render_subject_chart(programming, mathematics, science):
    scores = [programming, mathematics, science]
    labels = ["Programming", "Mathematics", "Science"]

    fig, ax = plt.subplots(figsize=(6, 3.2))
    bars = ax.bar(
        labels, scores,
        color=[PURPLE, CYAN, TEAL],
        width=0.58,
    )

    ax.set_ylim(0, 110)
    ax.set_ylabel("Score (%)")
    ax.grid(axis="y", alpha=0.18)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.bar_label(
        bars,
        labels=[f"{value:.0f}%" for value in scores],
        padding=3,
    )

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def render_subject_gauges(programming,mathematics, science):
    subjects = [
        ("Programming", PURPLE, programming),
        ("Mathematics", BLUE, mathematics),
        ("Science", CYAN, science),
    ]

