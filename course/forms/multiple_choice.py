from django import forms

from course.fields import JSONFormField
from course.forms.forms import ProblemCreateForm
from course.models.models import CheckboxQuestion, MultipleChoiceQuestion
from course.widgets import RadioInlineSelect


class ChoiceProblemCreateForm(ProblemCreateForm):
    choices = JSONFormField(
        widget=forms.HiddenInput(),
        initial='{}',
    )


class CheckboxQuestionForm(ChoiceProblemCreateForm):
    class Meta:
        model = CheckboxQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'visible_distractor_count', 'variables', 'event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    visible_distractor_count = forms.ChoiceField(
        choices=[('999', 'All'), ('2', '2'), ('3', '3')],
        initial='All',
        widget=RadioInlineSelect()
    )

    answer = None
    choices = None


class MultipleChoiceQuestionForm(ChoiceProblemCreateForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'visible_distractor_count', 'variables', 'event')

    visible_distractor_count = forms.ChoiceField(
        choices=[('999', 'All'), ('2', '2'), ('3', '3')],
        initial='All',
        widget=RadioInlineSelect()
    )

    choices = None
    answer = None


class ChoiceForm(forms.Form):
    text = forms.CharField(
        label='Answer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.empty_permitted = False