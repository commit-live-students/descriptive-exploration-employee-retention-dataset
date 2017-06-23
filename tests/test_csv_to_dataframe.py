from unittest import TestCase
import pandas as pd


filepath = "./data/employee_retention_data.csv"

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import csv_to_dataframe, dtype_category
        res = csv_to_dataframe(filepath)
        res_new = dtype_category(res, ["company_id", "dept"])
        self.assertTrue(isinstance(res_new, pd.DataFrame))

    def test_dtype_datetime(self):
        from build import csv_to_dataframe, dtype_datetime
        res = csv_to_dataframe(filepath)
        res_new = dtype_datetime(res, ["join_date", "quit_date"])
        self.assertTrue(isinstance(res_new, pd.DataFrame))

    def test_linear_regression_model(self):
        from build import csv_to_dataframe, linear_regression_model
        res = csv_to_dataframe(filepath)
        dependent_variable = "salary"
        independent_variable_list = ['Constant Term', 'seniority', 'seniority^2', 'dept_customer_service',
                                     'dept_data_science', 'dept_design', 'dept_engineer', 'dept_marketing',
                                     'dept_sales', 'company_id']
        res_new = linear_regression_model(res, dependent_variable, independent_variable_list)
        self.assertAlmostEqual(res_new, 3.6960569994332442, places=3)

    def test_random_forest_model(self):
        from build import csv_to_dataframe, random_forest_model
        res = csv_to_dataframe(filepath)
        dependent_variable = "salary"
        independent_variable_list = ['Constant Term', 'seniority', 'seniority^2', 'dept_customer_service',
                                     'dept_data_science', 'dept_design', 'dept_engineer', 'dept_marketing',
                                     'dept_sales', 'company_id']
        res_new = random_forest_model(res, dependent_variable, independent_variable_list)
        self.assertAlmostEqual(res_new, 95.984738152970976, places=3)