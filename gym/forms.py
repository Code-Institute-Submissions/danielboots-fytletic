from django import forms

from .models import Gym, GymType


class GymForm(forms.ModelForm):
    class Meta:
        model = Gym

        # change this to not include all fields -- only admin should

        fields = "__all__"

        # this excludes the below fields
        exclude = ("is_verified", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gymtype = GymType.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in gymtype]

        self.fields["gym_type"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


def __init__(self, *args, **kwargs):
    super(GymForm, self).__init__(*args, **kwargs)
