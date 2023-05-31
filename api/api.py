import pandas as pd
import asana
import json
#identification ASANA
personal_access_token = "personal_acces_token"
#personal_access_token generated by following these instructions : https://asana.com/fr/guide/help/api/api
# asana page app to generate personal access token : https://app.asana.com/0/my-apps

client = asana.Client.access_token(personal_access_token)

client.options["client_name"] = "extraction" #champ libre preferable en un adjectif ce que l on veut faire

#personal info
me = client.users.get_user("me")
workspace_id = me["workspaces"][0]["gid"]
#extraction
#listing des parametres extractibles depuis les appels API voir lien : https://developers.asana.com/reference/rest-api-reference
result1 = client.users.get_users_for_workspace(workspace_id,opt_pretty=True)
#result1bis = client.users.get_users_for_workspace("1110771343212871",{"opt_fields":"email"},opt_pretty=True) #recuperation listing mails
result2 = client.projects.get_projects_for_workspace(workspace_id,opt_pretty=True)
project_list = list(result2)
#example de recuperation de taches
project_id = project_list[0]["gid"]
result3 = client.tasks.get_tasks({"project": project_id})
task_list = list(result3)

users_list = list(result1)









#for task in client.tasks.get_tasks({"project": 1201479249541512}, page_size=3):
#    print(task)








