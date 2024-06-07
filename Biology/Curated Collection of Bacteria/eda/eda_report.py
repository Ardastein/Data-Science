import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import sweetviz as sv

from utils.data_loader import load_data

data = load_data('data/bacteria_list_200.csv')

report = sv.analyze(data)
report.show_html('eda_report.html')
