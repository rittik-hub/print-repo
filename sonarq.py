from copy import copy

import requests
from requests.auth import HTTPBasicAuth



class Sonarqube:
    PARAM = {'ps': '500'}
    sonarqube_url = 'https://localhost:9000'

    def __init__(self, component_key):
        self.token = 'test'
        self.PARAM['componentKeys'] = component_key
        self.PARAM['statuses'] = 'OPEN'

    def issue_analysis(self):
        issue_types = {
            'bug': 'BUG',
            'code_smell': 'CODE_SMELL',
            'vulnerability': 'VULNERABILITY'
        }

        params = copy(self.PARAM)
        for k, v in issue_types.items():
            params['types'] = v
            test_response = requests.get(self.sonarqube_url, auth=HTTPBasicAuth(username=self.token, password=''),
                                         params=params)
            issue_types[k] = test_response.json()['paging']['total']
          print(issue_types)

    def severities_analysis(self):
        severities_types = {
            'blocker': 'BLOCKER',
            'critical': 'CRITICAL',
            'major': 'MAJOR',
            'minor': 'MINOR',
            'info': 'INFO'

        }
        params = copy(self.PARAM)
        for k, v in severities_types.items():
            params['severities'] = v
            test_response = requests.get(self.sonarqube_url, auth=HTTPBasicAuth(username=self.token, password=''),
                                         params=params)
            severities_types[k] = test_response.json()['paging']['total']
         print(severities_types)

