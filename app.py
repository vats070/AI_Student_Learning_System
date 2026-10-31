
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from config import DATA_PATH, FEATURES, TARGET, PURPLE, BLUE, CYAN, TEAL
from styles import load_styles
from model import train_model, predict_marks
from charts import (
    render_performance_chart,
    render_academic_chart,
    render_subject_chart,
)
from recommendations import (
    generate_recommendations,
    generate_daily_plan,
)


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Student Learning System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_styles()


# =====================================================
# 2. HEADER
# =====================================================

st.markdown("""
<div class="dashboard-header">
    <div>
        <div class="brand">🎓 AI Student Learning System</div>
        <div class="brand-subtitle">Student Performance Dashboard</div>
    </div>
    <div class="header-right">
        🎓 &nbsp; Academic Analytics &nbsp; • &nbsp; AI Learning System
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# 3. LOAD DATA AND MODEL
# =====================================================

if not DATA_PATH.exists():
    st.error(
        "Dataset not found. Please create "
        "`data/student_data.csv` with the required columns."
    )
    st.stop()

try:
    data, model, mae, r2, test_count = train_model(
        str(DATA_PATH.resolve()),
        DATA_PATH.stat().st_mtime,
    )
except (ValueError, OSError) as error:
    st.error(f"Could not prepare the model: {error}")
    st.stop()


# =====================================================
# 4. ACADEMIC OVERVIEW
# =====================================================


st.markdown(
    '<div class="section-title">Academic Overview</div>',
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:
    st.metric(
        label="👥 Student Records",
        value=f"{len(data):,}",
        delta=None,
        help="Records in dataset"
    )

with m2:
    st.metric(
        label="📅 Average Attendance",
        value=f"{data['attendance'].mean():.1f}%",
        delta=None,
        help="Across all records"
    )

with m3:
    st.metric(
        label="🎯 Average Final Marks",
        value=f"{data[TARGET].mean():.1f}%",
        delta=None,
        help="Out of 100"
    )

with m4:
    st.metric(
        label=":material/smart_toy:  Model Test MAE",
        value=f"{mae:.2f}",
        delta=None,
        help="Mean absolute prediction error in marks."
    )

st.caption(
    f"Model evaluation: R² = {r2:.3f} | "
    f"Test records: {test_count}. "
    "Evaluation scores may be unstable for small datasets."
)

st.write("")


# =====================================================
# 5. MAIN DASHBOARD
# =====================================================

left, right = st.columns([1.55, 1], gap="large")


# -----------------------------------------------------
# LEFT: PERFORMANCE CHARTS AND DATASET
# -----------------------------------------------------

with left:

    with st.container(border=True):
        st.markdown(
            '<div class="section-title">Student Performance</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Distribution of final marks across the dataset'
            '</div>',
            unsafe_allow_html=True,
        )

        render_performance_chart(data)

    with st.container(border=True):
        st.markdown(
            '<div class="section-title">Academic Score Analysis</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Average scores for the available academic indicators'
            '</div>',
            unsafe_allow_html=True,
        )

        render_academic_chart(data)

    with st.expander("View student dataset and model details"):
        st.dataframe(
            data.reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
        )
        st.write("**Model:** Linear Regression")
        st.write(f"**Valid records:** {len(data)}")
        st.write(f"**Test MAE:** {mae:.3f} marks")
        st.write(f"**Test R²:** {r2:.3f}")
        st.write("**Model input features:**")
        st.write(", ".join(FEATURES))


# -----------------------------------------------------
# RIGHT: TOP PERFORMERS
# -----------------------------------------------------

with right:

    with st.container(border=True):
        st.markdown(
            '<div class="section-title">Top Performance</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Highest final marks in the available dataset'
            '</div>',
            unsafe_allow_html=True,
        )

        
        top_records = data.nlargest(3, TARGET).reset_index(drop=True)

        for i, row in top_records.iterrows():

            # Get actual student name from CSV
            student_name = row["student_name"]

            st.markdown(
                f"""
                <div style="border:1px solid #e0ddef;
                            border-radius:10px;padding:13px;
                            margin-bottom:10px;background:#fff;">
                    <div style="display:flex;
                                justify-content:space-between;
                                align-items:center;">
                        <div>
                            <div style="font-weight:700;color:#454653;
                                        font-size:13px;">
                                🧑‍🎓 {student_name}
                            </div>
                            <div style="font-size:11px;color:#888797;
                                        margin-top:5px;">
                                Attendance: {row['attendance']:.1f}%
                            </div>
                        </div>
                        <div style="font-size:22px;font-weight:800;
                                    color:#4b0dbb;">
                            {row[TARGET]:.1f}%
                        </div>
                    </div>
                    <div style="display:flex;gap:14px;margin-top:10px;
                                font-size:10px;color:#858595;">
                        <span>Previous: {row['previous_marks']:.1f}%</span>
                        <span>Assignments: {row['assignments_score']:.1f}%</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


    # -------------------------------------------------
    # STUDENT INPUT FORM
    # -------------------------------------------------

    with st.container(border=True):
        st.markdown(
            '<div class="section-title">Student Details</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="section-subtitle">'
            'Enter student information for an AI-assisted estimate'
            '</div>',
            unsafe_allow_html=True,
        )

        with st.form("student_form"):
            study_hours = st.number_input(
                "Study hours per day",
                min_value=0.0, max_value=24.0,
                value=4.0, step=0.5,
            )

            attendance = st.slider("Attendance (%)", 0, 100, 80)
            previous_marks = st.slider("Previous marks (%)", 0, 100, 65)
            assignments_score = st.slider("Assignment score (%)", 0, 100, 70)

            st.markdown("**Subject-level scores**")

            programming = st.slider("Programming", 0, 100, 55)
            mathematics = st.slider("Mathematics", 0, 100, 50)
            science = st.slider("Science", 0, 100, 65)

            submitted = st.form_submit_button(
                "Predict Performance",
                type="primary",
                use_container_width=True,
            )


    # -------------------------------------------------
    # AVERAGE SCORE GAUGES
    # -------------------------------------------------

    with st.container(border=True):
        st.markdown(
            '<div class="section-title">Average Score</div>',
            unsafe_allow_html=True,
        )

        subject_averages = [
            ("Programming", programming, PURPLE),
            ("Mathematics", mathematics, BLUE),
            ("Science", science, CYAN),
        ]

        score_cols = st.columns(3)

        for col, (subject, score, color) in zip(
            score_cols, subject_averages
        ):
            with col:
                fig, ax = plt.subplots(figsize=(1.55, 1.55))
                fig.patch.set_facecolor("white")
                ax.set_facecolor("white")

                ax.pie(
                    [score, max(0, 100 - score)],
                    startangle=90,
                    colors=[color, "#dedee8"],
                    counterclock=False,
                    wedgeprops={
                        "width": 0.12,
                        "edgecolor": "white",
                    },
                )

                ax.text(
                    0, 0, f"{score:.0f}%",
                    ha="center", va="center",
                    fontsize=12, fontweight="bold",
                    color="#454653",
                )

                ax.axis("equal")
                plt.tight_layout(pad=0)
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)

                st.markdown(
                    f"""
                    <div style="text-align:center;font-size:11px;
                                color:#777687;margin-top:-8px;">
                        {subject}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# =====================================================
# 6. PREDICTION RESULTS
# =====================================================

if submitted:

    student_input = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignments_score": assignments_score,
    }])

    predicted_marks = predict_marks(model, student_input)

    if predicted_marks >= 75:
        performance_level = "High"
        performance_color = "#16865d"
    elif predicted_marks >= 50:
        performance_level = "Moderate"
        performance_color = "#bd7c0a"
    else:
        performance_level = "Needs support"
        performance_color = "#c53b52"

    st.markdown("---")
    st.markdown(
        '<div class="section-title">Performance Prediction Results</div>',
        unsafe_allow_html=True,
    )

    r1, r2_col, r3 = st.columns(3)

    r1.metric("🎯 Predicted Final Marks", f"{predicted_marks:.1f}/100")
    r2_col.metric("📊 Performance Level", performance_level)
    r3.metric("📅 Attendance", f"{attendance}%")

    st.markdown(
        f"""
        <div style="background:white;border:1px solid #ded9ef;
                    border-radius:12px;padding:18px;margin:15px 0;">
            <div style="font-weight:700;color:#454653;margin-bottom:10px;">
                Estimated final marks
            </div>
            <div style="background:#efedf7;height:13px;border-radius:10px;">
                <div style="background:{performance_color};height:13px;
                            width:{predicted_marks:.2f}%;
                            max-width:100%;border-radius:10px;"></div>
            </div>
            <div style="margin-top:8px;font-size:12px;color:#858595;">
                Prediction: {predicted_marks:.1f}% &nbsp; | &nbsp;
                Performance band:
                <span style="color:{performance_color};font-weight:700;">
                    {performance_level}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "This is an estimate from Linear Regression, not a guarantee "
        "of future marks. Performance bands are illustrative."
    )

    result_left, result_right = st.columns(2, gap="large")

    with result_left:
        with st.container(border=True):
            st.markdown(
                '<div class="section-title">Subject Score Overview</div>',
                unsafe_allow_html=True,
            )
            render_subject_chart(programming, mathematics, science)

    with result_right:
        with st.container(border=True):
            st.markdown(
                '<div class="section-title">Personalized Learning Plan</div>',
                unsafe_allow_html=True,
            )

            recommendations = generate_recommendations(
                study_hours,
                attendance,
                assignments_score,
                programming,
                mathematics,
                science,
            )

            for item in recommendations:
                if item["priority"] == "High":
                    color, symbol = "#c53b52", "🔴"
                elif item["priority"] == "Medium":
                    color, symbol = "#bd7c0a", "🟠"
                else:
                    color, symbol = "#16865d", "🟢"

                st.markdown(
                    f"""
                    <div style="background:#fff;border:1px solid #e1ddef;
                                border-radius:9px;padding:12px;
                                margin-bottom:10px;">
                        <div style="font-weight:700;color:{color};
                                    font-size:13px;">
                            {symbol} {item['area']} — {item['priority']} priority
                        </div>
                        <div style="font-size:12px;color:#686879;
                                    margin-top:7px;line-height:1.6;">
                            {item['action']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


    # -------------------------------------------------
    # DAILY STUDY PLAN
    # -------------------------------------------------

    st.markdown(
        '<div class="section-title">Suggested Daily Study Plan</div>',
        unsafe_allow_html=True,
    )

    plan = generate_daily_plan(programming, mathematics, science)
    plan_cols = st.columns(4)

    for col, (duration, task, color) in zip(plan_cols, plan):
        with col:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style="font-size:11px;font-weight:700;color:{color};">
                        {duration}
                    </div>
                    <div style="font-size:13px;font-weight:600;
                                color:#454653;margin-top:8px;min-height:42px;">
                        {task}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.caption(
        "Adjust the plan to the student's syllabus, available time, "
        "and individual learning needs."
    )


# =====================================================
# 7. FOOTER
# =====================================================

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:#89899a;font-size:11px;
                padding:10px 0 0;">
        AI Student Learning System &nbsp; • &nbsp;
        Built with Python, Streamlit, Pandas and Scikit-learn
    </div>
    """,
    unsafe_allow_html=True,
)