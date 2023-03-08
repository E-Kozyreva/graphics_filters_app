import classes
from threading import Thread
from PIL import Image
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create main layout
        main_layout = QHBoxLayout()

        # Create left widget with picture
        picture_widget = QLabel(self)
        picture_widget.setPixmap(QPixmap("cat.jpg"))
        main_layout.addWidget(picture_widget)

        # Create right widget with buttons
        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)

        # Create sport button
        self.sport_button = QPushButton("sport filters")
        button_layout.addWidget(self.sport_button)
        self.sport_button.clicked.connect(self.on_sport_clicked)

        # Create matrix button
        self.matrix_button = QPushButton("matrix filters")
        button_layout.addWidget(self.matrix_button)
        self.matrix_button.clicked.connect(self.on_matrix_clicked)

        # Create close button
        self.close_button = QPushButton("close")
        button_layout.addWidget(self.close_button)
        self.close_button.clicked.connect(self.close)

        # Add button widget to main layout
        main_layout.addWidget(button_widget)

        # Set main layout
        self.setLayout(main_layout)


    def on_sport_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        inverion_button = QPushButton("inversion")
        filter_layout.addWidget(inverion_button)
        grayscale_button = QPushButton("grayscale")
        filter_layout.addWidget(grayscale_button)
        blackwhite_button = QPushButton("black / white")
        filter_layout.addWidget(blackwhite_button)
        sepia_button = QPushButton("sepia")
        filter_layout.addWidget(sepia_button)
        brightness_button = QPushButton("brightness")
        filter_layout.addWidget(brightness_button)
        contrast_button = QPushButton("contrast")
        filter_layout.addWidget(contrast_button)
        gamma_button = QPushButton("gamma")
        filter_layout.addWidget(gamma_button)
        blur_button = QPushButton("blur")
        filter_layout.addWidget(blur_button)
        green_button = QPushButton("green")
        filter_layout.addWidget(green_button)
        red_button = QPushButton("red")
        filter_layout.addWidget(red_button)
        blue_button = QPushButton("blue")
        filter_layout.addWidget(blue_button)

        inverion_button.clicked.connect(self.on_inversion_clicked)
        grayscale_button.clicked.connect(self.on_grayscale_clicked)
        blackwhite_button.clicked.connect(self.on_blackwhite_clicked)
        sepia_button.clicked.connect(self.on_sepia_clicked)
        brightness_button.clicked.connect(self.on_brightness_clicked)
        contrast_button.clicked.connect(self.on_contrast_clicked)
        gamma_button.clicked.connect(self.on_gamma_clicked)
        blur_button.clicked.connect(self.on_blur_clicked)
        green_button.clicked.connect(self.on_green_clicked)
        red_button.clicked.connect(self.on_red_clicked)
        blue_button.clicked.connect(self.on_blue_clicked)

        return_button = QPushButton("return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        self.layout().addWidget(filter_widget)

    
    def on_inversion_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        inv = Thread(target=spot.inversion)
        inv.start()
        inv.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/inversion.jpg"))

    
    def on_grayscale_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        gs = Thread(target=spot.grayscale)
        gs.start()
        gs.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/grayscale.jpg"))

    
    def on_blackwhite_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        bw = Thread(target=spot.blackwhite)
        bw.start()
        bw.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/blackwhite.jpg"))


    def on_sepia_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        sep = Thread(target=spot.sepia)
        sep.start()
        sep.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/sepia.jpg"))


    def on_brightness_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        br = Thread(target=spot.brightness)
        br.start()
        br.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/brightness.jpg"))


    def on_contrast_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        cont = Thread(target=spot.contrast)
        cont.start()
        cont.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/contrast.jpg"))


    def on_gamma_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        gam = Thread(target=spot.gamma)
        gam.start()
        gam.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/gamma.jpg"))


    def on_blur_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        bl = Thread(target=spot.blur)
        bl.start()
        bl.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/blur.jpg"))


    def on_green_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        gr = Thread(target=spot.green)
        gr.start()
        gr.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/green.jpg"))

    
    def on_red_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        re = Thread(target=spot.red)
        re.start()
        re.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/red.jpg"))

    
    def on_blue_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        bl = Thread(target=spot.blue)
        bl.start()
        bl.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/blue.jpg"))


    def on_matrix_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        sobel_button = QPushButton("sobel")
        filter_layout.addWidget(sobel_button)
        sharpen_button = QPushButton("sharpen")
        filter_layout.addWidget(sharpen_button)
        operator_scharra = QPushButton("operator scharra")
        filter_layout.addWidget(operator_scharra)
        operator_pruitt = QPushButton("operator pruitt")
        filter_layout.addWidget(operator_pruitt)
        waves_1_button = QPushButton("waves 1")
        filter_layout.addWidget(waves_1_button)
        waves_2_button = QPushButton("waves 2")
        filter_layout.addWidget(waves_2_button)
        mirror_button = QPushButton("mirror")
        filter_layout.addWidget(mirror_button)
        motion_blur_button = QPushButton("motion blur")
        filter_layout.addWidget(motion_blur_button)
        shift_button = QPushButton("shift")
        filter_layout.addWidget(shift_button)
        rotate_button = QPushButton("rotate")
        filter_layout.addWidget(rotate_button)

        sobel_button.clicked.connect(self.on_sobel_clicked)
        sharpen_button.clicked.connect(self.on_sharpen_clicked)
        operator_scharra.clicked.connect(self.on_operator_scharra_clicked)
        operator_pruitt.clicked.connect(self.on_operator_pruitt_clicked)
        waves_1_button.clicked.connect(self.on_waves_1_clicked)
        waves_2_button.clicked.connect(self.on_waves_2_clicked)
        mirror_button.clicked.connect(self.on_mirror_clicked)
        motion_blur_button.clicked.connect(self.on_motion_blur_clicked)
        shift_button.clicked.connect(self.on_shift_clicked)
        rotate_button.clicked.connect(self.on_rotate_clicked)

        return_button = QPushButton("return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        self.layout().addWidget(filter_widget)

    
    def on_sobel_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        sob = Thread(target=matrix.sobel)
        sob.start()
        sob.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/sobel.jpg"))


    def on_sharpen_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        shar = Thread(target=matrix.sharpen)
        shar.start()
        shar.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/sharpen.jpg"))

    
    def on_operator_scharra_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        op_scharra = Thread(target=matrix.operator_scharra)
        op_scharra.start()
        op_scharra.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/operator_scharra.jpg"))


    def on_operator_pruitt_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        op_pruitt = Thread(target=matrix.operator_pruitt)
        op_pruitt.start()
        op_pruitt.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/operator_pruitt.jpg"))


    def on_waves_1_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        wav = Thread(target=matrix.waves_1)
        wav.start()
        wav.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/waves_1.jpg"))
    

    def on_waves_2_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        wav = Thread(target=matrix.waves_2)
        wav.start()
        wav.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/waves_2.jpg"))


    def on_mirror_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        mir = Thread(target=matrix.mirror)
        mir.start()
        mir.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/mirror.jpg"))


    def on_motion_blur_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        mot = Thread(target=matrix.motion_blur)
        mot.start()
        mot.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/motion_blur.jpg"))


    def on_shift_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        shi = Thread(target=matrix.shift)
        shi.start()
        shi.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/shift.jpg"))


    def on_rotate_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        rot = Thread(target=matrix.rotate)
        rot.start()
        rot.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/rotate.jpg"))


    def on_return_clicked(self):
        # Clear layout
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        # Show first set of buttons
        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)
        button_layout.addWidget(self.sport_button)
        button_layout.addWidget(self.matrix_button)
        button_layout.addWidget(self.close_button)
        self.layout().addWidget(button_widget)
        self.sport_button.show()
        self.matrix_button.show()
        self.close_button.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
