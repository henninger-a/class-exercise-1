import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    # Create a Path object from args.input.
    # Inside a try block, load that path using pd.read_csv().
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.
    path = Path(args.input)
    try:
        df = pd.read_csv(path)
        logger.info(f'Loaded {df.shape[0]} rows and {df.shape[1]} columns')
    except FileNotFoundError:
        logger.error(f'File not found: {path}')
        sys.exit(1)

    # TODO 5:
    # Call show_overview().
    # Log an INFO message.
    show_overview(df)
    logger.info('Displayed DataFrame overview')

    # TODO 6:
    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.
    no_dupes = remove_duplicates(df)
    logger.info(f'Removed {len(df) - len(no_dupes)} duplicate rows(s)')
    cleaned_df = drop_missing_rows(no_dupes)
    logger.info(f'Removed {len(no_dupes) - len(cleaned_df)} row(s) with missing values')

if __name__ == "__main__":
    main()
