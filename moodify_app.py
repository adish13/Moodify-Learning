import streamlit as st
import pandas as pd 
import numpy as np 
import cv2
import os
import imghdr
import tempfile
from PIL import Image, ImageOps
import emotion_classify as EC
from classify import recommend
import fetching_playlists as fp
#[theme]
#base="light"
#primaryColor="#751a55"
#secondaryBackgroundColor="#fbcfd5"

IMAGE_DISPLAY_SIZE = (330, 330)
IMAGE_DIR = 'demo_photos'
TEAM_DIR = 'moodify_team'

st.image(os.path.join(TEAM_DIR,'Logo.png'), use_column_width = True)
st.title('Welcome to Moodify!')
st.write(" ------ ")

# Constants for sidebar dropdown
SIDEBAR_OPTION_PROJECT_INFO = "Show Project Info"
SIDEBAR_OPTION_DEMO_IMAGE = "Select a Demo Image"
SIDEBAR_OPTION_UPLOAD_IMAGE = "Upload an Image"
SIDEBAR_OPTION_MEET_TEAM = "Meet the Team"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO, SIDEBAR_OPTION_DEMO_IMAGE, SIDEBAR_OPTION_UPLOAD_IMAGE, SIDEBAR_OPTION_MEET_TEAM]
#needs one arg as mood ,history should return csv format of history of songs including their stats ((csv format))
def load_model(mood):
    df  = pd.read_csv("moods.csv")
    final_play_lst=recommend(mood,df)
    st.write(final_play_lst)
    #if st.button("Redirect to Spotify") :
     #   '''code from api team'''
       

def load_and_preprocess_img(img_path, num_hg_blocks, bbox=None):
    img = Image.open(img_path).convert('RGB')
        
    # Required because PIL will read EXIF tags about rotation by default. We want to
    # preserve the input image rotation so we manually apply the rotation if required.
    # See https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image/
    # and the answer I used: https://stackoverflow.com/a/63798032
    try:
        img = ImageOps.exif_transpose(img)
    except: 
        pass
    #exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
    #if not exif['Orientation']:
     #   img=img.rotate(90, expand=True)
    #if bbox is None:
        #w, h = img.size

        #if w != h:
            # if the image is not square
            # Indexed so upper left corner is (0,0)
            #bbox = data_generator.transform_bbox_square((0, 0, w, h))

    #if bbox is not None:
        # If a bounding box is provided, use it
        #bbox = np.array(bbox, dtype=int)

        # Crop with box of order left, upper, right, lower
        #img = img.crop(box=bbox)

    new_img = cv2.resize(np.array(img), IMAGE_DISPLAY_SIZE,
                        interpolation=cv2.INTER_LINEAR)

    # Add a 'batch' axis
    #X_batch = np.expand_dims(new_img.astype('float'), axis=0)

    # Add dummy heatmap "ground truth", duplicated 'num_hg_blocks' times
    #y_batch = [np.zeros((1, *(OUTPUT_DIM), NUM_COCO_KEYPOINTS), dtype='float') for _ in range(num_hg_blocks)]

    # Normalize input image
    #X_batch/=255.0
    return new_img

def run_app(img):

    left_column, right_column = st.beta_columns(2)
    xb = load_and_preprocess_img(img, num_hg_blocks=1)
    display_image = cv2.resize(xb, IMAGE_DISPLAY_SIZE,
                        interpolation=cv2.INTER_LINEAR)
    mood_img=EC.emotion_detect(display_image)
    left_column.image(display_image, caption = "Selected Input")
    right_column.image(display_image, caption = "Predicted mood:" + str(mood_img) )
    load_model(mood_img)
     


