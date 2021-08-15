import unittest
from transform import Transform
import imghdr


class TestTransform(unittest.TestCase):


    def test_load_image(self):
        img = Transform.load_image(self, './gc.jpg')
        res = imghdr.what('./gc.jpg')
        self.assertEqual(res, "jpeg")
        Transform.close_image(self, img)

    def test_resize_image(self):
        img = Transform.load_image(self, './gc.jpg')
        width, height = Transform.resize_image(self, img).size
        self.assertEqual(width+height, 173)
        Transform.close_image(self, img)

    def test_grayscale(self):
        img = Transform.load_image(self, './gc.jpg')
        img = Transform.grayscale_image(self, img)
        self.assertEqual(img.mode, "L")
        Transform.close_image(self, img)

    def test_get_pixels(self):
        img = Transform.load_image(self, './gc.jpg')
        resized_image = Transform.resize_image(self, img)
        gray_img = Transform.grayscale_image(self, resized_image)
        pixels = Transform.get_pixels(self, gray_img)
        self.assertEqual(7300, len(pixels))
        Transform.close_image(self, img)

    def test_image_to_ascii(self):
        img = Transform.load_image(self, './gc.jpg')
        gray_image = Transform.grayscale_image(self, img)
        resized_image = Transform.resize_image(self, gray_image)
        result = Transform.convert_image_to_ascii(Transform, resized_image)
        self.assertEqual(72, len(result))
        Transform.close_image(self, img)

if __name__ == "__main__":
    unittest.main()