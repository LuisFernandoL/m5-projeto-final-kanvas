from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
