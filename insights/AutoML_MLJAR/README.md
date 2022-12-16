MLJAR ANALYSIS: Focused around regression studying the gender of patient and noshow as the continuous variable - The Xgboost was selected as the best model type as the metric value was 11.3922, whereas the metric value for baseline model was 19.9162. Thus, the Xgboost performed better than the baseline model.        - There were two values that equaled to 1, one value that equaled to 0.925 and one equaled to 0.875 in the spearman correlations of models. The closer the AUC value is to 1, the more accurate the model is.







# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | rmse          |        19.9162 |         1.28 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | rmse          |        12.6346 |        83.08 |
| **the best** | [3_Default_Xgboost](3_Default_Xgboost/README.md)             | Xgboost        | rmse          |        11.3922 |       188.64 |
|              | [4_Default_NeuralNetwork](4_Default_NeuralNetwork/README.md) | Neural Network | rmse          |        13.346  |       105.8  |
|              | [5_Default_RandomForest](5_Default_RandomForest/README.md)   | Random Forest  | rmse          |        12.2772 |       167.22 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | rmse          |        11.3922 |         0.28 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

