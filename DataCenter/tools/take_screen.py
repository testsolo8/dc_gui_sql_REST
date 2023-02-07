# Standart libraries
import datetime
import io
import os

# Packages for tests
import allure
from PIL import Image
# Third party packages
from allure_commons.types import AttachmentType
from pywinauto import Application

PATH = os.getenv("TEMP") + "\\"


def make_screenshot_if_error(is_ok):
    if not is_ok:
        app = Application(backend="uia").connect(
            path=r"c:\Program Files (x86)\SearchInform\SearchInform DataCenter\DCClient.exe"
        )
        screen = app.window(name_re="DataCenter*")
        with allure.step("ERROR Screenshot"):
            date_stamp = str(datetime.datetime.now()).split(".")[0]
            date_stamp = (
                date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
            )
            file_name = "allure_" + date_stamp + ".png"
            image = screen.capture_as_image()
            name_of_image = PATH + file_name
            image.save(name_of_image)
            image = Image.open(name_of_image)
            image_to_byte = io.BytesIO()
            image.save(image_to_byte, format="PNG")
            image_byte = image_to_byte.getvalue()
            allure.attach(
                image_byte, name="Screenshot", attachment_type=AttachmentType.PNG
            )
