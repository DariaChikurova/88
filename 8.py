from PIL import Image
def zadanie1():
    # Задаем пути к исходному и выходному изображениям
    input_image_path = 'pythonProject1/image.jpg'
    output_image_path = 'pythonProject1/cropped_image.jpg'
    # Задаем координаты для обрезки
    left = 100
    upper = 100
    right = 400
    lower = 400
    # Открываем изображение
    image = Image.open('dr.jpg')
    # Определяем область для обрезки
    cropped_image = image.crop((left, upper, right, lower))
    # Сохраняем обрезанное изображение
    cropped_image.save(output_image_path)
    print(f"Изображение успешно обрезано и сохранено как {output_image_path}")

def zadanie2():
        prazd = {
            '8 Марта': 'mart.jpg',
            'День рождения': 'dr.jpg',
            'Новый Год': 'snow.jpg'
        }
        imageR = 'snow.jpg'
        imageD = 'dr.jpg'
        imageV = 'mart.jpg'
        s = input("Напишите праздник: ")
        if s in prazd:
            image_path = prazd[s]
            image = Image.open(image_path)
            image.show()
        elif s != "День рожднения":
            image_path = prazd[s]
            image = Image.open(imageR)
            image.show()
        elif s != "День святого валентина":
            image_path = prazd[s]
            image = Image.open(imageD)
            image.show()
        elif s != "Рождество":
            image_path = prazd[s]
            image = Image.open(imageV)
            image.show()

        else:
            print("Введенное значение не найдено в списке.")

def zadanie3():
        name = input("Введите имя: ")
        image = Image.open("dr.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 30)

        text = f"{name}, поздравляю!"
        text_width, text_height = draw.textsize(text, font=font)
        position = ((image.width - text_width) // 2, 10)  # Позиция текста в центре вверху
        draw.text(position, text, font=font, fill="black")
        image.save("new_dr.png")
zadanie3()

