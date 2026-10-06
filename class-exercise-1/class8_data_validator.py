import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logger.error(f'{len(missing_columns)} column(s) not in dataframe')
        raise ValueError(f'{len(missing_columns)} column(s) not in dataframe')
    # Log an INFO.
    logger.info('checked if required columns are in dataframe')
    # Return the DataFrame.
    return df
