
from django.forms import BaseInlineFormSet, ModelForm, modelformset_factory
from django.core.exceptions import ValidationError
from django import forms

from .models import Choice


class ChoiceInlineFormSet(BaseInlineFormSet):
    def clean(self):
        num_correct_answer = sum(1 for form in self.forms if form.cleaned_data['is_correct'])

        if num_correct_answer == 0:
            raise ValidationError('Необходимо выбрать как минимум 1 правильный ответ.')

        if num_correct_answer == len(self.forms):
            raise ValidationError('Не могут быть все ответы правильными')



class QuestionInlineFormSet(BaseInlineFormSet):
    def clean(self):
        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError('Кол-во вопросов должно быть в диапазоне от {} до {}'.format(
                self.instance.QUESTION_MIN_LIMIT,
                self.instance.QUESTION_MAX_LIMIT
            ))

        clean_order_num = [form.cleaned_data['order_num'] for form in self.forms]

        if min(clean_order_num) != 1:
            raise ValidationError('Numeration must start from 1')
        if max(clean_order_num) != len(self.forms):
            raise ValidationError('Maximal number mustn`t be more of count questions')
        if len(clean_order_num) != len(set(clean_order_num)):
            raise ValidationError('Falce numeration')



class ChoiceForm(ModelForm):
    is_selected = forms.BooleanField(required=True)

    class Meta:
        model = Choice
        fields = ['text']


ChoicesFormset = modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)