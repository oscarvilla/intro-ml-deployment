from dvc import api
import pandas as pd

import sys
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info("Fetching data...")

movie_data_path = api.get_url(
    "dataset/movies.csv", remote="dataset-track")
finantials_data_path = api.get_url(
    "dataset/finantials.csv", remote="dataset-track")
opening_data_path = api.get_url(
    "dataset/opening_gross.csv", remote="dataset-track")

movie_data = pd.read_csv(movie_data_path)
finantials_data = pd.read_csv(finantials_data_path)
opening_data = pd.read_csv(opening_data_path)

breakpoint()
