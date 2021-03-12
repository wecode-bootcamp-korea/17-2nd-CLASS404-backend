# user/tests.py

class MyPageImageUploadTest(TestCase):
    @patch('class404.utils.boto3.client')
    def test_post_image_success(self, mock_s3client):
        client  = Client()
        mock_file = MagicMock(spec=File)
        mock_file.name = 'test.png'
        mock_s3client.upload_fileobj = MagicMock()

        response = client.post(
            '/user/mypage/image',
            {'fileName': mock_file},
            **{"HTTP_AUTHORIZATION":self.access_token}
            )
        self.assertEqual(response.status_code, 200)
    