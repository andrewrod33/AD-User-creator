import random
import os

"""
Lets create some fake names.  We need to make sure we have
Name, samAccountName, Description, Department, EmployeeID, Path, and Enabled
"""

"""
Values to generate random names
"""
fname = ["Bob","John","Tom","Jack","Jill","Sam","Bill","Jerry","Frank","Thomas","Lucas"]
lname = ["Smith","Jones","Davis","Fox","Chang","Washington","Adams","Jefferson","Skywalker","Palpatine"]
samAname = 0
description = ["Sales","Support","Engineer","Administration"]
department = ["Sales","Support","Engineering","Administration"]
employeeID = 1000
path = ["OU=support,DC=pfoxcorp,DC=local","OU=sales,DC=pfoxcorp,DC=local","OU=engineering,DC=pfoxcorp,DC=local","OU=administration,DC=pfoxcorp,DC=local"]
enabled = "True"
output = []



"""
dsadd command:
dsadd user CN=John,CN=Users,DC=it,DC=uk,DC=savilltech,DC=com -samid John -pwd Pa55word 
-fn John -ln Savill -display "John Savill" -email john@savilltech.com -webpg http://www.savilltech.com -pwdneverexpires yes 
-memberof "CN=Domain Admins,CN=Users,DC=it,DC=uk,DC=savilltech,DC=com"
"""


for x in range(500):
	first = random.choice(fname)
	last = random.choice(lname)
	name = first + " " + last
	samName = str.lower(first+last+str(samAname))
	samAname += 1
	desc = random.choice(description)
	depa = random.choice(department)
	emp = str(employeeID)
	employeeID += 10
	pth = random.choice(path)
	record = 'dsadd user CN="' + samName + str(samAname) + ',' + pth + '" -upn ' + samName+ '@pfoxcorp.local' +' -empid '\
	+ str(employeeID) +' -pwd P@ssw0rd2@ -fn ' + first + ' -ln ' + last + ' -display ' +\
	'"' + name + '"' + ' -email ' + samName+str(samAname) + '@doesn0tex1st.com' + \
	' -pwdneverexpires yes' + ' -disabled no' + ' -acctexpires never'
	if record not in output:
		output.append(record)

"""Lets remove any existing files so we do not write the same user record twice"""

try:
	os.remove('output.txt')
except:
	pass

""" Write the output to output.txt"""
f = open('output.txt', 'w')
for each in output:
	f.write(each + "\n")

f.close()