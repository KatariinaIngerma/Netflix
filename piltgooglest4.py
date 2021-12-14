from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
absolute_image_paths = response.download({
                "keywords": "kass",
                 "format": "png",
                 "limit":1,
                 "size": "medium",
                 "aspect_ratio":"panoramic"})