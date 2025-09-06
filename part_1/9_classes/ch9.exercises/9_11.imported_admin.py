from privileges import Admin

admin_1 = Admin("Xavier", "Lopez")

admin_1.show_privileges()
"""
Admin Xavier Lopez, has the following privileges:
- can add posts
- can delete post
- can ban user
- can unban user
- can access deleted posts
"""