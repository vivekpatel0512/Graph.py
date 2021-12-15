import pandas as pd
import seaborn as sns
from scipy import stats

con = pd.read_csv('scatter - Sheet6.csv')
con
print(con)
import seaborn as sns
sns.scatterplot(x="Popular Votes", y="Electoral" , data=con);

ax = sns.scatterplot(x="Popular Votes", y="Electoral", data=con)
ax.set_title("Republican Correlation of Popular and Electoral Votes")
sns.lmplot(x="Popular Votes", y="Electoral", data=con);
ax.set_title("Republican Correlation of Popular and Electoral Votes")


sns.lmplot(x="Popular Votes", y="Electoral", data=con);
ax.set_title("Democrat Correlation of Popular and Electoral Votes")
