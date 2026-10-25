
def generate_recommendations(
    study_hours,
    attendance,
    assignments_score,
    programming,
    mathematics,
    science,
):
    recommendations = []

    subjects = {
        "Programming": programming,
        "Mathematics": mathematics,
        "Science": science,
    }

    for subject, score in subjects.items():
        if score < 40:
            recommendations.append({
                "priority": "High",
                "area": subject,
                "action": (
                    f"Revise {subject} fundamentals and solve "
                    "five beginner-level questions daily."
                ),
            })
        elif score < 60:
            recommendations.append({
                "priority": "Medium",
                "area": subject,
                "action": (
                    f"Spend 30 minutes practising {subject} "
                    "and review mistakes after each session."
                ),
            })

    if attendance < 75:
        recommendations.append({
            "priority": "High",
            "area": "Attendance",
            "action": (
                "Improve class attendance and catch up "
                "on missed lessons."
            ),
        })

    if assignments_score < 60:
        recommendations.append({
            "priority": "Medium",
            "area": "Assignments",
            "action": (
                "Complete pending assignments and review "
                "feedback before submitting new work."
            ),
        })

    if study_hours < 2:
        recommendations.append({
            "priority": "Medium",
            "area": "Study routine",
            "action": (
                "Try two focused 25-minute study sessions "
                "each day, with short breaks."
            ),
        })

    if not recommendations:
        recommendations.append({
            "priority": "Positive",
            "area": "Continue learning",
            "action": (
                "Keep your current routine, practise "
                "challenging questions, and review progress weekly."
            ),
        })

    return recommendations


def generate_daily_plan(programming, mathematics, science):
    weakest = sorted([
        ("Programming", programming),
        ("Mathematics", mathematics),
        ("Science", science),
    ], key=lambda item: item[1])

    return [
        ("25 min", f"Practise {weakest[0][0]}", "#4B0DBB"),
        ("25 min", f"Revise {weakest[1][0]}", "#347CF6"),
        ("15 min", "Review mistakes and key concepts", "#22C7E8"),
        ("10 min", "Take a short self-test", "#40D8C5"),
    ]