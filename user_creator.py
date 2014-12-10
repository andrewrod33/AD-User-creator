import random
import os

"""
Lets create some fake names.  We need to make sure we have
Name, samAccountName, Description, Department, EmployeeID, Path, and Enabled
"""

"""
Values to generate random names
"""
fname = ["Bob","John","Tom","Jack","Jill","Sam","Bill","Jerry","Frank","Thomas","Lucas","James","Andrew","David","Jim","Sean"]
lname = ["Smith","Jones","Davis","Fox","Johnson","Washington","Adams","Jefferson","Skywalker","Brown","Miller","Wilson","King","Baker",]
samCount = 0
department = ["Sales","Support","Engineering","Administration"]
employeeID = 1000
path = ["OU=support","OU=sales","OU=engineering","OU=administration"]
dc = ",DC=pfoxcorp,DC=local"
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
	depa = random.choice(department)
	emp = str(employeeID)
	employeeID += 10
	pth = random.choice(path)
	record = 'dsadd user CN="' + samName + str(samCount) + ',' + pth + dc + '" -upn ' + samName+ '@pfoxcorp.local' +' -empid '\
	+ str(employeeID) +' -pwd P@ssw0rd2@ -fn ' + first + ' -ln ' + last + ' -display ' +\
	'"' + name + '"' + ' -email ' + samName+str(samCount) + '@doesn0tex1st.com' + \
	' -pwdneverexpires yes -disabled no -acctexpires never'
	
	"""check for the record that was just created in the output list, if record exists, create another one, if not, write
	the output to the list for recording"""
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