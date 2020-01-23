# PySee (In-Progress)
 A Python program that takes images as inputs and uses OCR to return a file that contains the texts from those images along with the original photos.

 # Setup

 ### Requirements

 *   pytesseract 0.3.1.
 *   tessdata file containing all languages.
     On macOS and Linux, this can be done by inputting ```sudo port install tesseract-<all>``` on your terminal.
 *   A Python interpreter.

 ### Startup

 1. Download PyRead.py.
 2. On your terminal CD into the directory containing the file. On macOS, this would likely be _/Users/[your_user_name]/Downloads/_ ; accordingly input ```cd downloads```.
 3. Input ```python PyRead.py```. A user interface should appear welcoming you with language options. Select the appropriate language of the images.
 4. A window should then appear asking which photos you want to select. You can select more than one photo in the same folder.

 ### The design process and observations

 Writing this program did not take many lines of code. However, there was an abundance of drudgery I endured for functionality.

 At first, I originally wrote the code for the user inputting each file by name, including the entire path (e.g., _/Users/[your_user_name]/spring2020/lecture_notes/images_). When testing my methods inside the class, I found this burdensome, as I had to type those file paths every time I tested a new image. I then decided to include a GUI to allow the user to select multiple images using his familiar OS interface with ```tkinter.filedialog.askopenfilenames()```. This easily streamlined my testing workflow, and I was able to test five images per language under one minute rather than one image every three minutes. This will be of great help for anyone wanting to experiment with the program themselves.

 I renamed the parameters ```images``` inside the class methods so they do not get confused for the ```img``` variables in __main__. I also renamed the variables inside each language method, so they represent their respective languages. This helps with debugging and helps avoid conflating variables.

 During unit testing I had issues comparing string return values of the methods with with the actual expected results. I then found that I did not have return statements; only print statements. I added return statements for the converted texts for unit testing and the possibility of these functions being used in abstraction as higher-order functions.

 In the future, I plan on adding PDF as a feature, where the PDF contains the scanned images along with the output text. I also may use ```ImageEnhance``` if my tests show that it improves average accuracy of output.

  ### Limitations
  Without a doubt that OCR is a software engineering marvel. Rather than hiring some to tediously read and retype an 800-page-book, OCR has allowed us to efficiently convert images to texts, giving access to numerous classics that can be opened as documents to parse.

  In my testing, however, I found that the training data provided to the tesseract algorithm was sufficient for mostly ideally-lit situations and characters that hardly digress from the training data. When testing the handwritten "¡Todo lo que hago es ganar" in Spanish, I found that even after varying the lighting, changing the crop of the photo with no other texts, and even constraining it to a screenshot of the handwritten text could not yield the "¡," which is crucial for interpreting and differentiating between other commonly-used characters among various languages.

 ## References
1. https://pypi.org/project/pytesseract/
2. https://github.com/tesseract-ocr/tesseract/wiki
3. http://www.explainthatstuff.com/how-ocr-works.html


 ---

 ## License

 MIT License

 Copyright (c) 2020 Ranelle Gomez

 ---

 ## Author Info

 As of writing in January 2020, I am an undergraduate at UC Berkeley studying applied math and computer science. If you have any questions or comments, please reach me by the following: 1) email: ranellegomez@gmail.com 2) Text: (323) 999-4720 3)
 LinkedIn: https://www.linkedin.com/in/ranellegomez/
