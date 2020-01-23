# coding: utf-8
from atlassian.rest_client import AtlassianRestAPI


class JiraCore(AtlassianRestAPI):

    def get_issue_remotelinks(self, issue_key, global_id=None):
        """
        Finding all Remote Links on an issue, also with filtering by Global ID
        :param issue_key:
        :param global_id: str
        :return:
        """
        url = 'rest/api/2/issue/{issue_key}/remotelink'.format(issue_key=issue_key)
        params = {}
        if global_id:
            params['globalId'] = global_id
        return self.get(url, params=params)

    def add_issue_remotelinks(self, issue_key, remote_url, description, global_id=None):
        """
        Finding all Remote Links on an issue, also with filtering by Global ID
        :param issue_key:
        :param remote_url:
        :param description:
        :param global_id: str
        :return:
        """
        url = 'rest/api/2/issue/{issue_key}/remotelink'.format(issue_key=issue_key)
        params = {}

        data = {
            "object": {
                "url": remote_url,
                "title": description
            }
        }
        if global_id:
            params['globalId'] = global_id
        return self.post(url, data=data, params=params)
