from django.test import TestCase
from .models import Person, Job, Recruiter
import simplejson as json


class PersonTest(TestCase):

    def setUp(self):
        Person.objects.create(
                first_name='Lock', last_name='Ness', address='Monster'
                )
        Person.objects.create(
                first_name='Big', last_name='Foot', address='Monster'
                )

        def test_candidate_creation(self):
            pass

        def test_person_first_name(self):
            lock_person = Person.objects.get(first_name='Lock')
            big_person = Person.objects.get(first_name='Big')
            self.assertEqual(lock_person.first_name, 'Lock')
            self.assertEqual(big_person.first_name, 'Big')

        def test_person_last_name(self):
            lock_person = Person.objects.get(first_name='Lock')
            big_person = Person.objects.get(first_name='Big')
            self.assertEqual(lock_person.last_name, 'Ness')
            self.assertEqual(big_person.last_name, 'Foot')


class JobAPITest(TestCase):
    def setUp(self):
        pass

    def test_can_create_job_on_api(self):
        response = self.client.post('/api/jobs', json.dumps(job_data), 'application/vnd.api+json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, Job.object.all().count())

    def test_can_edit_job_on_api(self):
        job = createJob()
        job_data = {
                'data': {
                    'attributes': {
                        'job-type': 'full time',
                        'job-title': 'late',
                        'company-name': 'always',
                        'company-address': 'deep dark ocean',
                        'job-description': 'dont be late anymore'
                        },
                    'type': 'jobs',
                    'id': job.pk
                    }
                }
        response = self.client.patch('/api/jobs/{}'.format(job.pk), json.dumps(job_data),
                                     content_type='application/vnd.api+json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Job.objects.all().count())
        response_id = json.loads(response.content)['data']['id']
        self.assertEqual(job.pk, Job.objects.get(id=response_id).id)

    def test_can_delete_job_on_api(self):
        job = createJob()
        beforeDelete = self.client.get('/api/jobs/{}'.format(job.pk))
        response = self.client.delete('/api/jobs/{}'.format(job.pk))
        afterDelete = self.client.get('/api/jobs/{}'.format(job.pk))
        self.assertEqual(200, beforeDelete.status_code)
        self.assertEqual(204, response.status_code)
        self.assertEqual(404, afterDelete.status_code)


class PersonAPITest(TestCase):
    def test_can_create_person_on_api(self):
        job = createJob()
        data = {
                'data': {
                    'attributes': {
                        'first-name': 'Test',
                        'last-name': 'Person',
                        'address': '1234 north e. rd',
                        },
                    'type': 'people',
                    'relationships': {
                        'job': {
                            'data': {
                                'type': 'jobs',
                                'id': job.pk
                                }
                            }
                        }
                    }
                }
        response = self.client.post('/api/people', json.dumbs(data), 'application/vnd.api+json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, Person.objects.all().count())

    def test_can_edit_person_on_api(self):
        person = createPerson()
        person_data = {
                'data': {
                    'id': person.pk,
                    'attributes': {
                        'first-name': 'Test',
                        'last-name': 'Person',
                        'address': '123 rainbow rd.',
                        },
                    'type': 'people',
                    'relationships': {
                        'job': {
                            'data': None
                            }
                    }
                }
                }
        response = self.client.patch('/api/people/{}'.format(person.pk), json.dumps(person_data),
                                     content_type='application/vnd.api+json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Person.objects.all().count())
        response_id = json.loads(response.content)['data']['id']
        self.assertEqual(person.pk, Person.objects.get(id=response_id).id)
        self.assertEqual('Test', Person.objects.get(id=response-id).first_name)

    def test_can_delete_person_on_api(self):
        person = createPerson()
        beforeDelete = self.client.get('/api/people/{}'.format(person.pk))
        response = self.client.delete('/api/people/{}'.format(person.pk))
        afterDelete = self.client.get('/api/people/{}'.format(person.pk))
        self.assertEqual(200, beforeDelete.status_code)
        self.assertEqual(204, response.status_code)
        self.assertEqual(404, afterDelete.status_code)


class RecruiterAPITest(TestCase):
    def test_can_creat_recruiter_on_api(self):
        data = {
                'data': {
                    'type': 'recruiters',
                    'attributes': {
                        'first-name': 'Brain',
                        'last-name': 'Elliott',
                        'address': 'under the sea',
                        },
                    'relationships': {
                        'candidate': None
                        }
                    }
                }
        response = self.client.post('/api/recruiters', json.dumps(data), 'application/vnd.api+json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, Recruiter.objects.all().count())

    def test_can_edit_recruiter_on_api(self):
        recruiter = createRecruiter()
        recruiter_data = {
                'data': {
                    'id': recruiter.pk,
                    'type': 'recruiters',
                    'attributes': {
                        'first-name': 'T',
                        'last-name': 'Rex',
                        'address': 'extinct'
                        },
                    'relationships': {
                        'candidate': None
                        }
                    }
                }
        response = self.client.patch('/api/recruiters/{}'/format(recruiter.pk), json.dumps(recruiter_data),
                                     content_type='application/vnd.api+json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, Recruiter.objects.all().count())
        response_id = json.loads(response.content)['data']['id']
        self.assertEqual(recruiter.pk, Recruiter.objects.get(id=response_id).id)
        self.assertEqual('Brian', Recruiter.objects.get(id=response_id).first_name)

    def test_can_delete_recruiter_on_api(self):
        recruiter = createRecruiter()
        beforeDelete = self.client.get('/api/recruiters/{}'.format(recruiter.pk))
        response = self.client.delete('/api/recruiters/{}'.format(recruiter.pk))
        afterDelete = self.client.get('/api/recruiters/{}'.format(recruiter.pk))
        self.assertEqual(200, beforeDelete.status_code)
        self.assertEqual(204, response.status_code)
        self.assertEqual(404, afterDelete.status_code)


def createPerson():
    return Person.objects.create(first_name='Ron', last_name='Swanson')


def createRecruiter():
    return Recruiter.objects.create(first_name='Leslie', last_name='Knope')


def createJob():
    return Job.objects.create(job_type='No Time', job_title="snooze")


job_data = {
        'data': {
            'attributes': {
                'job-type': 'No Time',
                'job-title': 'late',
                'company-name': 'deep sea',
                'company-address': '123 candy st',
                'job-description': 'dont be late and eat cnady'
                },
            'type': 'jobs'
            }
        }
