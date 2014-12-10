AD-User-creator
===============
		it currently generates 500 users, you can edit the for loop to create more or less. 
		update these values in the script to match your environment
		department = ["Sales","Support","Engineering","Administration"]
		path = ["OU=support","OU=sales","OU=engineering","OU=administration"]
		dc = ",DC=pfoxcorp,DC=local"

		Department - (not used for permissions, only to create more 'realistic' users)
		path - List all of your OU's that you want User's to go into
		dc - Enter the DN of your AD