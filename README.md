
https://lewagon-alumni.slack.com/archives/C015E0C601F/p1643729354949839

# steps

## create student env + generate pickles

``` bash
. ./env_student.sh
python challenge.py
```

## tests succeed with student env

``` bash
pyenv local nbr_student
pytest tests/test_data.py
```

## create glovebox env

``` bash
. ./env_glovebox.sh
```

## tests fail with glovebox env

``` bash
pyenv local nbr_glovebox
pytest tests/test_data.py
```
