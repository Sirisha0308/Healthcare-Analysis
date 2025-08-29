import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("cleaned_healthcare_dataset.csv")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to section:",
    [
        "Overview",
        "Demographics",
        "Medical Conditions",
        "Hospital & Doctor Performance",
        "Financial Patterns",
        "Time Trends",
        "Insurance Analysis",
        "Medication & Tests",
        "Admission Details",
        "Discharge & Stay Length"
    ]
)

# --- OVERVIEW ---
if section == "Overview":
    st.title("Healthcare Data Analysis Dashboard")
    st.write("This dashboard presents all insights from my Healthcare Analysis project.")
    st.write("Use the left sidebar to navigate between different sections.")

    st.subheader("Dataset Snapshot")
    st.write(f"**Total Records:** {df.shape[0]:,}")
    st.dataframe(df.head(10))  # show first 10 rows instead of just listing columns
    
    st.subheader("Available Columns")
    st.markdown(", ".join(df.columns))

# --- DEMOGRAPHICS ---
elif section == "Demographics":
    st.title("Demographics Insights")

    st.subheader("Age Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['Age'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Gender Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='Gender', ax=ax)
    st.pyplot(fig)

# --- MEDICAL CONDITIONS ---
elif section == "Medical Conditions":
    st.title("Medical Condition Insights")

    st.subheader("Top 10 Medical Conditions")
    top_conditions = df['Medical_Condition'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=top_conditions.values, y=top_conditions.index, ax=ax)
    st.pyplot(fig)

# --- HOSPITAL & DOCTOR PERFORMANCE ---
elif section == "Hospital & Doctor Performance":
    st.title("Hospital & Doctor Performance")

    st.subheader("Admissions by Hospital")
    fig, ax = plt.subplots(figsize=(8, 5))
    top_hospitals = df['Hospital'].value_counts().head(10)
    sns.barplot(x=top_hospitals.values, y=top_hospitals.index, ax=ax)
    st.pyplot(fig)

    st.subheader("Top Performing Doctors")
    fig, ax = plt.subplots(figsize=(8, 5))
    top_doctors = df['Doctor'].value_counts().head(10)
    sns.barplot(x=top_doctors.values, y=top_doctors.index, ax=ax)
    st.pyplot(fig)

# --- FINANCIAL PATTERNS ---
elif section == "Financial Patterns":
    st.title("Financial Insights")

    st.subheader("Billing Amount Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['Billing_Amount'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# --- TIME TRENDS ---
elif section == "Time Trends":
    st.title("Time-Based Trends")

    st.subheader("Admissions by Month")
    df['Admission_Month'] = pd.to_datetime(df['Date_of_Admission']).dt.month
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='Admission_Month', ax=ax)
    st.pyplot(fig)

# --- INSURANCE ANALYSIS ---
elif section == "Insurance Analysis":
    st.title("Insurance Provider Insights")

    st.subheader("Top Insurance Providers")
    fig, ax = plt.subplots(figsize=(8, 5))
    top_insurance = df['Insurance_Provider'].value_counts().head(10)
    sns.barplot(x=top_insurance.values, y=top_insurance.index, ax=ax)
    st.pyplot(fig)

# --- MEDICATION & TESTS ---
elif section == "Medication & Tests":
    st.title("Medication and Test Results")

    st.subheader("Most Common Medications")
    fig, ax = plt.subplots(figsize=(8, 5))
    top_medications = df['Medication'].value_counts().head(10)
    sns.barplot(x=top_medications.values, y=top_medications.index, ax=ax)
    st.pyplot(fig)

# --- ADMISSION DETAILS ---
elif section == "Admission Details":
    st.title("Admission Details")

    st.subheader("Admission Types")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='Admission_Type', ax=ax)
    st.pyplot(fig)

# --- DISCHARGE & STAY LENGTH ---
elif section == "Discharge & Stay Length":
    st.title("Discharge and Stay Length")

    st.subheader("Stay Length Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['Stay_Length'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Developed by Sirisha")
