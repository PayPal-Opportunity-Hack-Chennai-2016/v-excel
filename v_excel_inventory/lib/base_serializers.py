from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if exclude_fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            disallowed = set(exclude_fields)
            existing = set(self.fields.keys())
            for field_name in existing.intersection(disallowed):
                self.fields.pop(field_name)
