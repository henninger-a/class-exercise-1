import logging
import re
import pandas as pd

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f'{df.shape[0]} rows and {df.shape[1]} columns')
    print(df.shape, df.head(), df.columns, df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    no_dupes_df = df.drop_duplicates()
    logger.debug(f'Row count with duplicates: {len(df)}, Row count without duplicates: {len(no_dupes_df)}')
    return no_dupes_df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    df_no_missing = df.dropna()
    logger.debug(f'Row count with missing values: {len(df)}, Row count without missing values: {len(df_no_missing)}')
    return df_no_missing

def clean_text(value):
    """Normalize one text value."""
    # TODO 1:
    # Strip surrounding whitespace.
    value = value.strip()
    # Convert text to lowercase.
    value = value.lower()
    # Collapse repeated whitespace.
    value = re.sub(r'\s+', '', value)



def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    # If column does not exist:
    if column not in df.columns:
        # Log an ERROR message and raise ValueError.
        logger.error(f'column {column} not found')
        raise ValueError(f'column {column} not found')
    else:
        # Calculate Q1, Q3, and IQR.
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        # Use threshold to calculate lower and upper bounds.
        lower = q1 - threshold * iqr
        upper = q3 + threshold * iqr
        # Keep rows inside the bounds.
        df_score_cleaned = df[(df[column] >= lower) & (df[column] <= upper)]
        # Log a DEBUG message containing the bounds and the number of rows removed.
        logger.debug(f'lower bound: {lower}, upper bound {upper}, {len(df) - len(df_score_cleaned)} row(s) removed')
        # Return the resulting DataFrame.
        return df_score_cleaned