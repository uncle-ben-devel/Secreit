if __name__ == "__main__":
    import Secreit
    from keras.preprocessing import image
    import numpy as np
    from matplotlib import pyplot as plt
    import matplotlib as mpl

    model=Secreit.vgg_model("models/weights.hdf5")
    img=image.load_img("Example/D.png")

    plt.imshow(img)
    predict=Secreit.predict(img, model)
    print('D:'+str(round(predict[0]*100))+'%, E:'+str(round(predict[1]*100))+'%, P:'+str(round(predict[2]*100))+'%')

    imgd=image.array_to_img(Secreit.Cam(np.array(img), "D", model))
    imge=image.array_to_img(Secreit.Cam(np.array(img), "E", model))
    imgp=image.array_to_img(Secreit.Cam(np.array(img), "P", model))

    mpl.rcParams['figure.figsize'] = [20, 4]

    plt.subplot(1,4,1)
    plt.imshow(img)
    plt.title('D:'+str(round(predict[0]*100))+'%, E:'+str(round(predict[1]*100))+'%, P:'+str(round(predict[2]*100))+'%', fontsize=25)

    plt.subplot(1,4,2)
    plt.imshow(imgd)
    plt.title("D place", fontsize=25)

    plt.subplot(1,4,3)
    plt.imshow(imge)
    plt.title("E place", fontsize=25)

    plt.subplot(1,4,4)
    plt.imshow(imgp)
    plt.title("P place", fontsize=25)

    plt.show()