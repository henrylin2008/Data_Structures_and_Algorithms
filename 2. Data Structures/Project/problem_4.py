# Active Directory
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can
# construct this hierarchy as such. Where User is represented by str representing their ids.
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:   # invalid input
        print("Please provide a valid user or group")
        return False

    if user in group.users:
        return True
    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False


# Test cases
# parent
#   -child1
#       -sub-child11
#       -sub-child12
#   -child2
#       -sub-child21
#       -sub-child22

# Groups
parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")
sub_child1 = Group("sub-child1")
sub_child2 = Group("sub-child2")

# Users
parent_user = "parent_user"
child1_user = "child1_user"
child2_user = "child2_user"
sub_child1_user1 = "sub_child1_user1"
sub_child1_user2 = "sub_child1_user2"
sub_child2_user1 = "sub_child2_user1"
sub_child2_user2 = "sub_child2_user2"

parent.add_user(parent_user)
parent.add_group(child1)
parent.add_group(child2)

child1.add_user(child1_user)
child1.add_group(sub_child1)

child2.add_user(child2_user)
child2.add_group(sub_child2)

child1.add_user(sub_child1_user1)
child1.add_user(sub_child1_user2)

child2.add_user(sub_child2_user1)
child2.add_user(sub_child2_user2)


print(is_user_in_group(parent_user, parent))  # Should return True
print(is_user_in_group(sub_child1_user1, sub_child1))  # should return False
print(is_user_in_group(sub_child1_user2, child1))   # should return True
print(is_user_in_group(sub_child2_user1, child2))  # Should return True
print(is_user_in_group(child1_user, child1))    # should return True
print(is_user_in_group(child2_user, child1))    # should return False
print(is_user_in_group(sub_child2_user1, parent))   # should return False
print(is_user_in_group(sub_child2_user2, child1))   # should return False
