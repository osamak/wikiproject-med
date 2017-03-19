from django import forms
from wikithon.models import Team
import random
import string

pool = string.uppercase + string.digits + string.lowercase

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']

    def save(self):
        team  = super(TeamForm, self).save(commit=False)
        while True:
            invitation_code = [random.choice(pool) for i in range(10)]
            if not Team.objects.filter(invitation_code=invitation_code).exists():
                break
        team.invitation_code = invitation_code
        team.save()
        return save
