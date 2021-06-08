import os
from selenium.webdriver.common.by import By
from src.the_internet.pages.base_page import BasePage
from tests.conftest import base_path
from typing import List


class FileUploaderPage(BasePage):
    CHOOSE_FILE_BTN = (By.ID, "file-upload")
    UPLOAD_BTN = (By.ID, "file-submit")
    DRAG_DROP_UPLOAD = (By.ID, "drag-drop-upload")
    UPLOADED_MSG = (By.TAG_NAME, "h3")
    UPLOADED_FILE = (By.XPATH, "//div[@class='example']/div")

    def get_file_uploader_page(self):
        self.driver.get(f"{self.url}/upload")

    def choose_file_via_btn(self, file_path):
        choose = self.find_element(self.CHOOSE_FILE_BTN)
        choose.send_keys(f"{base_path}/{file_path}")

    def click_upload_btn(self):
        self.click_on_element(self.UPLOAD_BTN)

    def success_msg(self):
        return self.element_text(self.UPLOADED_MSG)

    def upladed_file_name(self):
        return self.element_text(self.UPLOADED_FILE)

    def choose_file_via_drag_and_drop(self, file_path):
        choose = self.find_element(self.DRAG_DROP_UPLOAD)
        choose.send_keys(f"{base_path}/{file_path}")

    # def drop_files(self, element, files, offsetX=0, offsetY=0):
    #     JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"
    #
    #     driver = element.parent
    #     isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    #     paths = []
    #
    #     # ensure files are present, and upload to the remote server if session is remote
    #     for file in (files if isinstance(files, list) else [files]):
    #         if not os.path.isfile(file):
    #             raise FileNotFoundError(file)
    #         paths.append(file if isLocal else element._upload(file))
    #
    #     value = '\n'.join(paths)
    #     elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    #     elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

    def drop_files(self, element, files, offsetX=0, offsetY=0):
        JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"

        paths = []

        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, List) else [files]):
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file)

        value = '\n'.join(paths)
        elm_input = self.driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})
