def is_organizer(user):
    return user.groups.filter(name="Organizers").exists()

def is_reviewer(user):
    return user.groups.filter(name="Reviewers").exists()
