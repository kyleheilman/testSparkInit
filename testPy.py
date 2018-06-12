sc.addPyFile("sparkling-water-2.2.16.zip")
import h2o
from h2o.automl import H2OAutoML
h2o.init()
df = h2o.import_file("https://raw.githubusercontent.com/h2oai/sparkling-water/master/examples/smalldata/prostate.csv")
train, test = df.split_frame(ratios=[.9])
# Identify predictors and response
x = train.columns
y = "CAPSULE"
x.remove(y)
# For binary classification, response should be a factor
train[y] = train[y].asfactor()
test[y] = test[y].asfactor()
# Run AutoML for 60 seconds
aml = H2OAutoML(max_runtime_secs = 60)
aml.train(x = x, y = y, training_frame = train, leaderboard_frame = test)
# View the AutoML Leaderboard
aml.leaderboard
aml.leader
# To generate predictions on a test set, use `"H2OAutoML"` object, or on the leader model object directly as below:
preds = aml.predict(test)
# or
preds = aml.leader.predict(test)
