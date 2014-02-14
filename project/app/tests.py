from django.test import TestCase, Client

class IndexViewTest(TestCase):
    def test_index_page_displays_hello_world_message(self):
    	response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.template_name, ['index.html'])
        self.assertEquals(response.content, 'Hello World!')
