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


    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.pack(side="top")

    def callback(*args):
        labelTest.configure(text="The selected item is {}".format(variable.get()))

    variable.trace('w', callback)




    def askopenfile():
        global filename
        filename = tk.filedialog.askopenfilenames(title='Choose your images.', filetypes=[("PNG", "*.png"),
                                                                                          ("JPEGs", "*.jpeg jpg"),
                                                                                          ("GIF", "*.gif"),
                                                                                          (("BMP", "*.bmp"), (
                                                                                              "tiff", "*.tif tiff"))])
    choose_file = tk.ttk.Button(big_frame, text='Choose your file(s) to be converted.',
                                command=lambda:askopenfile())

    choose_file.pack()
    print(filename)
    file_path = filename
    print(file_path)


    obj = PyRead.Utils()
    if variable.get() == 'English':
        print(filename)
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_english(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable.get() == 'Spanish':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_spanish(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable.get() == 'French':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_french(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable.get() == 'German':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_german(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable.get() == 'Japanese':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_japanese(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    else:
        start_conversion = tk.ttk.Button(root, text='Start conversion.',
                                         command=lambda: PyRead.Utils.img_to_chinese(obj, filename, file_path))
        start_conversion.pack(side=tk.BOTTOM)

    root.mainloop()  # Window doesn't close until user exits window.


if __name__ == '__main__':
    main()

"""
1. Choose language (scroll-down list).
2. Choose file(s).
3. Save file as:
4. Start. (grayed-out until all fields have valid input.
Over here will be the code to allow the window to have four columns: Language (drop-down), File(s),
Preferred output (print? PDF? Word?), and start.
There will also be a list of all files selected.
"""
