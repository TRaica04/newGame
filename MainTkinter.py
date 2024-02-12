import tkinter as tk

def create_frame_with_label(master, text, relief_style):
    """Function to create a frame with a specified relief style and a label inside it."""
    frame = tk.Frame(master, relief=relief_style, borderwidth=4, bg='lightgray')
    frame.pack(padx=10, pady=10, fill='both', expand=True)
    
    label = tk.Label(frame, text=text, bg='lightgray')
    label.pack(padx=20, pady=20)
    return frame

# Create the main window
root = tk.Tk()
root.title("Frames with Different Reliefs")
root.geometry("400x400")

# Create frames with different relief styles
create_frame_with_label(root, "Flat Relief", "flat")
create_frame_with_label(root, "Raised Relief", "raised")
create_frame_with_label(root, "Sunken Relief", "sunken")
create_frame_with_label(root, "Groove Relief", "groove")
create_frame_with_label(root, "Ridge Relief", "ridge")

root.mainloop()
