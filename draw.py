#!/usr/bin/env python

from PIL import Image, ImageDraw




def main():
    image_height = 628
    image_width = 1200
    grid_height = 100
    grid_width = 100

    main_grid_color = (140, 172, 218)
    secondary_grid_color = (199, 214, 238)
    edge_color = (255, 0, 0)
    cross_color = edge_color


    img = Image.new('RGB', (image_width, image_height), color = 'white')
    draw = ImageDraw.Draw(img)

    top_y = (image_height % grid_height) / 2
    left_x = (image_width % grid_width) / 2


    for i in range(0, 12):
        x = left_x + i * 100
        mid = x + (grid_width // 2)
        right = x + grid_width - 1 # (i+1) * 100 - 1

        draw.line((x, 0) + (x, img.size[1]), fill=main_grid_color)
        draw.line((right, 0) + (right, img.size[1]), fill=main_grid_color)
        draw.line((mid, 0) + (mid, img.size[1]), fill=(199, 214, 238))

    for i in range(0, 60):
        y = top_y + i * 100
        mid = y + grid_height // 2
        y2 = y + grid_height - 1

        draw.line((0, y) + (img.size[0], y), fill=main_grid_color)
        draw.line((0, mid) + (img.size[0], mid), fill=(199, 214, 238))
        draw.line((0, y2) + (img.size[0], y2), fill=(140, 172, 218))

    # Edges
    draw.line((0, 0) + (0, img.size[1]-1), fill=(255,0,0))
    draw.line((0, 0) + (img.size[0]-1, 0), fill=(255,0,0))
    draw.line((img.size[0]-1, 0) + (img.size[0]-1, img.size[1]-1), fill=(255,0,0))
    draw.line((0, img.size[1]-1) + (img.size[0]-1, img.size[1]-1), fill=(255,0,0))

    # Cross
    draw.line((0, 0) + (img.size[0]-1, img.size[1]-1), fill=(255,0,0))
    draw.line((0, img.size[1]-1) + (img.size[0]-1, 0), fill=(255,0,0))
    del draw

    # write to stdout
    img.save('pil_red.png')




if __name__ == '__main__':
    main()
