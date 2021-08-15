from PIL import Image


class Transform():


    def load_image(self, path):
        return Image.open(path)

    def resize_image(self, image):
        height, width = image.size
        ratio = height/width
        width = 100
        height = int(0.5 * ratio * width)
        img = image.resize((width, height))
        return img

    def grayscale_image(self, image):
        return image.convert('L')

    def get_pixels(self, image):
        return image.getdata()

    def convert_image_to_ascii(self, image):
        pixels = self.get_pixels(self, image)
        chars = ['*','!','|','^','X','%','#','+','.','$','&']
        indx = 0
        art = []
        s = []
        for pix in pixels:
            point = chars[pix//25]
            s.append(point)
            if indx == 100:
                indx=0
                art.append(''.join(s))
                s.clear()
            indx += 1
        return art

    def close_image(self, image):
        image.close()