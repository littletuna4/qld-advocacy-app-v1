import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

# Create a connection object.


# Validation data
VALIDATION_DATA = [
    [
        "Sub Category 1",
        "Permanence - s24(1)(b)",
        "Functional Capacity – s24(1)(c)",
        "Permanence and Functional Capacity",
        "Early Intervention - s25",
        "Out of Time",
        "No s100 decision",
        "Scope of supports",
        "Compensation",
        "Parental Responsibility – s74 - 77",
        "Nominee or guardian issue",
        "Change of Circumstances – s48",
        "Independent Assessments",
        "Value for Money – 34(1)(c)",
        "Informal supports – 34(1)(e)",
        "Funding responsibility – 34(1)(f)",
        "Capacity Building",
        "Core Supports",
        "Housing / Accommodation",
        "Home modifications",
        "Assistive Technology",
        "Support Coordination",
        "Transport",
        "Assistance dog",
        "Other supports",
    ],
    [
        "Sub Category 2",
        "Permanence",
        "Functional Capacity",
        "Permanence and Functional Capacity",
        "Early Intervention - s25",
        "Out of Time",
        "No s100 decision",
        "Scope of supports",
        "Compensation",
        "Parental Responsibility – s74 - 77",
        "Nominee or guardian issue",
        "Change of Circumstances – s48",
        "Independent Assessments",
        "Value for Money – 34(1)(c)",
        "Informal supports – 34(1)(e)",
        "Funding responsibility – 34(1)(f)",
        "Capacity Building",
        "Core Supports",
        "Housing / Accommodation",
        "Home modifications",
        "Assistive Technology",
        "Support Coordination",
        "Transport",
        "Assistance dog",
        "Other supports",
    ],
    [
        "Gender",
        "Cis-Male",
        "Cis-Female",
        "Unknown",
        "Trans Male",
        "Trans Female",
        "Non-binary",
    ],
    [
        "Primary Impairment",
        "Physical",
        "Psychosocial",
        "Cognitive",
        "Neurological",
        "Intellectual",
        "Visual",
        "Hearing",
        "Physical/Neurological",
        "Autism Spectrum Disorder",
    ],
    [
        "Secondary Impairment",
        "Physical",
        "Psychosocial",
        "Cognitive",
        "Neurological",
        "Intellectual",
        "Visual",
        "Hearing",
        "Physical/Neurological",
        "Autism Spectrum Disorder",
    ],
    [
        "Applicants Primary Representative",
        "No representative",
        "Friend or Family",
        "Legal",
        "Appeals Advocate",
        "Service Provider",
    ],
    [
        "Applicants Secondary Representative",
        "No representative",
        "Friend or Family",
        "Legal",
        "Appeals Advocate",
        "Service Provider",
    ],
    [
        "Respondent Representative",
        "Internal (NDIA)",
        "External (Private firm/AGS)",
        "Unknown",
    ],
    ["Number of Case Conferences", 0, 1, 2, 3, 4, "5 or more"],
    ["Directions Hearing", 0, 1, 2, 3, 4, "5 or more"],
    ["Return of Summons Hearing", 0, 1, 2, 3, 4, "5 or more"],
    ["Interlocutory Hearings", 0, 1, 2, 3, 4, "5 or more"],
    ["Conciliation", 0, 1, 2, 3, 4, "5 or more"],
    ["CaLD", "CaLD", "Non-CaLD", "NS"],
    ["ATSI", "ATSI", "Non-ATSI", "NS"],
    ["History of Abuse/Violence", "Yes", "No", "NS"],
]

# Convert validation data to a dictionary for easy access
VALIDATION_DICT = {item[0]: item[1:] for item in VALIDATION_DATA}

date_columns = ["Decision Date", "Date AAT Lodged"]


