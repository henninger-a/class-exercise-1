import logging
import sys
from pathlib import Path
from class8_src import load_netflix, require_columns


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    input_path = Path("data/messy_netflix_titles.csv")

    # TODO 3:
    # Inside a try/except block:
    try:
         # Load the data and require columns: ["title", "type", "release_year"].
        require_columns(load_netflix(input_path), ["title", "type", "release_year"])
    except ValueError:
        # Catch ValueError and exit with status code 1.
        sys.exit(1)
    # Log an INFO
    logger.info(f'loaded {input_path} and checked for required columns')

if __name__ == "__main__":
    main()
