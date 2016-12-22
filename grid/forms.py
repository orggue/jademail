from __future__ import absolute_import
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms
from ckeditor.widgets import CKEditorWidget

from . import models


class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    template = forms.ModelChoiceField(queryset=models.Template.objects.all())
    content = forms.CharField(widget=CKEditorWidget())
    attachment = forms.FileField(required=False)

    class Meta:
        fields = ('name', 'email', 'subject', 'template', 'content', 'attachment')
        fields_required = ['name', 'email', 'content', 'template', 'subject']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['template'].queryset = models.Template.objects.filter(
                    user=self.request.user)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'template',
            'content',
            'attachment',
            ButtonHolder(
                Submit('send', 'Send', css_class='btn-primary')
                )
            )


class ListForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'template', 'description')
        model = models.List

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'template',
            'description',
            ButtonHolder(
                Submit('send', 'Send', css_class='btn-primary')
                )
            )


class PersonForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'last_name', 'email', 'mobile', 'web', 'linked_in',
                  'facebook', 'lists_id', 'street')
        model = models.Person

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'last_name',
            'email',
            'mobile',
            'web',
            'linked_in',
            'facebook',
            'lists_id',
            'street',
            ButtonHolder(
                Submit('send', 'Send', css_class='btn-primary')
                )
            )


class TemplateForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'content', 'template_file', 'attachment')
        model = models.Template

    def __init__(self, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'content',
            'template_file',
            'attachment',
            ButtonHolder(
                Submit('send', 'Send', css_class='btn-primary')
                )
            )


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'content', 'person_id')
        model = models.Comment

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'content',
            'person_id',
            ButtonHolder(
                Submit('send', 'Send', css_class='btn-primary')
                )
            )
