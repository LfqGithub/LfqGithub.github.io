---
layout: post
title: ImageMagick
categories: Linux
description: image operation
keywords: imagemagick, linux, convert
---

Linux 命令行图像处理, updating......

## 示例

```bash
# sudo apt install imagemagick python3-tk
# add export DISPLAY=localhost:0.0 to ~/.bashrc

$ convert -density 150 input.pdf -quality 90 output.png  
PNG, JPG or (virtually) any other image format can be chosen
-density xxx will set the dpi to xxx (common are 150 and 300)
-quality xxx will set the compression to xxx for PNG, JPG and MIFF file formates (100 means no compression)
all other options (such as trimming, grayscale, etc) can be viewed on the website of Image Magic.
$ convert -colorspace gray colorFigure.png grayFigure.png  # 灰度图
$ convert -monochrome colorFigure.png blackAndWhiteFigure.png  # 黑白图
# for more usage
$ convert -h
$ find ./ -regex '.*\(jpg\|JPG\)' -exec convert -resize 50%x50% {} {} \;  # 将当前文件夹中所有jpg图像的分辨率变成之前的1/4
```

## 降低图像亮度

传统网页背景为白色，因此网页中相当部分图片的背景为白色。当我们使用Chrome暗黑模式浏览网页时，会被明亮的白色背景图片晃瞎眼。
为解决这一问题，我们需要降低图像亮度以适配网页暗黑模式, 这里的降低图片亮度，相当于PPT中在图像上蒙上一张同样大小的灰色透明图片。
在 Linux 中，我们可以使用命令行来实现这一操作：

`convert -brightness-contrast -30x10 original_figure.png new_figure.png`

