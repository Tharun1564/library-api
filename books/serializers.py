from rest_framework import serializers
from .models import Book
from .validators import normalize_isbn, is_valid_isbn


class ISBNField(serializers.CharField):
    """Strips hyphens and spaces before length and format checks run."""

    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        return normalize_isbn(value)


class BookSerializer(serializers.ModelSerializer):
    isbn = ISBNField(max_length=13)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_isbn(self, value):
        # value is already normalized here
        if not is_valid_isbn(value):
            raise serializers.ValidationError(
                "Enter a valid ISBN-10 or ISBN-13 (checksum does not match)."
            )

        existing = Book.objects.filter(isbn=value)
        if self.instance is not None:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise serializers.ValidationError("A book with this ISBN already exists.")

        return value