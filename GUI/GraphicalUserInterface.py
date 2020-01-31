import tkinter as tk
from tkinter import ttk
import PyRead


def main():
    language_options = ['English', 'Spanish', 'French', 'German', 'Japanese', 'Simplified Chinese']
    root = tk.Tk()
    root.title('PyRead')
    big_frame = tk.ttk.Frame(root)
    big_frame.pack(fill='both', expand=True)
    variable = tk.StringVar(root)
    variable.set(language_options[0])
    language_choice = tk.OptionMenu(root, variable, *language_options)
    language_choice.pack()

    def askopenfile():
        filename, file_path = tk.filedialog.askopenfilenames(title='Choose your images.', filetypes=[("PNG", "*.png"),
                                                                                                     ("JPEGs",
                                                                                                      "*.jpeg jpg"),
                                                                                                     ("GIF", "*.gif"),
                                                                                                     (
                                                                                                         ("BMP",
                                                                                                          "*.bmp"), (
                                                                                                             "tiff",
                                                                                                             "*.tif "
                                                                                                             "tiff"))])
        obj = PyRead.Utils()
        if variable.get() == 'English':
            print(filename)
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'eng'))
            start_conversion.pack(side=tk.BOTTOM)
        elif variable.get() == 'Spanish':
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'spa'))
            start_conversion.pack(side=tk.BOTTOM)
        elif variable.get() == 'French':
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'fra'))
            start_conversion.pack(side=tk.BOTTOM)
        elif variable.get() == 'German':
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'deu'))
            start_conversion.pack(side=tk.BOTTOM)
        elif variable.get() == 'Japanese':
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'jpn'))
            start_conversion.pack(side=tk.BOTTOM)
        else:
            start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                             command=lambda: PyRead.Utils.img_to_text(obj, filename, file_path, 'chi_sim'))
            start_conversion.pack(side=tk.BOTTOM)

    choose_file = tk.ttk.Button(big_frame, text='Choose your file(s) to be converted.',
                                command=lambda: askopenfile())
    choose_file.pack()
    root.mainloop() 


if __name__ == '__main__':
    main()

