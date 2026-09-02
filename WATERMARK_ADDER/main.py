from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

window = Tk()

window.title("Add Watermark")
window.config(padx=30, pady=30)
window.geometry("600x700")




def addwatermark():
    image = window.original_image.copy()

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 50)


    draw.text(
        xy=(50, 50),  #form top and left
        text="@prayag-clicks",
        font=font,
        fill=(0,0,0),

    )

    window.watermarked_image = image  # image is a pillow object

    preview = image.copy()             #making the copy of watermarked image
    preview.thumbnail((500, 450))      #for previewing in tkinter window

    window.photo = ImageTk.PhotoImage(preview)  #converting preview(pillow object) into tkinter PhotoImage

    my_label.config(image=window.photo)           #changing the configuration of my_label

    save_button.grid(
        row=4,
        column=0,
        columnspan=2
    )

def selectphoto():

    filepath = filedialog.askopenfilename(          #askopenfilename for opening a file
        title="Select a file",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png"),
            ("All Files", "*.*")
        ]
    )

    if not filepath:
        return

    image = Image.open(filepath)


    window.original_image = image.copy()


    preview = image.copy()
    preview.thumbnail((500, 500))


    window.photo = ImageTk.PhotoImage(preview)


    my_label.config(image=window.photo)


    addwatermark_button.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )

def saveimage():

    image_to_save = window.watermarked_image

    filepath = filedialog.asksaveasfilename(     #asksaveasfilename() for saving the file
        title="Save Watermarked Image",
        defaultextension=".jpg",
        filetypes=[
            ("JPEG Image", "*.jpg"),
            ("PNG Image", "*.png")
        ]
    )

    if not filepath:
        return

    image_to_save.save(filepath)




title_label = Label(
    window,
    text="ADD WATERMARK",
    font=("Arial", 24, "bold")
)

title_label.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 25)
)




my_label = Label(
    window,
    text="No Photo Selected"
)

my_label.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=(0, 25)
)



openbutton = Button(
    window,
    text="Select Photo",
    command=selectphoto,
    padx=20,
    pady=10
)

openbutton.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=10
)



addwatermark_button = Button(
    window,
    text="Add Watermark",
    command=addwatermark,
    padx=20,
    pady=10
)



save_button = Button(
     window,
     text="Save Watermarked Image",
     command=saveimage,
     padx=20,
     pady=10,
     )


window.mainloop()