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

    choose_file = tk.ttk.Button(big_frame, text='Choose your file(s) to be converted.',
                                command=lambda: tk.filedialog.askopenfilenames(title='Choose your images.',
                                                                               filetypes=[("PNG", "*.png"),
                                                                                          ("JPEGs", "*.jpeg jpg"),
                                                                                          ("GIF", "*.gif"),
                                                                                          (("BMP", "*.bmp"), (
                                                                                              "tiff", "*.tif tiff"))]))
    file_path = choose_file
    choose_file.pack()
    obj = PyRead.Utils()
    if variable == 'English':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_english(obj, choose_file, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable == 'Spanish':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_spanish(obj, choose_file, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable == 'French':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_french(obj, choose_file, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable == 'German':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_german(obj, choose_file, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    elif variable == 'Japanese':
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_japanese(obj, choose_file, file_path))
        start_conversion.pack(side=tk.BOTTOM)
    else:
        start_conversion = tk.ttk.Button(root, text='Start conversion.',command=lambda: PyRead.Utils.img_to_chinese(obj, choose_file, file_path))
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
