import os
from datetime import datetime

from config import settings


def handle_uploaded_item_csv_file(countrt, ff):
    print(countrt)
    print(ff)
    # now = datetime.now()
    # # YY_mm_dd_HH_MM
    # dt_string = now.strftime("%Y_%m_%d_%H_%M")
    # file_name = os.path.join(settings.MEDIA_ROOT, f"tmp_csv/item_csv_{dt_string}.csv")
    # with open(file_name, 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    #
    # return f"tmp_csv/item_csv_{dt_string}.csv"