# from rest_framework import serializers
# from .models import Genre, Publisher, Author, Book, Member, Transaction, Lent

# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ('id', 'title')

# class PublisherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publisher
#         fields = ('id', 'name')

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('id', 'name', 'biography')

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#     genre = GenreSerializer()
#     publisher = PublisherSerializer()

#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'isbn', 'author', 'genre', 'publisher', 'publication_year', 'copies_available')

# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = ('id', 'address', 'membership_status', 'user', 'first_name', 'last_name')

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['user'] = {
#             'id': instance.user.id,
#             'username': instance.user.username,
#             'email': instance.user.email,
#             'phone number':instance.user.phone_number
#         }
#         return data

# class TransactionSerializer(serializers.ModelSerializer):
#     member = MemberSerializer()
#     book = BookSerializer()

#     class Meta:
#         model = Transaction
#         fields = ('id', 'transaction_time', 'member', 'book')

# class LentSerializer(serializers.ModelSerializer):
#     member = MemberSerializer()
#     book = BookSerializer()

#     class Meta:
#         model = Lent
#         fields = ('id', 'lent_time', 'member', 'book')
