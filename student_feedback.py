import os
import sys
import subprocess
from datetime import datetime
import zipfile

performance_map = { # Mapping dictionaries
    1: "performed at a basic level in this module.",
    2: "performed satisfactorily in this module.",
    3: "performed well throughout this module.",
    4: "performed at an excellent standard in this module!"
}

understanding_map = {
    1: "The learner showed limited understanding of key concepts.",
    2: "The learner showed a reasonable understanding of key concepts.",
    3: "The learner showed a strong understanding of key concepts.",
    4: "The learner showed an outstanding understanding of key concepts and ideas."
}

contribution_map = {
    1: "Contribution to discussions stayed minimal.",
    2: "Contribution to discussions stayed steady but could increase further.",
    3: "Contribution to discussions stayed meaningful and frequent.",
    4: "Contribution to discussions stayed highly engaged and insightful."
}

lab_completion_map = {
    1: "Lab completion stayed inconsistent and needs more focus.",
    2: "Lab completion stayed satisfactory with room for improvement.",
    3: "Lab completion stayed good and on track.",
    4: "Lab completion stayed excellent with all or most exercises completed."
}

punctuality_map = {
    1: "Punctuality stayed poor and needs significant improvement.",
    2: "Punctuality stayed mixed, with some late arrivals.",
    3: "Punctuality stayed good across the module.",
    4: "Punctuality stayed excellent throughout the module."
}

engagement_map = {
    1: "Engagement level stayed low in both sessions and online platforms.",
    2: "Engagement level stayed moderate and could increase further.",
    3: "Engagement level stayed strong in most sessions and online platforms.",
    4: "Engagement level stayed high with consistent focus and participation."
}

further_study_map = {
    1: "Focus on revising core basics, especially key topics from recent labs.",
    2: "Continue to revisit core concepts and practice with small tasks.",
    3: "Continue to deepen knowledge through extra practice and guided resources.",
    4: "Extend learning through advanced resources, projects, and independent study."
}


def get_timestamp():
    """Return current time as YYYYMMDD_HHMMSS string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_students():
    """Return list of student names."""
    return ["Alice", "Bob", "Mark"]


def ask_score(label):
    """Ask user for one score between 1 and 4."""
    while True:
        raw = input(f"{label} (1-4): ")
        try:
            value = int(raw)
            if value in (1, 2, 3, 4):
                return value
            print("Enter a whole number from 1 to 4.")
        except ValueError:
            print("Enter a whole number from 1 to 4.")


def get_scores_for_student(student_name):
    """Return dict of scores for one student."""
    print(f"\nEnter scores for {student_name}. Use 1 to 4.")

    scores = {}
    scores["performance"] = ask_score("Overall performance")
    scores["understanding"] = ask_score("General understanding")
    scores["contribution"] = ask_score("Contribution level")
    scores["lab_completion"] = ask_score("Lab completion")
    scores["punctuality"] = ask_score("Punctuality")
    scores["engagement"] = ask_score("Engagement")
    scores["further_study"] = ask_score("Further study level")

    return scores


def build_feedback_text(student_name, scores):
    """Return full feedback text for one student."""
    lines = []

    lines.append("General comments")     # General comments section
    lines.append(
        f"{student_name} {performance_map[scores['performance']]} "
        f"{understanding_map[scores['understanding']]}"
    )
    lines.append(contribution_map[scores["contribution"]])
    lines.append(lab_completion_map[scores["lab_completion"]])
    lines.append("")

    lines.append("Learner Punctuality and engagement")     # Punctuality and engagement section
    lines.append(punctuality_map[scores["punctuality"]])
    lines.append(engagement_map[scores["engagement"]])
    lines.append("")

    lines.append("Recommendations on further learning")     # Further study section
    lines.append(further_study_map[scores["further_study"]])

    return "\n".join(lines)


def ensure_directories():
    """Create feedback and archive folders if they do not exist."""
    feedback_dir = "feedback"
    archive_dir = "feedback_archive"

    os.makedirs(feedback_dir, exist_ok=True)
    os.makedirs(archive_dir, exist_ok=True)

    return feedback_dir, archive_dir


def write_feedback_file(student_name, feedback_text, feedback_dir):
    """Write feedback text to a timestamped file and return full path."""
    timestamp = get_timestamp()
    safe_name = student_name.replace(" ", "_")
    filename = f"{safe_name}_{timestamp}_feedback.txt"
    path = os.path.join(feedback_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(feedback_text)

    return path


def open_feedback_file(path):
    """Open feedback file for manual editing with platform specific tool."""
    if sys.platform.startswith("win"):
        subprocess.Popen(["notepad.exe", path])
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def create_zip_archive(feedback_dir, archive_dir):
    """Zip all feedback files into one timestamped archive."""
    timestamp = get_timestamp()
    archive_name = f"feedback_{timestamp}.zip"
    archive_path = os.path.join(archive_dir, archive_name)

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(feedback_dir):
            if filename.endswith("_feedback.txt"):
                full_path = os.path.join(feedback_dir, filename)
                zipf.write(full_path, arcname=filename)

    print(f"\nCreated archive: {archive_path}")


def main():
    print("Automated Student Feedback Generator\n")

    feedback_dir, archive_dir = ensure_directories()

    students = get_students()
    feedback_files = []

    for student in students:
        scores = get_scores_for_student(student)
        feedback_text = build_feedback_text(student, scores)
        file_path = write_feedback_file(student, feedback_text, feedback_dir)
        feedback_files.append(file_path)
        print(f"Saved feedback for {student} to {file_path}")
        open_feedback_file(file_path)

    create_zip_archive(feedback_dir, archive_dir)
    print("\nAll feedback generated and archived.")


if __name__ == "__main__":
    main()
