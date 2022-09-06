import yaml
from time import sleep
from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from django.http import HttpResponse


class ListJob(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-create_time')
    serializer_class = JobSerializer


class DetailJob(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class LastestJob(generics.ListCreateAPIView):
    queryset = Job.objects.all().filter(
        job_status=0).order_by('-create_time')[:1]
    serializer_class = JobSerializer


def writeConfig(job_id_name, **kwargs):
    template = """apiVersion: batch/v1
    kind: Job
    metadata:
    name: {job_id}
    namespace: jobdemonamespace
    labels:
        job_name: {job_id}
    spec:
    template:
        metadata:
        labels:
            app: my-job-pod-id
        name: my-job-pod-id
        spec:
        containers:
            - image: "shuffler:latest"
            imagePullPolicy: Never
            name: "shuffler"
            command:
                - python3
                - -u
                - ./test.py "{user_id}" "{job_id}" "{app_id}" "{path}" "{img_selected}"
            args:
                - "Kubernetes"
        restartPolicy: Never"""
    with open('yaml_file/'+job_id_name+'.yaml', 'w') as yfile:
        yfile.write(template.format(**kwargs))


def make_yaml(request):
    sleep(1)
    try:
        print("going to make file")
        lastest_job = Job.objects.all().filter(
            job_status=0).order_by('create_time')[:1]
        print(lastest_job[0].job_id)

        writeConfig(lastest_job[0].job_id, job_id=lastest_job[0].job_id,
                    path=lastest_job[0].job_id,
                    user_id=lastest_job[0].user_id,
                    app_id=lastest_job[0].app_id,
                    img_selected=lastest_job[0].img_selected
                    )

        lastest_job = Job.objects.get(job_id=lastest_job[0].job_id)
        lastest_job.job_status = 1
        lastest_job.save()
    except:
        print("can't make yaml file")
    return HttpResponse("""<html><script>    windwow.location.replace('/');   </script></html>""")