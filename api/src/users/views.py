from rest_framework import generics, permissions
from rest_framework.response import Response
from users.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny, )

class WelcomeView(generics.GenericAPIView):
	permission_classes = (permissions.AllowAny, )

	def get(self,request,*args,**kwargs):
		return Response({'hello':'world'})

register = RegisterAPIView.as_view()
hello = WelcomeView.as_view()