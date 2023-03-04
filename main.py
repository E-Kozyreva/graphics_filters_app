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

        # Create return button
        return_button = QPushButton("Return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        # Add filter widget to main layout
        self.layout().addWidget(filter_widget)

    
    def on_inversion_clicked(self):
        img = Image.open('cat.jpg')
        spot = classes.SpotFilters(img)
        t1 = Thread(target=spot.inversion)
        t1.start()
        t1.join()
        self.layout().itemAt(0).widget().setPixmap(QPixmap("results/output/spot/inversion.jpg"))


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

        # Create return button
        return_button = QPushButton("Return")
        filter_layout.addWidget(return_button)
        return_button.clicked.connect(self.on_return_clicked)

        # Add filter widget to main layout
        self.layout().addWidget(filter_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
