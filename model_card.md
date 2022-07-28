# Model Card

- Date: 2022-JUL
- Author: Wonyoung Seo

## Model Details



## Intended Use

The model is intended to predict the salary category of a person based on census data.

## Training Data

Raw data is provided in the following source (https://archive.ics.uci.edu/ml/datasets/census+income). The raw data went through EDA and preprocessing. The final training data is prepared under `./data/prepared/census_cleaned.csv`

## Evaluation Data

15% of the total data is randomly picked in order to validate the model performance

## Metrics

The performance of the model is measured based on Precision, Recall and fbeta score.

```
precision: 0.7025862068965517
recall: 0.5582191780821918
fbeta: 0.6221374045801527
```

## Ethical Considerations

Predicting one's salary based on census information such as gender, race and age can result in bias because those features \
are based on a person's natural attributes. Also, census data is based on human survey, which can cause inaccurate data quality. \
Therefore it is advised to design much more accurate census survey in order to achieve data quality. 

## Caveats and Recommendations

Future work is needed to diversify `gender` category and `education`.
