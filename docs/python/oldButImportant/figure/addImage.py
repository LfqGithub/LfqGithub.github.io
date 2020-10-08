import matplotlib.pyplot as plt

im1 = plt.imread('subfigures/folding1.png')
im2 = plt.imread('subfigures/folding2.png')

fig,ax=plt.subplots(2,1)

ax[0].imshow(im1)
ax[0].axis('off')
ax[0].text(0.1,0.1,'a',transform=ax[0].transAxes)
ax[1].imshow(im2)
ax[1].axis('off')
#plt.savefig('foldingall1.tif',dpi=300)


plt.show()

