import colorama

from views import main_view as m_v


# define FaceRecognizerView as a subclass of MainView
class FaceRecognizerView(m_v.MainView):
    def __init__(self):
        super().__init__()

    def display_face_rec_menu(self, image_files: list):
        print(self.border_m)
        print("Pick an image contains only one face or enter q to exit:")
        for index, img in enumerate(image_files, 1):
            print(f"{index}: {img}")
        print(self.border_m)

    def display_wrong_image(self):
        print("\n")
        print(colorama.Fore.RED + self.border_f)
        print(f"------- Failed: the image doesn't fit the critera ------")
        print(self.border_f + colorama.Fore.RESET)
        input("")