def main():

    st.sidebar.warning('\
        Please upload SINGLE-person images. For best results, please also CENTER the person in the image.')
    st.sidebar.write(" ------ ")
    st.sidebar.title("Explore the Following")

    app_mode = st.sidebar.selectbox("Please select from the following", SIDEBAR_OPTIONS)

    if app_mode == SIDEBAR_OPTION_PROJECT_INFO:
        st.sidebar.write(" ------ ")
        st.sidebar.success("Project information showing on the right!")
        st.write('''
            # Mood based Music Recommender system

         This project helps the user to automatically play songs based on the emotions of the user. 
         It recognizes the facial emotions of the user and predicts the songs according to their mood.

         **Our goal is to build a song playlist for the individual in each picture.**

         👈 Please select **Select a Demo Image** in the sidebar to start.

         📸 Feel free to upload any image you want to get a song prediction under **Upload an Image**

         📞 Our team members are here to answer questions. Please refer to **Contact Information** under **Meet the Team**.''')

    elif app_mode == SIDEBAR_OPTION_DEMO_IMAGE:
        st.sidebar.write(" ------ ")

        directory = os.path.join(IMAGE_DIR)

        photos = []
        for file in os.listdir(directory):
            filepath = os.path.join(directory, file)

            # Find all valid images
            if imghdr.what(filepath) is not None:
                photos.append(file)

        photos.sort()

        option = st.sidebar.selectbox('Please select a sample image, then click the button', photos)
        pressed = st.sidebar.button('Create playlist')
        if pressed:
            st.empty()
            st.sidebar.write('Please wait for the playlist to be created! This may take up to a few minutes.')

            pic = os.path.join(directory, option)

            run_app(pic)


    elif app_mode == SIDEBAR_OPTION_UPLOAD_IMAGE:
        #upload = st.empty()
        #with upload:
        st.sidebar.info('PRIVACY POLICY: Uploaded images are never saved or stored. They are held entirely within memory for prediction \
            and discarded after the final results are displayed. ')
        f = st.sidebar.file_uploader("Please Select to Upload an Image", type=['png', 'jpg', 'jpeg', 'tiff', 'gif', 'JPG'])
        if f is not None:
            tfile = tempfile.NamedTemporaryFile(delete=True)
            tfile.write(f.read())
            st.sidebar.write('Please wait for the playlist to be created! This may take up to a few minutes.')
            run_app(tfile)
            


    elif app_mode == SIDEBAR_OPTION_MEET_TEAM:
        st.sidebar.write(" ------ ")
        st.subheader("We are the Moodify team")
        first_column, second_column, third_column, fourth_column, fifth_column = st.beta_columns(5)

        first_column.write('''**Mentors**''')
        first_column.write('Abhishek')
        first_column.write('Divyanshi')
        second_column.write('''**App dev**''')       
        second_column.write('Aaditi')
        second_column.write('Adish')
        second_column.write('Bhavesh')
        second_column.write('Kritheesh')
        third_column.write('''**Image Classification**''')        
        third_column.write('Karrthik')
        third_column.write('Sai Teja')
        third_column.write('Siddhant')
        fourth_column.write('''**Music API**''')        
        fourth_column.write('Dhawal')
        fourth_column.write('Tanirika')
        fifth_column.write('''**Music Classification**''')        
        fifth_column.write('Hastyn')
        fifth_column.write('Krutheeka')
        fifth_column.write('Sarthak')


        st.sidebar.write('Please feel free to connect with us!')
        st.sidebar.success('Hope you had a great time :)')

        expandar_linkedin = st.beta_expander('Contact Information')
        expandar_linkedin.write('Aaditi: https://github.com/aaditist')
        expandar_linkedin.write('Adish: https://github.com/adish13')
        expandar_linkedin.write('Bhavesh: https://github.com/bhaveshkhichi')
        expandar_linkedin.write('Dhawal: https://github.com/Dhawal-AI')
        expandar_linkedin.write('Hastyn: https://github.com/Hastyn')
        expandar_linkedin.write('Karrthik: https://github.com/Karrthik-Arya')
        expandar_linkedin.write('Kritheesh: https://github.com/E-Kritheesh')
        expandar_linkedin.write('Krutheeka: https://github.com/Krutheeka-RKJ')
        expandar_linkedin.write('Sai Teja: https://github.com/tejavaranasi2')
        expandar_linkedin.write('Sarthak: https://github.com/SarthakM320')
        expandar_linkedin.write('Siddhant: https://github.com/siddhant-dutta')
        expandar_linkedin.write('Tanirika: https://github.com/TanirikaRoy')
    else:
        raise ValueError('Selected sidebar option is not implemented. Please open an issue on Github: LINK SOON')

main()
expander_faq = st.beta_expander("More About Our Project")
expander_faq.write("Hi there! If you have any questions about our project, or simply want to check out the source code, please visit our github repo: LINK")


