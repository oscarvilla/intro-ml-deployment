## 1. Add remotes:
How to add your remotes

```bash
dvc remote add dataset_track gs://dvc-storage-tracker/dataset

dvc remote add name_of_your_remote url_of_your_storage
```

## 2. Add data: 
How to add data to tracking

```bash
dvc add dataset/finantials.csv
dvc add dataset/your_data_set.csv

dvc add model/model.pkl
```

## 3. Push data to remotes:
How to then push data to remotes

```bash
dvc push dataset/finantials.csv -r dataset-track
dvc push dataset/your_data_set.csv -r name_of_your_remote

dvc push model/model.pkl -r model-track
```

## 4. Create dags:
How to create teh DAGs

```bash
dvc run -n prepare -o dataset/full_data.csv python src/prepare.py 

dvc run -n training -d dataset/full_data.csv python src/train.py 
```

## 5. Run dags:

```bash
dvc repro
# to force the dags even if is in cache
dvc repro -f
```

## Fix: 
How to remove from Git tracking files added by error

```bash
git rm --cacged <file_to_remove>
git add .
git commit -m "removed files tracked by error"
```

## Run the app:

```bash
uvicorn api.main:app
```

## Run tests:
How to run the tests

````bash
pytest tests.py
```