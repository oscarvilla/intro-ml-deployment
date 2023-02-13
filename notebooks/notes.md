1. Add data:

dvc add dataset/finantials.csv
dvc add dataset/opening_gross.csv
dvc add dataset/movies.csv

dvc add model/model.pkl

2. Push it to remotes

dvc push dataset/finantials.csv -r dataset-track
dvc push dataset/opening_gross.csv -r dataset-track
dvc push dataset/movies.csv -r dataset-track

dvc push model/model.pkl -r model-track