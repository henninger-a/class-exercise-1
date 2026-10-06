import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    for column in required_columns:
    # If any are missing, log an ERROR and raise ValueError.
        if column not in df.columns:
            logger.error(f'column {column} not in dataframe')
            raise ValueError(f'column {column} not in dataframe')
    # Log an INFO.
    logger.info('checked if required columns are in dataframe')
    # Return the DataFrame.
    return df
