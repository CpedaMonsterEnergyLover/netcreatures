import json
import random

from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CreatureEncounter, Creature, CreatureInstance
from django.http import JsonResponse


class GetEncounter(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user

        # decide by time of previous encounter
        # decide by status of previous encounter (must not be in process)
        latest_encounter = CreatureEncounter.objects.filter(user=user).order_by('date_created').first()
        print((latest_encounter.date_created - timezone.now()).seconds)
        if latest_encounter and (latest_encounter.date_created - timezone.now()).seconds < 30:
            return JsonResponse(data={
                'status': 'error',
                'message': 'previous encounter is still pending'
            }, safe=False)

        # create encounter
        new_encounter = CreatureEncounter(
            creature=random.choice(list(Creature.objects.all())),
            user=user
        )
        new_encounter.save()

        return JsonResponse(data={
            'status': 'ok',
            'encounter_id': new_encounter.id
        }, safe=False)


class FinishEncounter(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        data = json.loads(request.body)
        encounter_id = data.get('encounter_id')

        encounter = CreatureEncounter.objects.find(user=user, id=encounter_id)
        if not encounter or encounter.status != 'pending':
            return JsonResponse(data={
                'status': 'error',
                'message': 'invalid encounter id'
            }, safe=False)

        encounter.status = 'success'
        encounter.save()

        CreatureInstance(
            user=user,
            creature=encounter.creature
        ).save()

        return JsonResponse(data={
            'status': 'ok',
        }, safe=False)