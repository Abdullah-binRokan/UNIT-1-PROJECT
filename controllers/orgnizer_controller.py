import os
import shutil

from views import orgnizer_view as o_v
from models import orgnizer_model as o_m

class OrgnizerController:
    def __init__(self, orgnizer_view: o_v.Orgnizer_view, orgnizer_model: o_m.OrgnizerModel):
        self.orgnizer_view = orgnizer_view
        self.orgnizer_model = orgnizer_model

    def orgnize_images_by_year(self):
        by_year_dict: dict = self.orgnizer_model.get_orgnized_by_date()
        if len(by_year_dict) > 0:
            # create the directories and copy the relevant images to it
            for year, img_list in by_year_dict.items():
                os.mkdir(f"Images_Destination/{year}")
                for img in img_list:
                    img_source = f"Images_Source/{img}"
                    img_destination = f"Images_Destination/{year}"
                    shutil.copy2(img_source, img_destination)
            self.orgnizer_view.display_orgniz_msg(True)
        else:
            # display failure message because the dict is empty
            self.orgnizer_view.display_orgniz_msg(False)
 