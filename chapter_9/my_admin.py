from chapter_9.admini import Admin

self = Admin('Rob', 'Tau', 25, 'none')
self.describe_user()
selfish = ['none', 'none', 'none']
self.privileges.privileges = selfish
self.privileges.show_privileges()