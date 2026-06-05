import PIL
from PIL import Image

def strip_layout(frames_names):

    frame = PIL.Image.open(frames_names[0])
    frame_size = frame.size
    strip = PIL.Image.new("RGB", (frame_size[0]+160, 500+(frame_size[1]*3)), (255, 255, 255)) # blank white image to paste the frames onto
    print(f"Created blank strip with size: {strip.size}")

    for i, frame_name in enumerate(frames_names):
        frame = PIL.Image.open(frame_name)
        strip.paste(frame, (80, 80+500*i)) # paste the frame onto the strip at the correct position
        photo_name = f"photo_{i}.jpg"
        strip.save(photo_name)
        #yield i
    
    strip.save("photostrip.jpg") # save the photostrip as an image file
    return strip

def get_photostrip(index):
    photo_name = f"photo_{index}.jpg"
    photo = PIL.Image.open(photo_name)
    return photo