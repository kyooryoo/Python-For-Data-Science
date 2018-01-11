import pandas as pd

# practice 1
sal = pd.read_csv('Salaries.csv')

print("head of the input data:\n{}".format(sal.head()))
print("summary of the input data:\n{}".format(sal.info()))
print("the average basepay: {}".format(sal['BasePay'].mean()))
print("the highest overtime pay: {}".format(sal['OvertimePay'].max()))

print("the job title of JOSEPH DRISCOLL:\n{}"
      .format(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']))

print("the total pay benefits of JOSEPH DRISCOLL:\n{}"
      .format(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']
      ['TotalPayBenefits']))

print("the highest payed person is:\n{}"
      .format(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
      ['EmployeeName']))
print("another way for the same answer:\n{}"
      .format(sal.loc[sal['TotalPayBenefits'].idxmax()].loc['EmployeeName']))


print("the lowest payed person is:\n{}"
      .format(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
      ['EmployeeName']))
print("another way for the same answer:\n{}"
      .format(sal.loc[sal['TotalPayBenefits'].idxmin()].loc['EmployeeName']))

print("average basepay per year is:\n{}"
      .format(sal.groupby('Year')['BasePay'].mean()))

print("the number of unique job title is: {}"
      .format(sal['JobTitle'].nunique()))

print("the top 5 most common jobs are:\n{}"
      .format(sal.groupby('JobTitle')['JobTitle'].count()
      .sort_values(ascending=False)[:5]))
# optional solution: sal['JobTitle'].value_counts().head(5)

s1 = sal.loc[sal['Year']==2013]
s2 = s1.groupby('JobTitle').count()
s3 = s2[s2['Id']==1]['Id']
print("# of job titles represented by only one person in 2013: {}"
      .format(s3.count()))
# optional: sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)

def search_chief(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

result = sum(sal['JobTitle'].apply(lambda x: search_chief(x)))
print("the number of persons have 'chief' in jot title is: {}"
      .format(result))

sal['TitleLength'] = sal['JobTitle'].apply(len)
result = sal[['TotalPayBenefits','TitleLength']].corr()
print("the correlation between length of jot title and salary is:\n{}"
      .format(result))

# note
# look up the application of value_counts(), idxmax(), argmax()

# practice 2
ecom = pd.read_csv('Ecommerce Purchases')

print("head of the ecommerce purchases dataframe:\n{}"
      .format(ecom.head()))
print("summary of this sample dataframe:\n{}"
      .format(ecom.info()))
print("the average purchase price is: {}"
      .format(ecom['Purchase Price'].mean()))
print("the highest purchase price: {}"
      .format(ecom['Purchase Price'].max()))
print("the lowest purchase price: {}"
      .format(ecom['Purchase Price'].min()))
print("the number of people have en as language of choice:\n{}"
      .format(ecom[ecom['Language']=='en'].count()))
print("the number of people have job title as lawyer:\n{}"
      .format(ecom[ecom['Job']=='Lawyer'].count()))
print("number of purchase during AM or PM:\n{}"
      .format(ecom['AM or PM'].value_counts()))
print("the 5 most common job title:\n{}"
      .format(ecom['Job'].value_counts().head(5)))
print("price of the purchase from lot 90 WT:\n{}"
      .format(ecom[ecom['Lot']=='90 WT']['Purchase Price']))
print("email of the person with credit card 4926535242672853:\n{}"
      .format(ecom[ecom['Credit Card']==4926535242672853]['Email']))

cond1 = ecom['CC Provider']=='American Express'
cond2 = ecom['Purchase Price'] > 95
print("# of people with American Express CC and purchased above 95$:\n{}"
      .format(ecom[cond1 & cond2].count()))

def exp_2025(date):
    if date[3:] == '25':
        return True
    else:
        return False
    
print("# of people with CC expired in 2025: \n{}"
      .format(sum(ecom['CC Exp Date'].apply(lambda x: exp_2025(x)))))

ecom['Email Domain'] = ecom['Email'].apply(lambda x: x.split('@')[1])
print("top 5 most popular email provider:\n{}"
      .format(ecom['Email Domain'].value_counts().head(5)))