from chapter_9.Admin import Admin, User, Privileges

adm = Admin('Tomas', 'Lukas', 37, 'truck driver')
adm.describe_user()
adm_Privileges = ['some', 'none', 'few']
adm.privileges.privileges = adm_Privileges
adm.privileges.show_privileges()