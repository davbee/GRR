This program calcualtes Gauge R&R parameters from test data.

acceptance criteria for pass or fail of the measurements value = GaugeRnR Variance

- if grr_value < 0.10: print('Gage R&R variance < 10%: Acceptable and good test method')
- elif grr_value > 0.10 and value < 0.3: print('Gage R&R variance between 10-30%: Acceptable dependent upon method of measurement, application')
- elif grr_value > 0.3: print('Gage R&R variance >30%: Unacceptable and requires improvement')