# DataScientest Study Project: Predictive Model for CO2 Emissions Based on Vehicle Attributes
Hello,

This is our Data Science training project at DataScientest.com during which we explored various machine learning modeling techniques to build a predictive model to detect CO2 emissions based on vehicle attributes.

Project team:
- Marta Escobar
- Liva Lacaisse
- Diego Diaz

In this project, we developed and evaluated three models to predict and classify vehicle CO2 emissions using various machine learning techniques: Linear Regression, Ridge Regression, and Classification models. Each model addressed the dataset's complexities uniquely.

We started with data cleaning and preprocessing, initially using a 5-year dataset from Portugal. Later, we expanded to include data from five countries over the same period, providing a robust foundation for our models. This overview highlights the methodologies, key findings, and performance metrics of these models, and the conclusion includes a visual summary of the data by country and energy type.

**Linear Regression Model.**
The goal was to predict CO2 emissions using features like vehicle type, model, fuel consumption, and engine size. We used a preprocessing pipeline with SimpleImputer, StandardScaler, OneHotEncoder, and Truncated SVD to reduce feature complexity. Model performance was evaluated with R² and RMSE metrics.

**Ridge Regression Model.**
To address multicollinearity, we used Ridge Regression, examining correlation matrices for each country. We analyzed vehicles by energy type, excluding zero-emission vehicles. Dimensionality reduction techniques (PCA, ICA, PLS) were tested, with PCA chosen for variable selection. Cross-validation and K-fold methods mitigated overfitting, and predictions were compared with actual outcomes to ensure model robustness.

**Classification Model.**
This model classified vehicles based on the European CO2 emission target of 95g CO2/km. We used Decision Tree, Random Forest, and XGBoost models, optimizing with GridSearchCV, RandomizedSearchCV, and SMOTE to handle data imbalance. The Random Forest model with SMOTE showed the best performance, maintaining high accuracy and balanced feature importance. 

**Streamlit App.**
As a part of the project requirements, we had to build a Streamlit application to present our work. Given that Ridge Regression model presented the most reliable and robust performance, we chose this model to present our work
