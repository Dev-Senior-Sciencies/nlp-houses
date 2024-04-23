# MLFlow

1. [Setup](#setup)
2. [Dataset](#dataset)

## Setup

### Pre-reqs

* Python 3 (I specifically use 3.9.12, but should work in other versions)
* Git
* Knowledge about Machine Learning Models

### Setting up your working environment

1. Clone this repo

```console
git clone ```

2. Create a Python venv

    There are many ways to do that. I'll use the simple one, but you can use your preferable.

    Inside of the clonned path run:

```console
py -m venv .env
```

3. Activate venv

> For Linux:
```console
source .env/bin/activate
```

> For Windows:

```console
.env/Scripts/Activate
```


3. Install requirements.txt

```console
pip install -r requirements.txt
```

## Dataset

#### Dataset Information

The Office of Policy and Management maintains a listing of all real estate sales with a sales price of $2,000 or greater that occur between October 1 and September 30 of each year. For each sale record, the file includes: town, property address, date of sale, property type (residential, apartment, commercial, industrial or vacant land), sales price, and property assessment.

#### Source

https://www.kaggle.com/datasets/utkarshx27/real-estate-sales-2001-2021-gl/download?datasetVersionNumber=1

US Real Estate Sales 2001-2021 GL
