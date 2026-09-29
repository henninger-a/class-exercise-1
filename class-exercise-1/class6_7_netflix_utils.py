import logging

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