# Function to load data
@st.cache_data
def load_data():
    # Replace this with your actual data loading method
    # For this example, we'll create a sample DataFrame with the specified columns

    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    print(df.head())
    print(df.columns)
    print(df.dtypes)
    print(df.shape)
    print(df.describe())
    # parse the date columns

    return df

    data = {
        "Applicant": np.random.choice(["A", "B", "C", "D"], 100),
        "Citation": [f"Citation {i}" for i in range(100)],
        "File Number": [f"FILE-{i:03d}" for i in range(100)],
        "Decision Date": pd.date_range(start="2020-01-01", periods=100),
        "Month Index (Decision Date)": np.random.randint(1, 13, 100),
        "Year Index (Decision Date)": np.random.randint(2020, 2024, 100),
        "Date AAT Lodged": pd.date_range(start="2019-01-01", periods=100),
        "Days from Lodgement to Decision": np.random.randint(1, 365, 100),
        "Days from Lodgement to Decision (Bucket)": np.random.choice(
            ["0-30", "31-60", "61-90", "90+"], 100
        ),
        "Member 1": np.random.choice(["John", "Jane", "Bob", "Alice"], 100),
        "Position 1": np.random.choice(["Judge", "Lawyer", "Consultant"], 100),
        "Location": np.random.choice(["Sydney", "Melbourne", "Brisbane", "Perth"], 100),
        "Decision Type": np.random.choice(["Approved", "Rejected", "Pending"], 100),
        "Applicant Age": np.random.randint(18, 80, 100),
        "Applicant Gender": np.random.choice(VALIDATION_DICT["Gender"], 100),
        "CALD": np.random.choice(VALIDATION_DICT["CaLD"], 100),
        "ATSI": np.random.choice(VALIDATION_DICT["ATSI"], 100),
        "Appealed to Federal Court": np.random.choice(["Yes", "No"], 100),
        "Result on Appeal": np.random.choice(["Upheld", "Overturned", "N/A"], 100),
        "Notes (Free Text)": [f"Note for entry {i}" for i in range(100)],
        "Sub Category 1": np.random.choice(VALIDATION_DICT["Sub Category 1"], 100),
        "Sub Category 2": np.random.choice(VALIDATION_DICT["Sub Category 2"], 100),
        "Primary Impairment": np.random.choice(
            VALIDATION_DICT["Primary Impairment"], 100
        ),
        "Secondary Impairment": np.random.choice(
            VALIDATION_DICT["Secondary Impairment"], 100
        ),
        "Applicants Primary Representative": np.random.choice(
            VALIDATION_DICT["Applicants Primary Representative"], 100
        ),
        "Applicants Secondary Representative": np.random.choice(
            VALIDATION_DICT["Applicants Secondary Representative"], 100
        ),
        "Respondent Representative": np.random.choice(
            VALIDATION_DICT["Respondent Representative"], 100
        ),
        "Number of Case Conferences": np.random.choice(
            VALIDATION_DICT["Number of Case Conferences"], 100
        ),
        "Directions Hearing": np.random.choice(
            VALIDATION_DICT["Directions Hearing"], 100
        ),
        "Return of Summons Hearing": np.random.choice(
            VALIDATION_DICT["Return of Summons Hearing"], 100
        ),
        "Interlocutory Hearings": np.random.choice(
            VALIDATION_DICT["Interlocutory Hearings"], 100
        ),
        "Conciliation": np.random.choice(VALIDATION_DICT["Conciliation"], 100),
        "History of Abuse/Violence": np.random.choice(
            VALIDATION_DICT["History of Abuse/Violence"], 100
        ),
    }
    df = pd.DataFrame(data)
    print(df.head())
    return df


# Main function to run the Streamlit app
def main():

    st.title("AAT Decision Search")

    # Load data
    df = load_data()

    # Sidebar for search options
    st.sidebar.header("Search Options")

    # Text search
    search_term = st.sidebar.text_input("Search term")

    # Date range filter
    date_column = st.sidebar.selectbox("Select date column", date_columns)

    start_date_st = st.sidebar.date_input("Start date", df[date_column].min())
    end_date_st = st.sidebar.date_input("End date", df[date_column].max())
    start_date = pd.to_datetime(start_date_st)
    end_date = pd.to_datetime(end_date_st)

    # Categorical filters
    categorical_columns = [
        "Applicant Gender",
        "CALD",
        "ATSI",
        "Appealed to Federal Court",
        "Sub Category 1",
        "Sub Category 2",
        "Primary Impairment",
        "Secondary Impairment",
        "Applicants Primary Representative",
        "Applicants Secondary Representative",
        "Respondent Representative",
        "History of Abuse/Violence",
    ]

    selected_categories = {}
    for col in categorical_columns:
        if col in VALIDATION_DICT:
            selected_categories[col] = st.sidebar.multiselect(
                f"Select {col}", VALIDATION_DICT[col]
            )
        else:
            selected_categories[col] = st.sidebar.multiselect(
                f"Select {col}", df[col].unique()
            )

    # Numeric range filters
    numeric_columns = ["Applicant Age", "Days from lodgement to decision"]
    selected_ranges = {}
    for col in numeric_columns:
        # parse into numbers if possible - handling the non-numeric values by converting them to NaN
        df[col] = pd.to_numeric(df[col], errors="coerce")

        # print where it's non null and non-numeric
        min_val, max_val = st.sidebar.slider(
            f"{col} range",
            float(df[col].min()),
            float(df[col].max()),
            (float(df[col].min()), float(df[col].max())),
        )
        selected_ranges[col] = (min_val, max_val)

    # Apply filters
    mask = df[date_column].between(start_date, end_date)

    if search_term:
        mask &= df.apply(
            lambda row: row.astype(str).str.contains(search_term, case=False).any(),
            axis=1,
        )

    for col, values in selected_categories.items():
        if values:
            mask &= df[col].isin(values)

    for col, (min_val, max_val) in selected_ranges.items():
        mask &= df[col].between(min_val, max_val)

    filtered_df = df[mask]

    # Display results
    st.write(f"Showing {len(filtered_df)} results")
    st.dataframe(filtered_df)

    # Export results
    if st.button("Export Results"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="search_results.csv",
            mime="text/csv",
        )

    # Display summary statistics
    if st.checkbox("Show Summary Statistics"):
        st.subheader("Summary Statistics")
        for col in categorical_columns:
            if col in filtered_df.columns:
                st.write(f"{col} Distribution:")
                st.bar_chart(filtered_df[col].value_counts())

        for col in numeric_columns:
            if col in filtered_df.columns:
                st.write(f"{col} Statistics:")
                st.write(filtered_df[col].describe())


if __name__ == "__main__":
    main()
