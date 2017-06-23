# Employee Retention Dataset

### Question 1
#### Write a funtion to convert given CSV file to Dataframe
* Define function with name `csv_to_dataframe` which should accept `filepath` as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `filepath` which does not exist, function should raise FileNotFoundError.


### Question 2
#### Write a function to convert datatype of given variables to "category"
* Define function with name `dtype_category` which should accept `dataframe` and `list of columns` as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError


### Question 3
#### Write a function to convert datatype of given variables to "datetime"
* Define function with name `dtype_datetime` which should accept `dataframe` and `columns_list`(list of variables) as parameters.
* Function should return a dataframe with type of given columns changed to "datetime".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError


### Question 4
#### Write a function to plot histogram for all numeric variables
* Define function with name `histogram` which should accept `dataframe`, `column_list` (of variables to be plotted) as parameters.
* Function should return plots of numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError


### Question 5
#### Write a function to build a Logistic Regression model
* Define function with name `linear_regression_model` which should accept `dataframe`, `dependent_variable` (as string) and `independent_variable_list` (as a list of columns) as parameters.
* Function should return accuracy of the model in %.
* As we require accuray, type of return variable should be numeric.
* In case if we pass column name which does not exist or is not numerical type, function should raise KeyError


### Question 6
#### Write a function to build a Random Forest model
* Define function with name `random_forest_model` which should accept `dataframe`, `dependent_variable` (as string) and `independent_variable_list` (as a list of columns) as parameters.
* Function should return accuracy of the model in %.
* As we require accuray, type of return variable should be numeric.
* In case if we pass column name which does not exist or is not numerical type, function should raise KeyError