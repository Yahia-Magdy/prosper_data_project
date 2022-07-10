#importing libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns



df= pd.read_csv('prosperLoanData.csv')
df.describe().to_csv('raw_data.csv',index=False)

#PERFORMING Data cleaning

df['TotalProsperLoans']=df['TotalProsperLoans'].fillna(0)
df['TotalProsperPaymentsBilled']=df['TotalProsperPaymentsBilled'].fillna(0)
df['OnTimeProsperPayments']=df['OnTimeProsperPayments'].fillna(0)
df['ProsperPaymentsLessThanOneMonthLate']=df['ProsperPaymentsLessThanOneMonthLate'].fillna(0)
df['ProsperPaymentsOneMonthPlusLate']=df['ProsperPaymentsOneMonthPlusLate'].fillna(0)
df['ProsperPrincipalBorrowed']=df['ProsperPrincipalBorrowed'].fillna(0)
df['ProsperPrincipalOutstanding']=df['ProsperPrincipalOutstanding'].fillna(0)
df['ScorexChangeAtTimeOfListing']=df['ScorexChangeAtTimeOfListing'].fillna(0)




df['Occupation']=df['Occupation'].fillna('No occupation')
df['ClosedDate']=df['ClosedDate'].fillna('NaN')
df['GroupKey']=df['GroupKey'].fillna('No_group')
df['DebtToIncomeRatio']=df['DebtToIncomeRatio'].fillna(df['DebtToIncomeRatio'].mean())
df['LoanFirstDefaultedCycleNumber']=df['LoanFirstDefaultedCycleNumber'].fillna('Not charged off')
#df['CreditGrade']=df['CreditGrade'].fillna('NaN')
#df['ProsperRating (Alpha)']=df['ProsperRating (Alpha)'].fillna('NaN')



df.dropna(subset = ["EmploymentStatusDuration"], inplace=True)
df.dropna(subset = ["CurrentCreditLines"], inplace=True)
#df = df.fillna('NaN')

#missing_values_count = df.isnull().sum()
#missing_values_count.to_csv('miss.csv',index=False)

#df.to_csv('data.csv' , index=False)


#plotting

sns.histplot(data=df,x='BorrowerRate',hue='LoanStatus')
plt.show()
sns.histplot(data=df['CreditGrade'])
plt.show()
sns.histplot(data=df['LoanStatus'])
plt.show()
sns.histplot(data=df['ProsperRating (Alpha)'] )
plt.show()
sns.histplot(data=df ,x='ProsperRating (Alpha)', hue='LoanStatus')
plt.show()
sns.histplot(data=df ,x='ProsperScore', hue='LoanStatus')
plt.show()
sns.histplot(data=df ,x='BankcardUtilization', hue='LoanStatus')
plt.show()
sns.histplot(data=df ,x='CreditGrade', hue='LoanStatus')
plt.show()

sns.lineplot(x=df['CreditGrade'], y=df['BorrowerRate'])
plt.show()

sns.histplot(data=df['DebtToIncomeRatio'])
plt.show()
sns.histplot(data=df ,x='TotalProsperLoans', hue='LoanStatus')
plt.show()

sns.histplot(data=df ,x='IncomeRange', hue='LoanStatus')
plt.show()
sns.boxplot(y = 'BorrowerRate',data= df, x= 'ProsperRating (Alpha)')
plt.show()

sns.boxplot(y = 'BorrowerRate',data= df, x= 'ProsperScore')
plt.show()
sns.boxplot(y = 'BankcardUtilization',data= df, x= 'ProsperScore')
plt.show()
sns.boxplot(y = 'ProsperScore',data= df, x= 'ProsperRating (Alpha)')
plt.show()

sns.boxplot(y = 'MonthlyLoanPayment',data= df, x= 'ProsperRating (Alpha)')
plt.show()

sns.histplot(data=df ,x='StatedMonthlyIncome')
plt.show()

sns.histplot(data=df ,x='EmploymentStatusDuration')
plt.show()

sns.histplot(data=df ,x='EmploymentStatusDuration', hue='CreditGrade')
plt.show()


sns.histplot(data=df ,x='TotalCreditLinespast7years')
plt.show()

sns.swarmplot(x=df['CurrentlyInGroup'], y=df['LoanStatus'])
plt.show()