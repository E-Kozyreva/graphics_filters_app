import classes
from threading import Thread
from PIL import Image
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Editor")
        self.main_layout = QHBoxLayout()

        self.left, self.top, self.width, self.height = 100, 100, 600, 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #EDEDED;")

        self.file_name = "temp.jpg"

        self.picture_widget = QLabel(self)
        self.picture_widget.setPixmap(QPixmap(self.file_name))
        self.main_layout.addWidget(self.picture_widget)

        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)

        button_widget.setStyleSheet("background-color: #EDEDED;")

        self.select_image_button = QPushButton("Select image")
        self.sport_button = QPushButton("Sport filters")
        self.matrix_button = QPushButton("Matrix filters")
        self.mathmorph_button = QPushButton("Math. morph.")
        self.close_button = QPushButton("Close")

        buttons = [self.select_image_button, 
                   self.sport_button, 
                   self.matrix_button, 
                   self.mathmorph_button]

        buttons_click = [self.on_select_image_button_clicked, 
                         self.on_sport_clicked, 
                         self.on_matrix_clicked,
                         self.on_mathmorph_clicked, 
                         self.on_close_clicked]

        for button in range(len(buttons)):
            button_layout.addWidget(buttons[button])
            buttons[button].setStyleSheet("background-color: #ED760E; color: white; border-radius: 5px; padding: 5px;")
            buttons[button].setFont(QFont("Arial", 9, QFont.Weight.Bold))
            buttons[button].clicked.connect(buttons_click[button])
        
        button_layout.addWidget(self.close_button)
        self.close_button.setStyleSheet("background-color: black; color: white; border-radius: 5px; padding: 5px;")
        self.close_button.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        self.close_button.clicked.connect(self.on_close_clicked)

        button_widget.setFixedSize(130, 600)
        self.picture_widget.setFixedSize(600, 600)
        
        self.main_layout.addWidget(button_widget)
        self.setLayout(self.main_layout)


    def on_select_image_button_clicked(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg *.png *.bmp)")

        if self.file_name:
            pixmap = QPixmap(self.file_name)
            self.picture_widget.setPixmap(pixmap)

            if pixmap.width() > 600 or pixmap.height() > 600:
                pixmap = pixmap.scaled(600, 600)

            self.picture_widget.setPixmap(pixmap)
            self.picture_widget.setFixedSize(600, 600)

            pixmap.save("temp.jpg", "jpg")
            self.file_name = "temp.jpg"


    def on_sport_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        inverion_button = QPushButton("Inversion")
        grayscale_button = QPushButton("Grayscale")
        blackwhite_button = QPushButton("Black / White")
        sepia_button = QPushButton("Sepia")
        brightness_button = QPushButton("Brightness")
        contrast_button = QPushButton("Contrast")
        gamma_button = QPushButton("Gamma")
        blur_button = QPushButton("Blur")
        green_button = QPushButton("Green")
        red_button = QPushButton("Red")
        blue_button = QPushButton("Blue")
        return_button = QPushButton("Return")

        buttons = [inverion_button, grayscale_button, blackwhite_button, sepia_button, 
                   brightness_button, contrast_button, gamma_button, blur_button, 
                   green_button, red_button, blue_button]

        buttons_click = [self.on_inversion_clicked, self.on_grayscale_clicked, self.on_blackwhite_clicked,
                            self.on_sepia_clicked, self.on_brightness_clicked, self.on_contrast_clicked,
                            self.on_gamma_clicked, self.on_blur_clicked, self.on_green_clicked,
                            self.on_red_clicked, self.on_blue_clicked]

        for button in range(len(buttons)):
            filter_layout.addWidget(buttons[button])
            buttons[button].setStyleSheet("background-color: #ED760E; color: white; border-radius: 5px; padding: 5px;")
            buttons[button].setFont(QFont("Arial", 9, QFont.Weight.Bold))
            buttons[button].clicked.connect(buttons_click[button])

        filter_layout.addWidget(return_button)
        return_button.setStyleSheet("background-color: black; color: white; border-radius: 5px; padding: 5px;")
        return_button.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        return_button.clicked.connect(self.on_return_clicked)

        filter_widget.setFixedSize(130, 600)

        self.layout().addWidget(filter_widget)

    
    def on_inversion_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        inv = Thread(target=spot.inversion)
        inv.start()
        inv.join()

        pixmap = QPixmap("results/output/spot/inversion.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_grayscale_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)
        gs = Thread(target=spot.grayscale)
        gs.start()
        gs.join()

        pixmap = QPixmap("results/output/spot/grayscale.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_blackwhite_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        bw = Thread(target=spot.blackwhite)
        bw.start()
        bw.join()
        
        pixmap = QPixmap("results/output/spot/blackwhite.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_sepia_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        sep = Thread(target=spot.sepia)
        sep.start()
        sep.join()
        
        pixmap = QPixmap("results/output/spot/sepia.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_brightness_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        br = Thread(target=spot.brightness)
        br.start()
        br.join()
        
        pixmap = QPixmap("results/output/spot/brightness.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_contrast_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        cont = Thread(target=spot.contrast)
        cont.start()
        cont.join()
        
        pixmap = QPixmap("results/output/spot/contrast.jpg")
        pixmap = pixmap.scaled(600, 600)    
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_gamma_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        gam = Thread(target=spot.gamma)
        gam.start()
        gam.join()
        
        pixmap = QPixmap("results/output/spot/gamma.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_blur_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        bl = Thread(target=spot.blur)
        bl.start()
        bl.join()
        
        pixmap = QPixmap("results/output/spot/blur.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_green_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        gr = Thread(target=spot.green)
        gr.start()
        gr.join()
        
        pixmap = QPixmap("results/output/spot/green.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_red_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        re = Thread(target=spot.red)
        re.start()
        re.join()
        
        pixmap = QPixmap("results/output/spot/red.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_blue_clicked(self):
        img = Image.open(self.file_name)
        spot = classes.SpotFilters(img)

        bl = Thread(target=spot.blue)
        bl.start()
        bl.join()
        
        pixmap = QPixmap("results/output/spot/blue.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_matrix_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        sobel_button = QPushButton("Sobel")
        sharpen_button = QPushButton("Sharpen")
        operator_scharra = QPushButton("Operator scharra")
        operator_pruitt = QPushButton("Operator pruitt")
        waves_1_button = QPushButton("Waves 1")
        waves_2_button = QPushButton("Waves 2")
        mirror_button = QPushButton("Mirror")
        motion_blur_button = QPushButton("Motion blur")
        shift_button = QPushButton("Shift")
        rotate_button = QPushButton("Rotate")
        return_button = QPushButton("Return")

        buttons = [sobel_button, sharpen_button, operator_scharra, operator_pruitt, 
                   waves_1_button, waves_2_button, mirror_button, motion_blur_button, 
                   shift_button, rotate_button]

        buttons_click = [self.on_sobel_clicked, self.on_sharpen_clicked, self.on_operator_scharra_clicked,
                         self.on_operator_pruitt_clicked, self.on_waves_1_clicked, self.on_waves_2_clicked,
                         self.on_mirror_clicked, self.on_motion_blur_clicked, self.on_shift_clicked, self.on_rotate_clicked]

        for button in range(len(buttons)):
            filter_layout.addWidget(buttons[button])
            buttons[button].setStyleSheet("background-color: #ED760E; color: white; border-radius: 5px; padding: 5px;")
            buttons[button].setFont(QFont("Arial", 9, QFont.Weight.Bold))
            buttons[button].clicked.connect(buttons_click[button])

        filter_layout.addWidget(return_button)
        return_button.setStyleSheet("background-color: black; color: white; border-radius: 5px; padding: 5px;")
        return_button.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        return_button.clicked.connect(self.on_return_clicked)

        filter_widget.setFixedSize(130, 600)

        self.layout().addWidget(filter_widget)

    
    def on_sobel_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        sob = Thread(target=matrix.sobel)
        sob.start()
        sob.join()
        
        pixmap = QPixmap("results/output/matrix/sobel.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_sharpen_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        shar = Thread(target=matrix.sharpen)
        shar.start()
        shar.join()
        
        pixmap = QPixmap("results/output/matrix/sharpen.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_operator_scharra_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        op_scharra = Thread(target=matrix.operator_scharra)
        op_scharra.start()
        op_scharra.join()
        
        pixmap = QPixmap("results/output/matrix/operator_scharra.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_operator_pruitt_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        op_pruitt = Thread(target=matrix.operator_pruitt)
        op_pruitt.start()
        op_pruitt.join()
        
        pixmap = QPixmap("results/output/matrix/operator_pruitt.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_waves_1_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        wav = Thread(target=matrix.waves_1)
        wav.start()
        wav.join()
        
        pixmap = QPixmap("results/output/matrix/waves_1.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)
    

    def on_waves_2_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        wav = Thread(target=matrix.waves_2)
        wav.start()
        wav.join()
        
        pixmap = QPixmap("results/output/matrix/waves_2.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_mirror_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        mir = Thread(target=matrix.mirror)
        mir.start()
        mir.join()
        
        pixmap = QPixmap("results/output/matrix/mirror.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_motion_blur_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        mot = Thread(target=matrix.motion_blur)
        mot.start()
        mot.join()
        
        pixmap = QPixmap("results/output/matrix/motion_blur.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_shift_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        shi = Thread(target=matrix.shift)
        shi.start()
        shi.join()
        
        pixmap = QPixmap("results/output/matrix/shift.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_rotate_clicked(self):
        img = Image.open(self.file_name)
        matrix = classes.MatrixFilters(img)

        rot = Thread(target=matrix.rotate)
        rot.start()
        rot.join()
        
        pixmap = QPixmap("results/output/matrix/rotate.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_mathmorph_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        dilate_button = QPushButton("Dilate")
        erode_button = QPushButton("Erode")
        open_button = QPushButton("Open")
        closef_button = QPushButton("Close")
        top_hat_button = QPushButton("Top hat")
        black_hat_button = QPushButton("Black hat")
        grad_button = QPushButton("Grad")
        
        return_button = QPushButton("Return")

        buttons = [dilate_button, erode_button, 
                   open_button, closef_button, 
                   top_hat_button, black_hat_button,
                   grad_button]

        buttons_click = [self.on_dilate_clicked, 
                         self.on_erode_clicked, 
                         self.on_opened_clicked,
                         self.on_closed_clicked,
                         self.on_top_hat_clicked,
                         self.on_black_hat_clicked,
                         self.on_grad_clicked,
                         self.on_close_clicked,]

        for button in range(len(buttons)):
            filter_layout.addWidget(buttons[button])
            buttons[button].setStyleSheet("background-color: #ED760E; color: white; border-radius: 5px; padding: 5px;")
            buttons[button].setFont(QFont("Arial", 9, QFont.Weight.Bold))
            buttons[button].clicked.connect(buttons_click[button])

        filter_layout.addWidget(return_button)
        return_button.setStyleSheet("background-color: black; color: white; border-radius: 5px; padding: 5px;")
        return_button.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        return_button.clicked.connect(self.on_return_clicked)

        filter_widget.setFixedSize(130, 600)

        self.layout().addWidget(filter_widget)


    def on_dilate_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        dil = Thread(target=mathmorph.dilate)
        dil.start()
        dil.join()
        
        pixmap = QPixmap("results/output/math_morph/dilate.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_erode_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        ero = Thread(target=mathmorph.erode)
        ero.start()
        ero.join()
        
        pixmap = QPixmap("results/output/math_morph/erode.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_opened_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        opn = Thread(target=mathmorph.opened)
        opn.start()
        opn.join()
        
        pixmap = QPixmap("results/output/math_morph/opened.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_closed_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        clo = Thread(target=mathmorph.closed)
        clo.start()
        clo.join()
        
        pixmap = QPixmap("results/output/math_morph/closed.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)


    def on_top_hat_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        gra = Thread(target=mathmorph.top_hat)
        gra.start()
        gra.join()
        
        pixmap = QPixmap("results/output/math_morph/top_hat.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_black_hat_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        blh = Thread(target=mathmorph.black_hat)
        blh.start()
        blh.join()
        
        pixmap = QPixmap("results/output/math_morph/black_hat.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)

    
    def on_grad_clicked(self):
        img = Image.open(self.file_name)
        mathmorph = classes.MathMorph(img)

        gra = Thread(target=mathmorph.grad)
        gra.start()
        gra.join()
        
        pixmap = QPixmap("results/output/math_morph/grad.jpg")
        pixmap = pixmap.scaled(600, 600)
        self.picture_widget.setPixmap(pixmap)
        self.picture_widget.setFixedSize(600, 600)
        
            
    def on_others_clicked(self):
        pass
    
    
    def on_return_clicked(self):
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        buttons = [self.select_image_button, 
                   self.sport_button, 
                   self.matrix_button,
                   self.mathmorph_button,
                   self.close_button]

        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)
        self.layout().addWidget(button_widget)

        for button in range(len(buttons)):
            button_layout.addWidget(buttons[button])
            buttons[button].show()

        button_widget.setFixedSize(130, 600)

    
    def on_close_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
