from django.db import models
import cv2
import json

# Create your models here.
class CCTV_Img(models.Model):

    name = models.CharField(max_length=50)
    CCTV_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return (self.name)

    def processImage(self):

        body_clsfr = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_upperbody.xml')
        new_img = cv2.imread(self.CCTV_Main_Img.path)
        save_location = "media/processed_images/"
        new_name = save_location + self.name[:-3] + "_processed.png"

        bodies = body_clsfr.detectMultiScale(
            new_img,
            scaleFactor=1.04,
            minSize=(30, 40)
        )

        for x, y, w, h in bodies:
            cv2.rectangle(new_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite(new_name, new_img)

        return_dict = {"original_path": self.CCTV_Main_Img.path, "new_path": new_name}
        json_dump = json.dumps(return_dict)
        json_object = json.loads(json_dump)

        return json_object