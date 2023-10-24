# easy_label
Labelling tool for custom segmentation mask creation
The main reason for the creation of this tool is to ease the process of creating segmentation masks - ground truths - for random images. Most of the datasets don't provide resources for the creation of the ground truths for your own custom images. This tool lets you select the objects in the image and assign your own custom class label - only integers - to them. 


**Required python packages:** 

1. tkinter
2. PIL
3. numpy

**Procedure:**

1. *python main.py* in your terminal after navigating to the repository.

2. A small dialog box will appear, asking you to select the image you wish to create the mask for.

3. The image will be opened in a window with the following buttons visible: 

    a. Zoom in: Allows you to zoom into the image. 

    b. Zoom out: Allows you to zoom out of the image.

    c. Select Coordinates: Allows you to select the cooridinates for the object to which you wish to assign a custom class label.

    d. End Coordinates: Creates a polygon on the image using the coordinates selected, giving you a visual representation of the mask. 

    e. Redo Selection: In case the user wants to redo the current object selection, the following button aids that. 

    f. Confirm Selection: Once the mask is visualised using End Coordinates, use the following to assign class label to the object.

    g. Save Mask: Saves the mask as a png file. 

4. The *Select Coordinates* button is clicked and this lets you select the object outline. Click around the object boundaries and lines will form, informing you of your selection.

5. Then, click on the *End Coordinates* button to visualise the mask of the selected image -- a polygon will be created. If unsatisfied, please click *Redo Selection*.

6. To assign class label to object, after selection, click the *Confirm Selection* button and this will open a dialog box, where you will give an integer value to be assigned to the object.

7. To save the created mask, the *Save Mask* button will be clicked and the mask will be saved accordingly in png format.


**DISCLAIMERS:**

1. The mask will be saved as mask.png in the same folder as main.py

2. *Zoom in* and *Zoom out* to be used before objects are selected


