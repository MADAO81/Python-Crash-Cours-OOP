import user

privileges = ["allowed to add messages", "allowed to delete users", "allowed to ban users"]
admin_gorilla = Admin("Isao", "Kondou", "male",33, "japanese",privileges)
print(admin_gorilla.greet_user())
admin_gorilla.admin_rights()