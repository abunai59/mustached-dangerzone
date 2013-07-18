# Image Loader
# By: abunai59

import glob

class ImageLoader:
    def __init__(self, res_path, extensions):
        # Load image paths
        pref = res_path + "\\*."
        self.img_list = []
        for ext in extensions:
            self.img_list += glob.glob(pref+ext)

        # Current image is the first in the list
        self.__current_index = 0

    # Get the current image
    def get_current(self):
        return self.img_list[self.__current_index]

    # Increment current index and return result
    def get_next(self):
        if (self.__current_index >= len(self.img_list)-1):
            self.__current_index = 0
        else:
            self.__current_index += 1
        return self.get_current()

    # Decrement current index and return result
    def get_prev(self):
        if(self.__current_index <= 0):
            self.__current_index = len(self.img_list)-1
        else:
            self.__current_index -= 1
        return self.get_current()
