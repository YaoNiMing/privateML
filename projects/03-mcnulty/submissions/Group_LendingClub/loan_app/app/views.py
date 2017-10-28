import logging
import json

from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
import pandas as pd
import numpy as np

from . import app, estimator, estimator2, target_names


logger = logging.getLogger('app')

class PredictForm(Form):
    """Fields for Predict"""
    states = [(0, "AK"), (1, "AL"), (2, "AR"), (3,"AZ"), 
        (4,"CA"), (5,"CO"), (6, "CT"), (7, "DC"), (8, "DE"),
        (9, "FL"), (10, "GA"), (11, "HI"), (26, 'IA'), (26, 'ID'), (12, "IL"),
        (13, "IN"), (14, "KS"), (15, "KY"), (16, "LA"),
        (17, "MA"), (18, "MD"), (19, "ME"), (20, "MI"),
        (21, "MN"), (22, "MO"), (23, "MS"), (24, "MT"),
        (25, "NC"), (26, "ND"), (27, "NE"), (28, "NH"),
        (29, "NJ"), (30, "NM"), (31, "NV"), (32, "NY"),
        (33, "OH"), (34, "OK"), (35, "OR"), (36, "PA"),
        (37, "RI"), (38, "SC"), (39, "SD"), (40, "TN"),
        (41, "TX"), (42, "UT"), (43, "VA"), (44, "VT"),
        (45, "WA"), (46, "WI"), (47, "WV"), (48, "WY")]

    emp_time = [(0, '1 year'), (1, '10+ years'),
     (2, '2 years'), (3, '3 years'), 
     (4, '4 years'), (5, '5 years'),
     (6, '6 years'), (7, '7 years'), 
     (8, '8 years'),(9, '9 years'), (10, '< 1 year'),
      (11, 'n/a')]

    title_options = [(0, 'Auto'), (1, 'Business'),
       (2, 'Credit Card Refinancing'), 
       (3, 'Debt Consolidation'),
       (4, 'Educational'), (5, 'Green Loan'), 
       (6, 'Home Buying'), (7, 'Home Improvement'), 
       (8, 'Major Purchase'), (9, 'Medical Expenses'), 
       (10, 'Moving and Relocation'), (11, 'Other'),
       (12, 'Renewable Energy'), (13, 'Vacation')]

    addr_state = fields.SelectField("State:", choices=states, coerce=int)
    loan_amnt = fields.DecimalField('Loan Amount:', places=2, validators=[Required()])
    dti = fields.DecimalField('Debt to Income Ratio:', places=2, validators=[Required()])
    emp_length = fields.SelectField('Employment Length:', choices=emp_time, coerce=int)
    title = fields.SelectField('Loan Title:', choices=title_options, coerce=int)

    term = fields.DecimalField('Term Length (in Months):', places=2, validators=[Required()])
    installment = fields.DecimalField('Monthly Installment:', places=2, validators=[Required()])
    bc_util = fields.DecimalField('Current Balance to Credit Limit Ratio:', places=2, validators=[Required()])
    num_tl_op_past_12m = fields.DecimalField('Accounts Opened in Past Year:', places=2, validators=[Required()])
    
    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    predicted_loan = None
    my_grade_prediction = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data

        # Retrieve values from form
        loan_amnt = float(submitted_data['loan_amnt'])
        title = float(submitted_data['title'])
        dti = float(submitted_data['dti'])
        addr_state = float(submitted_data['addr_state'])
        emp_length = float(submitted_data['emp_length'])
        
        term = float(submitted_data['term'])
        installment = float(submitted_data['installment'])
        bc_util = float(submitted_data['bc_util'])
        num_tl_op_past_12m = float(submitted_data['num_tl_op_past_12m'])
        # Create array from values
        application_instance = pd.DataFrame([[loan_amnt, dti, title, addr_state, emp_length]], 
            columns=['loan_amnt', 'dti', 'title', 'addr_state', 'emp_length'])

        grade_instance = pd.DataFrame([[term, installment, bc_util, dti, loan_amnt, num_tl_op_past_12m]],
            columns= ['term', 'installment', 'bc_util', 'dti', 'loan_amnt', 'num_tl_op_past_12m'])

        my_app_prediction = estimator.predict(application_instance)
        my_grade_prediction = estimator2.predict(grade_instance)
        my_grade_prediction = my_grade_prediction[0]
        # my_grade_prediction - my_grade_prediction.replace('\'', '')
        # Return only the Predicted loan decision
        predicted_loan = target_names[my_app_prediction]
    else:
        print(form.errors)

    return render_template('index.html',
        form=form,
        prediction=predicted_loan,
        prediction_grade=my_grade_prediction)
