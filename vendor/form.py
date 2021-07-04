# from django import forms


#     def __init__(self, *args, **kwargs):
#         super(PostModelForm, self).__init__(*args, **kwargs)
#         self.fields["title"].widget = forms.Textarea()
#         self.fields["title"].error_messages = {
#                 "max_length": "This title is too long.",
#                 "required": "The title field is required."
#             }
#         self.fields["slug"].error_messages = {
#                 "max_length": "This title is too long.",
#                 "required": "The slug field is required.",
#                 "unique": "The slug field must be unique."
#             }

#         for field in self.fields.values():
#             field.error_messages = {
#                 'required': "You know, {fieldname} is required".format(fieldname=field.label),
#             }