import uuid
from copy import deepcopy
from datetime import datetime

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import get_points

# Create your views here.

receipts = []


class ReceiptsProcess(APIView):
    # authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = request.data

        myuuid = str(uuid.uuid4())

        data['id'] = myuuid
        # data['purchaseDate'] = datetime.now().date().strftime("%Y-%m-%d")
        # data['purchaseTime'] = datetime.now().time().strftime("%H:%M")
        # data['total'] = str(round(sum([float(x['price']) for x in data['items']]), 2))
        data['points'] = get_points(data)

        receipts.append(data)

        return Response(data={'id': data['id']}, status=status.HTTP_201_CREATED)


class ReceiptsPoints(APIView):
    # authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get(self, request, id, format=None):
        receipt = [x for x in receipts if x['id'] == id]
        if receipt:
            receipt = receipt[0]
            return Response(data={"points": receipt['points']}, status=status.HTTP_200_OK)

        return Response(data=None, status=status.HTTP_404_NOT_FOUND)
