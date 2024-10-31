import json
import random

from django.http import JsonResponse
from django.utils import timezone
from social_django.views import login_required

from .models import CreatureEncounter, Creature, CreatureInstance


@login_required()
def get_encounter(request):
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


@login_required()
def finish_encounter(request):
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