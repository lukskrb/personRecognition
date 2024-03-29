# PERSON RECOGNITION BASED ON METHODS OF TEXT ENTRY THROUGH A TABLET
A program that uses the scikit-learn library to recognize the person who entered text into the tablet.

## Used data
The data must be in the picle file as a dictionary structure in the following way:
![Struktura_pod_IP2](https://github.com/lukskrb/personRecognition/assets/95753335/5c55cfc4-8b10-49d5-b340-b9ceb0136fee)
where the keys represent:

"0" - unique user ID (0 - 19)
"Finger" - input method (Finger or Stylus)
"tablet" - device (tablet only)
"126" - unique ID of the content to be entered - sentences/phrases (26 - 75), words (76 - 125) and letters (126 - 311) are entered;
"input_type" - input type (letter in this case)
"input_content" - the exact letter, word or phrase that was entered
"data" - vectors containing sensor readings (ts - timestamp; rawposX and rawposY - read position on the tablet; relposX and relposY - read relative position in the input section; velX and velY - input speeds at the time of reading; magX, magY and magZ - magnetometer readings; orientation - orientation of the stylus; pressure - pressure of the stylus; size - size of pressure during finger input)
