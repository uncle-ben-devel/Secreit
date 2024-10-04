
import numpy as np
import argparse
import os

def create_predicition_string(prediction:np.ndarray):
    return f"""D: {prediction[0]*100:.2f}% E: {prediction[1]*100:.2f}% P: {prediction[2]*100:.2f}% """

def shut_up_tensorflow():
    import logging
    logging.getLogger('tensorflow').setLevel(logging.ERROR)
    os.environ["KMP_AFFINITY"] = "noverbose"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Secreit command line interface",
        description='Tries to determine the estrous phase of a mouse using the Secreit project.',
    )
    parser.add_argument(
        "file_path",
        nargs=1,
        help="The releative or absolute path to the image file to analyze.", 
        #TODO: which file formats are supported? scaling? ...
    )
    parser.add_argument(
        "--disable-result-window",
        help="If this argument is present, the window with test result images will not be displayed.",
        action='store_true',
        default=False,
        required=False,
    )
    args = parser.parse_args()
    try:
        file_path = os.path.abspath(str(args.file_path[0]))
        print(f"The file at {file_path} will be analyzed...")
    except:
        parser.print_help()
        quit()

    shut_up_tensorflow()
    from keras.preprocessing import image
    from matplotlib import pyplot as plt
    import matplotlib as mpl
    import Secreit
    from util import pyinstaller_compatible_path

    model=Secreit.vgg_model(pyinstaller_compatible_path("models/weights.hdf5"))
    img=image.load_img(file_path)

    predict=Secreit.predict(img, model)
    prediction = create_predicition_string(predict)
    print(prediction)

    result_window_is_disabled = args.disable_result_window
    if result_window_is_disabled:
        quit()

    imgd=image.array_to_img(Secreit.Cam(np.array(img), "D", model))
    imge=image.array_to_img(Secreit.Cam(np.array(img), "E", model))
    imgp=image.array_to_img(Secreit.Cam(np.array(img), "P", model))

    mpl.rcParams['figure.figsize'] = [20, 4]
    fontsize = 18

    plt.subplot(2,2,1)
    plt.imshow(img)
    plt.title(prediction, fontsize=fontsize)

    plt.subplot(2,2,2)
    plt.imshow(imgd)
    plt.title("D place", fontsize=fontsize)

    plt.subplot(2,2,3)
    plt.imshow(imge)
    plt.title("E place", fontsize=fontsize)

    plt.subplot(2,2,4)
    plt.imshow(imgp)
    plt.title("P place", fontsize=fontsize)

    plt.show()