import os
import django
from django.utils import timezone
from dateutil.parser import parse
from datetime import timedelta, datetime
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Passcard, Visit

if __name__ == '__main__':
    current_time = timezone.localtime()
    # tmp_time = parse('2019-06-21 05:10:00+00:00')
    #
    # fin_time = current_time - tmp_time
    # print(fin_time)
    # all_passcards_list = list(Passcard.objects.all())
    all_visits_list = list(Visit.objects.filter(leaved_at=None))
    for visit in all_visits_list:
        print(f"Зашел в хранилище, время по Москве: {visit.entered_at}")
        print(f"Находится в хранилище: {current_time - visit.entered_at}")
    # print(Passcard.objects.filter(visit__leaved_at=None))
# execute_from_command_line("manage.py runserver 0.0.0.0:8000".split())

