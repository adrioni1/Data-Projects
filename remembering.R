data= iris
data
library(sqldf)
sqldf(
  "SELECT * from data
  WHERE Species == 'virginica'"
)
