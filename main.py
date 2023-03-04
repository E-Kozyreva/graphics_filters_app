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
        self.sport_button = QPushButton("Sport")
        button_layout.addWidget(self.sport_button)
        self.sport_button.clicked.connect(self.on_sport_clicked)

        # Create matrix button
        self.matrix_button = QPushButton("Matrix")
        button_layout.addWidget(self.matrix_button)
        self.matrix_button.clicked.connect(self.on_matrix_clicked)

        # Create close button
        self.close_button = QPushButton("Close")
        button_layout.addWidget(self.close_button)
        self.close_button.clicked.connect(self.close)

        # Add button widget to main layout
        main_layout.addWidget(button_widget)

        # Set main layout
        self.setLayout(main_layout)


    def on_sport_clicked(self):
        # Hide first set of buttons
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        # Create filter widget
        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        # Create filter buttons
        inverion_button = QPushButton("Inversion")
        filter_layout.addWidget(inverion_button)
        grayscale_button = QPushButton("Grayscale")
        filter_layout.addWidget(grayscale_button)
        blackwhite_button = QPushButton("Black & White")
        filter_layout.addWidget(blackwhite_button)
        sepia_button = QPushButton("Sepia")
        filter_layout.addWidget(sepia_button)
        brightness_button = QPushButton("Brightness")
        filter_layout.addWidget(brightness_button)
        contrast_button = QPushButton("Contrast")
        filter_layout.addWidget(contrast_button)
        gamma_button = QPushButton("Gamma")
        filter_layout.addWidget(gamma_button)
        blur_button = QPushButton("Blur")
        filter_layout.addWidget(blur_button)

        inverion_button.clicked.connect(self.on_inversion_clicked)
        grayscale_button.clicked.connect(self.on_grayscale_clicked)
        blackwhite_button.clicked.connect(self.on_blackwhite_clicked)
        sepia_button.clicked.connect(self.on_sepia_clicked)
        brightness_button.clicked.connect(self.on_brightness_clicked)
        contrast_button.clicked.connect(self.on_contrast_clicked)
        gamma_button.clicked.connect(self.on_gamma_clicked)
        blur_button.clicked.connect(self.on_blur_clicked)

        # Create return button
        return_button = QPushButton("Return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        # Add filter widget to main layout
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


    def on_matrix_clicked(self):
        # Hide first set of buttons
        self.layout().itemAt(1).widget().hide()
        self.layout().removeItem(self.layout().itemAt(1))

        # Create filter widget
        filter_widget = QWidget(self)
        filter_layout = QVBoxLayout(filter_widget)

        # Create filter buttons
        sobel_button = QPushButton("Sobel")
        filter_layout.addWidget(sobel_button)
        sharpen_button = QPushButton("Sharpen")
        filter_layout.addWidget(sharpen_button)
        emboss_button = QPushButton("Emboss")
        filter_layout.addWidget(emboss_button)
        edge_button = QPushButton("Edge")
        filter_layout.addWidget(edge_button)
        gaussian_button = QPushButton("Gaussian")
        filter_layout.addWidget(gaussian_button)
        median_button = QPushButton("Median")
        filter_layout.addWidget(median_button)

        sobel_button.clicked.connect(self.on_sobel_clicked)
        sharpen_button.clicked.connect(self.on_sharpen_clicked)
        emboss_button.clicked.connect(self.on_emboss_clicked)
        edge_button.clicked.connect(self.on_edge_clicked)
        gaussian_button.clicked.connect(self.on_gaussian_clicked)
        median_button.clicked.connect(self.on_median_clicked)

        # Create return button
        return_button = QPushButton("Return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        # Add filter widget to main layout
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


    def on_emboss_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        emb = Thread(target=matrix.emboss)
        emb.start()
        emb.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/emboss.jpg"))

    
    def on_edge_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        ed = Thread(target=matrix.edge)
        ed.start()
        ed.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/edge.jpg"))

    
    def on_gaussian_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        gaus = Thread(target=matrix.gaussian)
        gaus.start()
        gaus.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/gaussian.jpg"))


    def on_median_clicked(self):
        img = Image.open('cat.jpg')
        matrix = classes.MatrixFilters(img)
        med = Thread(target=matrix.median)
        med.start()
        med.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/matrix/median.jpg"))


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
